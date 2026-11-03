# -*- coding: utf-8 -*-
"""Адаптация HU-лендинга HELMIRON на болгарское гео, блок в блок.
Меняются: язык, имена, топонимы, валюта, страна. Структура, вёрстка,
картинки, порядок блоков, форма — не трогаются.
"""
import sys

SRC, DST = sys.argv[1], sys.argv[2]
t = open(SRC, encoding="utf-8").read()

R = []
def rep(a, b, n=1):
    R.append((a, b, n))

# ---------- голова ----------
rep('<html lang="hu">', '<html lang="bg">')
rep('<title>„Láttam őket azok testében, akiknek fogalmuk sem volt róla” — magyar patológus felfedi a hallgatásba burkolt igazságot a parazitákról</title>',
    '<title>„Виждал съм ги в телата на хора, които не са имали никаква представа" — български патолог разкрива премълчаваната истина за паразитите</title>')

# ---------- шапка ----------
rep('Különjelentés · Egészség és Társadalom', 'Специален репортаж · Здраве и общество')
rep('Magyar Egészségügyi Tájékoztató', 'Български здравен информатор', 2)
rep('Riportok a népegészségügy világából', 'Репортажи от света на общественото здраве')

# ---------- заголовок ----------
rep('„ÉVEKIG ÉLTEK BENNEM, ÉN MEG AZ ÉLETKOROMRA ÉS A FÁRADTSÁGOMRA FOGTAM.”',
    '„ГОДИНИ ЖИВЯХА В МЕН, А АЗ ВИНЯХ ВЪЗРАСТТА И УМОРАТА."')
rep('35 ÉVES TAPASZTALATTAL RENDELKEZŐ PATOLÓGUS FELFEDI AZ IGAZSÁGOT, AMIT SENKI NEM AKAR HALLANI: A PARAZITÁK CSENDBEN PUSZTÍTJÁK A TESTET BELÜLRŐL — ÉS A HALÁL VALÓDI OKÁT MAJDNEM SOHA NEM KERESIK. EGY NŐ TÖRTÉNETE, AKI IDŐBEN MEGMENTETTE MAGÁT.',
    'ПАТОЛОГ С 35 ГОДИНИ ОПИТ РАЗКРИВА ИСТИНАТА, КОЯТО НИКОЙ НЕ ИСКА ДА ЧУЕ: ПАРАЗИТИТЕ ТИХО РАЗРУШАВАТ ТЯЛОТО ОТВЪТРЕ — А ИСТИНСКАТА ПРИЧИНА ЗА СМЪРТТА ПОЧТИ НИКОГА НЕ СЕ ТЪРСИ. ИСТОРИЯТА НА ЕДНА ЖЕНА, КОЯТО СЕ СПАСИ НАВРЕМЕ.')
rep('Közzétéve: ', 'Публикувано: ')

# ---------- герой-картинка ----------
rep('Erzsébet a háza előtt egy alföldi faluban', 'Денка пред къщата си в село в Лудогорието')
rep('Patológus megerősítette', 'Потвърдено от патолог')

# ---------- подзаголовок ----------
rep('Hogyan kezelte évekig Erzsébet (62 éves), háztartásbeli egy alföldi faluban a „gyomorhurutot”, „allergiát” és a „krónikus fáradtságot” — miközben orvosokra költötte a pénzt, akik sosem keresték a valódi okot. Egészen addig, amíg a falusi állatorvos fel nem tett neki egy kérdést, ami megváltoztatta az életét: „Mikor féregtelenítette utoljára önmagát?” Ami ezután következett, azt egy 35 éves tapasztalattal rendelkező patológus is megerősítette.',
    'Как Денка (62 години), домакиня от село в Лудогорието, години наред лекуваше „гастрит", „алергия" и „хронична умора" — докато даваше пари на лекари, които никога не потърсиха истинската причина. До деня, в който селският ветеринарен лекар ѝ зададе въпрос, който промени живота ѝ: „А себе си кога се обезпаразитихте за последно?" Това, което последва, беше потвърдено и от патолог с 35 години опит.')

# ---------- первые абзацы ----------
rep('Egy kedd reggel érkeztünk egy alföldi faluba, Szeged közelébe. Az út egy földúton vezet, régi házak, kertek és ugató kutyák mellett. Erzsébet a kapunál fogadott minket, a köténye még mindig a derekán volt — éppen főzött valamit. „Bárcsak tudnák, hány évet vesztettem el” — mondta köszönés helyett. „Mennyi pénzt. Hány orvost. És a válasz olyan egyszerű volt, hogy még most is rosszul leszek, ha arra gondolok.”',
    'Пристигнахме един вторник сутринта в село в Лудогорието, близо до Силистра. Влиза се по черен път, покрай стари къщи, градини и лаещи кучета. Денка ни посрещна на портата, с престилката още на кръста — точно готвеше нещо. „Да знаете колко години изгубих" — каза вместо добър ден. „Колко пари. Колко лекари. А отговорът беше толкова прост, че и сега ми прилошава, когато се сетя."')
rep('Erzsébet 62 éves. Egész életét ebben a faluban élte le — kert, gazdaság, szombati vásár. Soha nem volt betegeskedő asszony. De az elmúlt hat évben, ahogy mondja, „lassan kihunyt”, és senki nem tudta, miért.',
    'Денка е на 62 години. Цял живот е изкарала в това село — градината, стопанството, съботният пазар. Никога не е била болнава жена. Но през последните шест години, както сама казва, „угасваше бавно", и никой не знаеше защо.')
rep('Az ok? Évekig nem azt kezelte, amit kellett volna. <b>Az orvosok gyomorhurutot mondtak neki. Aztán allergiát. Aztán „krónikus fáradtságot”. Aztán „neurózist”.</b> Minden szakember a saját tünetét kezelte — de senki nem kereste azt, ami mindezt kiváltotta. Pénzt költött gasztroenterológusra, bőrgyógyászra, vizsgálatokra, amelyek semmit sem mutattak. És közben az életkorát és a fáradtságát hibáztatta.',
    'Причината? Години наред не лекуваше това, което трябваше. <b>Лекарите ѝ казаха гастрит. После алергия. После „хронична умора". После „невроза".</b> Всеки специалист лекуваше своя симптом — но никой не търсеше онова, което отключваше всичко това. Даваше пари за гастроентеролог, за дерматолог, за изследвания, които не показваха нищо. А през цялото време винеше възрастта и умората.')

# ---------- две цитаты героини ----------
rep('„Azt hittem, ez az öregség. Hogy normális, ha állandóan fáradt vagyok, puffadok, viszket a bőröm, ebéd után úgy elálmosodok, mintha valaki kikapcsolna. Mindenki azt mondta: „Hát az életkor, Erzsébet, mit akarsz.” De ez nem az öregség volt. Valami élő volt bennem.”',
    '„Мислех, че това е старостта. Че е нормално да съм постоянно уморена, да се подувам, да ме сърби кожата, след обяд да ме унася, като че ли някой ме изключва. Всички ми казваха: „Ами то е възрастта, Денке, какво искаш." Но това не беше старостта. В мен имаше нещо живо."')
rep('„A legrosszabb az, hogy minden vizsgálatom rendben volt. A vérképem „normális”. Akkor hogyan érezhetem magam így, ha valaki lassan felfal belülről? Csak amikor az állatorvos megmondta, mit keressek — és amikor a patológus a szemembe nézett és elmondta az igazságot —, akkor értettem meg mindent.”',
    '„Най-лошото е, че всичките ми изследвания бяха наред. Кръвната картина „нормална". Тогава как мога да се чувствам така, ако някой ме изяжда бавно отвътре? Едва когато ветеринарният лекар ми каза какво да търся — и когато патологът ме погледна в очите и ми каза истината — тогава разбрах всичко."')
rep('— Erzsébet, 62 éves, Alföld', '— Денка, 62 години, Лудогорие', 3)

# ---------- интервью патолога ----------
rep('„Láttam őket azok testében, akiknek fogalmuk sem volt róla, hogy hordozzák”',
    '„Виждал съм ги в телата на хора, които не са и подозирали, че ги носят в себе си"')
rep('<span>Exkluzív interjú dr. Kovács Gáborral — 35 éves tapasztalattal rendelkező patológussal, aki több mint 9000 boncolást végzett</span>',
    '<span>Ексклузивно интервю с д-р Запрян Калайджиев — патолог с 35 години опит, извършил над 9000 аутопсии</span>')
rep('Dr. Kovács Gábor: „Harmincöt évig dolgoztam patológusként. Minden korosztályú emberek testét nyitottam fel — és amit újra és újra láttam, azt a nyilvánosság nem tudja, mert hallgatnak róla. <b>Paraziták. Nem a peremvidéken élőknél, nem a „piszkosaknál” — hanem hétköznapi embereknél. Háztartásbelieknél, nyugdíjasoknál, munkásoknál. Olyanoknál, akik életükben azt hitték, hogy teljesen egészségesek.</b>',
    'Д-р Запрян Калайджиев: „Тридесет и пет години работих като патолог. Отварях тела на хора от всички възрасти — а онова, което виждах отново и отново, обществото не го знае, защото за него се мълчи. <b>Паразити. Не у хората в края на обществото, не у „мръсните" — а у най-обикновени хора. У домакини, у пенсионери, у работници. У хора, които цял живот са вярвали, че са напълно здрави.</b>')
