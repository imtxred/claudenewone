# -*- coding: utf-8 -*-
"""Сборка TSL-лендинга из VSL-лендинга NEWPLlanding.html.

Что сохраняется байт-в-байт: <head>, весь <style>, топбар, шапка FB-поста,
блок реакций/кнопок, форма заказа, футер, лента из 20 комментариев с капельным
показом, backfix-модалка, скрипты санитайзеров и скролла.

Что меняется:
  1. #container_video (видео 16:9) -> длинная текстовая статья .tsl;
  2. js/video.js (тайминг-гейт) -> инлайн-скрипт со скролл-гейтом;
  3. формулировки «видео/трансляция» -> «запись/пост» в футере и модалке;
  4. #oneform переезжает к форме заказа (якорь для CTA-ссылок).
"""
import re, sys, io, os

SRC = "/root/.claude/uploads/6edf4558-aa97-5f8e-8789-ca34ac607d70/ba063552-NEWPLlanding.html"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                   "work/landings/PL/PL_stawy_Artrovia_tsl_pl.html")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from article_pl_tsl import ARTICLE

src = io.open(SRC, encoding="utf-8").read()
orig_style = src[src.index("<style>"): src.index("</style>") + len("</style>")]

# ---------------------------------------------------------------- 1. CSS
TSL_CSS = """
    <style>
        /* ---------- TSL: текстовая статья вместо видео ---------- */
        .fb-post-body {
            padding: 0;
        }

        .tsl {
            background: #fff;
            padding: 14px 16px 20px;
            font-size: 17px;
            line-height: 1.62;
            color: #1c1e21;
            text-align: left;
            word-wrap: break-word;
        }

        .tsl p {
            margin: 0 0 14px;
        }

        .tsl-live {
            display: flex;
            gap: 6px;
            align-items: center;
            margin-bottom: 14px;
        }

        .tsl-live .badge-live,
        .tsl-live .badge-viewers {
            position: static;
        }

        .tsl-h1 {
            font-size: 23px;
            line-height: 1.28;
            font-weight: 800;
            margin: 0 0 14px;
            color: #050505;
        }

        .tsl h2 {
            font-size: 20px;
            line-height: 1.3;
            font-weight: 800;
            margin: 30px 0 14px;
            padding-left: 12px;
            border-left: 4px solid #1877f2;
            color: #050505;
        }

        .tsl h3 {
            font-size: 17.5px;
            font-weight: 800;
            margin: 24px 0 10px;
            color: #050505;
        }

        .tsl-lead {
            font-size: 18px;
            font-weight: 600;
            color: #1c1e21;
        }

        .tsl-sign {
            font-size: 14px;
            color: #65676b;
            font-style: italic;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid #e4e6eb;
        }

        .tsl-ava {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            object-fit: cover;
            flex-shrink: 0;
            background: #dfe3ee;
        }

        .tsl-doc {
            margin: 0 0 6px;
        }

        .tsl-doc-head,
        .tsl-quote-head {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }

        .tsl-doc-name,
        .tsl-quote-name {
            font-weight: 700;
            font-size: 15.5px;
            color: #050505;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .tsl-doc-role,
        .tsl-quote-role {
            font-size: 13px;
            color: #65676b;
        }

        .tsl-quote,
        .tsl-story {
            background: #f0f2f5;
            border-left: 3px solid #1877f2;
            border-radius: 0 10px 10px 0;
            padding: 14px 14px 2px;
            margin: 18px 0;
            font-size: 16.5px;
        }

        .tsl-quote-user {
            border-left-color: #28a745;
        }

        .tsl-story {
            background: #fff9ec;
            border-left-color: #f7b500;
        }

        .tsl-promise {
            font-weight: 700;
            color: #1877f2;
        }

        .tsl-underline {
            font-weight: 700;
            box-shadow: inset 0 -10px 0 #ffe9a8;
            display: inline-block;
        }

        .tsl-note {
            font-size: 15.5px;
            color: #65676b;
            font-style: italic;
        }

        .tsl-ask {
            font-weight: 700;
            color: #050505;
        }

        .tsl-key {
            background: #fff8e1;
            border: 1px solid #f2d68a;
            border-left: 4px solid #f7b500;
            border-radius: 8px;
            padding: 14px 14px 2px;
            margin: 18px 0;
        }

        .tsl-key-title {
            font-weight: 800;
            font-size: 15px;
            text-transform: uppercase;
            letter-spacing: .3px;
            color: #8a6100;
            margin-bottom: 8px;
        }

        .tsl-danger {
            background: #fff0f0;
            border: 1px solid #f3c2c2;
            border-left: 4px solid #d90000;
            border-radius: 8px;
            padding: 14px 14px 2px;
            margin: 18px 0;
        }

        .tsl-danger-title {
            font-weight: 900;
            font-size: 19px;
            color: #d90000;
            margin-bottom: 8px;
        }

        .tsl-fact {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            background: #eef4ff;
            border: 1px solid #c6d8f7;
            border-radius: 8px;
            padding: 14px;
            margin: 18px 0;
        }

        .tsl-fact p {
            margin: 0;
            font-size: 15.5px;
        }

        .tsl-fact-num {
            font-size: 27px;
            font-weight: 900;
            color: #1877f2;
            line-height: 1;
            flex-shrink: 0;
        }

        .tsl-step {
            border: 1px solid #e4c98a;
            border-radius: 8px;
            background: #fff;
            padding: 12px 12px 2px;
            margin: 0 0 14px;
        }

        .tsl-step-num {
            font-weight: 800;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: .3px;
            color: #b06f00;
            margin-bottom: 6px;
        }

        .tsl-ing {
            display: flex;
            gap: 12px;
            margin: 0 0 18px;
        }

        .tsl-ing-num {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: #1877f2;
            color: #fff;
            font-weight: 800;
            font-size: 17px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .tsl-ing-body {
            flex: 1;
        }

        .tsl-ing-name {
            font-weight: 800;
            font-size: 16.5px;
            margin-bottom: 6px;
            color: #050505;
        }

        .tsl-mini {
            font-size: 14.5px;
            color: #3a3b3c;
            background: #f0f2f5;
            border-radius: 6px;
            padding: 10px 12px;
        }

        .tsl-phases {
            margin: 0 0 18px;
        }

        .tsl-phase {
            border-left: 3px solid #28a745;
            padding: 8px 0 8px 12px;
            margin-bottom: 10px;
            font-size: 16px;
        }

        .tsl-phase span {
            display: block;
            font-weight: 800;
            color: #1e7e34;
            font-size: 14.5px;
            text-transform: uppercase;
            letter-spacing: .3px;
            margin-bottom: 2px;
        }

        .tsl-days {
            background: #f0f2f5;
            border-radius: 8px;
            padding: 12px 14px;
            margin: 0 0 18px;
        }

        .tsl-day {
            padding: 6px 0;
            border-bottom: 1px dashed #d5d8dd;
            font-size: 16px;
        }

        .tsl-day:last-child {
            border-bottom: none;
        }

        .tsl-ul {
            margin: 0 0 14px 18px;
            font-size: 16px;
        }

        .tsl-ul li {
            margin-bottom: 5px;
        }

        .tsl-brand {
            font-size: 20px;
            font-weight: 800;
            text-align: center;
            color: #050505;
        }

        .tsl-price {
            background: #f6fff8;
            border: 2px solid #28a745;
            border-radius: 10px;
            padding: 16px 14px 2px;
            margin: 18px 0;
            text-align: center;
        }

        .tsl-price-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }

        .tsl-price-old {
            font-size: 22px;
            color: #90949c;
            text-decoration: line-through;
            font-weight: 700;
        }

        .tsl-price-arrow {
            font-size: 20px;
            color: #28a745;
        }

        .tsl-price-new {
            font-size: 34px;
            font-weight: 900;
            color: #28a745;
            line-height: 1;
        }

        .tsl-price p {
            text-align: left;
        }

        .tsl-cta {
            display: block;
            text-align: center;
            background: #28a745;
            color: #fff !important;
            font-weight: 800;
            font-size: 17px;
            text-decoration: none;
            padding: 16px 12px;
            border-radius: 10px;
            box-shadow: 0 5px 0 #1e7e34;
            margin: 22px 0 26px;
            letter-spacing: .2px;
        }

        .tsl-road {
            border: 1px solid #dcdfe3;
            border-radius: 8px;
            padding: 12px 14px 2px;
            margin: 0 0 14px;
            background: #fafbfc;
        }

        .tsl-road-good {
            border-color: #28a745;
            background: #f6fff8;
        }

        .tsl-road-num {
            font-weight: 800;
            font-size: 15px;
            text-transform: uppercase;
            letter-spacing: .3px;
            color: #65676b;
            margin-bottom: 6px;
        }

        .tsl-road-good .tsl-road-num {
            color: #1e7e34;
        }

        .tsl-final {
            font-weight: 700;
            font-size: 17.5px;
        }

        .tsl-scrollhint {
            display: none;
            text-align: center;
            font-size: 14px;
            color: #65676b;
            margin-top: 10px;
        }

        .tsl-scrollhint.is-on {
            display: block;
        }

        .tsl-arrow {
            font-size: 18px;
            color: #28a745;
            animation: tsl-bounce 1.2s infinite;
        }

        @keyframes tsl-bounce {

            0%,
            100% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(5px);
            }
        }

        @media (max-width: 400px) {
            .tsl {
                font-size: 16.5px;
                padding: 12px 13px 18px;
            }

            .tsl-h1 {
                font-size: 21px;
            }

            .tsl h2 {
                font-size: 18.5px;
            }
        }
    </style>
"""

