# 30 хуков к сторитейлам: паразиты, HU, лендинг с патологом

Класс I — хук к сторитейлу на 133 абзаца. Лендинг: `work/landings/HU/Helmiron_HU_patolog/index.html`
(д-р Kovács Gábor, патолог, 35 лет и 9000 вскрытий; д-р Szabó Ilona, сельский ветеринар; Erzsébet, 62).
Файлы: `work/hooks/hooks_30_parazity_HU_patolog_hu.txt` (венгерский, в заливку),
`work/hooks/hooks_30_parazity_HU_patolog_ru.txt` (русский, для чтения).

Батарея: `python3 work/tools/check_hooks.py work/hooks/hooks_30_parazity_HU_patolog_hu.txt --alphabet latin --brand HELMIRON` → **проблем: 0 из 30**.

| | |
|---|---|
| Всего | 30 |
| Видны целиком (≤120) | 15 |
| С обрывом на 125 (130–143, внутри слова) | 15 |
| Мёртвая зона 121–129 | 0 |
| Слово-диагноз («paraziták», «giliszta», «féreg») | 0 вхождений |
| Название препарата | 0 вхождений |
| Имён собственных | 0 — в хуках нет ни одного |
| Пересечения с лендингом и его комментаторами | 0 |
| Восклицательных знаков, капса, кириллицы | 0 |

Скрытая часть у всех длинных не меньше пяти знаков: на 127–129 «Ещё» прячет два-три знака
и читается как мёртвая зона, хоть формально и проходит.

**Главное ограничение этой пачки.** Слово «паразиты» не звучит ни в одном из тридцати.
Ни в одном не назван ни один из диагнозов, которыми лендинг играет (gyomorhurut, allergia,
neurózis), и ни в одном нет пункта назначения: ни патолога, ни ветеринара, ни капсул,
ни рецепта. Читатель должен понять, ЧТО случилось, и не понять ПОЧЕМУ.

---

## Группа A. Лаборатория и диагностика

Тот, кто пишет «всё в порядке» и знает, что это значит только «мы искали не то». Теряет деньги на повторных анализах и на бесконечном приёме.

**A1** · 141 зн. · обрыв на 125

> Tizennégy éve írom a leletekre, hogy „minden rendben". Ez nem azt jelenti, hogy nincs semmi. Azt jelenti, hogy nem azt kerestük. Egyszer sem.

Видно: `Tizennégy éve írom a leletekre, hogy „minden rendben". Ez nem azt jelenti, hogy nincs semmi. Azt jelenti, hogy nem azt kerest`  
Скрыто: `ük. Egyszer sem.`

*Четырнадцать лет я пишу в заключениях «всё в порядке». Это не значит, что ничего нет. Это значит, что мы искали не то. Ни разу не искали.*

**A2** · 132 зн. · обрыв на 125

> A laborban egy név hat éven át ugyanazt az eredményt adta. Áprilisban tisztán jött vissza, és háromszor ellenőriztem. Nem hittem el.

Видно: `A laborban egy név hat éven át ugyanazt az eredményt adta. Áprilisban tisztán jött vissza, és háromszor ellenőriztem. Nem hit`  
Скрыто: `tem el.`

*В лаборатории одна фамилия шесть лет давала один и тот же результат. В апреле пришёл чистый, и я перепроверила трижды. Не поверила.*

**A3** · 140 зн. · обрыв на 125

> „Ismeretlen eredetű kiütés" — ezt írom le naponta többször. Tizenegy év alatt egy beteg sem kérdezte meg, mit jelent ez. Egyetlen beteg sem.

Видно: `„Ismeretlen eredetű kiütés" — ezt írom le naponta többször. Tizenegy év alatt egy beteg sem kérdezte meg, mit jelent ez. Egye`  
Скрыто: `tlen beteg sem.`

*«Сыпь неизвестного происхождения» — я пишу это по нескольку раз в день. За одиннадцать лет ни один больной не спросил, что это значит. Ни один.*