rep('<b>SZÍVROHAMRA, AGYVÉRZÉSRE, ARRA HALTÁK MEG, AMIT „ISMERETLEN EREDETŰ DAGANATNAK” NEVEZTEK —\n          <span class="red-txt">DE A VALÓDI OKOT SENKI NEM KERESTE. MERT SENKINEK NEM JUTOTT ESZÉBE, HOGY ODA NÉZZEN.”</span></b>',
    '<b>УМИРАХА ОТ ИНФАРКТ, ОТ МОЗЪЧЕН ИНСУЛТ, ОТ ОНОВА, КОЕТО НАРИЧАХА „ТУМОР С НЕИЗВЕСТЕН ПРОИЗХОД" —\n          <span class="red-txt">А ИСТИНСКАТА ПРИЧИНА НИКОЙ НЕ ПОТЪРСИ. ЗАЩОТО НА НИКОГО НЕ МУ ДОЙДЕ НА УМ ДА ПОГЛЕДНЕ ТАМ."</span></b>')
rep('Dr. Kovács nyugodtan beszél, drámaiság nélkül — mint aki túl sokszor látta a történetek végét. Néhány éve nyugdíjba vonult, de amit a boncasztalnál tanult, mint mondja, „minden alkalommal kísérti, amikor látja, hogy az emberek a következményeket kezelik, nem az okot”.',
    'Д-р Калайджиев говори спокойно, без драма — като човек, който твърде често е виждал края на историите. Пенсионира се преди няколко години, но онова, което научи на аутопсионната маса, както казва, „ме преследва всеки път, когато видя хора да лекуват последствията, а не причината".')
rep('„A legtöbb ember azt hiszi, hogy a paraziták a múlté, a szegénységé, más országoké. Ez a tévedés öl. A paraziták mindenhol körülöttünk vannak — a félig átsült húsban, a saját kertből származó mosatlan zöldségekben, a földben, a vízben, a kezeken, miután megsimogattuk a kutyát vagy a macskát. És ha egyszer bejutnak, évekig élhetnek a testben, szaporodhatnak és lassan mérgezhetik a szervezetet — miközben Ön azt hiszi, hogy ez <b>gyomorhurut, allergia vagy „csak fáradtság”</b>.“',
    '„Повечето хора мислят, че паразитите са нещо от миналото, от бедността, от други страни. Тази заблуда убива. Паразитите са навсякъде около нас — в недопеченото месо, в неизмитите зеленчуци от собствената градина, в пръстта, във водата, по ръцете, след като погалим кучето или котката. А влязат ли веднъж, могат да живеят години в тялото, да се размножават и бавно да тровят организма — докато вие мислите, че това е <b>гастрит, алергия или „само умора"</b>."')
rep('„Feltártam egy 58 éves férfi testét, aki szívrohamban halt meg. Első pillantásra tiszta eset. De amit a beleiben és a májában találtam — annak nem lett volna szabad ott lennie. Ez az ember évekig hordozott magában valamit, ami belülről mérgezte. A jegyzőkönyvben az állt: „szívroham”. A valódi okról — egy szó sem. Ez történik szinte mindig.”',
    '„Отворих тялото на мъж на 58 години, който почина от инфаркт. На първо виждане ясен случай. Но онова, което намерих в червата и в черния му дроб — то не биваше да бъде там. Този човек е носил в себе си години нещо, което го е тровило отвътре. В протокола пишеше: „инфаркт". За истинската причина — нито дума. Така става почти винаги."')
rep('— dr. Kovács Gábor interjújából', '— от интервюто с д-р Запрян Калайджиев')

# ---------- аптечные таблетки ----------
rep('„A gyógyszertári tabletták nem oldják meg a problémát — egy fajtát ütnek le, és ott hagynak tucatnyit”',
    '„Хапчетата от аптеката не решават проблема — свалят един вид, а оставят дузина"')
rep('<span>Miért vall kudarcot a szokásos féregellenes kezelés szinte mindig — és miért károsítja a májat</span>',
    '<span>Защо обичайното лечение против паразити почти винаги се проваля — и защо уврежда черния дроб</span>')
rep('— Őszintén szólva: az nyugtalanít a legjobban, hogy mennyi ember hiszi azt, hogy elég bevenni egy tablettát a gyógyszertárból és kész. Ez veszélyes tévedés. <b>Több mint ötven parazitafaj élhet az emberi testben</b> — egyesek a bélben, mások a májban, mások az epeutakban, mások az izmokban. Egy gyógyszertári tabletta legfeljebb egy-két fajtát támad meg. A többi ott marad, szaporodik és tovább mérgezi a szervezetet.',
    '— Честно казано: най-много ме притеснява колко хора вярват, че е достатъчно да изпиеш едно хапче от аптеката и готово. Това е опасна заблуда. <b>В човешкото тяло могат да живеят над петдесет вида паразити</b> — едни в червата, други в черния дроб, трети в жлъчните пътища, четвърти в мускулите. Едно хапче от аптеката атакува най-много един или два вида. Останалите остават, размножават се и продължават да тровят организма.')
rep('Ez egy ördögi kör: az ember lenyel egy tablettát, néhány hétig jobban érzi magát, aztán a tünetek visszatérnek — fáradtság, puffadás, bőrproblémák —, és azt gondolja, hogy ez „nem a parazitáktól van, mert hiszen szedtem a gyógyszert”. Pedig valójában csak a probléma egy részét érintette. És ami még rosszabb: <b>az ezekben a tablettákban lévő erős vegyszerek a májat és a vesét támadják</b>, pontosan azokat a szerveket, amelyek már amúgy is túlterheltek a paraziták elleni küzdelemben.',
    'Това е омагьосан кръг: човекът изпива едно хапче, няколко седмици се чувства по-добре, после симптомите се връщат — умора, подуване, проблеми с кожата — и си мисли, че това „не е от паразити, защото нали пих лекарството". А всъщност е засегнал само част от проблема. И което е по-лошо: <b>силните химикали в тези хапчета атакуват черния дроб и бъбреците</b>, точно онези органи, които и без това вече са претоварени в борбата с паразитите.')
rep('Erzsébet évekig hordta magával a vizsgálati leleteit. „Minden rendben” — mondták neki. Míg a teste gyengült. Az éjjeliszekrényen dobozok a „gyomorhurut” és „allergia” elleni szerekkel, amelyek semmit sem oldottak meg, mert a valódi okot senki nem kereste.',
    'Денка години наред носеше изследванията си със себе си. „Всичко е наред" — ѝ казваха. Докато тялото ѝ слабееше. На нощното шкафче кутии с лекарства против „гастрит" и „алергия", които не решиха нищо, защото истинската причина никой не потърси.')
rep('A krónikus fáradtság, puffadás, bőrproblémák, allergiák és „neurózis” 40 éves kor után nem mindig „az életkortól” vannak — nagyon gyakran annak a jelei, hogy a test parazitákat hordoz, amelyek belülről pusztítják.',
    'Хроничната умора, подуването, проблемите с кожата, алергиите и „неврозата" след 40-годишна възраст не винаги са „от възрастта" — много често са знак, че тялото носи паразити, които го разрушават отвътре.')
rep('A „gyomorhurutra” és „allergiára” szedett tabletták csak elfedik a tüneteket, miközben a valódi ok csendben tovább szaporodik. Megfelelő, teljes mértékű testtisztítás nélkül a test évről évre gyengül — és a paraziták elterjednek a májban, az epehólyagban és más szervekben.',
    'Хапчетата, които се вземат за „гастрит" и „алергия", само прикриват симптомите, докато истинската причина тихо продължава да се размножава. Без правилно и пълно очистване на организма тялото слабее година след година — а паразитите се разпространяват в черния дроб, в жлъчния мехур и в други органи.')
rep('— Kérem, fogják fel a helyzet súlyát. Egész karrierem során láttam, mit tesznek a paraziták a testtel az évek során. Az emberek járják az orvosokat „neurózis”, „allergia”, „gyomorhurut”, „migrén” miatt — és senki nem teszi meg, amit kellene, és nem néz oda, ahová kellene. <b>A GYÓGYSZERTÁRI TABLETTÁK NEM TISZTÍTJÁK MEG TELJESEN A TESTET — EGY FAJTÁT ÜTNEK LE, A TÖBBIT PEDIG OTT HAGYJÁK, HOGY TOVÁBB PUSZTÍTSON BELÜLRŐL!</b>',
    '— Моля ви, разберете сериозността на положението. През цялата си кариера съм виждал какво правят паразитите на тялото през годините. Хората обикалят лекарите заради „невроза", „алергия", „гастрит", „мигрена" — и никой не прави онова, което трябва, и не гледа там, където трябва. <b>ХАПЧЕТАТА ОТ АПТЕКАТА НЕ ОЧИСТВАТ ТЯЛОТО ДОКРАЙ — СВАЛЯТ ЕДИН ВИД, А ОСТАНАЛИТЕ ОСТАВЯТ ДА РАЗРУШАВАТ ОТВЪТРЕ!</b>')
rep('És ami a leginkább megérint: ezek az emberek nem tudták. Azt hitték, hogy egészségesek. Az éveket, a munkát, a stresszt hibáztatták. Pedig egész idő alatt valami élőt hordoztak magukban, ami belülről mérgezte őket — és senki nem mondta nekik, hogy ellenőriztessék.',
    'А онова, което най-много ме докосва: тези хора не знаеха. Вярваха, че са здрави. Виняха годините, работата, стреса. А през цялото време носеха в себе си нещо живо, което ги тровеше отвътре — и никой не им каза да се проверят.')
rep('„Hét évig kezeltem az „allergiámat”. Krém, tabletta, csepp. A bőröm égett, viszketett, a kiütések a semmiből jöttek. Egyetlen bőrgyógyász sem említette a parazitákat. Csak amikor elkezdtem szedni a kapszulákat — három hét alatt megnyugodott a bőröm, először hét év után.”',
    '„Седем години лекувах своята „алергия". Крем, хапчета, капки. Кожата ми гореше, сърбеше, обривите излизаха от нищото. Нито един дерматолог не спомена паразити. Едва когато започнах да пия капсулите — за три седмици кожата ми се успокои, за първи път след седем години."')
