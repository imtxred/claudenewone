# 20 хуков к сторитейлу из видеокреатива «102 года» (PL, суставы)

Источник: `work/transcript/kreativ_102_let_PL_pol.txt`, разбор — `work/ops/razbor_kreativa_102_let_PL.md`  
Лендинг: `video11_pol` (Metonil), разбор — `work/ops/razbor_video11_PL_Metonil.md`  
Генератор и проверка: `work/tools/hooks_20_kreativ_102_src.py`

---

## Что переносим из креатива в сторитейл

Креатив — трёхминутный монолог, который **ничего не продаёт, а ставит рамку**. Сторитейл
должен делать то же самое на 133 абзацах, поэтому в хук уходит не финал, а **аномалия**:
факт, который сам по себе полон, а причина спрятана.

| Блок креатива | Куда идёт в сторитейле |
|---|---|
| 102 года, сам по лестнице | пункт назначения, финал воронки, не хук |
| Ровесники в колясках, тот же год | **хук** — контрольная группа в одной фразе |
| 70 лет резал, всё напрасно | **хук** — признание против себя |
| Скрывал 40 лет | цена правды + мотив рассказчика |
| Таблетка приближает к коляске | **хук** — враг в тумбочке |
| Три больницы отказали | четыре независимых источника называют одно место |
| Способность засыпает, её можно разбудить | механизм, абзацы 60–75%, не хук |
| Здоровье не позволяет принимать лично | «нет лаборатории», ~87% |
| Синяя кнопка, видео не навсегда | CTA, ~95% |

**Главная развилка.** В креативе рассказчик и есть герой. В сторитейле по рабочему
шаблону рассказчик — отдельная фигура, которая **теряет деньги, когда читатель
выздоравливает**, и которая в конце отправляет к старику. Группа A сохраняет голос
креатива, группы B–F ставят между читателем и стариком носителя системы. Ставку я бы
делал на B и C: там работают все девять инвариантов без натяжки.

---

## Спецификация обрыва (проверена скриптом на всех 20)

- либо **≤120 знаков** — виден целиком, «Ещё» не появляется;
- либо **127–143 знака**, причём 125-й знак попадает **внутрь слова**, а хвост после
  обрыва ≤18 знаков;
- **мёртвая зона 121–126 запрещена** — «Ещё» появляется, но прячет 2–3 знака,
  читается как техническая поломка;
- в видимой части — **законченный шок, причина спрятана**;
- проверено: ноль латиницы в русских версиях, ноль кириллицы в польских,
  имена не пересекаются с корпусом сторитейлов и с лендингами.

Все 20 прошли: `проблем: 0 из 20`.

---

## Группа A. Голос самого героя — 102-летний ортопед

Прямая конверсия креатива: рассказывает он сам. Максимально близко к видео, узнавание на лендинге стопроцентное. Минус — герой лендинга и рассказчик сливаются, воронка теряет фигуру «инсайдера, который отправляет к нему».

### A1 — голос героя лендинга, 102 года

**PL (в объявление):**  
Mam sto dwa lata i wczoraj sam wszedłem po schodach na trzecie piętro. Moi rówieśnicy, ci którzy jeszcze żyją, siedzą na wózkach.

`129 зн., обрыв на 125` → видно до «Ещё»:  
`Mam sto dwa lata i wczoraj sam wszedłem po schodach na trzecie piętro. Moi rówieśnicy, ci którzy jeszcze żyją, siedzą na wózk`

**RU (для чтения):** Мне сто два года, и вчера я сам поднялся по лестнице на третий этаж. Мои ровесники, те кто ещё жив, сидят в колясках.  
`117 зн.`

### A2 — голос героя лендинга, признание против себя

**PL (в объявление):**  
Byłem ortopedą siedemdziesiąt lat, przez moje ręce przeszło czterdzieści tysięcy ludzi. I prawie wszystko, co im robiłem, było na darmo.

`136 зн., обрыв на 125` → видно до «Ещё»:  
`Byłem ortopedą siedemdziesiąt lat, przez moje ręce przeszło czterdzieści tysięcy ludzi. I prawie wszystko, co im robiłem, był`