# ---------------------------------------------------------------- 2. JS
TSL_JS = """<script>
/* TSL-контроллер: заменяет js/video.js.
   Гейт формы — по глубине прокрутки статьи, а не по таймкоду видео. */
(function () {
    var REVEAL_AT = 0.60;      /* доля статьи, после которой открывается форма */
    var TIMER_MIN = 5;         /* минут на таймере скидки */
    var STOCK_START = 36;
    var STOCK_FLOOR = 7;

    var revealed = false;
    var form = document.getElementById('order-form-container');
    var article = document.getElementById('tsl-article');
    var hint = document.getElementById('tsl-scrollhint');

    /* ---------- счётчик «читают сейчас» ---------- */
    var viewers = document.getElementById('live-viewers');
    if (viewers) {
        var base = 21486;
        setInterval(function () {
            base += Math.floor(Math.random() * 61) - 28;
            if (base < 20800) base = 20800 + Math.floor(Math.random() * 60);
            if (base > 22400) base = 22400 - Math.floor(Math.random() * 60);
            viewers.textContent = String(base).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ' ');
        }, 4000);
    }

    /* ---------- таймер скидки ---------- */
    var timerStarted = false;
    function startTimer() {
        if (timerStarted) return;
        timerStarted = true;
        var left = TIMER_MIN * 60;
        var h = document.getElementById('hour-val');
        var m = document.getElementById('min-val');
        var s = document.getElementById('sec-val');
        function pad(n) { return n < 10 ? '0' + n : '' + n; }
        function tick() {
            var hh = Math.floor(left / 3600);
            var mm = Math.floor((left % 3600) / 60);
            var ss = left % 60;
            if (h) h.textContent = pad(hh);
            if (m) m.textContent = pad(mm);
            if (s) s.textContent = pad(ss);
            if (left > 0) left--;
        }
        tick();
        setInterval(tick, 1000);
    }

    /* ---------- остаток на складе ---------- */
    var stockStarted = false;
    function startStock() {
        if (stockStarted) return;
        stockStarted = true;
        var n = STOCK_START;
        var a = document.getElementById('live-stock-count');
        var b = document.getElementById('bf-stock-count');
        function step() {
            if (n > STOCK_FLOOR) {
                n--;
                if (a) a.textContent = n;
                if (b) b.textContent = n;
            }
            setTimeout(step, 22000 + Math.floor(Math.random() * 34000));
        }
        setTimeout(step, 26000);
    }

    /* ---------- открытие формы ---------- */
    function reveal() {
        if (revealed) return;
        revealed = true;
        if (form) form.style.display = 'block';
        if (hint) hint.classList.add('is-on');
        startTimer();
        startStock();
    }

    function onScroll() {
        if (revealed || !article) return;
        var r = article.getBoundingClientRect();
        var seen = (window.innerHeight - r.top) / (r.height || 1);
        if (seen >= REVEAL_AT) reveal();
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    document.addEventListener('DOMContentLoaded', onScroll);
    onScroll();

    /* страховка: если читатель завис наверху, форма всё равно откроется */
    setTimeout(function () { reveal(); }, 240000);

    /* ---------- backfix ---------- */
    var overlay = document.getElementById('backfix-overlay');
    var st1 = document.getElementById('bf-state-1');
    var st2 = document.getElementById('bf-state-2');
    var bfShown = false;
    var bfTimerId = null;

    function showBackfix() {
        if (!overlay || overlay.classList.contains('is-open')) return;
        if (revealed) {
            if (st1) st1.style.display = 'none';
            if (st2) st2.style.display = 'block';
        } else {
            if (st1) st1.style.display = 'block';
            if (st2) st2.style.display = 'none';
            startBfTimer();
        }
        overlay.classList.add('is-open');
        overlay.style.display = 'flex';
        document.body.classList.add('noscroll');
        bfShown = true;
    }

    function startBfTimer() {
        if (bfTimerId) return;
        var left = 120;
        var el = document.getElementById('bf-timer');
        bfTimerId = setInterval(function () {
            var mm = Math.floor(left / 60), ss = left % 60;
            if (el) el.textContent = (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
            if (left > 0) left--;
        }, 1000);
    }

    window.closeBackfixAndScroll = function () {
        if (overlay) {
            overlay.classList.remove('is-open');
            overlay.style.display = 'none';
        }
        document.body.classList.remove('noscroll');
        var target = revealed ? document.getElementById('oneform') : document.getElementById('tsl-article');
        if (target && target.getBoundingClientRect) {
            var top = window.pageYOffset + target.getBoundingClientRect().top - 60;
            window.scrollTo({ top: top, behavior: 'smooth' });
        }
    };

    document.addEventListener('mouseout', function (e) {
        if (!e.relatedTarget && e.clientY <= 0 && !bfShown) showBackfix();
    });

    try {
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function () {
            history.pushState(null, '', location.href);
            showBackfix();
        });
    } catch (err) { }
})();
</script>"""