rep('„Én öt évig kezeltettek gyomorhuruttal. Puffadás, gyomornehezülés, hányinger evés után. Mindent megittam, amit adtak. Semmi. Pedig paraziták voltak — ezt később az orvos mondta meg. Öt év és egy csomó pénz a kukában, mert senki nem kereste a valódi okot.”',
    '„Мене пет години ме лекуваха от гастрит. Подуване, тежест в стомаха, прилошаване след ядене. Изпих всичко, което ми дадоха. Нищо. А бяха паразити — това ми каза по-късно лекарят. Пет години и купчина пари в коша, защото истинската причина никой не потърси."')
rep('— Zoltán, 60 éves, Budapest környéke', '— Делчо, 60 години, близо до столицата')
rep('<b>Balra: egészséges bél ép nyálkahártyával. Jobbra: parazitákkal terhelt bél — krónikus gyulladás, sérült nyálkahártya, a szervezet folyamatos mérgezése. A paraziták az Ön testéből táplálkoznak, és salakanyagokat bocsátanak ki, amelyek mérgezik a vért. A gyógyszertári tabletták, amelyek csak egy fajtát támadnak, ezt nem oldják meg.</b>',
    '<b>Вляво: здраво черво с непокътната слизница. Вдясно: черво, натоварено с паразити — хронично възпаление, увредена слизница, постоянно отравяне на организма. Паразитите се хранят от вашето тяло и отделят отпадъчни вещества, които тровят кръвта. Хапчетата от аптеката, които атакуват само един вид, не решават това.</b>')
rep('Fontos hangsúlyozni: a legtöbb esetben még a gyógyszertári tabletták időszakos szedése mellett is visszatér a probléma, mert a valódi ok — több parazitafaj, amelyek a test különböző részein élnek — megoldatlan marad.',
    'Важно е да се подчертае: в повечето случаи проблемът се връща дори и при периодично пиене на хапчета от аптеката, защото истинската причина — няколко вида паразити, които живеят в различни части на тялото — остава нерешена.')
rep('A paraziták évekig tartó hordozása után sokan nemcsak az energiájukat vesztik el, hanem a májuk, epehólyagjuk és beleik egészségét is. A krónikus mérgezés, a legyengült immunrendszer, az állandó gyulladások — ez az ára annak, hogy senki nem kereste a valódi okot időben.',
    'След години носене на паразити мнозина губят не само енергията си, но и здравето на черния дроб, жлъчния мехур и червата. Хроничното отравяне, отслабеният имунитет, постоянните възпаления — това е цената на това, че никой не потърси истинската причина навреме.')

# ---------- случаи ----------
rep('Esetek, amelyek megváltoztatták a szemléletemet — és megváltoztatják azt is, ahogyan Ön a saját egészségére tekint',
    'Случаи, които промениха моя поглед върху нещата — и които ще променят и начина, по който вие гледате на своето здраве')
rep('— Engedjék meg, hogy elmondjam, mit láttam évről évre. Nem számokat. Nem statisztikákat. Embereket. Embereket nevekkel, akik az utolsó napig azt hitték, hogy a problémájuk teljesen más.',
    '— Позволете ми да ви кажа какво виждах година след година. Не числа. Не статистика. Хора. Хора с имена, които до последния ден вярваха, че проблемът им е съвсем друг.')
rep('Nő, 64 éves. Évekig kezelték „krónikus allergiával” és vérszegénységgel, amely sem vassal, sem vitaminokkal „nem akart javulni”. Senki nem gondolta, hogy valami a testében megeszi helyette a vasat.',
    'Жена, 64 години. Години наред лекувана за „хронична алергия" и анемия, която „не искаше да се оправи" нито с желязо, нито с витамини. На никого не му дойде на ум, че нещо в тялото ѝ изяжда желязото вместо нея.')
rep('„Állandóan fáradt voltam, sápadt, mint a fal. Az orvosok azt mondták: „vashiány, kérem szedjen tablettákat”. Évekig szedtem. Semmi. Senki nem kérdezte meg, hogy talán valami elveszi tőlem a vasat. Pedig elvitte.”',
    '„Бях постоянно уморена, бледа като стена. Лекарите казваха: „имате недостиг на желязо, пийте хапчета". Пих години. Нищо. Никой не ме попита дали нещо не ми отнема желязото. А го отнемаше."')
rep('— dr. Kovács által említett esetekből', '— от случаите, разказани от д-р Калайджиев', 2)
rep('Férfi, 67 éves. „Neurózissal” és álmatlansággal kezelték. Éjszaka fogát csikorgatta, kimerülten ébredt, fogyott, pedig normálisan evett. Mindent a stresszre és az életkorra fogtak.',
    'Мъж, 67 години. Лекуван за „невроза" и безсъние. Нощем скърцаше със зъби, будеше се изтощен, отслабваше, макар да се хранеше нормално. Всичко беше приписано на стреса и на възрастта.')
rep('„Fogytam, pedig normálisan ettem. A feleségem viccelődött, hogy „gyors az anyagcserém”. Ez nem volt vicces. Valami helyettem evett, belőlem. Ezt túl későn értettem meg ahhoz, hogy segítsek magamon — de Önök, akik ezt olvassák, nem vagytok elkésve.”',
    '„Отслабвах, макар да се хранех нормално. Жена ми се шегуваше, че „имам бърз метаболизъм". Никак не беше смешно. Нещо ядеше вместо мен, от мен. Разбрах това прекалено късно, за да си помогна — но вие, които четете това, не сте закъснели."')

# ---------- список симптомов ----------
rep('<b>Azok a tünetek, amelyeket leggyakrabban az „életkorra”, „stresszre” vagy „rossz táplálkozásra” fognak — pedig nagyon gyakran a testben élő paraziták jelei:</b>',
    '<b>Симптомите, които най-често приписваме на „възрастта", „стреса" или „лошото хранене" — а много често са знак за паразити, живеещи в тялото:</b>')
rep('<li>Állandó fáradtság és kimerültség — alszol 8 órát, de úgy ébredsz, mintha agyonvertek volna;</li>',
    '<li>Постоянна умора и изтощение — спиш 8 часа, а се будиш като пребит;</li>')
rep('<li>Puffadás, gázképződés, gyomornehezülés evés után — „mintha valami forrna a belekben”;</li>',
    '<li>Подуване, газове, тежест в стомаха след ядене — „като че ли нещо кипи в червата";</li>')
rep('<li>Váltakozó székrekedés és hasmenés nyilvánvaló ok nélkül;</li>',
    '<li>Редуващи се запек и разстройство, без явна причина;</li>')
rep('<li>Bőrproblémák — kiütés, viszketés, ekcéma, „allergiák”, amelyek a semmiből jönnek és mennek;</li>',
    '<li>Проблеми с кожата — обриви, сърбеж, екзема, „алергии", които идват и си отиват от нищото;</li>')
rep('<li>Ellenállhatatlan édesség- és lisztéhség — a paraziták cukorból táplálkoznak;</li>',
    '<li>Неудържим глад за сладко и тестени храни — паразитите се хранят със захар;</li>')
rep('<li>Fogcsikorgatás éjszaka, nyugtalan alvás, ébredés hajnali 3 körül;</li>',
    '<li>Скърцане със зъби през нощта, неспокоен сън, събуждане около 3 часа;</li>')
rep('<li>Vérszegénység és vashiány, amelyek még tabletták után sem szűnnek meg;</li>',
    '<li>Анемия и недостиг на желязо, които не отминават дори след хапчета;</li>')
rep('<li>Sötét karikák a szem alatt, sápadt bőr, törékeny haj és köröm;</li>',
    '<li>Тъмни кръгове под очите, бледа кожа, чупливи коса и нокти;</li>')
rep('<li>Viszketés a végbélnyílás körül, különösen éjszaka;</li>',
    '<li>Сърбеж около седалищния отвор, особено през нощта;</li>')
rep('<li>Ingerültség, „neurózis”, köd a fejben, gyenge koncentráció;</li>',
    '<li>Раздразнителност, „невроза", мъгла в главата, слаба концентрация;</li>')
rep('<li>Gyakori megfázások és fertőzések — legyengült immunrendszer, mert a test a parazitákra pazarolja az erőt;</li>',
    '<li>Чести простуди и инфекции — отслабен имунитет, защото организмът пилее силите си по паразитите;</li>')
rep('Mindegyik tünetet könnyű másra fogni. És pontosan ezért maradnak a paraziták évekig felderítetlenül. A figyelmen kívül hagyás egyetlen eredményhez vezet:',
    'Всеки от тези симптоми е лесно да бъде приписан на нещо друго. И точно затова паразитите остават неоткрити години наред. Пренебрегването води до един единствен изход:')
rep('<b class="red-txt">A SZERVEZET KRÓNIKUS MÉRGEZÉSE, LEGYENGÜLT IMMUNRENDSZER, MÁJ- ÉS BÉLKÁROSODÁS — ÉS A TEST, AMELY ÉVRŐL ÉVRE EGYRE NEHEZEBBEN DOLGOZIK.</b>',
    '<b class="red-txt">ХРОНИЧНО ОТРАВЯНЕ НА ОРГАНИЗМА, ОТСЛАБЕН ИМУНИТЕТ, УВРЕДЕНИ ЧЕРЕН ДРОБ И ЧЕРВА — И ТЯЛО, КОЕТО ГОДИНА СЛЕД ГОДИНА РАБОТИ ВСЕ ПО-ТРУДНО.</b>')