**RU (для чтения):** Семьдесят лет я был ортопедом, через мои руки прошло сорок тысяч человек. Почти всё, что я им делал, было напрасно.  
`115 зн.`

### A3 — голос героя лендинга, сорок лет молчания

**PL (в объявление):**  
Czterdzieści lat milczałem, bo za to odebrano by mi prawo wykonywania zawodu. Dziś mam sto dwa lata i nie mam już czego stracić.

`128 зн., обрыв на 125` → видно до «Ещё»:  
`Czterdzieści lat milczałem, bo za to odebrano by mi prawo wykonywania zawodu. Dziś mam sto dwa lata i nie mam już czego strac`

**RU (для чтения):** Сорок лет я молчал, потому что за это лишили бы права работать. Мне сто два года, мне больше нечего терять.  
`107 зн.`

### A4 — голос героя лендинга, враг в тумбочке

**PL (в объявление):**  
Nigdy nie mówiłem tego przy świadkach. Każda tabletka na ból stawów, którą pan dziś połknął, przybliżyła pana do wózka inwalidzkiego.

`133 зн., обрыв на 125` → видно до «Ещё»:  
`Nigdy nie mówiłem tego przy świadkach. Każda tabletka na ból stawów, którą pan dziś połknął, przybliżyła pana do wózka inwali`

**RU (для чтения):** Не говорил этого при свидетелях. Каждая таблетка от боли в суставах, что вы выпили утром, придвинула вас к коляске.  
`115 зн.`

---

## Группа B. Оперирующий ортопед — теряет деньги, когда читатель встаёт

Самая сильная позиция по шаблону BG/RS: рассказчик кормится операциями и сам от них отговаривает. Признание против собственного интереса читается как правда.

### B1 — оперирующий ортопед, отмены

**PL (в объявление):**  
Operuję kolana dwadzieścia lat. W zeszłym miesiącu czterech pacjentów odwołało zabieg trzy dni przed terminem, i żaden nie podał powodu.

`136 зн., обрыв на 125` → видно до «Ещё»:  
`Operuję kolana dwadzieścia lat. W zeszłym miesiącu czterech pacjentów odwołało zabieg trzy dni przed terminem, i żaden nie po`

**RU (для чтения):** Оперирую колени двадцать лет. В прошлом месяце четверо отменили операцию за три дня до срока. Ни один не назвал причину.  
`120 зн.`

### B2 — оперирующий ортопед, вернулась без операции

**PL (в объявление):**  
Powiedziałem jej: proszę się przygotować, po tej operacji nie wróci pani do ogrodu. Wróciła po pół roku — bez operacji, z workiem jabłek.

`137 зн., обрыв на 125` → видно до «Ещё»:  
`Powiedziałem jej: proszę się przygotować, po tej operacji nie wróci pani do ogrodu. Wróciła po pół roku — bez operacji, z wor`

**RU (для чтения):** Я сказал ей: готовьтесь, после этой операции вы уже не вернётесь в сад. Она пришла через полгода — без операции, с мешком яблок.  
`128 зн.`

### B3 — оперирующий ортопед, отговаривает от своего же хлеба

**PL (в объявление):**  
Mam dwa lata do emerytury i właśnie zacząłem odradzać ludziom operację, z której przez całe życie się utrzymywałem.

`115 зн., виден целиком`

**RU (для чтения):** Мне два года до пенсии, и я только что начал отговаривать людей от операции, которой кормился всю жизнь.  
`104 зн.`

### B4 — оперирующий ортопед, очередь тает

**PL (в объявление):**  
Na moim biurku leży lista dwudziestu siedmiu osób czekających na endoprotezę. Jedenaście z nich w tym roku po cichu się wypisało.

`129 зн., обрыв на 125` → видно до «Ещё»:  
`Na moim biurku leży lista dwudziestu siedmiu osób czekających na endoprotezę. Jedenaście z nich w tym roku po cichu się wypis`

**RU (для чтения):** У меня на столе список из двадцати семи человек в очереди на эндопротез. Одиннадцать в этом году тихо вычеркнулись сами.  
`120 зн.`

---

## Группа C. Металл, протезы, техника — те, кому падает выручка

