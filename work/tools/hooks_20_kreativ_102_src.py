# -*- coding: utf-8 -*-
"""Хуки к сторитейлу, собранному из видеокреатива «102 года» (PL, суставы).
Для каждого хука — список вариантов формулировки; берётся первый,
проходящий спецификацию обрыва на 125-м знаке."""

def ok(x):
    n = len(x)
    if n <= 120:
        return True                      # виден целиком, «Ещё» не появляется
    if n < 127 or n > 143:
        return False                     # мёртвая зона 121-126 / слишком длинный хвост
    return x[124].isalpha() and x[125].isalpha() and n - 125 <= 18

HOOKS = [
 # ---------------- A. голос самого старика ----------------
 ("A1", "голос героя лендинга, 102 года", [
   "Mam sto dwa lata i wczoraj sam wszedłem po schodach na trzecie piętro. Moi rówieśnicy, ci którzy jeszcze żyją, siedzą na wózkach.",
   "Mam sto dwa lata i wczoraj sam wszedłem po schodach na trzecie piętro. Moi rówieśnicy, ci co jeszcze żyją, siedzą na wózkach.",
   "Mam sto dwa lata i wczoraj sam wszedłem na trzecie piętro. Moi rówieśnicy, ci którzy jeszcze żyją, siedzą na wózkach inwalidzkich.",
 ], "Мне сто два года, и вчера я сам поднялся по лестнице на третий этаж. Мои ровесники, те кто ещё жив, сидят в колясках."),

 ("A2", "голос героя лендинга, признание против себя", [
   "Przez siedemdziesiąt lat byłem ortopedą, przez moje ręce przeszło czterdzieści tysięcy ludzi. Prawie wszystko, co im robiłem, było na darmo.",
   "Byłem ortopedą siedemdziesiąt lat, przez moje ręce przeszło czterdzieści tysięcy ludzi. I prawie wszystko, co im robiłem, było na darmo.",
   "Siedemdziesiąt lat byłem ortopedą. Przez moje ręce przeszło czterdzieści tysięcy osób. Prawie wszystko, co im zrobiłem, było na darmo.",
 ], "Семьдесят лет я был ортопедом, через мои руки прошло сорок тысяч человек. Почти всё, что я им делал, было напрасно."),

 ("A3", "голос героя лендинга, сорок лет молчания", [
   "Czterdzieści lat milczałem, bo za to odebrano by mi prawo wykonywania zawodu. Mam sto dwa lata i nie mam już czego stracić.",
   "Czterdzieści lat milczałem, bo za to odebrano by mi prawo wykonywania zawodu. Dziś mam sto dwa lata i nie mam już czego stracić.",
   "Milczałem czterdzieści lat, bo za to odebrano by mi prawo wykonywania zawodu. Mam sto dwa lata i nie mam już nic do stracenia.",
 ], "Сорок лет я молчал, потому что за это лишили бы права работать. Мне сто два года, мне больше нечего терять."),

 ("A4", "голос героя лендинга, враг в тумбочке", [
   "Nigdy nie powiedziałem tego przy świadkach. Każda tabletka na ból stawów, którą pan dziś połknął, przybliżyła pana do wózka.",
   "Nigdy nie powiedziałem tego przy świadkach: każda tabletka na ból stawów, którą pan dziś połknął, przybliżyła pana do wózka.",
   "Nigdy nie mówiłem tego przy świadkach. Każda tabletka na ból stawów, którą pan dziś połknął, przybliżyła pana do wózka inwalidzkiego.",
 ], "Не говорил этого при свидетелях. Каждая таблетка от боли в суставах, что вы выпили утром, придвинула вас к коляске."),

 # ---------------- B. хирург-ортопед, теряет деньги ----------------
 ("B1", "оперирующий ортопед, отмены", [
   "Operuję kolana od dwudziestu lat. W zeszłym miesiącu czterech pacjentów odwołało zabieg na trzy dni przed terminem. Nikt nie podał powodu.",
   "Operuję kolana dwadzieścia lat. W zeszłym miesiącu czterech pacjentów odwołało zabieg trzy dni przed terminem, i żaden nie podał powodu.",
   "Operuję kolana od dwudziestu lat. W maju czterech pacjentów odwołało zabieg na trzy dni przed terminem. Żaden nie podał powodu.",
 ], "Оперирую колени двадцать лет. В прошлом месяце четверо отменили операцию за три дня до срока. Ни один не назвал причину."),

 ("B2", "оперирующий ортопед, вернулась без операции", [
   "Powiedziałem jej: proszę się przygotować, po tej operacji nie wróci pani do ogrodu. Wróciła po pół roku — bez operacji, z workiem jabłek.",
   "Powiedziałem jej: proszę się przygotować, po tej operacji już nie wróci pani do ogrodu. Przyszła po pół roku z workiem jabłek.",
   "Mówiłem jej: proszę się przygotować, po tej operacji nie wróci pani do ogrodu. Wróciła po pół roku i przyniosła worek jabłek.",
 ], "Я сказал ей: готовьтесь, после этой операции вы уже не вернётесь в сад. Она пришла через полгода — без операции, с мешком яблок."),

 ("B3", "оперирующий ортопед, отговаривает от своего же хлеба", [
   "Mam dwa lata do emerytury i właśnie zacząłem odradzać ludziom operację, z której przez całe życie się utrzymywałem.",
   "Mam dwa lata do emerytury i właśnie zacząłem odradzać ludziom operację, z której żyję od dwudziestu ośmiu lat.",
   "Zostały mi dwa lata do emerytury i właśnie zacząłem odradzać ludziom operację, z której się utrzymuję.",
 ], "Мне два года до пенсии, и я только что начал отговаривать людей от операции, которой кормился всю жизнь."),

 ("B4", "оперирующий ортопед, очередь тает", [
   "Na moim biurku leży lista dwudziestu siedmiu osób czekających na endoprotezę. Jedenaście z nich w tym roku po cichu się wypisało.",
   "Na moim biurku leży lista dwudziestu siedmiu osób czekających na endoprotezę. Jedenaście osób w tym roku po cichu się wypisało.",
   "Mam listę dwudziestu siedmiu osób czekających na endoprotezę kolana. Jedenaście z nich w tym roku po cichu się z niej wypisało.",
 ], "У меня на столе список из двадцати семи человек в очереди на эндопротез. Одиннадцать в этом году тихо вычеркнулись сами."),

 # ---------------- C. металл, протезы, техника ----------------
 ("C1", "изготовитель протезов", [
   "Robię protezy stawów od osiemnastu lat. W tym roku pierwszy raz musiałem zwolnić człowieka, bo zamówień jest o połowę mniej.",
   "Robię protezy stawów osiemnaście lat. W tym roku pierwszy raz musiałem zwolnić pracownika, bo zamówień przyszło o połowę mniej.",
   "Robię protezy stawów od osiemnastu lat i w tym roku pierwszy raz zwolniłem człowieka, bo zamówień jest o połowę mniej.",
 ], "Я делаю протезы суставов восемнадцать лет. В этом году впервые пришлось уволить человека — заказов вдвое меньше."),

 ("C2", "прокат реабилитационной техники", [
   "Wypożyczalnia sprzętu rehabilitacyjnego, dwanaście lat. Nikt nigdy nie oddał balkonika przed terminem. W maju oddano mi cztery.",
   "Prowadzę wypożyczalnię sprzętu rehabilitacyjnego dwanaście lat. Nikt nigdy nie oddał balkonika przed terminem. W maju oddano cztery.",
   "Dwanaście lat prowadzę wypożyczalnię sprzętu rehabilitacyjnego. Nikt nigdy nie oddał balkonika przed terminem. W maju oddano cztery.",
 ], "Двенадцать лет держу прокат реабилитационной техники. Никто никогда не сдавал ходунки раньше срока. В мае сдали четверо."),

 ("C3", "поставщик металла для эндопротезов", [
   "Zadzwonił do mnie dostawca metalu do endoprotez i zapytał, czy coś się stało w naszym powiecie. Zamówienia spadły o czterdzieści procent.",
   "Dostawca metalu do endoprotez zadzwonił i pytał, czy coś się stało w naszym powiecie. Zamówienia spadły o czterdzieści procent.",
   "Zadzwonił dostawca metalu do endoprotez i zapytał, co się dzieje w naszym powiecie. Zamówienia spadły u nas o czterdzieści procent.",
 ], "Позвонил поставщик металла для эндопротезов, спросил, что у нас случилось. Заказы упали на сорок процентов."),

 # ---------------- D. аптека и фарма ----------------
 ("D1", "владелец аптеки", [
   "Prowadzę aptekę od dziewiętnastu lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego tak jest.",
   "Prowadzę aptekę od dziewiętnastu lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju zrozumiałem, dlaczego.",
   "Mam aptekę od dziewiętnastu lat. Najlepiej sprzedaje się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego akurat tak.",
   "Prowadzę aptekę dziewiętnaście lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego tak jest.",
   "Mam aptekę od dziewiętnastu lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego właśnie tak.",
   "Prowadzę aptekę od dziewiętnastu lat. Najlepiej sprzedaje mi się to, co nie leczy. Dlaczego, usłyszałem dopiero w maju.",
 ], "Девятнадцать лет держу аптеку. Лучше всего продаётся то, что не лечит, и только в мае я услышал, почему так."),

 ("D2", "фармпредставитель", [
   "Przez jedenaście lat uczyłem lekarzy zapisywać maść, o której wiedziałem, że nie wchodzi głębiej niż na dwa milimetry.",
   "Jedenaście lat uczyłem lekarzy, jak zapisywać maść, o której wiedziałem, że nie wchodzi głębiej niż na dwa milimetry.",
   "Przez jedenaście lat uczyłem lekarzy, jak zapisywać maść, o której doskonale wiedziałem, że nie wchodzi głębiej niż dwa milimetry.",
 ], "Одиннадцать лет я учил врачей выписывать мазь, о которой знал, что она не проходит глубже двух миллиметров."),

 ("D3", "фармпредставитель, премия", [
   "Moja premia liczy się od tego, ilu pacjentów wróci po drugie opakowanie. Nie od tego, ilu z nich wyzdrowieje.",
   "Moją premię liczy się od tego, ilu pacjentów wróci po drugie opakowanie. Nie od tego, ilu z nich wyzdrowieje.",
   "Premię liczą mi od tego, ilu pacjentów wróci po drugie opakowanie, a nie od tego, ilu z nich wyzdrowieje.",
 ], "Мою премию считают по тому, сколько пациентов вернётся за второй упаковкой. Не по тому, сколько выздоровеет."),

 # ---------------- E. те, кто ставит на ноги ----------------
 ("E1", "реабилитолог", [
   "Jestem rehabilitantką. Pani Leokadia chodziła do mnie cztery lata i nagle przestała. Myślałam, że umarła. Spotkałam ją na targu, z siatkami.",
   "Jestem rehabilitantką. Pani Leokadia chodziła do mnie cztery lata i nagle przestała. Byłam pewna, że umarła. Spotkałam ją na targu.",
   "Jestem rehabilitantką. Pani Leokadia przychodziła do mnie cztery lata i nagle przestała. Myślałam, że umarła. Minęła mnie wczoraj na targu.",
 ], "Я реабилитолог. Пани Леокадия ходила ко мне четыре года и вдруг перестала. Я решила — умерла. Встретила её на рынке."),

 ("E2", "санитар, носил по лестнице", [
   "Przez dziewięć lat wnosiłem ludzi po schodach do gabinetu. Pana Tadeusza wnosiłem osiemnaście razy. Za dziewiętnastym wszedł sam.",
   "Dziewięć lat wnosiłem ludzi po schodach do gabinetu. Pana Tadeusza wnosiłem osiemnaście razy. Za dziewiętnastym wszedł o własnych siłach.",
   "Przez dziewięć lat wnoszę ludzi po schodach do gabinetu. Pana Tadeusza wniosłem osiemnaście razy. Za dziewiętnastym wszedł sam.",
 ], "Девять лет я заносил людей по лестнице в кабинет. Пана Тадеуша заносил восемнадцать раз. На девятнадцатый он вошёл сам."),

 ("E3", "медсестра ортопедического отделения", [
   "Na ortopedii mówimy o tym tylko na papierosie i nigdy przy pacjencie: większość tych operacji wraca do nas w ciągu pięciu lat.",
   "Na oddziale ortopedii mówimy o tym tylko na papierosie, nigdy przy pacjencie: większość tych operacji wraca do nas po pięciu latach.",
   "Na ortopedii mówimy o tym wyłącznie na papierosie i nigdy przy pacjencie: większość tych operacji wraca do nas po pięciu latach.",
 ], "В ортопедии мы говорим об этом только на перекуре и никогда при пациенте: большинство этих операций возвращается к нам за пять лет."),

 # ---------------- F. те, кто рядом ----------------
 ("F1", "развозит обеды пожилым", [
   "Rozwożę obiady starszym ludziom. Pod jednym adresem od marca nikt nie otwiera. Sąsiadka powiedziała, że pani Kazimiera poszła na grzyby.",
   "Rozwożę obiady starszym ludziom. Pod jednym adresem od marca nikt nie otwiera. Sąsiadka mówi, że pani Kazimiera poszła na grzyby.",
   "Rozwożę obiady starszym ludziom. W jednym mieszkaniu od marca nikt nie otwiera. Sąsiadka powiedziała, że pani Kazimiera poszła na grzyby.",
   "Rozwożę obiady starszym ludziom. Pod jednym adresem od marca nikt nie otwiera. Sąsiadka powiedziała, że pani Kazimiera poszła po grzyby.",
   "Rozwożę obiady starszym ludziom. Pod jednym adresem nikt nie otwiera od marca. Sąsiadka powiedziała, że pani Kazimiera poszła na grzyby.",
   "Rozwożę obiady starszym ludziom. Pod jednym adresem nikt nie otwiera. Sąsiadka mówi, że pani Kazimiera poszła na grzyby.",
 ], "Развожу обеды пожилым. По одному адресу никто не открывает. Соседка сказала, что пани Казимера ушла за грибами."),

 ("F2", "возил на процедуры", [
   "Woziłem tę samą kobietę na zabiegi w każdy wtorek przez dwa lata. W październiku zadzwoniła, żeby odwołać kurs na stałe.",
   "Woziłem tę samą kobietę na zabiegi w każdy wtorek przez dwa lata. W październiku zadzwoniła i odwołała kurs na stałe.",
   "Przez dwa lata woziłem tę samą kobietę na zabiegi, w każdy wtorek. W październiku zadzwoniła, żeby odwołać kurs na stałe.",
 ], "Два года я возил одну и ту же женщину на процедуры, каждый вторник. В октябре она позвонила отменить поездку насовсем."),

 ("F3", "шьёт ортопедическую обувь", [
   "Szyję buty ortopedyczne na miarę. Klient wraca co dwa lata z gorszą stopą, taki jest ten zawód. Pan Eugeniusz wrócił z lepszą.",
   "Szyję buty ortopedyczne na miarę. Klient wraca co dwa lata z gorszą stopą — taki jest ten zawód. Pan Eugeniusz wrócił z lepszą.",
   "Szyję na miarę buty ortopedyczne. Klient wraca co dwa lata z gorszą stopą, taki już jest ten zawód. Pan Eugeniusz wrócił z lepszą.",
 ], "Шью ортопедическую обувь. Клиент возвращается раз в два года с худшей стопой. А пан Эугениуш вернулся с лучшей."),
]

if __name__ == "__main__":
    import sys
    bad = 0
    for code, who, variants, ru in HOOKS:
        chosen = None
        for v in variants:
            if ok(v):
                chosen = v
                break
        if chosen is None:
            bad += 1
            print("FAIL %s: %s" % (code, [len(v) for v in variants]))
            for v in variants:
                print("   %3d %r" % (len(v), v))
            continue
        n = len(chosen)
        kind = "виден целиком" if n <= 120 else "обрыв на 125"
        print("%s [%d, %s] %s" % (code, n, kind, chosen))
        if n > 120:
            print("     видно: %s|" % chosen[:125])
        rn = len(ru)
        flag = "  <-- RU в мёртвой зоне" if 121 <= rn <= 126 else ""
        print("     RU [%d]%s %s" % (rn, flag, ru))
    print("\nFAIL: %d из %d" % (bad, len(HOOKS)))