**A4** · 102 зн. · виден целиком

> Vashiányra adok tablettát nyolc éve ugyanannak a nőnek. A vas elmegy valahová, és nem az ő csontjaiba.

*Я восемь лет выписываю таблетки от нехватки железа одной и той же женщине. Железо куда-то уходит, и не в её кости.*

**A5** · 132 зн. · обрыв на 125

> Gasztroszkópiát végzek tizenkét éve. Látom a falat belülről. Van, amit gyakran látok, és amit nem írok le a leletbe. Nem véletlenül.

Видно: `Gasztroszkópiát végzek tizenkét éve. Látom a falat belülről. Van, amit gyakran látok, és amit nem írok le a leletbe. Nem véle`  
Скрыто: `tlenül.`

*Я делаю гастроскопии двенадцать лет. Я вижу стенку изнутри. Есть то, что я вижу часто и не пишу в заключении. Не случайно.*

## Группа B. Аптека

Продаёт шесть линеек одному человеку: одну от желудка, вторую от того, что испортила первая. Вертикаль паразитов построена на повторной покупке — это и есть признание против себя.

**B1** · 110 зн. · виден целиком

> Tizenhét éve van gyógyszertáram. Egy ember hat különböző dobozt visz haza egyszerre. És ezt hívjuk kezelésnek.

*Семнадцать лет у меня аптека. Один человек уносит домой шесть разных упаковок за раз. И это мы называем лечением.*

**B2** · 137 зн. · обрыв на 125

> Minden tavasszal ugyanazok az emberek jönnek ugyanazért a tablettáért. Idén egy asszony azt mondta, hogy már nem kell neki. Megkérdeztem.

Видно: `Minden tavasszal ugyanazok az emberek jönnek ugyanazért a tablettáért. Idén egy asszony azt mondta, hogy már nem kell neki. M`  
Скрыто: `egkérdeztem.`

*Каждую весну одни и те же люди приходят за одной и той же таблеткой. Этой весной одна женщина сказала, что ей больше не надо. Я спросил.*

**B3** · 115 зн. · виден целиком

> A gyógyszertárban tudom, ki mivel él. Ősszel három állandó vásárlóm abbahagyta, és egyik sem magyarázta meg, miért.

*В аптеке я знаю, кто чем живёт. Осенью трое постоянных покупателей перестали брать, и ни один не объяснил почему.*

**B4** · 137 зн. · обрыв на 125

> Eladtam az embernek a tablettát a gyomrára, aztán a másikat arra, amit az első elrontott. Hat doboz, minden hónapban. Így ment ez évekig.

Видно: `Eladtam az embernek a tablettát a gyomrára, aztán a másikat arra, amit az első elrontott. Hat doboz, minden hónapban. Így men`  
Скрыто: `t ez évekig.`

*Я продал человеку таблетку для желудка, потом вторую — от того, что испортила первая. Шесть упаковок, каждый месяц. Так шло годами.*

**B5** · 106 зн. · виден целиком

> Negyvenhét név van a füzetemben, emberek, akik minden hónapban bejöttek. Tizennégy közülük már nem jön be.

*В моей тетради сорок семь имён — людей, которые приходили каждый месяц. Четырнадцать из них больше не приходят.*

## Группа C. Императив-инструкция

Человеку сразу выдают действие, а не обещание. Лучше всех проходит модерацию: ни диагноза, ни обещания, ни цифры. Обязательное условие — первый кадр показывает само движение.

**C1** · 110 зн. · виден целиком

> Ma éjjel figyelje meg, nem csikorgatja-e a fogát az, aki ön mellett alszik. Reggel kérdezze meg tőle ugyanezt.

*Сегодня ночью проверьте, не скрежещет ли зубами тот, кто спит рядом с вами. Утром спросите его то же самое про вас.*

**C2** · 95 зн. · виден целиком