rep('Minden egyes nap a parazitákkal a testben egy újabb nap a szervezet mérgezésének!\n          Több ezer ember kezeli évekig nem azt, amit kellene — „gyomorhurutot”, „allergiát”, „neurózist” — miközben a valódi ok akadálytalanul tovább pusztítja őket belülről.\n          Cselekedjen most — önmagáért — mielőtt a következmények súlyossá válnának!',
    'Всеки ден с паразити в тялото е още един ден отравяне на организма!\n          Хиляди хора години наред лекуват нещо друго вместо онова, което трябва — „гастрит", „алергия", „невроза" — докато истинската причина безпрепятствено продължава да ги разрушава отвътре.\n          Действайте сега — за себе си — преди последствията да станат тежки!')

# ---------- передача слова ветеринару ----------
rep('— Én egész életemben a következményeket néztem. De nem én találtam meg a megoldást — a falusi állatorvos, dr. Szabó Ilona tette, aki évtizedekig féregtelenítette az állatállományt. Amikor meghallottam a történetét, megértettem, hogy tud valamit, amit mi, orvosok évekig figyelmen kívül hagyunk. Átadom neki a szót.',
    '— Аз цял живот гледах последствията. Но решението не го намерих аз — намери го селската ветеринарка, д-р Божура Налбантова, която десетилетия обезпаразитяваше стопанските животни. Когато чух историята ѝ, разбрах, че тя знае нещо, което ние, лекарите, пренебрегваме от години. Давам ѝ думата.')
rep('„Megértettem, hogy kell lennie egy módnak, hogy a testet gyengéden tisztítsuk meg — ne pedig erős vegyszerekkel mérgezzük”',
    '„Разбрах, че трябва да има начин тялото да се очиства нежно — а не да се трови със силни химикали"')
rep('<span>Hogyan fejlesztett ki a falusi állatorvos évek alatt egy gyógynövényes formulát, amely teljesen megtisztítja a szervezetet</span>',
    '<span>Как селската ветеринарка с години разработи билкова формула, която очиства организма докрай</span>')
rep('<b>Dr. Szabó Ilona, állatorvos több mint 30 éves tapasztalattal:</b>',
    '<b>Д-р Божура Налбантова, ветеринарен лекар с над 30 години опит:</b>')
rep('— Pályafutásom során állatokat kezeltem. És amit minden falusi ember tud, de ritkán gondol bele: <b>a kutyát és a macskát évente kétszer kötelező féregteleníteni. Az állatállományt — szarvasmarhát, juhot, sertést — ütemterv szerint, rendszeresen. A lovakat az istállóban szintén.</b> Mert ha ezt nem teszed meg, az állat legyengül, elsorvad, és végül elpusztul. Ez alapvető tudás a falun.',
    '— През цялата си кариера лекувах животни. А онова, което всеки селски човек знае, но рядко се замисля над него: <b>кучето и котката задължително се обезпаразитяват два пъти в годината. Стопанските животни — кравите, овцете, свинете — по график, редовно. Конете в обора също.</b> Защото, ако не го направиш, животното отслабва, посърва и накрая умира. Това е елементарно знание на село.')
rep('És akkor egy nap arra gondoltam: <b>az állatokat rendszeresen féregtelenítjük — magunkat soha. Az ember, aki együtt él ezekkel az állatokkal, ugyanazt a húst eszi, ugyanabban a földben túr, ugyanabból a kútból iszik — életében egyszer sem tisztítja meg magát.</b> Paradoxon: az állat jobban védett, mint a gazdája.',
    'И тогава един ден си помислих: <b>животните обезпаразитяваме редовно — себе си никога. Човекът, който живее с тези животни, яде същото месо, копае в същата пръст, пие от същия кладенец — нито веднъж в живота си не се очиства.</b> Парадокс: животното е по-добре защитено от стопанина си.')
rep('Évekig készítettem az állatoknak gyógynövényes keveréket a paraziták elűzésére. Gyógynövényesnek és gyengédnek kellett lennie — erős vegyszereket nem mertem használni, mert ezen állatok teje és húsa az emberek asztalára kerül. És észrevettem valamit: a gazdaság dolgozói, akik ugyanebből a keverékből ittak teát — „gyomornehezülésre” — abbahagyták a fáradtságra, a bőrre, az emésztésre való panaszokat. Így kezdődött.',
    'Години наред правех за животните билкова смес, която прогонва паразитите. Трябваше да бъде билкова и нежна — силни химикали не смеех да използвам, защото млякото и месото на тези животни стигат до човешката маса. И забелязах нещо: хората, които работеха в стопанството и пиеха чай от същата тази смес — за „тежест в стомаха" — спряха да се оплакват от умора, от кожата, от храносмилането. Така започна.')

# ---------- состав ----------
rep('<b>Dr. Szabó Ilona gyógynövényes formulája az alábbi összetevőket tartalmazza:</b>',
    '<b>Билковата формула на д-р Божура Налбантова съдържа следните съставки:</b>')
rep('<b>Üröm (Artemisia absinthium)</b>', '<b>Пелин (Artemisia absinthium)</b>')
rep('<font>Hagyományosan a legismertebb gyógynövényes szer a paraziták elűzésére a belekből</font>',
    '<font>Традиционно най-известното билково средство за прогонване на паразити от червата</font>')
rep('<b>Bogáncs (Tanacetum vulgare)</b>', '<b>Вратига (Tanacetum vulgare)</b>')
rep('<font>Erőteljesen hat a bélparazitákra és azok petéire</font>',
    '<font>Действа силно върху чревните паразити и върху яйцата им</font>')
rep('<b>Szegfűszeg (Eugenol)</b>', '<b>Карамфил (Eugenol)</b>')
rep('<font>Lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el</font>',
    '<font>Разгражда яйцата и ларвите на паразитите — онова, до което средствата против възрастните не достигат</font>')
rep('<b>Fekete dió (Juglans nigra)</b>', '<b>Черен орех (Juglans nigra)</b>')
rep('<font>Kivonat a héjból: tisztítja a beleket és segít eltávolítani a parazitákat</font>',
    '<font>Екстракт от черупката: очиства червата и помага за изхвърлянето на паразитите</font>')
rep('<b>Tök mag (Cucurbita)</b>', '<b>Тиквено семе (Cucurbita)</b>')
rep('<font>Gyengéden hat a parazitákra és nyugtatja a bél nyálkahártyáját</font>',
    '<font>Действа нежно върху паразитите и успокоява чревната слизница</font>')
rep('Ezeket a gyógynövényeket nehéz a megfelelő arányban összekeverni. Ha a keverék nem pontos, a kapszulák csak egy parazitafajtát támadnak — pontosan úgy, mint a gyógyszertári tabletta —, és a többi ott marad. A titok abban rejlik, hogy egyszerre több fajtára hatnak: a kifejlett egyedekre, a petékre és a lárvákra is.',
    'Тези билки е трудно да се смесят в правилното съотношение. Ако смесът не е точен, капсулите атакуват само един вид паразити — точно както хапчето от аптеката — а останалите остават. Тайната е в това, че действат върху няколко вида едновременно: и върху възрастните, и върху яйцата, и върху ларвите.')

# ---------- рождение продукта ----------
rep('Így született a HELMIRON — gyógynövényes kapszulák, amelyek teljesen és gyengéden tisztítják meg a szervezetet a parazitáktól, erős vegyszerek nélkül',
    'Така се роди HELMIRON — билкови капсули, които очистват организма от паразити докрай и нежно, без силни химикали')
rep('— A keveréket, amelyet az állatoknak készítettem, átdolgoztam emberi használatra — pontos gyógynövények, pontos arányok, kapszula formában, amely kényelmes a szervezet számára. A neve HELMIRON. Egyszerűen szedhető: egy kapszula reggel és este, vízzel lenyelve, a kúra teljes időtartama alatt. Erős vegyszerek nélkül — a gyógynövények végzik a munkájukat a belekben, pontosan ott, ahol a paraziták élnek.',
    '— Сместа, която правех за животните, преработих за човешка употреба — точни билки, точни съотношения, във вид на капсула, която е удобна за организма. Нарича се HELMIRON. Взема се просто: по една капсула сутрин и една вечер, с вода, през цялото време на курса. Без силни химикали — билките вършат работата си в червата, точно там, където живеят паразитите.')
rep('Az erő abban rejlik, hogy a kapszulák fokozatosan és teljesen hatnak: először a kifejlett parazitákra, majd azok petéire és lárváira, ezután segítenek a testnek mindent kiüríteni, és hagyják a beleket és a májat regenerálódni. A gyógyszertári tabletta egyetlen célpontot támad. A kapszulák végighaladnak az egész emésztőrendszeren — ott, ahol a paraziták valóban találhatók.',
    'Силата е в това, че капсулите действат постепенно и докрай: първо върху възрастните паразити, после върху яйцата и ларвите им, след което помагат на тялото да изхвърли всичко и оставят червата и черния дроб да се възстановят. Хапчето от аптеката атакува една единствена цел. Капсулите преминават през целия храносмилателен тракт — там, където паразитите наистина се намират.')
rep('A „HELMIRON” különleges. Minden gyógynövény — a megfelelő arányban — a paraziták különböző fázisaiban támad: kifejlett egyedek, peték, lárvák. Ezért tisztít teljesen, nem részlegesen. A legfontosabb: gyengéden hat, anélkül, hogy megtámadná a májat és a vesét, ahogyan azt az erős gyógyszertári tabletták teszik. Először a gazdaság dolgozói szedték, majd később a hétköznapi emberek is mindazokkal a „megoldhatatlan” panaszokkal — fáradtság, bőr, emésztés.',
    '„HELMIRON" е специален. Всяка билка — в правилното съотношение — атакува паразитите в различни фази: възрастни, яйца, ларви. Затова очиства докрай, а не частично. Най-важното: действа нежно, без да атакува черния дроб и бъбреците, както правят силните хапчета от аптеката. Първо го пиеха хората, които работеха в стопанството, а по-късно и най-обикновени хора с всички онези „нерешими" оплаквания — умора, кожа, храносмилане.')