Аномалия видна в цифрах бизнеса, а не в самочувствии. Метрика превращается в тела: заказы, ходунки, очередь.

### C1 — изготовитель протезов

**PL (в объявление):**  
Robię protezy stawów osiemnaście lat. W tym roku pierwszy raz musiałem zwolnić pracownika, bo zamówień przyszło o połowę mniej.

`127 зн., обрыв на 125` → видно до «Ещё»:  
`Robię protezy stawów osiemnaście lat. W tym roku pierwszy raz musiałem zwolnić pracownika, bo zamówień przyszło o połowę mnie`

**RU (для чтения):** Я делаю протезы суставов восемнадцать лет. В этом году впервые пришлось уволить человека — заказов вдвое меньше.  
`112 зн.`

### C2 — прокат реабилитационной техники

**PL (в объявление):**  
Wypożyczalnia sprzętu rehabilitacyjnego, dwanaście lat. Nikt nigdy nie oddał balkonika przed terminem. W maju oddano mi cztery.

`127 зн., обрыв на 125` → видно до «Ещё»:  
`Wypożyczalnia sprzętu rehabilitacyjnego, dwanaście lat. Nikt nigdy nie oddał balkonika przed terminem. W maju oddano mi czter`

**RU (для чтения):** Двенадцать лет держу прокат реабилитационной техники. Никто никогда не сдавал ходунки раньше срока. В мае сдали четверо.  
`120 зн.`

### C3 — поставщик металла для эндопротезов

**PL (в объявление):**  
Zadzwonił do mnie dostawca metalu do endoprotez i zapytał, czy coś się stało w naszym powiecie. Zamówienia spadły o czterdzieści procent.

`137 зн., обрыв на 125` → видно до «Ещё»:  
`Zadzwonił do mnie dostawca metalu do endoprotez i zapytał, czy coś się stało w naszym powiecie. Zamówienia spadły o czterdzie`

**RU (для чтения):** Позвонил поставщик металла для эндопротезов, спросил, что у нас случилось. Заказы упали на сорок процентов.  
`107 зн.`

---

## Группа D. Аптека и фарма — носитель системы

Отсюда берётся дословная циничная цитата системы, один из девяти инвариантов.

### D1 — владелец аптеки

**PL (в объявление):**  
Prowadzę aptekę dziewiętnaście lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego tak jest.

`128 зн., обрыв на 125` → видно до «Ещё»:  
`Prowadzę aptekę dziewiętnaście lat. Najlepiej sprzedaje mi się to, co nie leczy, i dopiero w maju usłyszałem, dlaczego tak je`

**RU (для чтения):** Девятнадцать лет держу аптеку. Лучше всего продаётся то, что не лечит, и только в мае я услышал, почему так.  
`108 зн.`

### D2 — фармпредставитель

**PL (в объявление):**  
Przez jedenaście lat uczyłem lekarzy zapisywać maść, o której wiedziałem, że nie wchodzi głębiej niż na dwa milimetry.

`118 зн., виден целиком`

**RU (для чтения):** Одиннадцать лет я учил врачей выписывать мазь, о которой знал, что она не проходит глубже двух миллиметров.  
`107 зн.`

### D3 — фармпредставитель, премия

**PL (в объявление):**  
Moja premia liczy się od tego, ilu pacjentów wróci po drugie opakowanie. Nie od tego, ilu z nich wyzdrowieje.

`109 зн., виден целиком`

**RU (для чтения):** Мою премию считают по тому, сколько пациентов вернётся за второй упаковкой. Не по тому, сколько выздоровеет.  
`108 зн.`

---

## Группа E. Те, кто ставит на ноги руками

Рассказчик видит результат физически, а не по бумагам. Самые тактильные хуки.

### E1 — реабилитолог

**PL (в объявление):**  
Jestem rehabilitantką. Pani Leokadia chodziła do mnie cztery lata i nagle przestała. Myślałam, że umarła. Spotkałam ją na targu, z siatkami.

`140 зн., обрыв на 125` → видно до «Ещё»:  
`Jestem rehabilitantką. Pani Leokadia chodziła do mnie cztery lata i nagle przestała. Myślałam, że umarła. Spotkałam ją na tar`

