# -*- coding: utf-8 -*-
"""Адаптация HU-лендинга HELMIRON на боснийское гео, блок в блок.
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
rep('<html lang="hu">', '<html lang="bs">')
rep('<title>„Láttam őket azok testében, akiknek fogalmuk sem volt róla” — magyar patológus felfedi a hallgatásba burkolt igazságot a parazitákról</title>',
    '<title>„Vidio sam ih u tijelima ljudi koji nisu imali pojma o tome" — bosanski patolog otkriva istinu o parazitima koja se prećutkuje</title>')

# ---------- шапка ----------
rep('Különjelentés · Egészség és Társadalom', 'Specijalni izvještaj · Zdravlje i društvo')
rep('Magyar Egészségügyi Tájékoztató', 'Zdravstveni informator BiH', 2)
rep('Riportok a népegészségügy világából', 'Reportaže iz svijeta javnog zdravstva')

# ---------- заголовок ----------
rep('„ÉVEKIG ÉLTEK BENNEM, ÉN MEG AZ ÉLETKOROMRA ÉS A FÁRADTSÁGOMRA FOGTAM.”',
    '„GODINAMA SU ŽIVJELI U MENI, A JA SAM SVE SVALJIVALA NA GODINE I NA UMOR."')
rep('35 ÉVES TAPASZTALATTAL RENDELKEZŐ PATOLÓGUS FELFEDI AZ IGAZSÁGOT, AMIT SENKI NEM AKAR HALLANI: A PARAZITÁK CSENDBEN PUSZTÍTJÁK A TESTET BELÜLRŐL — ÉS A HALÁL VALÓDI OKÁT MAJDNEM SOHA NEM KERESIK. EGY NŐ TÖRTÉNETE, AKI IDŐBEN MEGMENTETTE MAGÁT.',
    'PATOLOG S 35 GODINA ISKUSTVA OTKRIVA ISTINU KOJU NIKO NE ŽELI ČUTI: PARAZITI TIHO UNIŠTAVAJU TIJELO IZNUTRA — A PRAVI UZROK SMRTI GOTOVO NIKAD NIKO NE TRAŽI. PRIČA ŽENE KOJA SE SPASILA NA VRIJEME.')
rep('Közzétéve: ', 'Objavljeno: ')

# ---------- герой-картинка ----------
rep('Erzsébet a háza előtt egy alföldi faluban', 'Zejna pred svojom kućom u selu u Posavini')
rep('Patológus megerősítette', 'Potvrdio patolog')

# ---------- подзаголовок ----------
rep('Hogyan kezelte évekig Erzsébet (62 éves), háztartásbeli egy alföldi faluban a „gyomorhurutot”, „allergiát” és a „krónikus fáradtságot” — miközben orvosokra költötte a pénzt, akik sosem keresték a valódi okot. Egészen addig, amíg a falusi állatorvos fel nem tett neki egy kérdést, ami megváltoztatta az életét: „Mikor féregtelenítette utoljára önmagát?” Ami ezután következett, azt egy 35 éves tapasztalattal rendelkező patológus is megerősítette.',
    'Kako je Zejna (62 godine), domaćica iz sela u Posavini, godinama liječila „gastritis", „alergiju" i „hronični umor" — dok je novac davala ljekarima koji nikad nisu tražili pravi uzrok. Sve do dana kad joj je seoski veterinar postavio pitanje koje joj je promijenilo život: „A sebe kad ste zadnji put očistili od parazita?" Ono što je slijedilo potvrdio je i patolog s 35 godina iskustva.')

# ---------- первые абзацы ----------
rep('Egy kedd reggel érkeztünk egy alföldi faluba, Szeged közelébe. Az út egy földúton vezet, régi házak, kertek és ugató kutyák mellett. Erzsébet a kapunál fogadott minket, a köténye még mindig a derekán volt — éppen főzött valamit. „Bárcsak tudnák, hány évet vesztettem el” — mondta köszönés helyett. „Mennyi pénzt. Hány orvost. És a válasz olyan egyszerű volt, hogy még most is rosszul leszek, ha arra gondolok.”',
    'Došli smo jednog jutra u utorak u selo u Posavini, blizu Brčkog. Ulazi se zemljanim putem, pored starih kuća, bašča i pasa koji laju. Zejna nas je primila na kapiji, s keceljom još oko pasa — upravo je nešto kuhala. „Da znate koliko sam godina izgubila" — rekla je umjesto dobar dan. „Koliko novca. Koliko ljekara. A odgovor je bio tako jednostavan da mi i sad pozli kad se sjetim."')
rep('Erzsébet 62 éves. Egész életét ebben a faluban élte le — kert, gazdaság, szombati vásár. Soha nem volt betegeskedő asszony. De az elmúlt hat évben, ahogy mondja, „lassan kihunyt”, és senki nem tudta, miért.',
    'Zejna ima 62 godine. Cijeli život je provela u ovom selu — bašča, domaćinstvo, subotnja pijaca. Nikad nije bila bolešljiva žena. Ali u posljednjih šest godina, kako sama kaže, „polako se gasila", i niko nije znao zašto.')
rep('Az ok? Évekig nem azt kezelte, amit kellett volna. <b>Az orvosok gyomorhurutot mondtak neki. Aztán allergiát. Aztán „krónikus fáradtságot”. Aztán „neurózist”.</b> Minden szakember a saját tünetét kezelte — de senki nem kereste azt, ami mindezt kiváltotta. Pénzt költött gasztroenterológusra, bőrgyógyászra, vizsgálatokra, amelyek semmit sem mutattak. És közben az életkorát és a fáradtságát hibáztatta.',
    'Uzrok? Godinama nije liječila ono što je trebalo. <b>Ljekari su joj rekli gastritis. Zatim alergija. Zatim „hronični umor". Zatim „neuroza".</b> Svaki specijalista je liječio svoj simptom — ali niko nije tražio ono što je sve to pokretalo. Davala je novac za gastroenterologa, za dermatologa, za analize koje nisu pokazivale ništa. A sve to vrijeme je krivila godine i umor.')

# ---------- две цитаты героини ----------
rep('„Azt hittem, ez az öregség. Hogy normális, ha állandóan fáradt vagyok, puffadok, viszket a bőröm, ebéd után úgy elálmosodok, mintha valaki kikapcsolna. Mindenki azt mondta: „Hát az életkor, Erzsébet, mit akarsz.” De ez nem az öregség volt. Valami élő volt bennem.”',
    '„Mislila sam da je to starost. Da je normalno što sam stalno umorna, što se napuhavam, što me koža svrbi, što me posle jela uhvati san kao da me neko ugasi. Svi su mi govorili: „Pa to su godine, Zejna, šta hoćeš." Ali to nije bila starost. Bilo je nešto živo u meni."')
rep('„A legrosszabb az, hogy minden vizsgálatom rendben volt. A vérképem „normális”. Akkor hogyan érezhetem magam így, ha valaki lassan felfal belülről? Csak amikor az állatorvos megmondta, mit keressek — és amikor a patológus a szemembe nézett és elmondta az igazságot —, akkor értettem meg mindent.”',
    '„Najgore je to što su mi sve analize bile u redu. Krvna slika „normalna". Pa kako se onda mogu tako osjećati, ako me neko polako izjeda iznutra? Tek kad mi je veterinar rekao šta da tražim — i kad me patolog pogledao u oči i rekao istinu — tek tada sam sve shvatila."')
rep('— Erzsébet, 62 éves, Alföld', '— Zejna, 62 godine, Posavina', 3)

# ---------- интервью патолога ----------
rep('„Láttam őket azok testében, akiknek fogalmuk sem volt róla, hogy hordozzák”',
    '„Vidio sam ih u tijelima ljudi koji nisu ni slutili da ih nose u sebi"')
rep('<span>Exkluzív interjú dr. Kovács Gáborral — 35 éves tapasztalattal rendelkező patológussal, aki több mint 9000 boncolást végzett</span>',
    '<span>Ekskluzivni intervju s dr. Nedžadom Čauševićem — patologom s 35 godina iskustva, koji je obavio više od 9000 obdukcija</span>')
rep('Dr. Kovács Gábor: „Harmincöt évig dolgoztam patológusként. Minden korosztályú emberek testét nyitottam fel — és amit újra és újra láttam, azt a nyilvánosság nem tudja, mert hallgatnak róla. <b>Paraziták. Nem a peremvidéken élőknél, nem a „piszkosaknál” — hanem hétköznapi embereknél. Háztartásbelieknél, nyugdíjasoknál, munkásoknál. Olyanoknál, akik életükben azt hitték, hogy teljesen egészségesek.</b>',
    'Dr. Nedžad Čaušević: „Trideset i pet godina sam radio kao patolog. Otvarao sam tijela ljudi svih uzrasta — a ono što sam vidio iznova i iznova javnost ne zna, jer se o tome prećutkuje. <b>Paraziti. Ne kod onih s margine, ne kod „prljavih" — nego kod običnih ljudi. Kod domaćica, kod penzionera, kod radnika. Kod ljudi koji su cijeli život vjerovali da su potpuno zdravi.</b>')
rep('<b>SZÍVROHAMRA, AGYVÉRZÉSRE, ARRA HALTÁK MEG, AMIT „ISMERETLEN EREDETŰ DAGANATNAK” NEVEZTEK —\n          <span class="red-txt">DE A VALÓDI OKOT SENKI NEM KERESTE. MERT SENKINEK NEM JUTOTT ESZÉBE, HOGY ODA NÉZZEN.”</span></b>',
    '<b>UMIRALI SU OD SRČANOG UDARA, OD MOŽDANOG UDARA, OD ONOGA ŠTO SE NAZIVALO „TUMOR NEPOZNATOG PORIJEKLA" —\n          <span class="red-txt">A PRAVI UZROK NIKO NIJE TRAŽIO. JER NIKOME NIJE PALO NA PAMET DA POGLEDA TAMO."</span></b>')
rep('Dr. Kovács nyugodtan beszél, drámaiság nélkül — mint aki túl sokszor látta a történetek végét. Néhány éve nyugdíjba vonult, de amit a boncasztalnál tanult, mint mondja, „minden alkalommal kísérti, amikor látja, hogy az emberek a következményeket kezelik, nem az okot”.',
    'Dr. Čaušević govori mirno, bez drame — kao čovjek koji je previše puta vidio kraj priče. Penzionisao se prije nekoliko godina, ali ono što je naučio za obdukcionim stolom, kako kaže, „progoni me svaki put kad vidim ljude koji liječe posljedice, a ne uzrok".')
rep('„A legtöbb ember azt hiszi, hogy a paraziták a múlté, a szegénységé, más országoké. Ez a tévedés öl. A paraziták mindenhol körülöttünk vannak — a félig átsült húsban, a saját kertből származó mosatlan zöldségekben, a földben, a vízben, a kezeken, miután megsimogattuk a kutyát vagy a macskát. És ha egyszer bejutnak, évekig élhetnek a testben, szaporodhatnak és lassan mérgezhetik a szervezetet — miközben Ön azt hiszi, hogy ez <b>gyomorhurut, allergia vagy „csak fáradtság”</b>.“',
    '„Većina ljudi misli da su paraziti nešto iz prošlosti, iz sirotinje, iz drugih zemalja. Ta zabluda ubija. Paraziti su svuda oko nas — u nedovoljno pečenom mesu, u neopranom povrću iz vlastite bašče, u zemlji, u vodi, na rukama nakon što pomazimo psa ili mačku. A kad jednom uđu, mogu godinama živjeti u tijelu, razmnožavati se i polako trovati organizam — dok vi mislite da je to <b>gastritis, alergija ili „samo umor"</b>."')
rep('„Feltártam egy 58 éves férfi testét, aki szívrohamban halt meg. Első pillantásra tiszta eset. De amit a beleiben és a májában találtam — annak nem lett volna szabad ott lennie. Ez az ember évekig hordozott magában valamit, ami belülről mérgezte. A jegyzőkönyvben az állt: „szívroham”. A valódi okról — egy szó sem. Ez történik szinte mindig.”',
    '„Otvorio sam tijelo muškarca od 58 godina koji je umro od srčanog udara. Na prvi pogled jasan slučaj. Ali ono što sam našao u njegovim crijevima i u jetri — to tamo nije smjelo biti. Taj čovjek je godinama nosio u sebi nešto što ga je trovalo iznutra. U nalazu je pisalo: „srčani udar". O pravom uzroku — ni riječi. Tako je gotovo svaki put."')
rep('— dr. Kovács Gábor interjújából', '— iz intervjua s dr. Nedžadom Čauševićem')

# ---------- аптечные таблетки ----------
rep('„A gyógyszertári tabletták nem oldják meg a problémát — egy fajtát ütnek le, és ott hagynak tucatnyit”',
    '„Tablete iz apoteke ne rješavaju problem — obore jednu vrstu, a ostave desetak"')
rep('<span>Miért vall kudarcot a szokásos féregellenes kezelés szinte mindig — és miért károsítja a májat</span>',
    '<span>Zašto uobičajeno liječenje protiv parazita gotovo uvijek propada — i zašto oštećuje jetru</span>')
rep('— Őszintén szólva: az nyugtalanít a legjobban, hogy mennyi ember hiszi azt, hogy elég bevenni egy tablettát a gyógyszertárból és kész. Ez veszélyes tévedés. <b>Több mint ötven parazitafaj élhet az emberi testben</b> — egyesek a bélben, mások a májban, mások az epeutakban, mások az izmokban. Egy gyógyszertári tabletta legfeljebb egy-két fajtát támad meg. A többi ott marad, szaporodik és tovább mérgezi a szervezetet.',
    '— Iskreno: najviše me brine koliko ljudi vjeruje da je dovoljno popiti jednu tabletu iz apoteke i to je sve. To je opasna zabluda. <b>U ljudskom tijelu može živjeti više od pedeset vrsta parazita</b> — jedni u crijevima, drugi u jetri, treći u žučnim putevima, četvrti u mišićima. Jedna tableta iz apoteke napada najviše jednu ili dvije vrste. Ostali ostaju, razmnožavaju se i dalje truju organizam.')
rep('Ez egy ördögi kör: az ember lenyel egy tablettát, néhány hétig jobban érzi magát, aztán a tünetek visszatérnek — fáradtság, puffadás, bőrproblémák —, és azt gondolja, hogy ez „nem a parazitáktól van, mert hiszen szedtem a gyógyszert”. Pedig valójában csak a probléma egy részét érintette. És ami még rosszabb: <b>az ezekben a tablettákban lévő erős vegyszerek a májat és a vesét támadják</b>, pontosan azokat a szerveket, amelyek már amúgy is túlterheltek a paraziták elleni küzdelemben.',
    'To je zatvoren krug: čovjek popije tabletu, nekoliko sedmica se osjeća bolje, onda se simptomi vrate — umor, napuhavanje, problemi s kožom — i pomisli da to „nije od parazita, jer sam pio lijek". A u stvarnosti je dotakao samo jedan dio problema. I, što je još gore: <b>jake hemikalije u tim tabletama napadaju jetru i bubrege</b>, upravo one organe koji su i bez toga preopterećeni borbom s parazitima.')
rep('Erzsébet évekig hordta magával a vizsgálati leleteit. „Minden rendben” — mondták neki. Míg a teste gyengült. Az éjjeliszekrényen dobozok a „gyomorhurut” és „allergia” elleni szerekkel, amelyek semmit sem oldottak meg, mert a valódi okot senki nem kereste.',
    'Zejna je godinama nosila svoje nalaze sa sobom. „Sve je u redu" — govorili su joj. Dok joj je tijelo slabilo. Na noćnom ormariću kutije lijekova protiv „gastritisa" i „alergije", koji nisu riješili ništa, jer pravi uzrok niko nije tražio.')
rep('A krónikus fáradtság, puffadás, bőrproblémák, allergiák és „neurózis” 40 éves kor után nem mindig „az életkortól” vannak — nagyon gyakran annak a jelei, hogy a test parazitákat hordoz, amelyek belülről pusztítják.',
    'Hronični umor, napuhavanje, problemi s kožom, alergije i „neuroza" nakon 40. godine nisu uvijek „od godina" — veoma često su znak da tijelo nosi parazite koji ga uništavaju iznutra.')
rep('A „gyomorhurutra” és „allergiára” szedett tabletták csak elfedik a tüneteket, miközben a valódi ok csendben tovább szaporodik. Megfelelő, teljes mértékű testtisztítás nélkül a test évről évre gyengül — és a paraziták elterjednek a májban, az epehólyagban és más szervekben.',
    'Tablete koje se piju za „gastritis" i „alergiju" samo prekrivaju simptome, dok se pravi uzrok u tišini dalje razmnožava. Bez pravilnog i potpunog čišćenja organizma tijelo slabi iz godine u godinu — a paraziti se šire u jetru, u žučnu kesu i u druge organe.')
rep('— Kérem, fogják fel a helyzet súlyát. Egész karrierem során láttam, mit tesznek a paraziták a testtel az évek során. Az emberek járják az orvosokat „neurózis”, „allergia”, „gyomorhurut”, „migrén” miatt — és senki nem teszi meg, amit kellene, és nem néz oda, ahová kellene. <b>A GYÓGYSZERTÁRI TABLETTÁK NEM TISZTÍTJÁK MEG TELJESEN A TESTET — EGY FAJTÁT ÜTNEK LE, A TÖBBIT PEDIG OTT HAGYJÁK, HOGY TOVÁBB PUSZTÍTSON BELÜLRŐL!</b>',
    '— Molim vas, shvatite ozbiljnost situacije. U cijeloj svojoj karijeri sam vidio šta paraziti godinama rade tijelu. Ljudi obilaze ljekare zbog „neuroze", „alergije", „gastritisa", „migrene" — i niko ne radi ono što bi trebalo i ne gleda tamo gdje bi trebalo. <b>TABLETE IZ APOTEKE NE ČISTE TIJELO DO KRAJA — OBORE JEDNU VRSTU, A OSTALE OSTAVE DA DALJE UNIŠTAVAJU IZNUTRA!</b>')
rep('És ami a leginkább megérint: ezek az emberek nem tudták. Azt hitték, hogy egészségesek. Az éveket, a munkát, a stresszt hibáztatták. Pedig egész idő alatt valami élőt hordoztak magukban, ami belülről mérgezte őket — és senki nem mondta nekik, hogy ellenőriztessék.',
    'A ono što me najviše dira: ti ljudi nisu znali. Vjerovali su da su zdravi. Krivili su godine, posao, stres. A sve to vrijeme su nosili u sebi nešto živo što ih je trovalo iznutra — i niko im nije rekao da se provjere.')
rep('„Hét évig kezeltem az „allergiámat”. Krém, tabletta, csepp. A bőröm égett, viszketett, a kiütések a semmiből jöttek. Egyetlen bőrgyógyász sem említette a parazitákat. Csak amikor elkezdtem szedni a kapszulákat — három hét alatt megnyugodott a bőröm, először hét év után.”',
    '„Sedam godina sam liječila svoju „alergiju". Krema, tablete, kapi. Koža mi je gorjela, svrbila, osip se javljao iz čista mira. Nijedan dermatolog nije spomenuo parazite. Tek kad sam počela piti kapsule — za tri sedmice mi se koža umirila, prvi put nakon sedam godina."')
rep('„Én öt évig kezeltettek gyomorhuruttal. Puffadás, gyomornehezülés, hányinger evés után. Mindent megittam, amit adtak. Semmi. Pedig paraziták voltak — ezt később az orvos mondta meg. Öt év és egy csomó pénz a kukában, mert senki nem kereste a valódi okot.”',
    '„Mene su pet godina liječili od gastritisa. Napuhavanje, težina u stomaku, mučnina nakon jela. Popio sam sve što su mi dali. Ništa. A bili su paraziti — to mi je kasnije rekao doktor. Pet godina i gomila novca u smeće, jer pravi uzrok niko nije tražio."')
rep('— Zoltán, 60 éves, Budapest környéke', '— Suvad, 60 godina, blizu Sarajeva')
rep('<b>Balra: egészséges bél ép nyálkahártyával. Jobbra: parazitákkal terhelt bél — krónikus gyulladás, sérült nyálkahártya, a szervezet folyamatos mérgezése. A paraziták az Ön testéből táplálkoznak, és salakanyagokat bocsátanak ki, amelyek mérgezik a vért. A gyógyszertári tabletták, amelyek csak egy fajtát támadnak, ezt nem oldják meg.</b>',
    '<b>Lijevo: zdravo crijevo s netaknutom sluznicom. Desno: crijevo puno parazita — hronična upala, oštećena sluznica, stalno trovanje organizma. Paraziti se hrane iz vašeg tijela i izbacuju otpadne materije koje truju krv. Tablete iz apoteke, koje napadaju samo jednu vrstu, to ne rješavaju.</b>')
rep('Fontos hangsúlyozni: a legtöbb esetben még a gyógyszertári tabletták időszakos szedése mellett is visszatér a probléma, mert a valódi ok — több parazitafaj, amelyek a test különböző részein élnek — megoldatlan marad.',
    'Važno je naglasiti: u većini slučajeva problem se vraća čak i uz povremeno pijenje tableta iz apoteke, jer pravi uzrok — više vrsta parazita koji žive u različitim dijelovima tijela — ostaje neriješen.')
rep('A paraziták évekig tartó hordozása után sokan nemcsak az energiájukat vesztik el, hanem a májuk, epehólyagjuk és beleik egészségét is. A krónikus mérgezés, a legyengült immunrendszer, az állandó gyulladások — ez az ára annak, hogy senki nem kereste a valódi okot időben.',
    'Nakon godina nošenja parazita mnogi ne izgube samo energiju, nego i zdravlje jetre, žučne kese i crijeva. Hronično trovanje, oslabljen imunitet, stalne upale — to je cijena toga što niko nije na vrijeme tražio pravi uzrok.')

# ---------- случаи ----------
rep('Esetek, amelyek megváltoztatták a szemléletemet — és megváltoztatják azt is, ahogyan Ön a saját egészségére tekint',
    'Slučajevi koji su promijenili moj pogled na stvari — i koji će promijeniti i način na koji vi gledate na svoje zdravlje')
rep('— Engedjék meg, hogy elmondjam, mit láttam évről évre. Nem számokat. Nem statisztikákat. Embereket. Embereket nevekkel, akik az utolsó napig azt hitték, hogy a problémájuk teljesen más.',
    '— Dozvolite mi da vam kažem šta sam vidio iz godine u godinu. Ne brojeve. Ne statistiku. Ljude. Ljude s imenima, koji su do posljednjeg dana vjerovali da je njihov problem nešto sasvim drugo.')
rep('Nő, 64 éves. Évekig kezelték „krónikus allergiával” és vérszegénységgel, amely sem vassal, sem vitaminokkal „nem akart javulni”. Senki nem gondolta, hogy valami a testében megeszi helyette a vasat.',
    'Žena, 64 godine. Godinama liječena od „hronične alergije" i anemije koja „nije htjela da se popravi" ni sa željezom ni s vitaminima. Nikom nije palo na pamet da nešto u njenom tijelu jede željezo umjesto nje.')
rep('„Állandóan fáradt voltam, sápadt, mint a fal. Az orvosok azt mondták: „vashiány, kérem szedjen tablettákat”. Évekig szedtem. Semmi. Senki nem kérdezte meg, hogy talán valami elveszi tőlem a vasat. Pedig elvitte.”',
    '„Bila sam stalno umorna, blijeda kao kreč. Ljekari su govorili: „manjak željeza, pijte tablete". Pila sam godinama. Ništa. Niko me nije pitao da li mi možda nešto odnosi željezo. A odnosilo je."')
rep('— dr. Kovács által említett esetekből', '— iz slučajeva koje je iznio dr. Čaušević', 2)
rep('Férfi, 67 éves. „Neurózissal” és álmatlansággal kezelték. Éjszaka fogát csikorgatta, kimerülten ébredt, fogyott, pedig normálisan evett. Mindent a stresszre és az életkorra fogtak.',
    'Muškarac, 67 godina. Liječen od „neuroze" i nesanice. Noću je škripao zubima, budio se iscrpljen, mršavio je iako je normalno jeo. Sve je svaljeno na stres i na godine.')
rep('„Fogytam, pedig normálisan ettem. A feleségem viccelődött, hogy „gyors az anyagcserém”. Ez nem volt vicces. Valami helyettem evett, belőlem. Ezt túl későn értettem meg ahhoz, hogy segítsek magamon — de Önök, akik ezt olvassák, nem vagytok elkésve.”',
    '„Mršavio sam, iako sam normalno jeo. Žena se šalila da „imam brz metabolizam". Nije to bilo nimalo smiješno. Nešto je jelo umjesto mene, iz mene. To sam shvatio prepozno da bih sebi pomogao — ali vi, koji ovo čitate, nisi zakasnili."')

# ---------- список симптомов ----------
rep('<b>Azok a tünetek, amelyeket leggyakrabban az „életkorra”, „stresszre” vagy „rossz táplálkozásra” fognak — pedig nagyon gyakran a testben élő paraziták jelei:</b>',
    '<b>Simptomi koje najčešće svaljujemo na „godine", „stres" ili „lošu ishranu" — a veoma često su znak parazita koji žive u tijelu:</b>')
rep('<li>Állandó fáradtság és kimerültség — alszol 8 órát, de úgy ébredsz, mintha agyonvertek volna;</li>',
    '<li>Stalan umor i iscrpljenost — spavaš 8 sati, a budiš se kao prebijen;</li>')
rep('<li>Puffadás, gázképződés, gyomornehezülés evés után — „mintha valami forrna a belekben”;</li>',
    '<li>Napuhavanje, gasovi, težina u stomaku nakon jela — „kao da nešto vri u crijevima";</li>')
rep('<li>Váltakozó székrekedés és hasmenés nyilvánvaló ok nélkül;</li>',
    '<li>Zatvor i proliv koji se smjenjuju, bez očiglednog razloga;</li>')
rep('<li>Bőrproblémák — kiütés, viszketés, ekcéma, „allergiák”, amelyek a semmiből jönnek és mennek;</li>',
    '<li>Problemi s kožom — osip, svrab, ekcem, „alergije" koje dolaze i prolaze iz čista mira;</li>')
rep('<li>Ellenállhatatlan édesség- és lisztéhség — a paraziták cukorból táplálkoznak;</li>',
    '<li>Neodoljiva želja za slatkim i tjestenim — paraziti se hrane šećerom;</li>')
rep('<li>Fogcsikorgatás éjszaka, nyugtalan alvás, ébredés hajnali 3 körül;</li>',
    '<li>Škripanje zubima u snu, nemiran san, budenje oko 3 sata ujutro;</li>')
rep('<li>Vérszegénység és vashiány, amelyek még tabletták után sem szűnnek meg;</li>',
    '<li>Anemija i manjak željeza koji ne prolaze ni nakon tableta;</li>')
rep('<li>Sötét karikák a szem alatt, sápadt bőr, törékeny haj és köröm;</li>',
    '<li>Tamni podočnjaci, blijeda koža, krhka kosa i nokti;</li>')
rep('<li>Viszketés a végbélnyílás körül, különösen éjszaka;</li>',
    '<li>Svrab oko analnog otvora, posebno noću;</li>')
rep('<li>Ingerültség, „neurózis”, köd a fejben, gyenge koncentráció;</li>',
    '<li>Razdražljivost, „neuroza", magla u glavi, slaba koncentracija;</li>')
rep('<li>Gyakori megfázások és fertőzések — legyengült immunrendszer, mert a test a parazitákra pazarolja az erőt;</li>',
    '<li>Česte prehlade i infekcije — oslabljen imunitet, jer organizam troši snagu na parazite;</li>')
rep('Mindegyik tünetet könnyű másra fogni. És pontosan ezért maradnak a paraziták évekig felderítetlenül. A figyelmen kívül hagyás egyetlen eredményhez vezet:',
    'Svaki od ovih simptoma je lako svaliti na nešto drugo. I upravo zato paraziti godinama ostaju neotkriveni. Ignorisanje vodi do samo jednog ishoda:')
rep('<b class="red-txt">A SZERVEZET KRÓNIKUS MÉRGEZÉSE, LEGYENGÜLT IMMUNRENDSZER, MÁJ- ÉS BÉLKÁROSODÁS — ÉS A TEST, AMELY ÉVRŐL ÉVRE EGYRE NEHEZEBBEN DOLGOZIK.</b>',
    '<b class="red-txt">HRONIČNO TROVANJE ORGANIZMA, OSLABLJEN IMUNITET, OŠTEĆENA JETRA I CRIJEVA — I TIJELO KOJE IZ GODINE U GODINU RADI SVE TEŽE.</b>')
rep('Minden egyes nap a parazitákkal a testben egy újabb nap a szervezet mérgezésének!\n          Több ezer ember kezeli évekig nem azt, amit kellene — „gyomorhurutot”, „allergiát”, „neurózist” — miközben a valódi ok akadálytalanul tovább pusztítja őket belülről.\n          Cselekedjen most — önmagáért — mielőtt a következmények súlyossá válnának!',
    'Svaki dan s parazitima u tijelu je još jedan dan trovanja organizma!\n          Hiljade ljudi godinama liječe nešto drugo umjesto onoga što treba — „gastritis", „alergiju", „neurozu" — dok ih pravi uzrok nesmetano dalje uništava iznutra.\n          Djelujte sada — radi sebe — prije nego posljedice postanu teške!')

# ---------- передача слова ветеринару ----------
rep('— Én egész életemben a következményeket néztem. De nem én találtam meg a megoldást — a falusi állatorvos, dr. Szabó Ilona tette, aki évtizedekig féregtelenítette az állatállományt. Amikor meghallottam a történetét, megértettem, hogy tud valamit, amit mi, orvosok évekig figyelmen kívül hagyunk. Átadom neki a szót.',
    '— Ja sam cijeli život gledao posljedice. Ali rješenje nisam našao ja — našla ga je seoska veterinarka, dr. Hatidža Zukanović, koja je decenijama čistila stoku od parazita. Kad sam čuo njenu priču, shvatio sam da ona zna nešto što mi, ljekari, godinama ignorišemo. Dajem joj riječ.')
rep('„Megértettem, hogy kell lennie egy módnak, hogy a testet gyengéden tisztítsuk meg — ne pedig erős vegyszerekkel mérgezzük”',
    '„Shvatila sam da mora postojati način da se tijelo očisti nježno — a ne da se truje jakim hemikalijama"')
rep('<span>Hogyan fejlesztett ki a falusi állatorvos évek alatt egy gyógynövényes formulát, amely teljesen megtisztítja a szervezetet</span>',
    '<span>Kako je seoska veterinarka godinama razvijala biljnu formulu koja do kraja očisti organizam</span>')
rep('<b>Dr. Szabó Ilona, állatorvos több mint 30 éves tapasztalattal:</b>',
    '<b>Dr. Hatidža Zukanović, veterinarka s više od 30 godina iskustva:</b>')
rep('— Pályafutásom során állatokat kezeltem. És amit minden falusi ember tud, de ritkán gondol bele: <b>a kutyát és a macskát évente kétszer kötelező féregteleníteni. Az állatállományt — szarvasmarhát, juhot, sertést — ütemterv szerint, rendszeresen. A lovakat az istállóban szintén.</b> Mert ha ezt nem teszed meg, az állat legyengül, elsorvad, és végül elpusztul. Ez alapvető tudás a falun.',
    '— Cijelu karijeru sam liječila životinje. A ono što svaki čovjek na selu zna, ali o čemu rijetko razmišlja: <b>psa i mačku je obavezno očistiti od parazita dva puta godišnje. Stoku — krave, ovce, svinje — po planu, redovno. Konje u štali isto tako.</b> Jer ako to ne uradiš, životinja oslabi, usahne i na kraju ugine. To je osnovno znanje na selu.')
rep('És akkor egy nap arra gondoltam: <b>az állatokat rendszeresen féregtelenítjük — magunkat soha. Az ember, aki együtt él ezekkel az állatokkal, ugyanazt a húst eszi, ugyanabban a földben túr, ugyanabból a kútból iszik — életében egyszer sem tisztítja meg magát.</b> Paradoxon: az állat jobban védett, mint a gazdája.',
    'I onda sam jednog dana pomislila: <b>životinje redovno čistimo od parazita — sebe nikad. Čovjek, koji živi s tim životinjama, jede isto meso, kopa po istoj zemlji, pije iz istog bunara — sebe ni jednom u životu ne očisti.</b> Paradoks: životinja je bolje zaštićena od svog gospodara.')
rep('Évekig készítettem az állatoknak gyógynövényes keveréket a paraziták elűzésére. Gyógynövényesnek és gyengédnek kellett lennie — erős vegyszereket nem mertem használni, mert ezen állatok teje és húsa az emberek asztalára kerül. És észrevettem valamit: a gazdaság dolgozói, akik ugyanebből a keverékből ittak teát — „gyomornehezülésre” — abbahagyták a fáradtságra, a bőrre, az emésztésre való panaszokat. Így kezdődött.',
    'Godinama sam za životinje pravila biljnu mješavinu koja istjeruje parazite. Morala je biti biljna i nježna — jake hemikalije nisam smjela koristiti, jer mlijeko i meso tih životinja dolazi na ljudski stol. I zapazila sam nešto: ljudi koji su radili u domaćinstvu i pili čaj od te iste mješavine — zbog „težine u stomaku" — prestali su se žaliti na umor, na kožu, na probavu. Tako je počelo.')

# ---------- состав ----------
rep('<b>Dr. Szabó Ilona gyógynövényes formulája az alábbi összetevőket tartalmazza:</b>',
    '<b>Biljna formula dr. Hatidže Zukanović sadrži sljedeće sastojke:</b>')
rep('<b>Üröm (Artemisia absinthium)</b>', '<b>Pelin (Artemisia absinthium)</b>')
rep('<font>Hagyományosan a legismertebb gyógynövényes szer a paraziták elűzésére a belekből</font>',
    '<font>Tradicionalno najpoznatije biljno sredstvo za istjerivanje parazita iz crijeva</font>')
rep('<b>Bogáncs (Tanacetum vulgare)</b>', '<b>Povratič (Tanacetum vulgare)</b>')
rep('<font>Erőteljesen hat a bélparazitákra és azok petéire</font>',
    '<font>Snažno djeluje na crijevne parazite i na njihova jaja</font>')
rep('<b>Szegfűszeg (Eugenol)</b>', '<b>Karanfilić (Eugenol)</b>')
rep('<font>Lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el</font>',
    '<font>Razgrađuje jaja i larve parazita — ono do čega sredstva protiv odraslih ne dolaze</font>')
rep('<b>Fekete dió (Juglans nigra)</b>', '<b>Crni orah (Juglans nigra)</b>')
rep('<font>Kivonat a héjból: tisztítja a beleket és segít eltávolítani a parazitákat</font>',
    '<font>Ekstrakt iz ljuske: čisti crijeva i pomaže izbacivanju parazita</font>')
rep('<b>Tök mag (Cucurbita)</b>', '<b>Sjemenke bundeve (Cucurbita)</b>')
rep('<font>Gyengéden hat a parazitákra és nyugtatja a bél nyálkahártyáját</font>',
    '<font>Nježno djeluje na parazite i umiruje crijevnu sluznicu</font>')
rep('Ezeket a gyógynövényeket nehéz a megfelelő arányban összekeverni. Ha a keverék nem pontos, a kapszulák csak egy parazitafajtát támadnak — pontosan úgy, mint a gyógyszertári tabletta —, és a többi ott marad. A titok abban rejlik, hogy egyszerre több fajtára hatnak: a kifejlett egyedekre, a petékre és a lárvákra is.',
    'Ove biljke je teško pomiješati u pravom odnosu. Ako mješavina nije tačna, kapsule napadaju samo jednu vrstu parazita — isto kao tableta iz apoteke — a ostali ostaju. Tajna je u tome da djeluju na više vrsta istovremeno: i na odrasle, i na jaja, i na larve.')

# ---------- рождение продукта ----------
rep('Így született a HELMIRON — gyógynövényes kapszulák, amelyek teljesen és gyengéden tisztítják meg a szervezetet a parazitáktól, erős vegyszerek nélkül',
    'Tako je nastao HELMIRON — biljne kapsule koje do kraja i nježno čiste organizam od parazita, bez jakih hemikalija')
rep('— A keveréket, amelyet az állatoknak készítettem, átdolgoztam emberi használatra — pontos gyógynövények, pontos arányok, kapszula formában, amely kényelmes a szervezet számára. A neve HELMIRON. Egyszerűen szedhető: egy kapszula reggel és este, vízzel lenyelve, a kúra teljes időtartama alatt. Erős vegyszerek nélkül — a gyógynövények végzik a munkájukat a belekben, pontosan ott, ahol a paraziták élnek.',
    '— Mješavinu koju sam pravila za životinje preradila sam za ljudsku upotrebu — tačne biljke, tačni odnosi, u obliku kapsule, koja je ugodna za organizam. Zove se HELMIRON. Uzima se jednostavno: jedna kapsula ujutro i jedna uvečer, popiti s vodom, cijelo vrijeme kure. Bez jakih hemikalija — biljke rade svoj posao u crijevima, tačno tamo gdje paraziti žive.')
rep('Az erő abban rejlik, hogy a kapszulák fokozatosan és teljesen hatnak: először a kifejlett parazitákra, majd azok petéire és lárváira, ezután segítenek a testnek mindent kiüríteni, és hagyják a beleket és a májat regenerálódni. A gyógyszertári tabletta egyetlen célpontot támad. A kapszulák végighaladnak az egész emésztőrendszeren — ott, ahol a paraziták valóban találhatók.',
    'Snaga je u tome da kapsule djeluju postepeno i do kraja: prvo na odrasle parazite, zatim na njihova jaja i larve, nakon toga pomažu tijelu da sve izbaci i puštaju crijeva i jetru da se obnove. Tableta iz apoteke napada jednu jedinu tačku. Kapsule prolaze kroz cijeli probavni trakt — tamo gdje se paraziti stvarno nalaze.')
rep('A „HELMIRON” különleges. Minden gyógynövény — a megfelelő arányban — a paraziták különböző fázisaiban támad: kifejlett egyedek, peték, lárvák. Ezért tisztít teljesen, nem részlegesen. A legfontosabb: gyengéden hat, anélkül, hogy megtámadná a májat és a vesét, ahogyan azt az erős gyógyszertári tabletták teszik. Először a gazdaság dolgozói szedték, majd később a hétköznapi emberek is mindazokkal a „megoldhatatlan” panaszokkal — fáradtság, bőr, emésztés.',
    '„HELMIRON" je poseban. Svaka biljka — u pravom odnosu — napada parazite u različitim fazama: odrasli, jaja, larve. Zato čisti do kraja, a ne djelimično. Najvažnije: djeluje nježno, bez napada na jetru i bubrege, kako to rade jake tablete iz apoteke. Prvo su ga pili ljudi koji su radili u domaćinstvu, a kasnije i obični ljudi sa svim onim „nerješivim" tegobama — umor, koža, probava.')
rep('<p><b>Erzsébet:</b></p>', '<p><b>Zejna:</b></p>')
rep('— Az állatorvos adott nekem egy dobozzal, és azt mondta: „Próbáld ki, Erzsébet, mit veszíthetsz?” Reggel és este szedtem a kapszulákat. A harmadik-negyedik napon éreztem, hogy a gyomrom könnyebb, mint évek óta. Nem hittem el, hogy a kapszuláktól van. Azt hittem — véletlen. Csak később, amikor a patológus elmagyarázta, értettem meg, mi is történt valójában a testemben.',
    '— Veterinarka mi je dala jednu kutiju i rekla: „Probaj, Zejna, šta imaš izgubiti?" Pila sam kapsule ujutro i uvečer. Trećeg-četvrtog dana sam osjetila da mi je stomak lakši nego godinama. Nisam vjerovala da je od kapsula. Mislila sam — slučajnost. Tek kasnije, kad mi je patolog objasnio, shvatila sam šta se u mom tijelu stvarno dogodilo.')

# ---------- четыре шага ----------
rep('4 lépés, amelyben a HELMIRON megtisztítja a szervezetet a parazitáktól — bármilyen életkorban',
    '4 koraka kroz koje HELMIRON čisti organizam od parazita — u svakoj životnoj dobi')
rep('<h1>A „HELMIRON” kapszulák 4 alapvető hatása:</h1>', '<h1>4 osnovna djelovanja kapsula „HELMIRON":</h1>')
rep('<font>A kifejlett paraziták elűzése:</font>', '<font>Istjerivanje odraslih parazita:</font>')
rep('<span>A kúra első napjaiban az üröm és a bogáncs hat a belekben élő kifejlett parazitákra — gyengíti őket, és segít a szervezetnek természetes úton kiüríteni azokat. Nem egy fajtát, mint a gyógyszertári tabletta, hanem egyszerre többet.</span>',
    '<span>U prvim danima kure pelin i povratič djeluju na odrasle parazite koji žive u crijevima — slabe ih i pomažu organizmu da ih izbaci prirodnim putem. Ne jednu vrstu, kao tableta iz apoteke, nego više njih istovremeno.</span>')
rep('<font>A peték és lárvák elpusztítása:</font>', '<font>Uništavanje jaja i larvi:</font>')
rep('<span>A szegfűszeg (eugenol) lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el. Ez a lépés kulcsfontosságú: enélkül a paraziták visszatérnek a megmaradt petékből. Ezért tisztítanak a kapszulák teljesen, nem részlegesen.</span>',
    '<span>Karanfilić (eugenol) razgrađuje jaja i larve parazita — ono do čega sredstva protiv odraslih ne dolaze. Ovaj korak je ključan: bez njega se paraziti vraćaju iz preostalih jaja. Zato kapsule čiste do kraja, a ne djelimično.</span>')
rep('<font>Méregtelenítés a salakanyagoktól:</font>', '<font>Detoksikacija od otpadnih materija:</font>')
rep('<span>Amikor a paraziták távoznak, a szervezet megtisztul a salakanyagoktól, amelyeket azok évekig választottak ki a vérbe. A fekete dió és a tök mag segít a májnak és a beleknek kiüríteni a felhalmozódott méreganyagokat — megszűnik a fáradtság, a puffadás és a köd a fejben.</span>',
    '<span>Kad se paraziti izbace, organizam se čisti od otpadnih materija koje su oni godinama ispuštali u krv. Crni orah i sjemenke bundeve pomažu jetri i crijevima da izbace nakupljene toksine — prolaze umor, napuhavanje i magla u glavi.</span>')
rep('<font>A belek és az immunrendszer regenerálódása:</font>', '<font>Obnova crijeva i imuniteta:</font>')
rep('<span>A tisztítás után a gyógynövényes keverék nyugtatja a bél nyálkahártyáját, és segít a testnek visszanyerni az erejét. Visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés, és az immunrendszer — amely évekig a paraziták elleni küzdelemben merült ki — ismét megerősödik.</span>',
    '<span>Nakon čišćenja biljna mješavina umiruje crijevnu sluznicu i pomaže tijelu da povrati snagu. Vraća se energija, umiruje se koža, probava se normalizuje, a imunitet — godinama iscrpljen u borbi s parazitima — ponovo se ojača.</span>')

# ---------- наблюдение и таблица ----------
rep('„Először a HELMIRON-t hétköznapi emberek szedték „megoldhatatlan” panaszokkal — az eredmények még engem is megleptek”',
    '„Prvo su HELMIRON pili obični ljudi s „nerješivim" tegobama — rezultati su iznenadili čak i mene"')
rep('<span>2340, 45 és 86 év közötti személy megfigyelése</span>', '<span>Posmatranje na 2340 osoba, od 45 do 86 godina</span>')
rep('— Amikor évtizedes boncolások után először hallottam erről a gyógynövényes keverékről, szkeptikus voltam — mint minden orvos. De az eredmények, amelyeket a szedők mutattak, olyan egyértelműek voltak, hogy nem hagyhattam figyelmen kívül őket. Szakértői csoport kiterjesztette a megfigyelést több mint 2300, egész Magyarországról származó személyre — mindazokkal a tünetekkel, amelyeket szinte senki nem hozott összefüggésbe a parazitákkal.',
    '— Kad sam nakon decenija obdukcija prvi put čuo o toj biljnoj mješavini, bio sam skeptičan — kao svaki ljekar. Ali rezultati koje su pokazivali oni koji su je pili bili su tako jasni da ih nisam mogao ignorisati. Grupa stručnjaka je proširila posmatranje na više od 2300 osoba iz cijele Bosne i Hercegovine — sa svim onim simptomima koje gotovo niko nije vezivao za parazite.')
rep('Olyan embereket láttam, akik évekig kezelték a „gyomorhurutot” és az „allergiát” — és néhány hét alatt visszanyerték az energiájukat, megnyugodott a bőrük, normalizálódott az emésztésük. Amit egyetlen tabletta sem oldott meg évekig.',
    'Vidio sam ljude koji su godinama liječili „gastritis" i „alergiju" — a za nekoliko sedmica su povratili energiju, koža im se umirila, probava se normalizovala. Ono što nijedna tableta nije riješila godinama.')
rep('A „HELMIRON” megfigyelésének eredményei — kontrollcsoport: 2340 fő, 45–86 éves korig',
    'Rezultati posmatranja „HELMIRON" — kontrolna grupa: 2340 osoba, 45–86 godina')
rep('<td class="one">A puffadás és gyomornehezülés megszűnése</td>', '<td class="one">Prestanak napuhavanja i težine u stomaku</td>')
rep('<td class="one">Az energia visszatérése, a krónikus fáradtság megszűnése</td>', '<td class="one">Vraćanje energije, prestanak hroničnog umora</td>')
rep('<td class="one">A bőr megnyugvása (kiütés, viszketés, „allergiák”)</td>', '<td class="one">Umirivanje kože (osip, svrab, „alergije")</td>')
rep('<td class="one">Az emésztés és székletürítés normalizálódása</td>', '<td class="one">Normalizacija probave i stolice</td>')
rep('<td class="one">Az édesség utáni vágy megszűnése</td>', '<td class="one">Prestanak želje za slatkim</td>')
rep('<td class="one">Javuló alvás, a fogcsikorgatás megszűnése</td>', '<td class="one">Bolji san, prestanak škripanja zubima</td>')
rep('<td class="one">A vérkép javulása (vas)</td>', '<td class="one">Poboljšanje krvne slike (željezo)</td>')
rep('<td class="one">A fejben lévő köd megszűnése, jobb koncentráció</td>', '<td class="one">Prestanak magle u glavi, bolja koncentracija</td>')
rep('<td class="one">A sötét karikák eltűnése a szem alatt</td>', '<td class="one">Nestajanje podočnjaka</td>')
rep('<td class="one">Az immunrendszer megerősödése, ritkább fertőzések</td>', '<td class="one">Jačanje imuniteta, rjeđe infekcije</td>')

# ---------- случай героини ----------
rep('Az eset, amely a legjobban megmutatja, mennyi ideig maradnak rejtve a paraziták',
    'Slučaj koji najbolje pokazuje koliko dugo paraziti ostaju skriveni')
rep('Erzsébet, 62 éves. Hat évig kezelték „gyomorhuruttal”, „allergiával” és „krónikus fáradtsággal”. A HELMIRON kapszulák kúrája után — először évek óta kipihenten ébredt, és a bőre megnyugodott.',
    'Zejna, 62 godine. Šest godina liječena od „gastritisa", „alergije" i „hroničnog umora". Nakon kure kapsulama HELMIRON — prvi put nakon godina se probudila odmorna, a koža joj se umirila.')
rep('Erzsébet volt az egyik első, akinek dr. Szabó adta a kapszulákat. 62 évesen, hat év orvosjárás után, normális vizsgálati eredményekkel és egy testtel, amely napról napra egyre gyengébb volt. A lánya Bécsben, a fia Németországban — telefonáltak, küldték a pénzt, de senki nem vette észre, hogy kialszik, mert ők is azt hitték, hogy ez „csak fáradtság és az életkor”.',
    'Zejna je bila jedna od prvih kojima je dr. Zukanović dala kapsule. Sa 62 godine, nakon šest godina obilaženja ljekara, s normalnim nalazima i s tijelom koje je slabilo iz dana u dan. Kćerka u Beču, sin u Njemačkoj — telefonirali su, slali novac, ali niko nije primijetio da se gasi, jer su i oni vjerovali da je to „samo umor i godine".')
rep('„Hat éve vonszoltam magam orvostól orvosig. Állandóan fáradt voltam, puffadt, a bőröm égett és viszketett, a hajam hullott. Azt mondták: gyomorhurut, allergia, neurózis, életkor. Mindent beszedtem, amit adtak. Semmi sem segített, és úgy éreztem, mintha valaki lassan felfalna belülről.',
    '„Šest godina sam se vukla od ljekara do ljekara. Bila sam stalno umorna, naduta, koža mi je gorjela i svrbila, kosa mi je opadala. Govorili su: gastritis, alergija, neuroza, godine. Popila sam sve što su mi dali. Ništa nije pomoglo, a osjećala sam se kao da me neko polako izjeda iznutra.')
rep('A legrosszabb az volt, hogy minden vizsgálat „rendben” volt. Akkor hogyan lehetek ennyire kimerült? Már kezdtem azt hinni, hogy kitalálom, hogy hipochonder lettem. Senki, egyetlen orvos sem említette a parazitákat.',
    'Najgore je bilo to što su svi nalazi bili „u redu". Pa kako onda mogu biti toliko iscrpljena? Već sam počela misliti da izmišljam, da sam postala hipohondar. Niko, nijedan ljekar nije spomenuo parazite.')
rep('Aztán jött hozzám az állatorvos a tehén miatt. És mellékesen rám nézett, és megkérdezte: „Erzsébet, mikor féregtelenítetted utoljára magadat? A kutyát évente kétszer féregteleníted, magadat egyszer sem.” Adott a kapszuláiból. A harmadik napon a gyomrom könnyebb volt, mint évek óta. Egy hét múlva először ébredtem kipihenten. Három hét múlva megnyugodott a bőröm — először hét év után.',
    'Onda je došla kod mene veterinarka zbog krave. I usput me pogledala i pitala: „Zejna, a sebe kad si zadnji put očistila od parazita? Psa čistiš dva puta godišnje, a sebe nijedan put." Dala mi je od svojih kapsula. Trećeg dana mi je stomak bio lakši nego godinama. Nakon sedmicu dana sam se prvi put probudila odmorna. Nakon tri sedmice mi se umirila koža — prvi put nakon sedam godina.')
rep('Sírtam. Nem azért, mert jobban lettem. Hanem mert rájöttem, mennyi évet és pénzt vesztettem el azzal, hogy nem azt kezeltem, amit kellett volna — amikor a válasz ilyen egyszerű volt.',
    'Plakala sam. Ne zato što mi je bilo bolje. Nego zato što sam shvatila koliko sam godina i koliko novca izgubila liječeći nešto drugo umjesto onoga što je trebalo — kad je odgovor bio tako jednostavan.')
rep('<b>Erzsébet, 62 éves, alföldi falu</b>', '<b>Zejna, 62 godine, selo u Posavini</b>')

# ---------- случай шофёра ----------
rep('Egy másik eset: Zoltán, 60 éves, egész életében kamionsofőr, évekig kezelték „gyomorhuruttal”, amely semmilyen tablettára nem szűnt meg.',
    'Drugi slučaj: Suvad, 60 godina, cijeli život vozač kamiona, godinama liječen od „gastritisa" koji nije prošao ni na jednu tabletu.')
rep('„Öt évig kezeltek gyomorhuruttal. Nehézség a gyomorban minden étkezés után, hányinger, puffadás, mint egy dob. Mindenféle vizsgálat, gyógyszerek a gyomorra. Semmi. Fogytam, pedig normálisan ettem.',
    '„Pet godina su me liječili od gastritisa. Težina u stomaku nakon svakog jela, mučnina, naduto kao bubanj. Svakakve analize, lijekovi za stomak. Ništa. Mršavio sam, iako sam normalno jeo.')
rep('A feleségem hallott a HELMIRON kapszulákról a szomszédasszonytól. Azt mondta: próbáld ki, mit veszíthetsz. Reggel és este elkezdtem szedni. Körülbelül tíz nap múlva — először évek óta ettem, és utána semmi nem fájt és nem puffadtam. Egy hónap után úgy éreztem magam, mint egy új ember.',
    'Žena je čula o kapsulama HELMIRON od susjede. Rekla mi je: probaj, šta imaš izgubiti. Počeo sam ih piti ujutro i uvečer. Nakon desetak dana — prvi put nakon godina sam jeo i poslije me ništa nije boljelo i nisam bio naduo. Nakon mjesec dana sam se osjećao kao nov čovjek.')
rep('Ami a legjobban felháborított: öt év és egy csomó pénz a kukába a rossz diagnózis miatt. Paraziták voltak. És senkinek nem jutott eszébe, hogy odanézzen. Ha nincsenek ezek a kapszulák, ki tudja, meddig szenvedtem volna.”',
    'Ono što me najviše razbjesnilo: pet godina i gomila novca u smeće zbog pogrešne dijagnoze. Bili su paraziti. I nikome nije palo na pamet da pogleda tamo. Da nije bilo ovih kapsula, ko zna koliko bih još patio."')

# ---------- не симптомы, а причина ----------
rep('„A HELMIRON nem tüneteket fed el — megtisztítja a testet az okától”',
    '„HELMIRON ne prekriva simptome — čisti tijelo od njihovog uzroka"')
rep('Ebből nemcsak a súlyos esetek profitálnak. Mindenki 40 éves kor felett, aki az első tüneteket érzi, megelőzhet évek felesleges szenvedését.',
    'Od ovoga ne dobijaju samo teški slučajevi. Svako stariji od 40 godina ko osjeća prve simptome može spriječiti godine nepotrebne patnje.')
rep('— A kúra általában 3-4 hétig tart, és azoknál, akik évekig hordozzák a problémát, akár tovább is. Amint dr. Szabó elmagyarázta, a tisztítást évente kétszer, profilaktikusan meg kell ismételni — pontosan úgy, mint az állatoknál —, mert a paraziták újra bekerülhetnek az élelmiszerrel, vízzel vagy a háziállatoktól.',
    '— Kura obično traje 3-4 sedmice, a kod onih koji problem nose godinama i duže. Kako je objasnila dr. Zukanović, čišćenje treba ponoviti dva puta godišnje, profilaktički — tačno kao kod životinja — jer paraziti mogu ponovo ući s hranom, s vodom ili od domaćih životinja.')
rep('A HELMIRON fokozatosan hat: az első napokban megszűnik a puffadás és a gyomornehezülés, majd visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés.',
    'HELMIRON djeluje postepeno: u prvim danima prolaze napuhavanje i težina u stomaku, zatim se vraća energija, umiruje se koža, normalizuje se probava.')
rep('Olyan embereket láttam, akik évekig kezelték a „megoldhatatlan” panaszokat — és néhány hét alatt visszanyerték az erejüket, először hosszú idő után aludtak úgy, mint az emberek. A test maga tudja, hogyan regenerálódjon, ha levesszük róla a terhet, amely pusztította.',
    'Vidio sam ljude koji su godinama liječili „nerješive" tegobe — a za nekoliko sedmica su povratili snagu, prvi put nakon dugo vremena spavali kao ljudi. Tijelo samo zna kako da se obnovi, ako s njega skinemo teret koji ga je uništavao.')
rep('Dr. Szabó Ilona gyógynövényes formulájának köszönhetően Magyarországon több ezer ember tisztította meg a szervezetét a parazitáktól.\n          Íme néhány eset:',
    'Zahvaljujući biljnoj formuli dr. Hatidže Zukanović, hiljade ljudi u Bosni i Hercegovini je očistilo svoj organizam od parazita.\n          Evo nekoliko slučajeva:')

# ---------- четыре подписи ----------
rep('<figcaption>Férfi, 65 éves. Évekig „gyomorhurut” és krónikus fáradtság. HELMIRON kúra: megszűnt a puffadás, visszatért az energia, normalizálódott az emésztés.</figcaption>',
    '<figcaption>Muškarac, 65 godina. Godinama „gastritis" i hronični umor. Kura HELMIRON: napuhavanje je prestalo, energija se vratila, probava se normalizovala.</figcaption>')
rep('<figcaption>Nő, 58 éves. „Allergia” és bőrkiütés évek óta. Kúra után: tiszta bőr, viszketés megszűnt, megszűntek az „allergiás” reakciók.</figcaption>',
    '<figcaption>Žena, 58 godina. „Alergija" i osip na koži godinama. Nakon kure: čista koža, svrab je prestao, prestale su „alergijske" reakcije.</figcaption>')
rep('<figcaption>Nő, 72 éves. Vérszegénység, amely még vas pótlására sem szűnt meg. Kúra után: a vérkép javult, a fáradtság és sápadtság megszűnt.</figcaption>',
    '<figcaption>Žena, 72 godine. Anemija koja nije prošla ni uz dodatke željeza. Nakon kure: krvna slika se poboljšala, umor i bljedoća su prestali.</figcaption>')
rep('<figcaption>Férfi, 70 éves. Állandó puffadás, álmatlanság, fogcsikorgatás. Kúra után: nyugodt alvás, normális székletürítés, visszanyert súly.</figcaption>',
    '<figcaption>Muškarac, 70 godina. Stalno napuhavanje, nesanica, škripanje zubima. Nakon kure: miran san, normalna stolica, vraćena kilaža.</figcaption>')
rep('— Pályafutásom során végig néztem a paraziták testre gyakorolt hosszú távú hatásait. Ezért érintenek meg ezek az esetek: amint ezt a terhet levesszük a testről, az magától regenerálódik. Erős vegyszerek nélkül. Olyan tabletták nélkül, amelyek a májat támadják. <b>Az emberi test erős — csak időben le kell venni róla azt, ami belülről pusztítja.</b>',
    '— Cijelu karijeru sam gledao dugotrajne posljedice parazita na tijelo. Zato me ovi slučajevi diraju: u trenutku kad s tijela skinemo taj teret, ono se obnovi samo. Bez jakih hemikalija. Bez tableta koje napadaju jetru. <b>Ljudsko tijelo je snažno — treba mu samo na vrijeme skinuti ono što ga uništava iznutra.</b>')

# ---------- оффер ----------
rep('Miért nem kapható a HELMIRON a gyógyszertárakban? És hogyan lehet beszerezni?',
    'Zašto se HELMIRON ne nalazi u apotekama? I kako ga nabaviti?')
rep('<p>A HELMIRON gyártása lassú és gondos folyamat. Amint dr. Szabó elmagyarázta, a gyógynövényeket a megfelelő időben kell begyűjteni, és pontos arányban összekeverni — üröm, bogáncs, szegfűszeg, fekete dió, tök mag. Minden kis mennyiségben, kézzel készül, és nem lehet kielégíteni a teljes keresletet.</p>',
    '<p>Proizvodnja HELMIRONA je spor i pažljiv proces. Kako je objasnila dr. Zukanović, biljke se moraju brati u pravo vrijeme i pomiješati u tačnim odnosima — pelin, povratič, karanfilić, crni orah, sjemenke bundeve. Sve se radi u malim količinama, ručno, i nije moguće pokriti cijelu potražnju.</p>')
rep('<p>Legalább 2-3 évre van szükség ahhoz, hogy a HELMIRON a gyógyszertárakba kerüljön. Addig a termék kizárólag online, a támogatási program keretében érhető el. Mindazonáltal,\n      <font class="red-txt">a kedvezmény akár 50% is lehet</font>\n      — ami óriási jelentőséggel bír a nyugdíjasok számára.\n    </p>',
    '<p>Potrebne su najmanje 2-3 godine da HELMIRON dođe u apoteke. Do tada je proizvod dostupan isključivo online, u okviru programa podrške. Pri tome,\n      <font class="red-txt">popust može ići i do 50%</font>\n      — što ima ogromnu važnost za penzionere.\n    </p>')
rep('Kérem Önöket: NE SZALASSZÁK EL A TÁMOGATÁSI PROGRAMOT. Ne csak magukért — hanem a szeretteikért is, akik talán évekig nem azt kezelik, amit kellene, anélkül, hogy sejtenék a valódi okot. Tisztítsák meg magukat — és segítsenek azokon, akik számítanak Önöknek.',
    'Molim vas: NE PROPUSTITE PROGRAM PODRŠKE. Ne samo radi sebe — nego i radi svojih najbližih, koji možda godinama liječe nešto drugo umjesto onoga što treba, a ne slute pravi uzrok. Očistite sebe — i pomozite onima koji vam znače.')
rep('<b>A rendelés leadásához használják az alábbi űrlapot.</b>', '<b>Za narudžbu koristite obrazac ispod.</b>')
rep('Az utolsó lehetőség idén, hogy HELMIRON-t szerezzenek — maguknak vagy szeretteiknek, akik évek óta szenvednek a helyes válasz nélkül',
    'Posljednja prilika ove godine da nabavite HELMIRON — za sebe ili za svoje najbliže, koji godinama pate bez pravog odgovora')
rep('— Kizárólag ennek a portálnak az olvasói számára 20 000 dobozt különítettek el. Minden 40 év feletti magyar állampolgár <font class="red-txt">akár 50% kedvezményt</font> kaphat, de a program <span>',
    '— Isključivo za čitaoce ovog portala odvojeno je 20 000 kutija. Svaki državljanin Bosne i Hercegovine stariji od 40 godina može dobiti <font class="red-txt">popust do 50%</font>, ali program traje do <span>')
rep('      </span>-ig tart.\n    </p>', '      </span>.\n    </p>')
rep('<p>Ne várják meg, amíg a fáradtság, a bőrproblémák és az emésztési panaszok a mindennapok részévé válnak. Amíg pénzt költenek rossz diagnózisokra. Emlékezzenek: az állatokat évente kétszer féregtelenítjük, magunkat egyszer sem. A HELMIRON-t elegendő egy kúra formájában átvenni, majd évente kétszer megismételni — profilaktikusan, pontosan úgy, mint az állatoknál.</p>',
    '<p>Ne čekajte da umor, problemi s kožom i tegobe s probavom postanu dio svakog dana. Da dajete novac za pogrešne dijagnoze. Zapamtite: životinje čistimo od parazita dva puta godišnje, sebe nijedan put. HELMIRON je dovoljno uzeti u obliku kure, a zatim ponoviti dva puta godišnje — profilaktički, tačno kao kod životinja.</p>')
rep('<p>Írják be a nevüket és telefonszámukat. Szakértőnk felveszi Önökkel a kapcsolatot, kiválasztja a megfelelő programot, és megszervezi a kiszállítást futárral vagy postán 2-3 napon belül, közvetlenül a címükre.</p>',
    '<p>Upišite svoje ime i broj telefona. Naš stručnjak će vas kontaktirati, odabrati odgovarajući program i organizovati dostavu kurirom ili poštom u 2-3 dana, direktno na vašu adresu.</p>')
rep('<b>Reménnyel és tisztelettel — dr. Kovács Gábor, patológus. 35 év után a boncasztalnál az egyetlen, amit ajánlok: tisztítsák meg magukat időben. A testük nem fogja elfelejteni.</b>',
    '<b>S nadom i poštovanjem — dr. Nedžad Čaušević, patolog. Nakon 35 godina za obdukcionim stolom jedino što preporučujem je: očistite se na vrijeme. Vaše tijelo to neće zaboraviti.</b>')
rep('<span class="ramka-title">Frissítés: <span>', '<span class="ramka-title">Ažurirano: <span>')
rep('A hatalmas érdeklődés miatt a készletek korábban elfogyhatnak, mint várható! Ma —',
    'Zbog ogromnog interesa zalihe se mogu potrošiti brže od očekivanog! Danas —')
rep('        </span> — a program utolsó napja</font> vagy a készletek kimerüléséig.',
    '        </span> — posljednji je dan programa</font> ili do potrošnje zaliha.')
rep('Figyelem! Ne zárják be és ne frissítsék az oldalt, ellenkező esetben az Ön számára lefoglalt HELMIRON doboz egy másik személyhez kerül!',
    'Pažnja! Ne zatvarajte i ne osvježavajte stranicu, u protivnom će kutija HELMIRONA rezervisana za vas otići drugoj osobi!')
rep('Használják ki az ajánlatot — az Ön helye le van foglalva:', 'Iskoristite ponudu — vaše mjesto je rezervisano:')

# ---------- форма ----------
rep('<b>Hivatalos rendelési űrlap</b>', '<b>Službeni obrazac za narudžbu</b>')
rep('A <b>50% kedvezmény</b> igénybevételéhez írják be a nevüket és telefonszámukat az alábbi mezőkbe, majd nyomják meg a „MEGRENDELEM" gombot.',
    'Da biste iskoristili <b>popust od 50%</b>, upišite svoje ime i broj telefona u polja ispod, a zatim pritisnite dugme „NARUČUJEM".')
rep('Elérhetőség:', 'Dostupno:')
rep('<span class="price_old">19800 HUF</span>', '<span class="price_old">98 KM</span>')
rep('<span class="price_main">9900 HUF</span>', '<span class="price_main">49 KM</span>')
rep('<input type="hidden" name="country" value="HU">', '<input type="hidden" name="country" value="BA">')
rep('<label for="name-input">Név</label>', '<label for="name-input">Ime</label>')
rep('placeholder="Az Ön neve"', 'placeholder="Vaše ime"', 2)
rep('<label for="phone-input">Telefonszám</label>', '<label for="phone-input">Broj telefona</label>')
rep('placeholder="Az Ön telefonszáma"', 'placeholder="Vaš broj telefona"')
rep('<button class="button-submit" type="submit">MEGRENDELEM</button>', '<button class="button-submit" type="submit">NARUČUJEM</button>')
rep('✔️ A szállítást a Nemzeti Közegészségügyi Központ végzi<br> közvetlenül a megadott címre',
    '✔️ Dostavu obavlja Zavod za javno zdravstvo<br> direktno na navedenu adresu')

# ---------- комментарии: имена ----------
for hu, ba in [('Kovács Mária','Mevlida Karahodžić'), ('Nagy Erzsébet','Nermina Tahirović'),
               ('Varga Anna','Behija Mujezinović'), ('Kiss János','Mirsad Avdić'),
               ('Szabó Péter','Fikret Halilović'), ('Tóth Alexandra','Lejla Kadrić'),
               ('Horváth Judit','Zineta Softić'), ('Nagy Kázmér','Hamdija Bećirović'),
               ('Molnár Katalin','Rasema Omerbašić'), ('Farkas Erzsébet','Šefika Mustafić'),
               ('Papp József','Sulejman Pašalić'), ('Balogh Tádé','Vahidin Šabanović'),
               ('Gábor Ibolya','Hajrija Dervišević'), ('Kiss Zsuzsanna','Munira Smailbegović'),
               ('Nagy Gergely','Džemal Mehmedbašić')]:
    rep('<p class="comments__item-name">%s</p>' % hu, '<p class="comments__item-name">%s</p>' % ba)

# ---------- комментарии: тексты ----------
rep('Sírtam, amikor ezt a cikket olvastam. Anyukám 76 éves, és évek óta „gyomorhuruttal” és „allergiával” kezelteti magát — és senki sem említette soha a parazitákat. Minden stimmel, abszolút minden. Rendeltem neki HELMIRON-t. Hogy nem jutott ez hamarabb eszembe?',
    'Plakala sam dok sam čitala ovaj članak. Mama ima 76 godina i godinama se liječi od „gastritisa" i „alergije" — a niko nikad nije spomenuo parazite. Sve se poklapa, apsolutno sve. Naručila sam joj HELMIRON. Kako mi to nije prije palo na pamet?')
rep('A múlt héten megjött a HELMIRON. Reggel és este szedem a kapszulákat. 5 nap után — a puffadás, ami évekig gyötört, majdnem teljesen eltűnt, a gyomrom könnyebb, mint valaha. Ennek a patológusnak a története késztetett a rendelésre. Bárcsak tudnák, milyen jól érzem magam.',
    'Prošle sedmice mi je došao HELMIRON. Pijem kapsule ujutro i uvečer. Nakon 5 dana — napuhavanje koje me mučilo godinama je skoro potpuno prošlo, stomak mi je lakši nego ikad. Priča ovog patologa me natjerala da naručim. Da znate kako se dobro osjećam.')
rep('69 éves vagyok. Hét évig kezeltek „allergiával” — krémek, tabletták, cseppek. A bőröm égett és viszketett. 3 hét HELMIRON kapszula után — a bőröm először nyugodott meg ennyi év után. Magam járok piacra, főzök, normálisan élek. Visszatértem önmagamhoz.',
    'Imam 69 godina. Sedam godina su me liječili od „alergije" — kreme, tablete, kapi. Koža mi je gorjela i svrbila. Nakon 3 sedmice kapsula HELMIRON — koža mi se umirila prvi put nakon toliko godina. Sama idem na pijacu, kuham, živim normalno. Vratila sam se sebi.')
rep('Napi 10 órát dolgozom. Állandó fáradtság, köd a fejben, édesség utáni vágy, amit nem tudtam kontrollálni. Azt hittem — életkor, stressz. Kipróbáltam a HELMIRON-t. 4 hét után — visszatért az energia, tiszta a fejem. Hatalmas tisztelet ennek az állatorvosnak, azt az igazságot mondja, amit senki más nem mond.',
    'Radim 10 sati dnevno. Stalan umor, magla u glavi, želja za slatkim koju nisam mogao kontrolisati. Mislio sam — godine, stres. Probao sam HELMIRON. Nakon 4 sedmice — energija se vratila, glava mi je bistra. Ogromno poštovanje za ovu veterinarku, govori istinu koju niko drugi ne govori.')
rep('Rendeltem 3 dobozt — magamnak, a feleségemnek (állandó bőrproblémák) és az apósomnak. Az állatokat évente kétszer féregtelenítjük, magunkat soha — amikor ezt elolvastam, minden világossá vált. Köszönöm a cikket, felnyitotta a szemem.',
    'Naručio sam 3 kutije — za sebe, za ženu (stalni problemi s kožom) i za punca. Životinje čistimo od parazita dva puta godišnje, sebe nikad — kad sam ovo pročitao, sve mi je postalo jasno. Hvala za članak, otvorio mi je oči.')
rep('Gondolkodom a rendelésen az apukámnak. 78 éves, évek óta panaszkodik az emésztésre és fáradtságra, az orvosok nem találnak semmit. Szerintetek a HELMIRON segíthet ebben a korban is?',
    'Razmišljam da naručim za babu. Ima 78 godina, godinama se žali na probavu i na umor, ljekari ne nalaze ništa. Mislite li da HELMIRON može pomoći i u tim godinama?')
rep('Alexandra, az én anyukám 82 éves! Évek óta vérszegénység, ami még vas pótlására sem szűnt meg. Egy hónapig szedte a HELMIRON-t — javult a vérképe, elmúlt a fáradtság. Nem túlzok. Rendelj nyugodtan, az apukád megérdemli az esélyt.',
    'Lejla, moja mama ima 82 godine! Godinama anemija koja nije prošla ni uz dodatke željeza. Pila je HELMIRON mjesec dana — krvna slika se poboljšala, umor je prošao. Ne preterujem. Naruči bez brige, tvoj babo zaslužuje tu šansu.')
rep('Alexandra, rendelj nyugodtan. 78 évesen állandó gyomorproblémáim voltak — senki nem tudta, mi az. A HELMIRON egy hónap alatt talpra állított. Az apukádnak jobban szüksége van erre, mint gondolnád.',
    'Lejla, naruči bez straha. Sa 78 godina sam imao stalne probleme sa stomakom — niko nije znao šta je. HELMIRON me za mjesec dana podigao na noge. Tvom babi je ovo potrebnije nego što misliš.')
rep('Egy hete szedem a kapszulákat. Reggelre már nem puffadok, mint egy dob, megszűnt az evés utáni nehézség. És jobban alszom — már nem ébredek hajnali 3-kor. Rendeltem a szomszédasszonynak is, ő is évek óta szenved, mint én.',
    'Pijem kapsule sedmicu dana. Ujutro više nisam naduta kao bubanj, prošla je težina nakon jela. I bolje spavam — više se ne budim u 3 ujutro. Naručila sam i za susjedu, i ona godinama pati kao ja.')
rep('68 évesen azt hittem, normális, hogy állandóan fáradt vagyok. A HELMIRON kúra után — idén felástam az egész kertet, először hosszú idő után. Ez a történet mélyen megrázott. Még vannak becsületes emberek, akik igazat mondanak.',
    'Sa 68 godina sam mislila da je normalno što sam stalno umorna. Nakon kure HELMIRON — ove godine sam prekopala cijelu bašču, prvi put nakon dugo vremena. Ova priča me duboko potresla. Još ima čestitih ljudi koji govore istinu.')
rep('82 éves vagyok. Tavaly alig funkcionáltam — fáradtság, rossz emésztés, gyenge immunrendszer, állandóan beteg. Kipróbáltam a HELMIRON-t nagy remények nélkül. És működik! Van energiám, normálisan eszem, nem betegszem meg minden huzatnál. A legnagyobb öröm ezekben az években.',
    'Imam 82 godine. Prošle godine sam jedva funkcionisao — umor, loša probava, slab imunitet, stalno bolestan. Probao sam HELMIRON bez velikih nadanja. I radi! Imam energiju, normalno jedem, ne obolim na svaku promaju. Najveća radost u ovim godinama.')
rep('A feleségem évekig szenvedett — bőr, fáradtság, „neurózis”. Attól féltem, hogy valami komolyabb dologról van szó. Rendeltem HELMIRON-t a kedvezménnyel. 4 hét után — tegnap magától ment a piacra, és virágokkal tért vissza! Olyan mosolygós volt, mint régen. Szívből köszönöm.',
    'Moja žena je godinama patila — koža, umor, „neuroza". Bojao sam se da je nešto ozbiljnije. Naručio sam HELMIRON s popustom. Nakon 4 sedmice — jučer je sama otišla na pijacu i vratila se s cvijećem! Bila je nasmijana kao nekad. Hvala vam od srca.')
rep('Rendeltem 4 dobozt — anyukámnak, apukámnak és 2-t magamnak. A cikkben szereplő történetek lesújtottak. Ennyi évig mindannyian nem azt kezeltük, amit kellett volna. Már régen meg kellett volna tennem. Véget a kifogásoknak.',
    'Naručila sam 4 kutije — za mamu, za babu i 2 za sebe. Priče iz članka su me dotukle. Toliko godina smo svi liječili nešto drugo umjesto onoga što je trebalo. Davno sam to trebala uraditi. Dosta izgovora.')
rep('Megkaptam a HELMIRON-t — a futár 2 nap alatt kiszállította! Rögtön elkezdtem szedni a kapszulákat. Szívből drukkolok. Elküldöm ezt a cikket a nővéremnek is — ő is évek óta szenved az emésztéssel, és senki sem segít neki.',
    'Dobila sam HELMIRON — kurir ga je dostavio za 2 dana! Odmah sam počela piti kapsule. Držim palce od srca. Poslat ću ovaj članak i svojoj sestri — i ona godinama pati s probavom, a niko joj ne pomaže.')
rep('Kerestem a HELMIRON-t a gyógyszertárban — nincs. Azt mondták, csak erről az oldalról lehet rendelni. Remélem, még elérhető. Az apukámnak sürgősen szüksége van rá — évek óta szenved, az orvosok csak széttárják a kezüket.',
    'Tražio sam HELMIRON u apoteci — nema ga. Rekli su da se može naručiti samo s ove stranice. Nadam se da ga još ima. Mom babi je potreban hitno — godinama pati, ljekari samo šire ruke.')

# ---------- форма комментария, trust, футер ----------
rep('<p class="comments__header-title">HOZZÁSZÓLÁSOK</p>', '<p class="comments__header-title">KOMENTARI</p>')
rep('Profilkép</label>', 'Profilna slika</label>')
rep('placeholder="Az Ön hozzászólása"', 'placeholder="Vaš komentar"')
rep('<label class="custom-form__photo-label" for="photo">Kép hozzáadása</label>',
    '<label class="custom-form__photo-label" for="photo">Dodaj sliku</label>')
rep('<button disabled class="custom-form__btn">KÜLDÉS</button>', '<button disabled class="custom-form__btn">POŠALJI</button>')
rep('Tanúsított minőség</div>', 'Certificirana kvaliteta</div>')
rep('Szállítás 2–3 napon belül</div>', 'Dostava u 2–3 dana</div>')
rep('Vény nélkül</div>', 'Bez recepta</div>')
rep('Biztonságos rendelés</div>', 'Sigurna narudžba</div>')
rep('— különjelentés<br>', ' — specijalni izvještaj<br>')
rep('Az oldalon található adatok tájékoztató jellegűek, és nem helyettesítik az orvosi konzultációt.',
    'Podaci na ovoj stranici su informativne prirode i ne zamjenjuju ljekarski pregled.')

# ---------- применяем ----------
for a, b, n in R:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

for a, b, n in [('alt="Dr. Kovács Gábor"', 'alt="Dr. Nedžad Čaušević"', 1),
                ('Dr. Kovács Gábor\n          <small>', 'Dr. Nedžad Čaušević\n          <small>', 1),
                ('alt="Dr. Kovács Gábor, patológus"', 'alt="Dr. Nedžad Čaušević, patolog"', 1),
                ('<p><b>Dr. Kovács Gábor:</b></p>', '<p><b>Dr. Nedžad Čaušević:</b></p>', 9),
                ('<p><b>Dr. Szabó Ilona:</b></p>', '<p><b>Dr. Hatidža Zukanović:</b></p>', 1)]:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

open(DST, "w", encoding="utf-8").write(t)
print("записано:", DST, len(t), "знаков")