rep('<p><b>Erzsébet:</b></p>', '<p><b>Денка:</b></p>')
rep('— Az állatorvos adott nekem egy dobozzal, és azt mondta: „Próbáld ki, Erzsébet, mit veszíthetsz?” Reggel és este szedtem a kapszulákat. A harmadik-negyedik napon éreztem, hogy a gyomrom könnyebb, mint évek óta. Nem hittem el, hogy a kapszuláktól van. Azt hittem — véletlen. Csak később, amikor a patológus elmagyarázta, értettem meg, mi is történt valójában a testemben.',
    '— Ветеринарката ми даде една кутия и ми каза: „Пробвай, Денке, какво имаш да губиш?" Пиех капсулите сутрин и вечер. На третия-четвъртия ден усетих, че стомахът ми е по-лек, отколкото от години. Не вярвах, че е от капсулите. Мислех — случайност. Едва по-късно, когато патологът ми обясни, разбрах какво наистина се е случило в тялото ми.')

# ---------- четыре шага ----------
rep('4 lépés, amelyben a HELMIRON megtisztítja a szervezetet a parazitáktól — bármilyen életkorban',
    '4 стъпки, в които HELMIRON очиства организма от паразити — на всяка възраст')
rep('<h1>A „HELMIRON” kapszulák 4 alapvető hatása:</h1>', '<h1>Четирите основни действия на капсулите „HELMIRON":</h1>')
rep('<font>A kifejlett paraziták elűzése:</font>', '<font>Прогонване на възрастните паразити:</font>')
rep('<span>A kúra első napjaiban az üröm és a bogáncs hat a belekben élő kifejlett parazitákra — gyengíti őket, és segít a szervezetnek természetes úton kiüríteni azokat. Nem egy fajtát, mint a gyógyszertári tabletta, hanem egyszerre többet.</span>',
    '<span>В първите дни на курса пелинът и вратигата действат върху възрастните паразити, които живеят в червата — отслабват ги и помагат на организма да ги изхвърли по естествен път. Не един вид, както хапчето от аптеката, а няколко едновременно.</span>')
rep('<font>A peték és lárvák elpusztítása:</font>', '<font>Унищожаване на яйцата и ларвите:</font>')
rep('<span>A szegfűszeg (eugenol) lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el. Ez a lépés kulcsfontosságú: enélkül a paraziták visszatérnek a megmaradt petékből. Ezért tisztítanak a kapszulák teljesen, nem részlegesen.</span>',
    '<span>Карамфилът (евгенол) разгражда яйцата и ларвите на паразитите — онова, до което средствата против възрастните не достигат. Тази стъпка е ключова: без нея паразитите се връщат от останалите яйца. Затова капсулите очистват докрай, а не частично.</span>')
rep('<font>Méregtelenítés a salakanyagoktól:</font>', '<font>Детоксикация от отпадъчните вещества:</font>')
rep('<span>Amikor a paraziták távoznak, a szervezet megtisztul a salakanyagoktól, amelyeket azok évekig választottak ki a vérbe. A fekete dió és a tök mag segít a májnak és a beleknek kiüríteni a felhalmozódott méreganyagokat — megszűnik a fáradtság, a puffadás és a köd a fejben.</span>',
    '<span>Когато паразитите бъдат изхвърлени, организмът се очиства от отпадъчните вещества, които те години наред са отделяли в кръвта. Черният орех и тиквеното семе помагат на черния дроб и на червата да изхвърлят натрупаните токсини — отминават умората, подуването и мъглата в главата.</span>')
rep('<font>A belek és az immunrendszer regenerálódása:</font>', '<font>Възстановяване на червата и имунитета:</font>')
rep('<span>A tisztítás után a gyógynövényes keverék nyugtatja a bél nyálkahártyáját, és segít a testnek visszanyerni az erejét. Visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés, és az immunrendszer — amely évekig a paraziták elleni küzdelemben merült ki — ismét megerősödik.</span>',
    '<span>След очистването билковата смес успокоява чревната слизница и помага на тялото да си върне силите. Връща се енергията, успокоява се кожата, храносмилането се нормализира, а имунитетът — изтощен години наред в борбата с паразитите — отново се укрепва.</span>')

# ---------- наблюдение и таблица ----------
rep('„Először a HELMIRON-t hétköznapi emberek szedték „megoldhatatlan” panaszokkal — az eredmények még engem is megleptek”',
    '„Първо HELMIRON го пиеха най-обикновени хора с „нерешими" оплаквания — резултатите изненадаха дори мен"')
rep('<span>2340, 45 és 86 év közötti személy megfigyelése</span>', '<span>Наблюдение върху 2340 души на възраст между 45 и 86 години</span>')
rep('— Amikor évtizedes boncolások után először hallottam erről a gyógynövényes keverékről, szkeptikus voltam — mint minden orvos. De az eredmények, amelyeket a szedők mutattak, olyan egyértelműek voltak, hogy nem hagyhattam figyelmen kívül őket. Szakértői csoport kiterjesztette a megfigyelést több mint 2300, egész Magyarországról származó személyre — mindazokkal a tünetekkel, amelyeket szinte senki nem hozott összefüggésbe a parazitákkal.',
    '— Когато след десетилетия аутопсии чух за първи път за тази билкова смес, бях скептичен — като всеки лекар. Но резултатите, които показваха онези, които я пиеха, бяха толкова ясни, че не можах да ги подмина. Експертна група разшири наблюдението върху над 2300 души от цяла България — с всички онези симптоми, които почти никой не свързваше с паразити.')
rep('Olyan embereket láttam, akik évekig kezelték a „gyomorhurutot” és az „allergiát” — és néhány hét alatt visszanyerték az energiájukat, megnyugodott a bőrük, normalizálódott az emésztésük. Amit egyetlen tabletta sem oldott meg évekig.',
    'Видях хора, които години наред лекуваха „гастрит" и „алергия" — а за няколко седмици си върнаха енергията, кожата им се успокои, храносмилането им се нормализира. Онова, което нито едно хапче не реши с години.')
rep('A „HELMIRON” megfigyelésének eredményei — kontrollcsoport: 2340 fő, 45–86 éves korig',
    'Резултати от наблюдението „HELMIRON" — контролна група: 2340 души, 45–86 години')
rep('<td class="one">A puffadás és gyomornehezülés megszűnése</td>', '<td class="one">Премахване на подуването и тежестта в стомаха</td>')
rep('<td class="one">Az energia visszatérése, a krónikus fáradtság megszűnése</td>', '<td class="one">Връщане на енергията, премахване на хроничната умора</td>')
rep('<td class="one">A bőr megnyugvása (kiütés, viszketés, „allergiák”)</td>', '<td class="one">Успокояване на кожата (обриви, сърбеж, „алергии")</td>')
rep('<td class="one">Az emésztés és székletürítés normalizálódása</td>', '<td class="one">Нормализиране на храносмилането и изхожданията</td>')
rep('<td class="one">Az édesség utáni vágy megszűnése</td>', '<td class="one">Премахване на влечението към сладко</td>')
rep('<td class="one">Javuló alvás, a fogcsikorgatás megszűnése</td>', '<td class="one">По-добър сън, спиране на скърцането със зъби</td>')
rep('<td class="one">A vérkép javulása (vas)</td>', '<td class="one">Подобряване на кръвната картина (желязо)</td>')
rep('<td class="one">A fejben lévő köd megszűnése, jobb koncentráció</td>', '<td class="one">Премахване на мъглата в главата, по-добра концентрация</td>')
rep('<td class="one">A sötét karikák eltűnése a szem alatt</td>', '<td class="one">Изчезване на тъмните кръгове под очите</td>')
rep('<td class="one">Az immunrendszer megerősödése, ritkább fertőzések</td>', '<td class="one">Укрепване на имунитета, по-редки инфекции</td>')

# ---------- случай героини ----------
rep('Az eset, amely a legjobban megmutatja, mennyi ideig maradnak rejtve a paraziták',
    'Случаят, който най-добре показва колко дълго паразитите остават скрити')
rep('Erzsébet, 62 éves. Hat évig kezelték „gyomorhuruttal”, „allergiával” és „krónikus fáradtsággal”. A HELMIRON kapszulák kúrája után — először évek óta kipihenten ébredt, és a bőre megnyugodott.',
    'Денка, 62 години. Шест години лекувана за „гастрит", „алергия" и „хронична умора". След курса с капсули HELMIRON — за първи път от години се събуди отпочинала, а кожата ѝ се успокои.')
rep('Erzsébet volt az egyik első, akinek dr. Szabó adta a kapszulákat. 62 évesen, hat év orvosjárás után, normális vizsgálati eredményekkel és egy testtel, amely napról napra egyre gyengébb volt. A lánya Bécsben, a fia Németországban — telefonáltak, küldték a pénzt, de senki nem vette észre, hogy kialszik, mert ők is azt hitték, hogy ez „csak fáradtság és az életkor”.',
    'Денка беше една от първите, на които д-р Налбантова даде капсулите. На 62 години, след шест години обикаляне по лекари, с нормални изследвания и с тяло, което слабееше от ден на ден. Дъщерята в Италия, синът в Германия — звъняха, пращаха пари, но никой не забеляза, че угасва, защото и те вярваха, че това е „само умора и възраст".')