> Álljon a tükör elé a lámpa alatt. Ne az arcát nézze, hanem a nyelvét és a szemhéja alatti bőrt.

*Встаньте перед зеркалом под лампой. Смотрите не на лицо, а на язык и на кожу под веками.*

**C3** · 106 зн. · виден целиком

> Álljon a mérlegre, aztán írja fel, mit evett ma. Ha a két szám nem illik össze, valaki más is eszik önnel.

*Встаньте на весы, потом запишите, что вы съели сегодня. Если два числа не сходятся, кто-то ещё ест вместе с вами.*

**C4** · 92 зн. · виден целиком

> Kérdezze meg az unokáját, miért nem alszik szívesen a nagymamánál. Ne javítsa ki, amit mond.

*Спросите внука, почему он не хочет спать у бабушки. Не поправляйте то, что он скажет.*

**C5** · 111 зн. · виден целиком

> Keljen fel hajnali háromkor és jegyezze fel, mit érez. Ha ez a hetedik ilyen éjszaka, nem az idegeiről van szó.

*Встаньте в три часа ночи и запишите, что чувствуете. Если это седьмая такая ночь, дело не в нервах.*

## Группа D. Свидетель без интереса

Уборщица, мясник, кухня дома престарелых, воспитательница, прачка. Мягкий вход, нулевой мотив врать, никакой медицины в кадре.

**D1** · 139 зн. · обрыв на 125

> Húsz éve mosom egy iskola padlóját. Minden szeptemberben tudom, melyik osztályban lesz baj, mire a szülők megtudják. Nem a tanárok szólnak.

Видно: `Húsz éve mosom egy iskola padlóját. Minden szeptemberben tudom, melyik osztályban lesz baj, mire a szülők megtudják. Nem a ta`  
Скрыто: `nárok szólnak.`

*Двадцать лет я мою полы в школе. Каждый сентябрь я знаю, в каком классе будет беда, раньше, чем узнают родители. Не от учителей.*

**D2** · 137 зн. · обрыв на 125

> Hentes vagyok, huszonkét éve. Tudom, hogy néz ki az a máj, amit ki kell dobni. Tavasszal ugyanazt láttam egy képernyőn. Orvosi képernyőn.

Видно: `Hentes vagyok, huszonkét éve. Tudom, hogy néz ki az a máj, amit ki kell dobni. Tavasszal ugyanazt láttam egy képernyőn. Orvos`  
Скрыто: `i képernyőn.`

*Я мясник, двадцать два года. Я знаю, как выглядит печень, которую надо выбросить. Весной я увидел такую же на экране. На медицинском.*

**D3** · 98 зн. · виден целиком

> Konyhán dolgozom egy idősek otthonában. Látom, kinek a tányérja üres, és kinek fogy mégis a súlya.

*Я работаю на кухне в доме престарелых. Я вижу, у кого тарелка пустая, и у кого при этом уходит вес.*

**D4** · 142 зн. · обрыв на 125

> Minden ősszel mintát veszünk a gyerekektől. A szülő csak a saját gyereke eredményét látja. Én az egész csoport listáját. Minden évben ugyanaz.

Видно: `Minden ősszel mintát veszünk a gyerekektől. A szülő csak a saját gyereke eredményét látja. Én az egész csoport listáját. Mind`  
Скрыто: `en évben ugyanaz.`

*Каждую осень мы берём пробы у детей. Родитель видит только результат своего ребёнка. Я — список всей группы. Каждый год одно и то же.*

**D5** · 110 зн. · виден целиком

> Ágyneműt mosok egy szállodában. Meg tudom mondani, ki aludt rosszul és ki nem aludt egyáltalán. Egy lepedőből.

*Я стираю постельное в гостинице. Я могу сказать, кто спал плохо и кто не спал вообще. По одной простыне.*

## Группа E. Те, кто рядом с больным