**RU (для чтения):** Я реабилитолог. Пани Леокадия ходила ко мне четыре года и вдруг перестала. Я решила — умерла. Встретила её на рынке.  
`116 зн.`

### E2 — санитар, носил по лестнице

**PL (в объявление):**  
Dziewięć lat wnosiłem ludzi po schodach do gabinetu. Pana Tadeusza wnosiłem osiemnaście razy. Za dziewiętnastym wszedł o własnych siłach.

`137 зн., обрыв на 125` → видно до «Ещё»:  
`Dziewięć lat wnosiłem ludzi po schodach do gabinetu. Pana Tadeusza wnosiłem osiemnaście razy. Za dziewiętnastym wszedł o włas`

**RU (для чтения):** Девять лет я заносил людей по лестнице в кабинет. Пана Тадеуша заносил восемнадцать раз. На девятнадцатый он вошёл сам.  
`119 зн.`

### E3 — медсестра ортопедического отделения

**PL (в объявление):**  
Na ortopedii mówimy o tym wyłącznie na papierosie i nigdy przy pacjencie: większość tych operacji wraca do nas po pięciu latach.

`128 зн., обрыв на 125` → видно до «Ещё»:  
`Na ortopedii mówimy o tym wyłącznie na papierosie i nigdy przy pacjencie: większość tych operacji wraca do nas po pięciu lata`

**RU (для чтения):** В ортопедии мы говорим об этом только на перекуре и никогда при пациенте: большинство этих операций возвращается к нам за пять лет.  
`131 зн.`

---

## Группа F. Те, кто рядом каждый день

Свидетель без медицинского интереса. Мягкий вход, ниже сопротивление, но слабее мотив «теряю деньги».

### F1 — развозит обеды пожилым

**PL (в объявление):**  
Rozwożę obiady starszym ludziom. Pod jednym adresem od marca nikt nie otwiera. Sąsiadka mówi, że pani Kazimiera poszła na grzyby.

`129 зн., обрыв на 125` → видно до «Ещё»:  
`Rozwożę obiady starszym ludziom. Pod jednym adresem od marca nikt nie otwiera. Sąsiadka mówi, że pani Kazimiera poszła na grz`

**RU (для чтения):** Развожу обеды пожилым. По одному адресу никто не открывает. Соседка сказала, что пани Казимера ушла за грибами.  
`111 зн.`

### F2 — возил на процедуры

**PL (в объявление):**  
Woziłem tę samą kobietę na zabiegi w każdy wtorek przez dwa lata. W październiku zadzwoniła, żeby odwołać kurs na stałe.

`120 зн., виден целиком`

**RU (для чтения):** Два года я возил одну и ту же женщину на процедуры, каждый вторник. В октябре она позвонила отменить поездку насовсем.  
`118 зн.`

### F3 — шьёт ортопедическую обувь

**PL (в объявление):**  
Szyję buty ortopedyczne na miarę. Klient wraca co dwa lata z gorszą stopą — taki jest ten zawód. Pan Eugeniusz wrócił z lepszą.

`127 зн., обрыв на 125` → видно до «Ещё»:  
`Szyję buty ortopedyczne na miarę. Klient wraca co dwa lata z gorszą stopą — taki jest ten zawód. Pan Eugeniusz wrócił z lepsz`

**RU (для чтения):** Шью ортопедическую обувь. Клиент возвращается раз в два года с худшей стопой. А пан Эугениуш вернулся с лучшей.  
`111 зн.`

---

## Рекомендация по запуску

1. Первым тестом — **B3, C2, A2**. Три разных механики: отказ от собственного хлеба,
   бизнес-аномалия, признание против себя. Они максимально не похожи друг на друга,
   поэтому по ним видно, какая ветка вообще заходит.
2. Вторым заходом — победившая ветка целиком (все её хуки на один и тот же сторитейл).
3. Группу A держать отдельно: если зайдёт она, сторитейл придётся писать от первого
   лица старика, и тогда лендинг превращается в продолжение письма, а не в пункт
   назначения. Это другая воронка, её нельзя мешать с B–F в одном адсете.