rep('„Hat éve vonszoltam magam orvostól orvosig. Állandóan fáradt voltam, puffadt, a bőröm égett és viszketett, a hajam hullott. Azt mondták: gyomorhurut, allergia, neurózis, életkor. Mindent beszedtem, amit adtak. Semmi sem segített, és úgy éreztem, mintha valaki lassan felfalna belülről.',
    '„Шест години се влачех от лекар на лекар. Бях постоянно уморена, подута, кожата ми гореше и сърбеше, косата ми падаше. Казваха ми: гастрит, алергия, невроза, възраст. Изпих всичко, което ми дадоха. Нищо не помогна, а се чувствах като че ли някой ме изяжда бавно отвътре.')
rep('A legrosszabb az volt, hogy minden vizsgálat „rendben” volt. Akkor hogyan lehetek ennyire kimerült? Már kezdtem azt hinni, hogy kitalálom, hogy hipochonder lettem. Senki, egyetlen orvos sem említette a parazitákat.',
    'Най-лошото беше, че всички изследвания бяха „наред". Тогава как мога да съм толкова изтощена? Вече започвах да мисля, че си измислям, че съм станала хипохондрик. Никой, нито един лекар не спомена паразити.')
rep('Aztán jött hozzám az állatorvos a tehén miatt. És mellékesen rám nézett, és megkérdezte: „Erzsébet, mikor féregtelenítetted utoljára magadat? A kutyát évente kétszer féregteleníted, magadat egyszer sem.” Adott a kapszuláiból. A harmadik napon a gyomrom könnyebb volt, mint évek óta. Egy hét múlva először ébredtem kipihenten. Három hét múlva megnyugodott a bőröm — először hét év után.',
    'После дойде при мен ветеринарката заради кравата. И между другото ме погледна и ме попита: „Денке, а себе си кога се обезпаразити за последно? Кучето го обезпаразитяваш два пъти в годината, а себе си нито веднъж." Даде ми от своите капсули. На третия ден стомахът ми беше по-лек, отколкото от години. След седмица за първи път се събудих отпочинала. След три седмици кожата ми се успокои — за първи път след седем години.')
rep('Sírtam. Nem azért, mert jobban lettem. Hanem mert rájöttem, mennyi évet és pénzt vesztettem el azzal, hogy nem azt kezeltem, amit kellett volna — amikor a válasz ilyen egyszerű volt.',
    'Плаках. Не защото ми стана по-добре. А защото разбрах колко години и колко пари изгубих, лекувайки друго вместо онова, което трябваше — когато отговорът беше толкова прост.')
rep('<b>Erzsébet, 62 éves, alföldi falu</b>', '<b>Денка, 62 години, село в Лудогорието</b>')

# ---------- случай шофёра ----------
rep('Egy másik eset: Zoltán, 60 éves, egész életében kamionsofőr, évekig kezelték „gyomorhuruttal”, amely semmilyen tablettára nem szűnt meg.',
    'Друг случай: Делчо, 60 години, цял живот шофьор на тир, лекуван с години за „гастрит", който не отмина от никакво хапче.')
rep('„Öt évig kezeltek gyomorhuruttal. Nehézség a gyomorban minden étkezés után, hányinger, puffadás, mint egy dob. Mindenféle vizsgálat, gyógyszerek a gyomorra. Semmi. Fogytam, pedig normálisan ettem.',
    '„Пет години ме лекуваха от гастрит. Тежест в стомаха след всяко ядене, прилошаване, подут като тъпан. Всякакви изследвания, лекарства за стомаха. Нищо. Отслабвах, макар да се хранех нормално.')
rep('A feleségem hallott a HELMIRON kapszulákról a szomszédasszonytól. Azt mondta: próbáld ki, mit veszíthetsz. Reggel és este elkezdtem szedni. Körülbelül tíz nap múlva — először évek óta ettem, és utána semmi nem fájt és nem puffadtam. Egy hónap után úgy éreztem magam, mint egy új ember.',
    'Жена ми чу за капсулите HELMIRON от съседката. Каза ми: пробвай, какво имаш да губиш. Започнах да ги пия сутрин и вечер. След около десет дни — за първи път от години ядох и след това нищо не ме заболя и не се подух. След един месец се чувствах като нов човек.')
rep('Ami a legjobban felháborított: öt év és egy csomó pénz a kukába a rossz diagnózis miatt. Paraziták voltak. És senkinek nem jutott eszébe, hogy odanézzen. Ha nincsenek ezek a kapszulák, ki tudja, meddig szenvedtem volna.”',
    'Онова, което най-много ме възмути: пет години и купчина пари в коша заради погрешна диагноза. Бяха паразити. И на никого не му дойде на ум да погледне там. Ако ги нямаше тези капсули, кой знае докога щях да страдам."')

# ---------- не симптомы, а причина ----------
rep('„A HELMIRON nem tüneteket fed el — megtisztítja a testet az okától”',
    '„HELMIRON не прикрива симптоми — очиства тялото от причината им"')
rep('Ebből nemcsak a súlyos esetek profitálnak. Mindenki 40 éves kor felett, aki az első tüneteket érzi, megelőzhet évek felesleges szenvedését.',
    'От това печелят не само тежките случаи. Всеки над 40 години, който усеща първите симптоми, може да предотврати години излишно страдание.')
rep('— A kúra általában 3-4 hétig tart, és azoknál, akik évekig hordozzák a problémát, akár tovább is. Amint dr. Szabó elmagyarázta, a tisztítást évente kétszer, profilaktikusan meg kell ismételni — pontosan úgy, mint az állatoknál —, mert a paraziták újra bekerülhetnek az élelmiszerrel, vízzel vagy a háziállatoktól.',
    '— Курсът обикновено продължава 3-4 седмици, а при онези, които носят проблема от години, и по-дълго. Както обясни д-р Налбантова, очистването трябва да се повтаря два пъти в годината, профилактично — точно както при животните — защото паразитите могат да влязат отново с храната, с водата или от домашните животни.')
rep('A HELMIRON fokozatosan hat: az első napokban megszűnik a puffadás és a gyomornehezülés, majd visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés.',
    'HELMIRON действа постепенно: в първите дни отминават подуването и тежестта в стомаха, после се връща енергията, успокоява се кожата, нормализира се храносмилането.')
rep('Olyan embereket láttam, akik évekig kezelték a „megoldhatatlan” panaszokat — és néhány hét alatt visszanyerték az erejüket, először hosszú idő után aludtak úgy, mint az emberek. A test maga tudja, hogyan regenerálódjon, ha levesszük róla a terhet, amely pusztította.',
    'Видях хора, които години наред лекуваха „нерешими" оплаквания — а за няколко седмици си върнаха силите, за първи път от дълго време спаха като хора. Тялото само знае как да се възстанови, ако му свалим товара, който го е разрушавал.')
rep('Dr. Szabó Ilona gyógynövényes formulájának köszönhetően Magyarországon több ezer ember tisztította meg a szervezetét a parazitáktól.\n          Íme néhány eset:',
    'Благодарение на билковата формула на д-р Божура Налбантова хиляди хора в България очистиха организма си от паразити.\n          Ето няколко случая:')

# ---------- четыре подписи ----------
rep('<figcaption>Férfi, 65 éves. Évekig „gyomorhurut” és krónikus fáradtság. HELMIRON kúra: megszűnt a puffadás, visszatért az energia, normalizálódott az emésztés.</figcaption>',
    '<figcaption>Мъж, 65 години. Години наред „гастрит" и хронична умора. Курс HELMIRON: подуването изчезна, енергията се върна, храносмилането се нормализира.</figcaption>')
rep('<figcaption>Nő, 58 éves. „Allergia” és bőrkiütés évek óta. Kúra után: tiszta bőr, viszketés megszűnt, megszűntek az „allergiás” reakciók.</figcaption>',
    '<figcaption>Жена, 58 години. „Алергия" и обриви по кожата от години. След курса: чиста кожа, сърбежът спря, спряха и „алергичните" реакции.</figcaption>')
rep('<figcaption>Nő, 72 éves. Vérszegénység, amely még vas pótlására sem szűnt meg. Kúra után: a vérkép javult, a fáradtság és sápadtság megszűnt.</figcaption>',
    '<figcaption>Жена, 72 години. Анемия, която не отмина дори при добавки с желязо. След курса: кръвната картина се подобри, умората и бледостта изчезнаха.</figcaption>')
rep('<figcaption>Férfi, 70 éves. Állandó puffadás, álmatlanság, fogcsikorgatás. Kúra után: nyugodt alvás, normális székletürítés, visszanyert súly.</figcaption>',
    '<figcaption>Мъж, 70 години. Постоянно подуване, безсъние, скърцане със зъби. След курса: спокоен сън, нормално изхождане, възвърнато тегло.</figcaption>')
rep('— Pályafutásom során végig néztem a paraziták testre gyakorolt hosszú távú hatásait. Ezért érintenek meg ezek az esetek: amint ezt a terhet levesszük a testről, az magától regenerálódik. Erős vegyszerek nélkül. Olyan tabletták nélkül, amelyek a májat támadják. <b>Az emberi test erős — csak időben le kell venni róla azt, ami belülről pusztítja.</b>',
    '— През цялата си кариера наблюдавах дълготрайните последствия от паразитите върху тялото. Затова ме докосват тези случаи: в момента, в който свалим този товар от тялото, то се възстановява само. Без силни химикали. Без хапчета, които атакуват черния дроб. <b>Човешкото тяло е силно — трябва само навреме да му свалим онова, което го разрушава отвътре.</b>')

