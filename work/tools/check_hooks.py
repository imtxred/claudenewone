# -*- coding: utf-8 -*-
"""Батарея проверок для хуков сторитейлов.

Правила — в work/ops/pravila_hookov.md. Скрипт проверяет ровно то, что там описано:
зону обрыва, мёртвую зону 121-126, чужой алфавит, название препарата
и пересечение имён с корпусом сторитейлов и лендингов.

Запуск:
    python3 work/tools/check_hooks.py hooks.txt
    python3 work/tools/check_hooks.py hooks.txt --alphabet cyrillic --brand Metonil
    python3 work/tools/check_hooks.py work/tools/hooks_20_BG_parazity_src.py --module

Формат hooks.txt: один хук на строку, пустые строки и строки с # игнорируются.
С --module берётся список HOOKS из py-файла (кортежи с вариантами), проверяется
первый вариант, проходящий ok().
"""

import argparse
import os
import re
import sys
import unicodedata

CORPUS_DEFAULT = ["work/storytales", "work/landings"]

CYR = re.compile(r"[Ѐ-ӿ]")
LAT = re.compile(r"[A-Za-zÀ-ɏ]")


# --- спецификация обрыва -----------------------------------------------------

def ok(x):
    n = len(x)
    if n <= 120:
        return True                       # виден целиком
    if n < 127 or n > 143:
        return False                      # мёртвая зона / слишком длинный хвост
    return x[124].isalpha() and x[125].isalpha() and n - 125 <= 18


def zone(x):
    """Человекочитаемый вердикт по длине."""
    n = len(x)
    if n <= 120:
        return "виден целиком"
    if n <= 126:
        return "МЁРТВАЯ ЗОНА 121-126"
    if n > 143:
        return "хвост длиннее 18 знаков"
    if not (x[124].isalpha() and x[125].isalpha()):
        return "обрыв не внутри слова"
    return "обрыв на 125, внутри слова"


# --- остальные проверки ------------------------------------------------------

def foreign_letters(x, alphabet):
    """Буквы чужого алфавита. alphabet: cyrillic | latin | auto."""
    if alphabet == "auto":
        alphabet = "cyrillic" if len(CYR.findall(x)) >= len(LAT.findall(x)) else "latin"
    bad = LAT.findall(x) if alphabet == "cyrillic" else CYR.findall(x)
    return alphabet, sorted(set(bad))


def brand_hits(x, brands):
    return [b for b in brands if b.lower() in x.lower()]


SENT_END = tuple(".!?…»\"“„:;—-")


def names(x):
    """Заглавные слова, не стоящие в начале предложения, — кандидаты в имена."""
    out = []
    for m in re.finditer(r"[^\W\d_]{4,}", x, re.UNICODE):
        w = m.group(0)
        if not w[0].isupper():
            continue
        head = x[:m.start()].rstrip()
        if not head or head.endswith(SENT_END):
            continue                      # начало предложения — не имя
        out.append(w)
    return out


def load_corpus(paths):
    text = []
    for p in paths:
        if os.path.isfile(p):
            files = [p]
        else:
            files = [os.path.join(r, f)
                     for r, _, fs in os.walk(p) for f in fs
                     if f.endswith((".txt", ".md", ".html"))]
        for f in files:
            try:
                with open(f, encoding="utf-8", errors="ignore") as fh:
                    text.append((f, fh.read()))
            except OSError:
                pass
    return text


def fold(s):
    """Снимает диакритику, чтобы Halina и Halína считались одним именем."""
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def name_clashes(name, corpus):
    stem = fold(name)[:-1] or fold(name)   # обрезаем падежное окончание
    return sorted({os.path.basename(f) for f, t in corpus if stem in fold(t)})


# --- загрузка хуков ----------------------------------------------------------

def from_text(path):
    with open(path, encoding="utf-8") as fh:
        return [(str(i), ln.strip())
                for i, ln in enumerate(fh, 1)
                if ln.strip() and not ln.lstrip().startswith("#")]


def from_module(path):
    ns = {}
    with open(path, encoding="utf-8") as fh:
        exec(compile(fh.read(), path, "exec"), ns)      # noqa: S102 — свой же файл
    hooks = ns.get("HOOKS")
    if not hooks:
        sys.exit("в файле нет списка HOOKS")
    out = []
    for item in hooks:
        code, variants = item[0], item[2]
        chosen = next((v for v in variants if ok(v)), variants[0])
        out.append((code, chosen))
    return out


# --- вывод -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Батарея проверок для хуков сторитейлов")
    ap.add_argument("path")
    ap.add_argument("--module", action="store_true",
                    help="взять список HOOKS из py-файла")
    ap.add_argument("--alphabet", choices=["cyrillic", "latin", "auto"], default="auto")
    ap.add_argument("--brand", action="append", default=[],
                    help="название препарата, можно несколько раз")
    ap.add_argument("--corpus", nargs="*", default=CORPUS_DEFAULT,
                    help="папки для проверки пересечения имён")
    ap.add_argument("--no-names", action="store_true",
                    help="пропустить проверку имён")
    args = ap.parse_args()

    hooks = from_module(args.path) if args.module else from_text(args.path)
    corpus = [] if args.no_names else load_corpus(args.corpus)

    problems = 0
    for code, x in hooks:
        issues = []
        n = len(x)
        if not ok(x):
            issues.append("обрыв: " + zone(x))

        alpha, bad = foreign_letters(x, args.alphabet)
        if bad:
            issues.append("чужой алфавит (%s): %s" % (alpha, " ".join(bad)))

        hit = brand_hits(x, args.brand)
        if hit:
            issues.append("название препарата: " + ", ".join(hit))

        for nm in dict.fromkeys(names(x)):
            where = name_clashes(nm, corpus)
            if where:
                issues.append("имя %s уже есть: %s" % (nm, ", ".join(where[:3])))

        mark = "OK " if not issues else "!! "
        print("%s%-4s %3d зн.  %s" % (mark, code, n, zone(x)))
        if n > 120:
            print("        видно: %s|%s" % (x[:125], x[125:]))
        for i in issues:
            print("        - " + i)
        if issues:
            problems += 1

    print("\nпроблем: %d из %d" % (problems, len(hooks)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