# ---------------------------------------------------------------- 3. Сборка
out = src

# 3.1 title
out = out.replace('<title>Wideo na zywo | Facebook</title>',
                  '<title>Wpis na zywo | Facebook</title>', 1)

# 3.2 новый <style> сразу после исходного (исходный не трогаем)
assert out.count(orig_style) == 1
out = out.replace(orig_style, orig_style + "\n" + TSL_CSS, 1)

# 3.3 видеоблок -> статья
start = out.index('        <span id="oneform"></span>\n        <div class="vsl-sticky-wrap">')
end_marker = '        <div class="fb-post fb-post-bottom">'
end = out.index(end_marker, start)
video_block = out[start:end]
assert 'container_video' in video_block and 'media/vid.mp4' in video_block
out = out[:start] + ARTICLE.lstrip('\n') + "\n\n\n" + out[end:]

# 3.4 якорь #oneform переезжает к форме заказа
anchor = '        <div class="order-container" id="order-form-container">'
assert out.count(anchor) == 1
out = out.replace(anchor, '        <span id="oneform"></span>\n\n' + anchor, 1)

# 3.5 «видео/трансляция» -> «пост/запись»
subs = [
    ('UWAGA! Nagranie tej transmisji NIE zostanie zapisane! Obejrzyj uwaznie do konca.',
     'UWAGA! Ten wpis NIE zostanie zarchiwizowany! Przeczytaj uwaznie do konca.'),
    ('Nie odchodz jeszcze! Nagranie tej poufnej transmisji <b>NIE ZOSTANIE ZAPISANE</b>.',
     'Nie odchodz jeszcze! Ten poufny wpis <b>NIE ZOSTANIE ZAPISANY</b>.'),
    ('Musisz obejrzec wideo do konca!', 'Musisz przeczytac wpis do konca!'),
    ('<p style="margin-bottom: 10px; font-size: 15px; color: #333; font-weight: bold;">Twoj dostep do\n                        wideo wygasa za:</p>',
     '<p style="margin-bottom: 10px; font-size: 15px; color: #333; font-weight: bold;">Twoj dostep do\n                        wpisu wygasa za:</p>'),
    ('<button onclick="window.closeBackfixAndScroll()" class="bf-btn">➤ KONTYNUUJ OGLADANIE</button>',
     '<button onclick="window.closeBackfixAndScroll()" class="bf-btn">➤ KONTYNUUJ CZYTANIE</button>'),
    ('<span>🔴 Transmisja na zywo</span><span>•</span><span>👁 +21 000 ogladajacych</span>',
     '<span>🔴 Wpis na zywo</span><span>•</span><span>👁 +21 000 czytajacych</span>'),
]
for a, b in subs:
    assert out.count(a) == 1, a[:60]
    out = out.replace(a, b, 1)

# 3.6 js/video.js -> инлайн-контроллер
assert out.count('<script src="js/video.js"></script>') == 1
out = out.replace('<script src="js/video.js"></script>', TSL_JS, 1)

# 3.7 backfix-оверлей открывается через .is-open
old_bf = '        #backfix-overlay {'
assert out.count(old_bf) == 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
io.open(OUT, 'w', encoding='utf-8').write(out)
print("written:", OUT, len(out), "bytes")