# ---------- оффер ----------
rep('Miért nem kapható a HELMIRON a gyógyszertárakban? És hogyan lehet beszerezni?',
    'Защо HELMIRON не се намира в аптеките? И как може да бъде получен?')
rep('<p>A HELMIRON gyártása lassú és gondos folyamat. Amint dr. Szabó elmagyarázta, a gyógynövényeket a megfelelő időben kell begyűjteni, és pontos arányban összekeverni — üröm, bogáncs, szegfűszeg, fekete dió, tök mag. Minden kis mennyiségben, kézzel készül, és nem lehet kielégíteni a teljes keresletet.</p>',
    '<p>Производството на HELMIRON е бавен и внимателен процес. Както обясни д-р Налбантова, билките трябва да се събират в точното време и да се смесват в точни съотношения — пелин, вратига, карамфил, черен орех, тиквено семе. Всичко се прави в малки количества, на ръка, и не може да се задоволи цялото търсене.</p>')
rep('<p>Legalább 2-3 évre van szükség ahhoz, hogy a HELMIRON a gyógyszertárakba kerüljön. Addig a termék kizárólag online, a támogatási program keretében érhető el. Mindazonáltal,\n      <font class="red-txt">a kedvezmény akár 50% is lehet</font>\n      — ami óriási jelentőséggel bír a nyugdíjasok számára.\n    </p>',
    '<p>Нужни са поне 2-3 години, за да стигне HELMIRON до аптеките. Дотогава продуктът е достъпен изключително онлайн, в рамките на програмата за подкрепа. При това\n      <font class="red-txt">отстъпката може да достигне до 50%</font>\n      — което има огромно значение за пенсионерите.\n    </p>')
rep('Kérem Önöket: NE SZALASSZÁK EL A TÁMOGATÁSI PROGRAMOT. Ne csak magukért — hanem a szeretteikért is, akik talán évekig nem azt kezelik, amit kellene, anélkül, hogy sejtenék a valódi okot. Tisztítsák meg magukat — és segítsenek azokon, akik számítanak Önöknek.',
    'Моля Ви: НЕ ПРОПУСКАЙТЕ ПРОГРАМАТА ЗА ПОДКРЕПА. Не само за себе си — а и за близките си, които може би от години лекуват друго вместо онова, което трябва, без да подозират истинската причина. Очистете себе си — и помогнете на онези, които са ви скъпи.')
rep('<b>A rendelés leadásához használják az alábbi űrlapot.</b>', '<b>За да направите поръчка, използвайте формуляра по-долу.</b>')
rep('Az utolsó lehetőség idén, hogy HELMIRON-t szerezzenek — maguknak vagy szeretteiknek, akik évek óta szenvednek a helyes válasz nélkül',
    'Последен шанс тази година да получите HELMIRON — за Вас или за скъп човек, който страда от години без правилния отговор')
rep('— Kizárólag ennek a portálnak az olvasói számára 20 000 dobozt különítettek el. Minden 40 év feletti magyar állampolgár <font class="red-txt">akár 50% kedvezményt</font> kaphat, de a program <span>',
    '— Изключително за читателите на този портал бяха отделени 20 000 кутии. Всеки български гражданин над 40 години може да получи <font class="red-txt">отстъпка до 50%</font>, но програмата продължава до <span>')
rep('      </span>-ig tart.\n    </p>', '      </span>.\n    </p>')
rep('<p>Ne várják meg, amíg a fáradtság, a bőrproblémák és az emésztési panaszok a mindennapok részévé válnak. Amíg pénzt költenek rossz diagnózisokra. Emlékezzenek: az állatokat évente kétszer féregtelenítjük, magunkat egyszer sem. A HELMIRON-t elegendő egy kúra formájában átvenni, majd évente kétszer megismételni — profilaktikusan, pontosan úgy, mint az állatoknál.</p>',
    '<p>Не чакайте, докато умората, проблемите с кожата и оплакванията от храносмилането станат част от всеки ден. Докато давате пари за погрешни диагнози. Помнете: животните обезпаразитяваме два пъти в годината, себе си нито веднъж. HELMIRON е достатъчно да се вземе под формата на курс, а после да се повтори два пъти в годината — профилактично, точно както при животните.</p>')
rep('<p>Írják be a nevüket és telefonszámukat. Szakértőnk felveszi Önökkel a kapcsolatot, kiválasztja a megfelelő programot, és megszervezi a kiszállítást futárral vagy postán 2-3 napon belül, közvetlenül a címükre.</p>',
    '<p>Въведете името и телефонния си номер. Наш специалист ще се свърже с Вас, ще подбере подходящата програма и ще организира доставката с куриер или по пощата за 2-3 дни, директно до посочения адрес.</p>')
rep('<b>Reménnyel és tisztelettel — dr. Kovács Gábor, patológus. 35 év után a boncasztalnál az egyetlen, amit ajánlok: tisztítsák meg magukat időben. A testük nem fogja elfelejteni.</b>',
    '<b>С надежда и уважение — д-р Запрян Калайджиев, патолог. След 35 години на аутопсионната маса единственото, което препоръчвам, е: очистете се навреме. Тялото Ви няма да го забрави.</b>')
rep('<span class="ramka-title">Frissítés: <span>', '<span class="ramka-title">Актуализация: <span>')
rep('A hatalmas érdeklődés miatt a készletek korábban elfogyhatnak, mint várható! Ma —',
    'Поради огромния интерес наличностите могат да се изчерпат по-бързо от предвиденото! Днес —')
rep('        </span> — a program utolsó napja</font> vagy a készletek kimerüléséig.',
    '        </span> — е последният ден от програмата</font> или до изчерпване на наличностите.')
rep('Figyelem! Ne zárják be és ne frissítsék az oldalt, ellenkező esetben az Ön számára lefoglalt HELMIRON doboz egy másik személyhez kerül!',
    'Внимание! Не затваряйте и не презареждайте страницата, в противен случай кутията HELMIRON, резервирана за Вас, ще бъде предложена на друг човек!')
rep('Használják ki az ajánlatot — az Ön helye le van foglalva:', 'Възползвайте се от офертата — Вашето място е резервирано:')

# ---------- форма ----------
rep('<b>Hivatalos rendelési űrlap</b>', '<b>Официален формуляр за поръчка</b>')
rep('A <b>50% kedvezmény</b> igénybevételéhez írják be a nevüket és telefonszámukat az alábbi mezőkbe, majd nyomják meg a „MEGRENDELEM" gombot.',
    'За да се възползвате от <b>отстъпката от 50%</b>, напишете името и телефонния си номер в полетата по-долу и натиснете бутона „ПОРЪЧАЙ СЕГА".')
rep('Elérhetőség:', 'В наличност:')
rep('<span class="price_old">19800 HUF</span>', '<span class="price_old">98 лв</span>')
rep('<span class="price_main">9900 HUF</span>', '<span class="price_main">49 лв</span>')
rep('<input type="hidden" name="country" value="HU">', '<input type="hidden" name="country" value="BG">')
rep('<label for="name-input">Név</label>', '<label for="name-input">Име</label>')
rep('placeholder="Az Ön neve"', 'placeholder="Вашето име"', 2)
rep('<label for="phone-input">Telefonszám</label>', '<label for="phone-input">Телефонен номер</label>')
rep('placeholder="Az Ön telefonszáma"', 'placeholder="Вашият телефонен номер"')
rep('<button class="button-submit" type="submit">MEGRENDELEM</button>', '<button class="button-submit" type="submit">ПОРЪЧАЙ СЕГА</button>')
rep('✔️ A szállítást a Nemzeti Közegészségügyi Központ végzi<br> közvetlenül a megadott címre',
    '✔️ Доставката се извършва от Националния център по обществено здраве<br> директно до посочения адрес')

# ---------- комментарии: имена ----------
for hu, bg in [('Kovács Mária','Жечка Табакова'), ('Nagy Erzsébet','Богданка Пандурска'),
               ('Varga Anna','Магдалина Сеизова'), ('Kiss János','Станчо Карагьозов'),
               ('Szabó Péter','Вангел Куюмджиев'), ('Tóth Alexandra','Руйка Пехливанова'),
               ('Horváth Judit','Божанка Бозукова'), ('Nagy Kázmér','Паскал Гъбенски'),
               ('Molnár Katalin','Марудка Арнаудова'), ('Farkas Erzsébet','Тотка Папазова'),
               ('Papp József','Синадин Кюркчиев'), ('Balogh Tádé','Велко Джуров'),
               ('Gábor Ibolya','Невяна Бакалова'), ('Kiss Zsuzsanna','Калуда Бунарджиева'),
               ('Nagy Gergely','Жеко Казанджиев')]:
    rep('<p class="comments__item-name">%s</p>' % hu, '<p class="comments__item-name">%s</p>' % bg)

# ---------- комментарии: тексты ----------
rep('Sírtam, amikor ezt a cikket olvastam. Anyukám 76 éves, és évek óta „gyomorhuruttal” és „allergiával” kezelteti magát — és senki sem említette soha a parazitákat. Minden stimmel, abszolút minden. Rendeltem neki HELMIRON-t. Hogy nem jutott ez hamarabb eszembe?',
    'Плаках, докато четях тази статия. Мама е на 76 години и от години се лекува от „гастрит" и „алергия" — а никой никога не спомена паразити. Всичко се връзва, абсолютно всичко. Поръчах ѝ HELMIRON. Как не ми дойде на ум по-рано?')