Дети и внуки. Покупает не больной, а они. ОТДЕЛЬНЫЙ АДСЕТ — тянет 30–45, а не 55–70.

**E1** · 141 зн. · обрыв на 125

> Anyám hat éven át azt mondta a telefonban, hogy jól van. Külföldről nem látszik, hogy valaki minden hónapban kevesebb. Vasárnaponként hívtam.

Видно: `Anyám hat éven át azt mondta a telefonban, hogy jól van. Külföldről nem látszik, hogy valaki minden hónapban kevesebb. Vasárn`  
Скрыто: `aponként hívtam.`

*Мать шесть лет говорила мне по телефону, что у неё всё хорошо. Издалека не видно, что человек каждый месяц становится меньше. Я звонила по воскресеньям.*

**E2** · 134 зн. · обрыв на 125

> Apám normálisan evett és közben fogyott. Anyám azzal viccelt, hogy gyors az anyagcseréje. Egy éven át viccelt ezzel. Aztán abbahagyta.

Видно: `Apám normálisan evett és közben fogyott. Anyám azzal viccelt, hogy gyors az anyagcseréje. Egy éven át viccelt ezzel. Aztán ab`  
Скрыто: `bahagyta.`

*Отец ел нормально и при этом худел. Мать шутила, что у него быстрый обмен. Она шутила об этом целый год. Потом перестала.*

**E3** · 103 зн. · виден целиком

> Pénzt küldtem haza minden hónapban. Azt hittem, ez a segítség. Nem néztem meg, mi van a konyhaasztalon.

*Я каждый месяц посылала деньги домой. Думала, что это и есть помощь. Я не посмотрела, что стоит на кухонном столе.*

**E4** · 109 зн. · виден целиком

> A lányom nem akart többé a nagymamájánál aludni. Nem tudta megmondani, miért. Három éven át nem kérdeztem rá.

*Моя дочь перестала хотеть спать у бабушки. Она не могла объяснить почему. Три года я не спрашивала.*

**E5** · 142 зн. · обрыв на 125

> Anyám minden leletét megtartotta egy dossziéban. Mindegyik azt mondta: minden rendben. A dosszié hat centi vastag volt. Nem nyitotta ki senki.

Видно: `Anyám minden leletét megtartotta egy dossziéban. Mindegyik azt mondta: minden rendben. A dosszié hat centi vastag volt. Nem n`  
Скрыто: `yitotta ki senki.`

*Мать хранила все свои заключения в папке. В каждом было написано: всё в порядке. Папка была толщиной шесть сантиметров. Её никто не открыл.*

## Группа F. Голос героев лендинга

Патолог и ветеринар со страницы. ОТДЕЛЬНЫЙ АДСЕТ, вне сравнения первого теста: у него другая экономика, рассказчик и пункт назначения сливаются.

**F1** · 135 зн. · обрыв на 125

> Harmincöt évig nyitottam fel embereket. A jegyzőkönyvbe azt írtam, amit kérdeztek. Amit láttam, arról nem kérdezett senki. Egyszer sem.

Видно: `Harmincöt évig nyitottam fel embereket. A jegyzőkönyvbe azt írtam, amit kérdeztek. Amit láttam, arról nem kérdezett senki. Eg`  
Скрыто: `yszer sem.`

*Тридцать пять лет я вскрывал людей. В протокол я писал то, о чём меня спрашивали. О том, что я видел, не спросил никто. Ни разу.*

**F2** · 105 зн. · виден целиком

> Kilencezer boncolás után egyetlen dolgot tanultam meg: a halál okát ritkán keresik ott, ahol valóban van.

*После девяти тысяч вскрытий я понял одно: причину смерти редко ищут там, где она в самом деле есть.*

**F3** · 130 зн. · обрыв на 125

> Egy ötvennyolc éves férfi szívrohamban halt meg. A szíve rendben volt. Ami a májában volt, annak nem lett volna szabad ott lennie.