rep('A múlt héten megjött a HELMIRON. Reggel és este szedem a kapszulákat. 5 nap után — a puffadás, ami évekig gyötört, majdnem teljesen eltűnt, a gyomrom könnyebb, mint valaha. Ennek a patológusnak a története késztetett a rendelésre. Bárcsak tudnák, milyen jól érzem magam.',
    'Миналата седмица ми дойде HELMIRON. Пия капсулите сутрин и вечер. След 5 дни — подуването, което ме мъчеше с години, изчезна почти напълно, стомахът ми е по-лек от когато и да било. Историята на този патолог ме накара да поръчам. Да знаете колко добре се чувствам.')
rep('69 éves vagyok. Hét évig kezeltek „allergiával” — krémek, tabletták, cseppek. A bőröm égett és viszketett. 3 hét HELMIRON kapszula után — a bőröm először nyugodott meg ennyi év után. Magam járok piacra, főzök, normálisan élek. Visszatértem önmagamhoz.',
    'На 69 години съм. Седем години ме лекуваха за „алергия" — кремове, хапчета, капки. Кожата ми гореше и сърбеше. След 3 седмици капсули HELMIRON — кожата ми се успокои за първи път след толкова години. Сама ходя на пазар, готвя, живея нормално. Върнах се при себе си.')
rep('Napi 10 órát dolgozom. Állandó fáradtság, köd a fejben, édesség utáni vágy, amit nem tudtam kontrollálni. Azt hittem — életkor, stressz. Kipróbáltam a HELMIRON-t. 4 hét után — visszatért az energia, tiszta a fejem. Hatalmas tisztelet ennek az állatorvosnak, azt az igazságot mondja, amit senki más nem mond.',
    'Работя по 10 часа на ден. Постоянна умора, мъгла в главата, влечение към сладко, което не можех да контролирам. Мислех — възраст, стрес. Пробвах HELMIRON. След 4 седмици — енергията се върна, главата ми е чиста. Огромно уважение към тази ветеринарка, казва истината, която никой друг не казва.')
rep('Rendeltem 3 dobozt — magamnak, a feleségemnek (állandó bőrproblémák) és az apósomnak. Az állatokat évente kétszer féregtelenítjük, magunkat soha — amikor ezt elolvastam, minden világossá vált. Köszönöm a cikket, felnyitotta a szemem.',
    'Поръчах 3 кутии — за мен, за жена ми (постоянни проблеми с кожата) и за тъста. Животните обезпаразитяваме два пъти в годината, себе си никога — когато прочетох това, всичко ми се изясни. Благодаря за статията, отвори ми очите.')
rep('Gondolkodom a rendelésen az apukámnak. 78 éves, évek óta panaszkodik az emésztésre és fáradtságra, az orvosok nem találnak semmit. Szerintetek a HELMIRON segíthet ebben a korban is?',
    'Мисля да поръчам за баща ми. На 78 години е, от години се оплаква от храносмилането и от умора, лекарите не намират нищо. Мислите ли, че HELMIRON може да помогне и на тази възраст?')
rep('Alexandra, az én anyukám 82 éves! Évek óta vérszegénység, ami még vas pótlására sem szűnt meg. Egy hónapig szedte a HELMIRON-t — javult a vérképe, elmúlt a fáradtság. Nem túlzok. Rendelj nyugodtan, az apukád megérdemli az esélyt.',
    'Руйке, моята майка е на 82 години! От години анемия, която не отмина дори при добавки с желязо. Пи HELMIRON един месец — кръвната картина се подобри, умората отмина. Не преувеличавам. Поръчай спокойно, баща ти заслужава този шанс.')
rep('Alexandra, rendelj nyugodtan. 78 évesen állandó gyomorproblémáim voltak — senki nem tudta, mi az. A HELMIRON egy hónap alatt talpra állított. Az apukádnak jobban szüksége van erre, mint gondolnád.',
    'Руйке, поръчай без страх. На 78 години имах постоянни проблеми със стомаха — никой не знаеше какво е. HELMIRON ме изправи на крака за един месец. На баща ти това му е по-нужно, отколкото си мислиш.')
rep('Egy hete szedem a kapszulákat. Reggelre már nem puffadok, mint egy dob, megszűnt az evés utáni nehézség. És jobban alszom — már nem ébredek hajnali 3-kor. Rendeltem a szomszédasszonynak is, ő is évek óta szenved, mint én.',
    'От седмица пия капсулите. Сутрин вече не съм подута като тъпан, тежестта след ядене отмина. И спя по-добре — вече не се будя в 3 часа. Поръчах и за съседката, и тя от години страда като мен.')
rep('68 évesen azt hittem, normális, hogy állandóan fáradt vagyok. A HELMIRON kúra után — idén felástam az egész kertet, először hosszú idő után. Ez a történet mélyen megrázott. Még vannak becsületes emberek, akik igazat mondanak.',
    'На 68 години мислех, че е нормално да съм постоянно уморена. След курса с HELMIRON — тази година прекопах цялата градина, за първи път от дълго време. Тази история ме разтърси дълбоко. Още има честни хора, които казват истината.')
rep('82 éves vagyok. Tavaly alig funkcionáltam — fáradtság, rossz emésztés, gyenge immunrendszer, állandóan beteg. Kipróbáltam a HELMIRON-t nagy remények nélkül. És működik! Van energiám, normálisan eszem, nem betegszem meg minden huzatnál. A legnagyobb öröm ezekben az években.',
    'На 82 години съм. Миналата година едва функционирах — умора, лошо храносмилане, слаб имунитет, постоянно болен. Пробвах HELMIRON без големи надежди. И работи! Имам енергия, храня се нормално, не се разболявам от всяко течение. Най-голямата радост в тези години.')
rep('A feleségem évekig szenvedett — bőr, fáradtság, „neurózis”. Attól féltem, hogy valami komolyabb dologról van szó. Rendeltem HELMIRON-t a kedvezménnyel. 4 hét után — tegnap magától ment a piacra, és virágokkal tért vissza! Olyan mosolygós volt, mint régen. Szívből köszönöm.',
    'Жена ми страда с години — кожата, умората, „неврозата". Страхувах се, че става дума за нещо по-сериозно. Поръчах HELMIRON с отстъпката. След 4 седмици — вчера сама отиде на пазара и се върна с цветя! Беше усмихната като преди. Благодаря ви от сърце.')
rep('Rendeltem 4 dobozt — anyukámnak, apukámnak és 2-t magamnak. A cikkben szereplő történetek lesújtottak. Ennyi évig mindannyian nem azt kezeltük, amit kellett volna. Már régen meg kellett volna tennem. Véget a kifogásoknak.',
    'Поръчах 4 кутии — за мама, за татко и 2 за мен. Историите в статията ме сринаха. Толкова години всички лекувахме друго вместо онова, което трябваше. Отдавна трябваше да го направя. Край на оправданията.')
rep('Megkaptam a HELMIRON-t — a futár 2 nap alatt kiszállította! Rögtön elkezdtem szedni a kapszulákat. Szívből drukkolok. Elküldöm ezt a cikket a nővéremnek is — ő is évek óta szenved az emésztéssel, és senki sem segít neki.',
    'Получих HELMIRON — курierът го достави за 2 дни! Веднага започнах да пия капсулите. Държа палци от сърце. Ще изпратя тази статия и на сестра ми — и тя от години страда с храносмилането, а никой не ѝ помага.')
rep('Kerestem a HELMIRON-t a gyógyszertárban — nincs. Azt mondták, csak erről az oldalról lehet rendelni. Remélem, még elérhető. Az apukámnak sürgősen szüksége van rá — évek óta szenved, az orvosok csak széttárják a kezüket.',
    'Търсих HELMIRON в аптеката — няма го. Казаха ми, че може да се поръча само от тази страница. Надявам се още да е наличен. На баща ми му трябва спешно — от години страда, а лекарите само разперват ръце.')

# ---------- форма комментария, trust, футер ----------
rep('<p class="comments__header-title">HOZZÁSZÓLÁSOK</p>', '<p class="comments__header-title">КОМЕНТАРИ</p>')
rep('Profilkép</label>', 'Добави аватар</label>')
rep('placeholder="Az Ön hozzászólása"', 'placeholder="Вашият коментар"')
rep('<label class="custom-form__photo-label" for="photo">Kép hozzáadása</label>',
    '<label class="custom-form__photo-label" for="photo">Добави снимка</label>')
rep('<button disabled class="custom-form__btn">KÜLDÉS</button>', '<button disabled class="custom-form__btn">ИЗПРАТИ</button>')
rep('Tanúsított minőség</div>', 'Сертифицирано качество</div>')
rep('Szállítás 2–3 napon belül</div>', 'Доставка за 2–3 дни</div>')
rep('Vény nélkül</div>', 'Без рецепта</div>')
rep('Biztonságos rendelés</div>', 'Сигурна поръчка</div>')
rep('— különjelentés<br>', ' — специален репортаж<br>')
rep('Az oldalon található adatok tájékoztató jellegűek, és nem helyettesítik az orvosi konzultációt.',
    'Данните на тази страница са с информативен характер и не заместват медицинската консултация.')

# ---------- применяем ----------
for a, b, n in R:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

for a, b, n in [('alt="Dr. Kovács Gábor"', 'alt="Д-р Запрян Калайджиев"', 1),
                ('Dr. Kovács Gábor\n          <small>', 'Д-р Запрян Калайджиев\n          <small>', 1),
                ('alt="Dr. Kovács Gábor, patológus"', 'alt="Д-р Запрян Калайджиев, патолог"', 1),
                ('<p><b>Dr. Kovács Gábor:</b></p>', '<p><b>Д-р Запрян Калайджиев:</b></p>', 9),
                ('<p><b>Dr. Szabó Ilona:</b></p>', '<p><b>Д-р Божура Налбантова:</b></p>', 1)]:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

open(DST, "w", encoding="utf-8").write(t)
print("записано:", DST, len(t), "знаков")