Видно: `Egy ötvennyolc éves férfi szívrohamban halt meg. A szíve rendben volt. Ami a májában volt, annak nem lett volna szabad ott le`  
Скрыто: `nnie.`

*Пятидесятивосьмилетний мужчина умер от инфаркта. Сердце было в порядке. То, что было в его печени, не должно было там быть.*

**F4** · 107 зн. · виден целиком

> A kutyát évente kétszer kezeljük, a lovat ütemterv szerint, a marhát is. Az embert, aki mellettük él, soha.

*Собаку мы обрабатываем дважды в год, коня по графику, скот тоже. Человека, который живёт рядом с ними, — никогда.*

**F5** · 136 зн. · обрыв на 125

> Egy tehén miatt mentem ki egy házhoz. A tehénnel nem volt komoly baj. A gazdasszonyával igen, és ő nem tudott róla. Én a tehenet néztem.

Видно: `Egy tehén miatt mentem ki egy házhoz. A tehénnel nem volt komoly baj. A gazdasszonyával igen, és ő nem tudott róla. Én a tehe`  
Скрыто: `net néztem.`

*Я приехала на двор из-за коровы. С коровой ничего серьёзного не было. С хозяйкой было, и она об этом не знала. Я смотрела корову.*

---

## Что раскрывает тело сторитейла

| В хуке | Сшивается с лендингом как |
|---|---|
| «всё в порядке» в заключении | нормальные анализы при угасающем теле — центральный блок страницы |
| железо уходит не в её кости | женщина 64 лет, анемия, «что-то съедало железо вместо неё» |
| шесть упаковок в месяц | пять-шесть товарных линеек на одного пациента |
| кто-то ещё ест вместе с вами | мужчина 67 лет, худел при нормальной еде, «быстрый обмен» |
| седьмая ночь подряд в три часа | скрежет зубами и пробуждение около трёх из списка симптомов |
| печень, которую надо выбросить | вскрытие пятидесятивосьмилетнего |
| корову посмотрели, хозяйку нет | та самая фраза ветеринара, с которой начинается страница |

## Первым тестом — три максимально непохожие механики

Не три лучшие формулировки, иначе тест не покажет ничего.

1. **B1** — бизнес-аномалия в чистом виде: аптека, одна цифра, ноль медицины и ноль симптомов.
2. **C3** — императив, лучше всех проходит модерацию и даёт самый дешёвый клик.
3. **D5** — свидетель без интереса, прачка в гостинице: ни врача, ни диагноза, ни кабинета.

Группы E и F — отдельные адсеты, вне сравнения. E тянет другой возраст, F сливает
рассказчика с пунктом назначения и живёт по своей экономике.

## Стык с первым экраном

| Группа | Первый абзац сторитейла обязан |
|---|---|
| A. Лаборатория | начать с бумаги в руках, а не с человека |
| B. Аптека | дать цифру раньше, чем профессию |
| C. Императив | показать само действие: лампу, зеркало, весы, часы |
| D. Свидетель | дать бытовой кадр до любого медицинского слова |
| E. Те, кто рядом | открыть телефонным разговором, а не диагнозом |
| F. Голос героя | назвать стаж вслух в первой строке |

## Что переиспользовано из старой пачки

Из `hooks_20_BG_parazity` взяты и переложены на этот лендинг шесть механик:
лаборант с фамилией, которая шесть лет давала один результат (A2); дерматологическая
«сыпь неизвестного происхождения» (A3); гастроскопия и то, что не пишут в заключении (A5);
аптекарь с повторной покупкой (B1); мясник с печенью на бойне (D2); воспитательница
с осенними пробами (D4).

Остальные двадцать четыре — новые, и построены на том, чего в болгарском лендинге
не было: девять тысяч вскрытий, «причина смерти в протоколе», железо, которое уходит
не в кости, шесть упаковок на одного человека, папка с заключениями, и реплика
ветеринара про животное, которое защищено лучше хозяина.
