# -*- coding: utf-8 -*-
"""Адаптация HU-лендинга HELMIRON на румынское гео, блок в блок.
Меняются: язык, имена, топонимы, валюта, страна. Структура, вёрстка,
картинки, порядок блоков, форма — не трогаются.
"""
import re, sys

SRC = sys.argv[1]
DST = sys.argv[2]
t = open(SRC, encoding="utf-8").read()

R = []
def rep(a, b, n=1):
    R.append((a, b, n))

# ---------- голова ----------
rep('<html lang="hu">', '<html lang="ro">')
rep('<title>„Láttam őket azok testében, akiknek fogalmuk sem volt róla” — magyar patológus felfedi a hallgatásba burkolt igazságot a parazitákról</title>',
    '<title>„I-am văzut în corpurile celor care nu aveau nici cea mai mică idee" — un patolog român dezvăluie adevărul trecut sub tăcere despre paraziți</title>')

# ---------- шапка ----------
rep('Különjelentés · Egészség és Társadalom', 'Raport special · Sănătate și Societate')
rep('Magyar Egészségügyi Tájékoztató', 'Informatorul Român de Sănătate', 2)
rep('Riportok a népegészségügy világából', 'Reportaje din lumea sănătății publice')

# ---------- заголовок ----------
rep('„ÉVEKIG ÉLTEK BENNEM, ÉN MEG AZ ÉLETKOROMRA ÉS A FÁRADTSÁGOMRA FOGTAM.”',
    '„AU TRĂIT ANI ÎN MINE, IAR EU DĂDEAM VINA PE VÂRSTĂ ȘI PE OBOSEALĂ."')
rep('35 ÉVES TAPASZTALATTAL RENDELKEZŐ PATOLÓGUS FELFEDI AZ IGAZSÁGOT, AMIT SENKI NEM AKAR HALLANI: A PARAZITÁK CSENDBEN PUSZTÍTJÁK A TESTET BELÜLRŐL — ÉS A HALÁL VALÓDI OKÁT MAJDNEM SOHA NEM KERESIK. EGY NŐ TÖRTÉNETE, AKI IDŐBEN MEGMENTETTE MAGÁT.',
    'UN PATOLOG CU 35 DE ANI DE EXPERIENȚĂ DEZVĂLUIE ADEVĂRUL PE CARE NIMENI NU VREA SĂ-L AUDĂ: PARAZIȚII DISTRUG CORPUL DIN INTERIOR, ÎN LINIȘTE — IAR CAUZA REALĂ A MORȚII APROAPE NICIODATĂ NU ESTE CĂUTATĂ. ISTORIA UNEI FEMEI CARE S-A SALVAT LA TIMP.')
rep('Közzétéve: ', 'Publicat: ')

# ---------- герой-картинка ----------
rep('Erzsébet a háza előtt egy alföldi faluban', 'Ileana în fața casei, într-un sat din Bărăgan')
rep('Patológus megerősítette', 'Confirmat de patolog')

# ---------- подзаголовок ----------
rep('Hogyan kezelte évekig Erzsébet (62 éves), háztartásbeli egy alföldi faluban a „gyomorhurutot”, „allergiát” és a „krónikus fáradtságot” — miközben orvosokra költötte a pénzt, akik sosem keresték a valódi okot. Egészen addig, amíg a falusi állatorvos fel nem tett neki egy kérdést, ami megváltoztatta az életét: „Mikor féregtelenítette utoljára önmagát?” Ami ezután következett, azt egy 35 éves tapasztalattal rendelkező patológus is megerősítette.',
    'Cum a tratat Ileana (62 de ani), casnică într-un sat din Bărăgan, ani de zile „gastrita", „alergia" și „oboseala cronică" — în timp ce dădea banii pe doctori care nu au căutat niciodată cauza reală. Până în ziua în care medicul veterinar din sat i-a pus o întrebare care i-a schimbat viața: „Dumneavoastră când v-ați deparazitat ultima dată?" Ceea ce a urmat a fost confirmat și de un patolog cu 35 de ani de experiență.')

# ---------- первые абзацы ----------
rep('Egy kedd reggel érkeztünk egy alföldi faluba, Szeged közelébe. Az út egy földúton vezet, régi házak, kertek és ugató kutyák mellett. Erzsébet a kapunál fogadott minket, a köténye még mindig a derekán volt — éppen főzött valamit. „Bárcsak tudnák, hány évet vesztettem el” — mondta köszönés helyett. „Mennyi pénzt. Hány orvost. És a válasz olyan egyszerű volt, hogy még most is rosszul leszek, ha arra gondolok.”',
    'Am ajuns într-o dimineață de marți într-un sat din Bărăgan, lângă Slobozia. Drumul intră pe un drum de pământ, pe lângă case vechi, grădini și câini care latră. Ileana ne-a primit la poartă, cu șorțul încă la mijloc — tocmai gătea ceva. „Dacă ați ști câți ani am pierdut" — a spus în loc de bună ziua. „Câți bani. Câți doctori. Iar răspunsul era atât de simplu că și acum mi se face rău când mă gândesc."')
rep('Erzsébet 62 éves. Egész életét ebben a faluban élte le — kert, gazdaság, szombati vásár. Soha nem volt betegeskedő asszony. De az elmúlt hat évben, ahogy mondja, „lassan kihunyt”, és senki nem tudta, miért.',
    'Ileana are 62 de ani. Toată viața a trăit în satul acesta — grădina, gospodăria, piața de sâmbătă. Nu a fost niciodată o femeie bolnăvicioasă. Dar în ultimii șase ani, cum spune ea, „s-a stins încet", și nimeni nu știa de ce.')
rep('Az ok? Évekig nem azt kezelte, amit kellett volna. <b>Az orvosok gyomorhurutot mondtak neki. Aztán allergiát. Aztán „krónikus fáradtságot”. Aztán „neurózist”.</b> Minden szakember a saját tünetét kezelte — de senki nem kereste azt, ami mindezt kiváltotta. Pénzt költött gasztroenterológusra, bőrgyógyászra, vizsgálatokra, amelyek semmit sem mutattak. És közben az életkorát és a fáradtságát hibáztatta.',
    'Cauza? Ani de zile nu a tratat ceea ce trebuia. <b>Doctorii i-au spus gastrită. Apoi alergie. Apoi „oboseală cronică". Apoi „nevroză".</b> Fiecare specialist trata simptomul lui — dar nimeni nu căuta ceea ce declanșa toate acestea. A dat bani pe gastroenterolog, pe dermatolog, pe analize care nu arătau nimic. Iar în tot acest timp dădea vina pe vârstă și pe oboseală.')

# ---------- две цитаты героини ----------
rep('„Azt hittem, ez az öregség. Hogy normális, ha állandóan fáradt vagyok, puffadok, viszket a bőröm, ebéd után úgy elálmosodok, mintha valaki kikapcsolna. Mindenki azt mondta: „Hát az életkor, Erzsébet, mit akarsz.” De ez nem az öregség volt. Valami élő volt bennem.”',
    '„Credeam că asta e bătrânețea. Că e normal să fiu obosită tot timpul, să mă umflu, să mă mănânce pielea, să mă ia somnul după masă ca și cum cineva m-ar opri. Toți îmi spuneau: „Păi e vârsta, Ileana, ce vrei." Dar nu era bătrânețea. Era ceva viu în mine."')
rep('„A legrosszabb az, hogy minden vizsgálatom rendben volt. A vérképem „normális”. Akkor hogyan érezhetem magam így, ha valaki lassan felfal belülről? Csak amikor az állatorvos megmondta, mit keressek — és amikor a patológus a szemembe nézett és elmondta az igazságot —, akkor értettem meg mindent.”',
    '„Cel mai rău e că toate analizele îmi ieșeau bine. Hemoleucograma „normală". Atunci cum pot să mă simt așa, dacă cineva mă mănâncă încet din interior? Abia când veterinarul mi-a spus ce să caut — și când patologul m-a privit în ochi și mi-a spus adevărul — am înțeles totul."')
rep('— Erzsébet, 62 éves, Alföld', '— Ileana, 62 de ani, Bărăgan', 3)

# ---------- интервью патолога ----------
rep('„Láttam őket azok testében, akiknek fogalmuk sem volt róla, hogy hordozzák”',
    '„I-am văzut în corpurile celor care nici nu bănuiau că îi purtau în ei"')
rep('<span>Exkluzív interjú dr. Kovács Gáborral — 35 éves tapasztalattal rendelkező patológussal, aki több mint 9000 boncolást végzett</span>',
    '<span>Interviu exclusiv cu dr. Octavian Brezeanu — patolog cu 35 de ani de experiență, care a efectuat peste 9000 de autopsii</span>')
rep('Dr. Kovács Gábor: „Harmincöt évig dolgoztam patológusként. Minden korosztályú emberek testét nyitottam fel — és amit újra és újra láttam, azt a nyilvánosság nem tudja, mert hallgatnak róla. <b>Paraziták. Nem a peremvidéken élőknél, nem a „piszkosaknál” — hanem hétköznapi embereknél. Háztartásbelieknél, nyugdíjasoknál, munkásoknál. Olyanoknál, akik életükben azt hitték, hogy teljesen egészségesek.</b>',
    'Dr. Octavian Brezeanu: „Am lucrat treizeci și cinci de ani ca patolog. Am deschis corpuri de oameni de toate vârstele — și ceea ce am văzut iar și iar publicul nu îl știe, pentru că despre asta se tace. <b>Paraziți. Nu la cei de la marginea societății, nu la „cei murdari" — ci la oameni obișnuiți. La casnice, la pensionari, la muncitori. La oameni care toată viața au crezut că sunt perfect sănătoși.</b>')
rep('<b>SZÍVROHAMRA, AGYVÉRZÉSRE, ARRA HALTÁK MEG, AMIT „ISMERETLEN EREDETŰ DAGANATNAK” NEVEZTEK —\n          <span class="red-txt">DE A VALÓDI OKOT SENKI NEM KERESTE. MERT SENKINEK NEM JUTOTT ESZÉBE, HOGY ODA NÉZZEN.”</span></b>',
    '<b>AU MURIT DE INFARCT, DE HEMORAGIE CEREBRALĂ, DE CEEA CE S-A NUMIT „TUMORĂ DE ORIGINE NECUNOSCUTĂ" —\n          <span class="red-txt">DAR CAUZA REALĂ NU A CĂUTAT-O NIMENI. PENTRU CĂ NIMĂNUI NU I-A TRECUT PRIN MINTE SĂ SE UITE ACOLO."</span></b>')
rep('Dr. Kovács nyugodtan beszél, drámaiság nélkül — mint aki túl sokszor látta a történetek végét. Néhány éve nyugdíjba vonult, de amit a boncasztalnál tanult, mint mondja, „minden alkalommal kísérti, amikor látja, hogy az emberek a következményeket kezelik, nem az okot”.',
    'Dr. Brezeanu vorbește calm, fără dramatism — ca un om care a văzut prea des sfârșitul poveștilor. S-a pensionat acum câțiva ani, dar ceea ce a învățat la masa de autopsie, cum spune el, „mă urmărește de fiecare dată când văd oameni care tratează consecințele, nu cauza".')
rep('„A legtöbb ember azt hiszi, hogy a paraziták a múlté, a szegénységé, más országoké. Ez a tévedés öl. A paraziták mindenhol körülöttünk vannak — a félig átsült húsban, a saját kertből származó mosatlan zöldségekben, a földben, a vízben, a kezeken, miután megsimogattuk a kutyát vagy a macskát. És ha egyszer bejutnak, évekig élhetnek a testben, szaporodhatnak és lassan mérgezhetik a szervezetet — miközben Ön azt hiszi, hogy ez <b>gyomorhurut, allergia vagy „csak fáradtság”</b>.“',
    '„Cei mai mulți oameni cred că paraziții sunt ceva din trecut, din sărăcie, din alte țări. Greșeala asta omoară. Paraziții sunt în jurul nostru peste tot — în carnea insuficient gătită, în legumele nespălate din propria grădină, în pământ, în apă, pe mâini după ce am mângâiat câinele sau pisica. Iar o dată intrați, pot trăi ani în corp, se pot înmulți și pot otrăvi încet organismul — în timp ce dumneavoastră credeți că este <b>gastrită, alergie sau „doar oboseală"</b>."')
rep('„Feltártam egy 58 éves férfi testét, aki szívrohamban halt meg. Első pillantásra tiszta eset. De amit a beleiben és a májában találtam — annak nem lett volna szabad ott lennie. Ez az ember évekig hordozott magában valamit, ami belülről mérgezte. A jegyzőkönyvben az állt: „szívroham”. A valódi okról — egy szó sem. Ez történik szinte mindig.”',
    '„Am deschis corpul unui bărbat de 58 de ani care a murit de infarct. La prima vedere, un caz clar. Dar ceea ce am găsit în intestinele și în ficatul lui — nu ar fi trebuit să fie acolo. Omul acesta a purtat în el ani de zile ceva ce îl otrăvea din interior. În procesul-verbal scria: „infarct". Despre cauza reală — niciun cuvânt. Așa se întâmplă aproape întotdeauna."')
rep('— dr. Kovács Gábor interjújából', '— din interviul cu dr. Octavian Brezeanu')

# ---------- аптечные таблетки ----------
rep('„A gyógyszertári tabletták nem oldják meg a problémát — egy fajtát ütnek le, és ott hagynak tucatnyit”',
    '„Pastilele de la farmacie nu rezolvă problema — doboară o specie și lasă în urmă o duzină"')
rep('<span>Miért vall kudarcot a szokásos féregellenes kezelés szinte mindig — és miért károsítja a májat</span>',
    '<span>De ce eșuează aproape întotdeauna tratamentul antiparazitar obișnuit — și de ce afectează ficatul</span>')
rep('— Őszintén szólva: az nyugtalanít a legjobban, hogy mennyi ember hiszi azt, hogy elég bevenni egy tablettát a gyógyszertárból és kész. Ez veszélyes tévedés. <b>Több mint ötven parazitafaj élhet az emberi testben</b> — egyesek a bélben, mások a májban, mások az epeutakban, mások az izmokban. Egy gyógyszertári tabletta legfeljebb egy-két fajtát támad meg. A többi ott marad, szaporodik és tovább mérgezi a szervezetet.',
    '— Sincer: ceea ce mă neliniștește cel mai mult este câți oameni cred că e suficient să iei o pastilă de la farmacie și s-a rezolvat. Este o greșeală periculoasă. <b>În corpul uman pot trăi peste cincizeci de specii de paraziți</b> — unii în intestin, alții în ficat, alții în căile biliare, alții în mușchi. O pastilă de la farmacie atacă cel mult una sau două specii. Restul rămân, se înmulțesc și otrăvesc mai departe organismul.')
rep('Ez egy ördögi kör: az ember lenyel egy tablettát, néhány hétig jobban érzi magát, aztán a tünetek visszatérnek — fáradtság, puffadás, bőrproblémák —, és azt gondolja, hogy ez „nem a parazitáktól van, mert hiszen szedtem a gyógyszert”. Pedig valójában csak a probléma egy részét érintette. És ami még rosszabb: <b>az ezekben a tablettákban lévő erős vegyszerek a májat és a vesét támadják</b>, pontosan azokat a szerveket, amelyek már amúgy is túlterheltek a paraziták elleni küzdelemben.',
    'Este un cerc vicios: omul înghite o pastilă, se simte mai bine câteva săptămâni, apoi simptomele revin — oboseală, balonare, probleme de piele — și crede că „nu e de la paraziți, pentru că am luat medicamentul". În realitate însă a atins doar o parte din problemă. Și, ce e mai grav: <b>substanțele chimice puternice din aceste pastile atacă ficatul și rinichii</b>, exact organele care sunt deja suprasolicitate în lupta cu paraziții.')
rep('Erzsébet évekig hordta magával a vizsgálati leleteit. „Minden rendben” — mondták neki. Míg a teste gyengült. Az éjjeliszekrényen dobozok a „gyomorhurut” és „allergia” elleni szerekkel, amelyek semmit sem oldottak meg, mert a valódi okot senki nem kereste.',
    'Ileana a purtat ani de zile rezultatele analizelor cu ea. „Totul este în regulă" — i se spunea. În timp ce corpul i se slăbea. Pe noptieră, cutii cu leacuri pentru „gastrită" și „alergie", care nu au rezolvat nimic, pentru că nimeni nu a căutat cauza reală.')
rep('A krónikus fáradtság, puffadás, bőrproblémák, allergiák és „neurózis” 40 éves kor után nem mindig „az életkortól” vannak — nagyon gyakran annak a jelei, hogy a test parazitákat hordoz, amelyek belülről pusztítják.',
    'Oboseala cronică, balonarea, problemele de piele, alergiile și „nevroza" după 40 de ani nu sunt întotdeauna „de la vârstă" — foarte des sunt semnul că organismul poartă paraziți care îl distrug din interior.')
rep('A „gyomorhurutra” és „allergiára” szedett tabletták csak elfedik a tüneteket, miközben a valódi ok csendben tovább szaporodik. Megfelelő, teljes mértékű testtisztítás nélkül a test évről évre gyengül — és a paraziták elterjednek a májban, az epehólyagban és más szervekben.',
    'Pastilele luate pentru „gastrită" și „alergie" doar acoperă simptomele, în timp ce cauza reală se înmulțește mai departe, în liniște. Fără o curățare completă și corectă a organismului, corpul slăbește an după an — iar paraziții se răspândesc în ficat, în vezica biliară și în alte organe.')
rep('— Kérem, fogják fel a helyzet súlyát. Egész karrierem során láttam, mit tesznek a paraziták a testtel az évek során. Az emberek járják az orvosokat „neurózis”, „allergia”, „gyomorhurut”, „migrén” miatt — és senki nem teszi meg, amit kellene, és nem néz oda, ahová kellene. <b>A GYÓGYSZERTÁRI TABLETTÁK NEM TISZTÍTJÁK MEG TELJESEN A TESTET — EGY FAJTÁT ÜTNEK LE, A TÖBBIT PEDIG OTT HAGYJÁK, HOGY TOVÁBB PUSZTÍTSON BELÜLRŐL!</b>',
    '— Vă rog să înțelegeți gravitatea situației. În toată cariera mea am văzut ce fac paraziții corpului de-a lungul anilor. Oamenii umblă pe la doctori pentru „nevroză", „alergie", „gastrită", „migrenă" — și nimeni nu face ceea ce ar trebui și nu se uită unde ar trebui. <b>PASTILELE DE LA FARMACIE NU CURĂȚĂ COMPLET ORGANISMUL — DOBOARĂ O SPECIE, IAR PE CELELALTE LE LASĂ SĂ DISTRUGĂ MAI DEPARTE DIN INTERIOR!</b>')
rep('És ami a leginkább megérint: ezek az emberek nem tudták. Azt hitték, hogy egészségesek. Az éveket, a munkát, a stresszt hibáztatták. Pedig egész idő alatt valami élőt hordoztak magukban, ami belülről mérgezte őket — és senki nem mondta nekik, hogy ellenőriztessék.',
    'Și ceea ce mă atinge cel mai mult: oamenii aceștia nu știau. Credeau că sunt sănătoși. Dădeau vina pe ani, pe muncă, pe stres. Iar în tot acest timp purtau în ei ceva viu care îi otrăvea din interior — și nimeni nu le-a spus să se verifice.')
rep('„Hét évig kezeltem az „allergiámat”. Krém, tabletta, csepp. A bőröm égett, viszketett, a kiütések a semmiből jöttek. Egyetlen bőrgyógyász sem említette a parazitákat. Csak amikor elkezdtem szedni a kapszulákat — három hét alatt megnyugodott a bőröm, először hét év után.”',
    '„Șapte ani mi-am tratat „alergia". Cremă, pastile, picături. Pielea îmi ardea, mă mânca, erupțiile apăreau din senin. Niciun dermatolog nu a pomenit de paraziți. Abia când am început să iau capsulele — în trei săptămâni pielea mi s-a liniștit, prima dată în șapte ani."')
rep('„Én öt évig kezeltettek gyomorhuruttal. Puffadás, gyomornehezülés, hányinger evés után. Mindent megittam, amit adtak. Semmi. Pedig paraziták voltak — ezt később az orvos mondta meg. Öt év és egy csomó pénz a kukában, mert senki nem kereste a valódi okot.”',
    '„Pe mine m-au tratat cinci ani de gastrită. Balonare, greutate în stomac, greață după ce mâncam. Am băut tot ce mi-au dat. Nimic. Și erau paraziți — mi-a spus mai târziu doctorul. Cinci ani și o grămadă de bani la coș, pentru că nimeni nu a căutat cauza reală."')
rep('— Zoltán, 60 éves, Budapest környéke', '— Gheorghe, 60 de ani, lângă Ploiești')
rep('<b>Balra: egészséges bél ép nyálkahártyával. Jobbra: parazitákkal terhelt bél — krónikus gyulladás, sérült nyálkahártya, a szervezet folyamatos mérgezése. A paraziták az Ön testéből táplálkoznak, és salakanyagokat bocsátanak ki, amelyek mérgezik a vért. A gyógyszertári tabletták, amelyek csak egy fajtát támadnak, ezt nem oldják meg.</b>',
    '<b>Stânga: intestin sănătos, cu mucoasă intactă. Dreapta: intestin încărcat de paraziți — inflamație cronică, mucoasă lezată, otrăvire continuă a organismului. Paraziții se hrănesc din corpul dumneavoastră și eliberează deșeuri care otrăvesc sângele. Pastilele de la farmacie, care atacă o singură specie, nu rezolvă asta.</b>')
rep('Fontos hangsúlyozni: a legtöbb esetben még a gyógyszertári tabletták időszakos szedése mellett is visszatér a probléma, mert a valódi ok — több parazitafaj, amelyek a test különböző részein élnek — megoldatlan marad.',
    'Este important de subliniat: în cele mai multe cazuri, chiar și cu administrarea periodică a pastilelor de la farmacie, problema revine, pentru că cauza reală — mai multe specii de paraziți care trăiesc în diferite părți ale corpului — rămâne nerezolvată.')
rep('A paraziták évekig tartó hordozása után sokan nemcsak az energiájukat vesztik el, hanem a májuk, epehólyagjuk és beleik egészségét is. A krónikus mérgezés, a legyengült immunrendszer, az állandó gyulladások — ez az ára annak, hogy senki nem kereste a valódi okot időben.',
    'După ani de purtare a paraziților, mulți nu își pierd doar energia, ci și sănătatea ficatului, a vezicii biliare și a intestinelor. Otrăvirea cronică, imunitatea slăbită, inflamațiile permanente — acesta este prețul faptului că nimeni nu a căutat cauza reală la timp.')

# ---------- случаи ----------
rep('Esetek, amelyek megváltoztatták a szemléletemet — és megváltoztatják azt is, ahogyan Ön a saját egészségére tekint',
    'Cazuri care mi-au schimbat modul de a privi lucrurile — și care vor schimba și felul în care dumneavoastră vă priviți propria sănătate')
rep('— Engedjék meg, hogy elmondjam, mit láttam évről évre. Nem számokat. Nem statisztikákat. Embereket. Embereket nevekkel, akik az utolsó napig azt hitték, hogy a problémájuk teljesen más.',
    '— Permiteți-mi să vă spun ce am văzut an după an. Nu cifre. Nu statistici. Oameni. Oameni cu nume, care până în ultima zi au crezut că problema lor era cu totul alta.')
rep('Nő, 64 éves. Évekig kezelték „krónikus allergiával” és vérszegénységgel, amely sem vassal, sem vitaminokkal „nem akart javulni”. Senki nem gondolta, hogy valami a testében megeszi helyette a vasat.',
    'Femeie, 64 de ani. Ani de zile tratată pentru „alergie cronică" și anemie care „nu voia să se îndrepte" nici cu fier, nici cu vitamine. Nimeni nu s-a gândit că ceva din corpul ei mânca fierul în locul ei.')
rep('„Állandóan fáradt voltam, sápadt, mint a fal. Az orvosok azt mondták: „vashiány, kérem szedjen tablettákat”. Évekig szedtem. Semmi. Senki nem kérdezte meg, hogy talán valami elveszi tőlem a vasat. Pedig elvitte.”',
    '„Eram obosită tot timpul, palidă ca varul. Doctorii spuneau: „aveți deficit de fier, luați pastile". Am luat ani de zile. Nimic. Nimeni nu m-a întrebat dacă nu îmi ia cineva fierul. Pentru că mi-l lua."')
rep('— dr. Kovács által említett esetekből', '— din cazurile relatate de dr. Brezeanu', 2)
rep('Férfi, 67 éves. „Neurózissal” és álmatlansággal kezelték. Éjszaka fogát csikorgatta, kimerülten ébredt, fogyott, pedig normálisan evett. Mindent a stresszre és az életkorra fogtak.',
    'Bărbat, 67 de ani. Tratat pentru „nevroză" și insomnie. Scrâșnea din dinți noaptea, se trezea epuizat, slăbea deși mânca normal. Totul a fost pus pe stres și pe vârstă.')
rep('„Fogytam, pedig normálisan ettem. A feleségem viccelődött, hogy „gyors az anyagcserém”. Ez nem volt vicces. Valami helyettem evett, belőlem. Ezt túl későn értettem meg ahhoz, hogy segítsek magamon — de Önök, akik ezt olvassák, nem vagytok elkésve.”',
    '„Slăbeam, deși mâncam normal. Soția glumea că „am metabolism rapid". Nu era deloc o glumă. Ceva mânca în locul meu, din mine. Am înțeles asta prea târziu ca să mă pot ajuta — dar dumneavoastră, care citiți acum, nu ați întârziat."')

# ---------- список симптомов ----------
rep('<b>Azok a tünetek, amelyeket leggyakrabban az „életkorra”, „stresszre” vagy „rossz táplálkozásra” fognak — pedig nagyon gyakran a testben élő paraziták jelei:</b>',
    '<b>Simptomele pe care cel mai des le punem pe „vârstă", „stres" sau „alimentație proastă" — deși foarte adesea sunt semnele paraziților care trăiesc în corp:</b>')
rep('<li>Állandó fáradtság és kimerültség — alszol 8 órát, de úgy ébredsz, mintha agyonvertek volna;</li>',
    '<li>Oboseală și epuizare permanente — dormi 8 ore, dar te trezești ca bătut;</li>')
rep('<li>Puffadás, gázképződés, gyomornehezülés evés után — „mintha valami forrna a belekben”;</li>',
    '<li>Balonare, gaze, greutate în stomac după masă — „ca și cum ar fierbe ceva în intestine";</li>')
rep('<li>Váltakozó székrekedés és hasmenés nyilvánvaló ok nélkül;</li>',
    '<li>Constipație și diaree alternante, fără o cauză evidentă;</li>')
rep('<li>Bőrproblémák — kiütés, viszketés, ekcéma, „allergiák”, amelyek a semmiből jönnek és mennek;</li>',
    '<li>Probleme de piele — erupții, mâncărimi, eczeme, „alergii" care vin și pleacă din senin;</li>')
rep('<li>Ellenállhatatlan édesség- és lisztéhség — a paraziták cukorból táplálkoznak;</li>',
    '<li>Poftă irezistibilă de dulce și de făinoase — paraziții se hrănesc din zahăr;</li>')
rep('<li>Fogcsikorgatás éjszaka, nyugtalan alvás, ébredés hajnali 3 körül;</li>',
    '<li>Scrâșnit din dinți în timpul nopții, somn agitat, trezire în jurul orei 3 dimineața;</li>')
rep('<li>Vérszegénység és vashiány, amelyek még tabletták után sem szűnnek meg;</li>',
    '<li>Anemie și deficit de fier care nu trec nici după pastile;</li>')
rep('<li>Sötét karikák a szem alatt, sápadt bőr, törékeny haj és köröm;</li>',
    '<li>Cearcăne întunecate, piele palidă, păr și unghii fragile;</li>')
rep('<li>Viszketés a végbélnyílás körül, különösen éjszaka;</li>',
    '<li>Mâncărimi în jurul anusului, mai ales noaptea;</li>')
rep('<li>Ingerültség, „neurózis”, köd a fejben, gyenge koncentráció;</li>',
    '<li>Irascibilitate, „nevroză", ceață în cap, concentrare slabă;</li>')
rep('<li>Gyakori megfázások és fertőzések — legyengült immunrendszer, mert a test a parazitákra pazarolja az erőt;</li>',
    '<li>Răceli și infecții frecvente — imunitate slăbită, pentru că organismul își risipește forțele pe paraziți;</li>')
rep('Mindegyik tünetet könnyű másra fogni. És pontosan ezért maradnak a paraziták évekig felderítetlenül. A figyelmen kívül hagyás egyetlen eredményhez vezet:',
    'Fiecare dintre aceste simptome este ușor de pus pe altceva. Și exact de aceea paraziții rămân nedescoperiți ani de zile. Ignorarea duce la un singur rezultat:')
rep('<b class="red-txt">A SZERVEZET KRÓNIKUS MÉRGEZÉSE, LEGYENGÜLT IMMUNRENDSZER, MÁJ- ÉS BÉLKÁROSODÁS — ÉS A TEST, AMELY ÉVRŐL ÉVRE EGYRE NEHEZEBBEN DOLGOZIK.</b>',
    '<b class="red-txt">OTRĂVIREA CRONICĂ A ORGANISMULUI, IMUNITATE SLĂBITĂ, FICAT ȘI INTESTINE AFECTATE — ȘI UN CORP CARE LUCREAZĂ DIN CE ÎN CE MAI GREU, AN DUPĂ AN.</b>')
rep('Minden egyes nap a parazitákkal a testben egy újabb nap a szervezet mérgezésének!\n          Több ezer ember kezeli évekig nem azt, amit kellene — „gyomorhurutot”, „allergiát”, „neurózist” — miközben a valódi ok akadálytalanul tovább pusztítja őket belülről.\n          Cselekedjen most — önmagáért — mielőtt a következmények súlyossá válnának!',
    'Fiecare zi cu paraziți în corp este încă o zi de otrăvire a organismului!\n          Mii de oameni tratează ani de zile altceva decât ar trebui — „gastrită", „alergie", „nevroză" — în timp ce cauza reală îi distruge mai departe din interior, nestingherită.\n          Acționați acum — pentru dumneavoastră — înainte ca urmările să devină grave!')

# ---------- передача слова ветеринару ----------
rep('— Én egész életemben a következményeket néztem. De nem én találtam meg a megoldást — a falusi állatorvos, dr. Szabó Ilona tette, aki évtizedekig féregtelenítette az állatállományt. Amikor meghallottam a történetét, megértettem, hogy tud valamit, amit mi, orvosok évekig figyelmen kívül hagyunk. Átadom neki a szót.',
    '— Eu toată viața m-am uitat la consecințe. Dar soluția nu am găsit-o eu — a găsit-o medicul veterinar de la sat, dr. Mioara Zaharia, care a deparazitat animalele timp de decenii. Când i-am auzit povestea, am înțeles că ea știe ceva ce noi, medicii, ignorăm de ani de zile. Îi dau cuvântul.')
rep('„Megértettem, hogy kell lennie egy módnak, hogy a testet gyengéden tisztítsuk meg — ne pedig erős vegyszerekkel mérgezzük”',
    '„Am înțeles că trebuie să existe o cale de a curăța corpul cu blândețe — nu de a-l otrăvi cu substanțe chimice puternice"')
rep('<span>Hogyan fejlesztett ki a falusi állatorvos évek alatt egy gyógynövényes formulát, amely teljesen megtisztítja a szervezetet</span>',
    '<span>Cum a dezvoltat în ani de muncă un medic veterinar de sat o formulă pe bază de plante care curăță complet organismul</span>')
rep('<b>Dr. Szabó Ilona, állatorvos több mint 30 éves tapasztalattal:</b>',
    '<b>Dr. Mioara Zaharia, medic veterinar cu peste 30 de ani de experiență:</b>')
rep('— Pályafutásom során állatokat kezeltem. És amit minden falusi ember tud, de ritkán gondol bele: <b>a kutyát és a macskát évente kétszer kötelező féregteleníteni. Az állatállományt — szarvasmarhát, juhot, sertést — ütemterv szerint, rendszeresen. A lovakat az istállóban szintén.</b> Mert ha ezt nem teszed meg, az állat legyengül, elsorvad, és végül elpusztul. Ez alapvető tudás a falun.',
    '— În toată cariera mea am tratat animale. Și ceea ce orice om de la sat știe, dar la care rar se gândește: <b>câinele și pisica trebuie deparazitați obligatoriu de două ori pe an. Animalele din gospodărie — vacile, oile, porcii — după un program, regulat. Caii din grajd la fel.</b> Pentru că, dacă nu faci asta, animalul slăbește, se ofilește și, în final, moare. Acesta este un lucru elementar la sat.')
rep('És akkor egy nap arra gondoltam: <b>az állatokat rendszeresen féregtelenítjük — magunkat soha. Az ember, aki együtt él ezekkel az állatokkal, ugyanazt a húst eszi, ugyanabban a földben túr, ugyanabból a kútból iszik — életében egyszer sem tisztítja meg magát.</b> Paradoxon: az állat jobban védett, mint a gazdája.',
    'Și atunci, într-o zi, m-am gândit: <b>animalele le deparazităm regulat — pe noi niciodată. Omul, care trăiește împreună cu aceste animale, mănâncă aceeași carne, sapă în același pământ, bea din aceeași fântână — nu se curăță niciodată în viața lui.</b> Un paradox: animalul este mai bine apărat decât stăpânul lui.')
rep('Évekig készítettem az állatoknak gyógynövényes keveréket a paraziták elűzésére. Gyógynövényesnek és gyengédnek kellett lennie — erős vegyszereket nem mertem használni, mert ezen állatok teje és húsa az emberek asztalára kerül. És észrevettem valamit: a gazdaság dolgozói, akik ugyanebből a keverékből ittak teát — „gyomornehezülésre” — abbahagyták a fáradtságra, a bőrre, az emésztésre való panaszokat. Így kezdődött.',
    'Ani de zile am făcut pentru animale un amestec de plante care alungă paraziții. Trebuia să fie din plante și blând — nu îndrăzneam să folosesc substanțe chimice puternice, pentru că laptele și carnea acestor animale ajung pe masa oamenilor. Și am observat ceva: oamenii care lucrau în gospodărie și care beau ceai din același amestec — pentru „greutate în stomac" — s-au oprit cu plângerile legate de oboseală, de piele, de digestie. Așa a început.')

# ---------- состав ----------
rep('<b>Dr. Szabó Ilona gyógynövényes formulája az alábbi összetevőket tartalmazza:</b>',
    '<b>Formula pe bază de plante a dr. Mioara Zaharia conține următoarele ingrediente:</b>')
rep('<b>Üröm (Artemisia absinthium)</b>', '<b>Pelin (Artemisia absinthium)</b>')
rep('<font>Hagyományosan a legismertebb gyógynövényes szer a paraziták elűzésére a belekből</font>',
    '<font>Tradițional, cel mai cunoscut remediu din plante pentru alungarea paraziților din intestine</font>')
rep('<b>Bogáncs (Tanacetum vulgare)</b>', '<b>Vetricea (Tanacetum vulgare)</b>')
rep('<font>Erőteljesen hat a bélparazitákra és azok petéire</font>',
    '<font>Acționează puternic asupra paraziților intestinali și asupra ouălor acestora</font>')
rep('<b>Szegfűszeg (Eugenol)</b>', '<b>Cuișoare (Eugenol)</b>')
rep('<font>Lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el</font>',
    '<font>Descompun ouăle și larvele paraziților — ceea ce remediile împotriva adulților nu ating</font>')
rep('<b>Fekete dió (Juglans nigra)</b>', '<b>Nuc negru (Juglans nigra)</b>')
rep('<font>Kivonat a héjból: tisztítja a beleket és segít eltávolítani a parazitákat</font>',
    '<font>Extract din coajă: curăță intestinele și ajută la eliminarea paraziților</font>')
rep('<b>Tök mag (Cucurbita)</b>', '<b>Semințe de dovleac (Cucurbita)</b>')
rep('<font>Gyengéden hat a parazitákra és nyugtatja a bél nyálkahártyáját</font>',
    '<font>Acționează blând asupra paraziților și calmează mucoasa intestinală</font>')
rep('Ezeket a gyógynövényeket nehéz a megfelelő arányban összekeverni. Ha a keverék nem pontos, a kapszulák csak egy parazitafajtát támadnak — pontosan úgy, mint a gyógyszertári tabletta —, és a többi ott marad. A titok abban rejlik, hogy egyszerre több fajtára hatnak: a kifejlett egyedekre, a petékre és a lárvákra is.',
    'Aceste plante sunt greu de amestecat în proporția corectă. Dacă amestecul nu este exact, capsulele atacă doar o singură specie de paraziți — exact ca pastila de la farmacie — iar restul rămân. Secretul stă în faptul că acționează pe mai multe specii în același timp: și pe adulți, și pe ouă, și pe larve.')

# ---------- рождение продукта ----------
rep('Így született a HELMIRON — gyógynövényes kapszulák, amelyek teljesen és gyengéden tisztítják meg a szervezetet a parazitáktól, erős vegyszerek nélkül',
    'Așa s-a născut HELMIRON — capsule pe bază de plante care curăță complet și blând organismul de paraziți, fără substanțe chimice puternice')
rep('— A keveréket, amelyet az állatoknak készítettem, átdolgoztam emberi használatra — pontos gyógynövények, pontos arányok, kapszula formában, amely kényelmes a szervezet számára. A neve HELMIRON. Egyszerűen szedhető: egy kapszula reggel és este, vízzel lenyelve, a kúra teljes időtartama alatt. Erős vegyszerek nélkül — a gyógynövények végzik a munkájukat a belekben, pontosan ott, ahol a paraziták élnek.',
    '— Amestecul pe care îl făceam pentru animale l-am refăcut pentru folosul oamenilor — plante exacte, proporții exacte, sub formă de capsulă, comodă pentru organism. Se numește HELMIRON. Se ia simplu: o capsulă dimineața și una seara, înghițită cu apă, pe toată durata curei. Fără substanțe chimice puternice — plantele își fac treaba în intestine, exact acolo unde trăiesc paraziții.')
rep('Az erő abban rejlik, hogy a kapszulák fokozatosan és teljesen hatnak: először a kifejlett parazitákra, majd azok petéire és lárváira, ezután segítenek a testnek mindent kiüríteni, és hagyják a beleket és a májat regenerálódni. A gyógyszertári tabletta egyetlen célpontot támad. A kapszulák végighaladnak az egész emésztőrendszeren — ott, ahol a paraziták valóban találhatók.',
    'Forța stă în faptul că capsulele acționează treptat și complet: mai întâi asupra paraziților adulți, apoi asupra ouălor și larvelor lor, după care ajută corpul să elimine totul și lasă intestinele și ficatul să se refacă. Pastila de la farmacie atacă o singură țintă. Capsulele parcurg tot tractul digestiv — acolo unde paraziții se găsesc în realitate.')
rep('A „HELMIRON” különleges. Minden gyógynövény — a megfelelő arányban — a paraziták különböző fázisaiban támad: kifejlett egyedek, peték, lárvák. Ezért tisztít teljesen, nem részlegesen. A legfontosabb: gyengéden hat, anélkül, hogy megtámadná a májat és a vesét, ahogyan azt az erős gyógyszertári tabletták teszik. Először a gazdaság dolgozói szedték, majd később a hétköznapi emberek is mindazokkal a „megoldhatatlan” panaszokkal — fáradtság, bőr, emésztés.',
    '„HELMIRON" este special. Fiecare plantă — în proporția potrivită — atacă paraziții în faze diferite: adulți, ouă, larve. De aceea curăță complet, nu parțial. Cel mai important: acționează blând, fără să atace ficatul și rinichii, așa cum fac pastilele puternice de la farmacie. Întâi l-au luat oamenii care lucrau în gospodărie, iar mai târziu și oamenii obișnuiți, cu toate acele plângeri „fără rezolvare" — oboseală, piele, digestie.')
rep('<p><b>Erzsébet:</b></p>', '<p><b>Ileana:</b></p>')
rep('— Az állatorvos adott nekem egy dobozzal, és azt mondta: „Próbáld ki, Erzsébet, mit veszíthetsz?” Reggel és este szedtem a kapszulákat. A harmadik-negyedik napon éreztem, hogy a gyomrom könnyebb, mint évek óta. Nem hittem el, hogy a kapszuláktól van. Azt hittem — véletlen. Csak később, amikor a patológus elmagyarázta, értettem meg, mi is történt valójában a testemben.',
    '— Veterinarul mi-a dat o cutie și mi-a spus: „Încearcă, Ileana, ce ai de pierdut?" Am luat capsulele dimineața și seara. În a treia-a patra zi am simțit stomacul mai ușor decât în ultimii ani. Nu credeam că e de la capsule. Credeam — întâmplare. Abia mai târziu, când patologul mi-a explicat, am înțeles ce se întâmplase de fapt în corpul meu.')

# ---------- четыре шага ----------
rep('4 lépés, amelyben a HELMIRON megtisztítja a szervezetet a parazitáktól — bármilyen életkorban',
    '4 pași prin care HELMIRON curăță organismul de paraziți — la orice vârstă')
rep('<h1>A „HELMIRON” kapszulák 4 alapvető hatása:</h1>', '<h1>Cele 4 efecte fundamentale ale capsulelor „HELMIRON":</h1>')
rep('<font>A kifejlett paraziták elűzése:</font>', '<font>Alungarea paraziților adulți:</font>')
rep('<span>A kúra első napjaiban az üröm és a bogáncs hat a belekben élő kifejlett parazitákra — gyengíti őket, és segít a szervezetnek természetes úton kiüríteni azokat. Nem egy fajtát, mint a gyógyszertári tabletta, hanem egyszerre többet.</span>',
    '<span>În primele zile ale curei, pelinul și vetricea acționează asupra paraziților adulți care trăiesc în intestine — îi slăbesc și ajută organismul să îi elimine pe cale naturală. Nu o singură specie, ca pastila de la farmacie, ci mai multe în același timp.</span>')
rep('<font>A peték és lárvák elpusztítása:</font>', '<font>Distrugerea ouălor și a larvelor:</font>')
rep('<span>A szegfűszeg (eugenol) lebontja a paraziták petéit és lárváit — amit a kifejlett egyedek elleni szerek nem érnek el. Ez a lépés kulcsfontosságú: enélkül a paraziták visszatérnek a megmaradt petékből. Ezért tisztítanak a kapszulák teljesen, nem részlegesen.</span>',
    '<span>Cuișoarele (eugenol) descompun ouăle și larvele paraziților — ceea ce remediile împotriva adulților nu ating. Acest pas este esențial: fără el, paraziții revin din ouăle rămase. De aceea capsulele curăță complet, nu parțial.</span>')
rep('<font>Méregtelenítés a salakanyagoktól:</font>', '<font>Detoxifierea de deșeuri:</font>')
rep('<span>Amikor a paraziták távoznak, a szervezet megtisztul a salakanyagoktól, amelyeket azok évekig választottak ki a vérbe. A fekete dió és a tök mag segít a májnak és a beleknek kiüríteni a felhalmozódott méreganyagokat — megszűnik a fáradtság, a puffadás és a köd a fejben.</span>',
    '<span>Când paraziții sunt eliminați, organismul se curăță de deșeurile pe care aceștia le-au eliberat ani de zile în sânge. Nucul negru și semințele de dovleac ajută ficatul și intestinele să elimine toxinele acumulate — dispar oboseala, balonarea și ceața din cap.</span>')
rep('<font>A belek és az immunrendszer regenerálódása:</font>', '<font>Refacerea intestinelor și a imunității:</font>')
rep('<span>A tisztítás után a gyógynövényes keverék nyugtatja a bél nyálkahártyáját, és segít a testnek visszanyerni az erejét. Visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés, és az immunrendszer — amely évekig a paraziták elleni küzdelemben merült ki — ismét megerősödik.</span>',
    '<span>După curățare, amestecul de plante calmează mucoasa intestinală și ajută corpul să își recapete forțele. Revine energia, se liniștește pielea, digestia se normalizează, iar imunitatea — epuizată ani de zile în lupta cu paraziții — se întărește din nou.</span>')

# ---------- наблюдение и таблица ----------
rep('„Először a HELMIRON-t hétköznapi emberek szedték „megoldhatatlan” panaszokkal — az eredmények még engem is megleptek”',
    '„Întâi HELMIRON a fost luat de oameni obișnuiți, cu plângeri „fără rezolvare" — rezultatele m-au surprins chiar și pe mine"')
rep('<span>2340, 45 és 86 év közötti személy megfigyelése</span>', '<span>Observație pe 2340 de persoane, între 45 și 86 de ani</span>')
rep('— Amikor évtizedes boncolások után először hallottam erről a gyógynövényes keverékről, szkeptikus voltam — mint minden orvos. De az eredmények, amelyeket a szedők mutattak, olyan egyértelműek voltak, hogy nem hagyhattam figyelmen kívül őket. Szakértői csoport kiterjesztette a megfigyelést több mint 2300, egész Magyarországról származó személyre — mindazokkal a tünetekkel, amelyeket szinte senki nem hozott összefüggésbe a parazitákkal.',
    '— Când, după decenii de autopsii, am auzit prima dată despre acest amestec de plante, am fost sceptic — ca orice medic. Dar rezultatele pe care le arătau cei care îl luau erau atât de limpezi că nu le puteam ignora. Un grup de specialiști a extins observația la peste 2300 de persoane din toată România — cu toate simptomele pe care aproape nimeni nu le lega de paraziți.')
rep('Olyan embereket láttam, akik évekig kezelték a „gyomorhurutot” és az „allergiát” — és néhány hét alatt visszanyerték az energiájukat, megnyugodott a bőrük, normalizálódott az emésztésük. Amit egyetlen tabletta sem oldott meg évekig.',
    'Am văzut oameni care tratau ani de zile „gastrita" și „alergia" — și care în câteva săptămâni și-au recăpătat energia, li s-a liniștit pielea, li s-a normalizat digestia. Ceea ce nicio pastilă nu a rezolvat în ani de zile.')
rep('A „HELMIRON” megfigyelésének eredményei — kontrollcsoport: 2340 fő, 45–86 éves korig',
    'Rezultatele observației „HELMIRON" — grup de control: 2340 de persoane, 45–86 de ani')
rep('<td class="one">A puffadás és gyomornehezülés megszűnése</td>', '<td class="one">Dispariția balonării și a greutății în stomac</td>')
rep('<td class="one">Az energia visszatérése, a krónikus fáradtság megszűnése</td>', '<td class="one">Revenirea energiei, dispariția oboselii cronice</td>')
rep('<td class="one">A bőr megnyugvása (kiütés, viszketés, „allergiák”)</td>', '<td class="one">Liniștirea pielii (erupții, mâncărimi, „alergii")</td>')
rep('<td class="one">Az emésztés és székletürítés normalizálódása</td>', '<td class="one">Normalizarea digestiei și a scaunului</td>')
rep('<td class="one">Az édesség utáni vágy megszűnése</td>', '<td class="one">Dispariția poftei de dulce</td>')
rep('<td class="one">Javuló alvás, a fogcsikorgatás megszűnése</td>', '<td class="one">Somn mai bun, dispariția scrâșnitului din dinți</td>')
rep('<td class="one">A vérkép javulása (vas)</td>', '<td class="one">Îmbunătățirea hemoleucogramei (fier)</td>')
rep('<td class="one">A fejben lévő köd megszűnése, jobb koncentráció</td>', '<td class="one">Dispariția ceții din cap, concentrare mai bună</td>')
rep('<td class="one">A sötét karikák eltűnése a szem alatt</td>', '<td class="one">Dispariția cearcănelor</td>')
rep('<td class="one">Az immunrendszer megerősödése, ritkább fertőzések</td>', '<td class="one">Întărirea imunității, infecții mai rare</td>')

# ---------- случай героини ----------
rep('Az eset, amely a legjobban megmutatja, mennyi ideig maradnak rejtve a paraziták',
    'Cazul care arată cel mai bine cât de mult rămân ascunși paraziții')
rep('Erzsébet, 62 éves. Hat évig kezelték „gyomorhuruttal”, „allergiával” és „krónikus fáradtsággal”. A HELMIRON kapszulák kúrája után — először évek óta kipihenten ébredt, és a bőre megnyugodott.',
    'Ileana, 62 de ani. Șase ani tratată pentru „gastrită", „alergie" și „oboseală cronică". După cura cu capsule HELMIRON — prima dată în ani de zile s-a trezit odihnită, iar pielea i s-a liniștit.')
rep('Erzsébet volt az egyik első, akinek dr. Szabó adta a kapszulákat. 62 évesen, hat év orvosjárás után, normális vizsgálati eredményekkel és egy testtel, amely napról napra egyre gyengébb volt. A lánya Bécsben, a fia Németországban — telefonáltak, küldték a pénzt, de senki nem vette észre, hogy kialszik, mert ők is azt hitték, hogy ez „csak fáradtság és az életkor”.',
    'Ileana a fost una dintre primele cărora dr. Zaharia le-a dat capsulele. La 62 de ani, după șase ani de umblat pe la doctori, cu analize normale și cu un corp care slăbea din zi în zi. Fiica în Spania, fiul în Germania — telefonau, trimiteau bani, dar nimeni nu a observat că se stinge, pentru că și ei credeau că e „doar oboseală și vârstă".')
rep('„Hat éve vonszoltam magam orvostól orvosig. Állandóan fáradt voltam, puffadt, a bőröm égett és viszketett, a hajam hullott. Azt mondták: gyomorhurut, allergia, neurózis, életkor. Mindent beszedtem, amit adtak. Semmi sem segített, és úgy éreztem, mintha valaki lassan felfalna belülről.',
    '„Șase ani m-am târât de la un doctor la altul. Eram obosită tot timpul, umflată, pielea îmi ardea și mă mânca, îmi cădea părul. Îmi spuneau: gastrită, alergie, nevroză, vârstă. Am înghițit tot ce mi-au dat. Nimic nu a ajutat, și simțeam ca și cum cineva m-ar mânca încet din interior.')
rep('A legrosszabb az volt, hogy minden vizsgálat „rendben” volt. Akkor hogyan lehetek ennyire kimerült? Már kezdtem azt hinni, hogy kitalálom, hogy hipochonder lettem. Senki, egyetlen orvos sem említette a parazitákat.',
    'Cel mai rău era că toate analizele ieșeau „în regulă". Atunci cum pot să fiu atât de epuizată? Începusem deja să cred că îmi imaginez, că am devenit ipohondră. Nimeni, niciun doctor nu a pomenit de paraziți.')
rep('Aztán jött hozzám az állatorvos a tehén miatt. És mellékesen rám nézett, és megkérdezte: „Erzsébet, mikor féregtelenítetted utoljára magadat? A kutyát évente kétszer féregteleníted, magadat egyszer sem.” Adott a kapszuláiból. A harmadik napon a gyomrom könnyebb volt, mint évek óta. Egy hét múlva először ébredtem kipihenten. Három hét múlva megnyugodott a bőröm — először hét év után.',
    'Apoi a venit la mine veterinarul pentru vacă. Și, în treacăt, s-a uitat la mine și m-a întrebat: „Ileana, dumneata când te-ai deparazitat ultima dată? Câinele îl deparazitezi de două ori pe an, pe dumneata niciodată." Mi-a dat din capsulele ei. În a treia zi stomacul îmi era mai ușor decât în ultimii ani. După o săptămână m-am trezit prima dată odihnită. După trei săptămâni mi s-a liniștit pielea — prima dată în șapte ani.')
rep('Sírtam. Nem azért, mert jobban lettem. Hanem mert rájöttem, mennyi évet és pénzt vesztettem el azzal, hogy nem azt kezeltem, amit kellett volna — amikor a válasz ilyen egyszerű volt.',
    'Am plâns. Nu pentru că mi-era mai bine. Ci pentru că am înțeles câți ani și câți bani am pierdut tratând altceva decât trebuia — când răspunsul era atât de simplu.')
rep('<b>Erzsébet, 62 éves, alföldi falu</b>', '<b>Ileana, 62 de ani, sat din Bărăgan</b>')

# ---------- случай шофёра ----------
rep('Egy másik eset: Zoltán, 60 éves, egész életében kamionsofőr, évekig kezelték „gyomorhuruttal”, amely semmilyen tablettára nem szűnt meg.',
    'Un alt caz: Gheorghe, 60 de ani, toată viața șofer de TIR, tratat ani de zile pentru „gastrită" care nu a trecut la nicio pastilă.')
rep('„Öt évig kezeltek gyomorhuruttal. Nehézség a gyomorban minden étkezés után, hányinger, puffadás, mint egy dob. Mindenféle vizsgálat, gyógyszerek a gyomorra. Semmi. Fogytam, pedig normálisan ettem.',
    '„Cinci ani m-au tratat de gastrită. Greutate în stomac după fiecare masă, greață, balonare ca o tobă. Tot felul de analize, medicamente pentru stomac. Nimic. Slăbeam, deși mâncam normal.')
rep('A feleségem hallott a HELMIRON kapszulákról a szomszédasszonytól. Azt mondta: próbáld ki, mit veszíthetsz. Reggel és este elkezdtem szedni. Körülbelül tíz nap múlva — először évek óta ettem, és utána semmi nem fájt és nem puffadtam. Egy hónap után úgy éreztem magam, mint egy új ember.',
    'Soția a auzit de capsulele HELMIRON de la vecină. Mi-a spus: încearcă, ce ai de pierdut. Am început să le iau dimineața și seara. Cam după zece zile — prima dată în ani de zile am mâncat și după aceea nu m-a durut nimic și nu m-am balonat. După o lună mă simțeam ca un om nou.')
rep('Ami a legjobban felháborított: öt év és egy csomó pénz a kukába a rossz diagnózis miatt. Paraziták voltak. És senkinek nem jutott eszébe, hogy odanézzen. Ha nincsenek ezek a kapszulák, ki tudja, meddig szenvedtem volna.”',
    'Ce m-a revoltat cel mai mult: cinci ani și o grămadă de bani la coș din cauza unui diagnostic greșit. Erau paraziți. Și nimănui nu i-a trecut prin minte să se uite acolo. Dacă nu erau capsulele astea, cine știe cât aș mai fi suferit."')

# ---------- не симптомы, а причина ----------
rep('„A HELMIRON nem tüneteket fed el — megtisztítja a testet az okától”',
    '„HELMIRON nu acoperă simptome — curăță corpul de cauza lor"')
rep('Ebből nemcsak a súlyos esetek profitálnak. Mindenki 40 éves kor felett, aki az első tüneteket érzi, megelőzhet évek felesleges szenvedését.',
    'Nu profită de asta numai cazurile grave. Oricine peste 40 de ani care simte primele simptome poate preveni ani de suferință inutilă.')
rep('— A kúra általában 3-4 hétig tart, és azoknál, akik évekig hordozzák a problémát, akár tovább is. Amint dr. Szabó elmagyarázta, a tisztítást évente kétszer, profilaktikusan meg kell ismételni — pontosan úgy, mint az állatoknál —, mert a paraziták újra bekerülhetnek az élelmiszerrel, vízzel vagy a háziállatoktól.',
    '— Cura durează de obicei 3-4 săptămâni, iar la cei care poartă problema de ani de zile, chiar mai mult. Cum a explicat dr. Zaharia, curățarea trebuie repetată de două ori pe an, profilactic — exact ca la animale — pentru că paraziții pot intra din nou cu mâncarea, cu apa sau de la animalele din casă.')
rep('A HELMIRON fokozatosan hat: az első napokban megszűnik a puffadás és a gyomornehezülés, majd visszatér az energia, megnyugszik a bőr, normalizálódik az emésztés.',
    'HELMIRON acționează treptat: în primele zile dispar balonarea și greutatea în stomac, apoi revine energia, se liniștește pielea, se normalizează digestia.')
rep('Olyan embereket láttam, akik évekig kezelték a „megoldhatatlan” panaszokat — és néhány hét alatt visszanyerték az erejüket, először hosszú idő után aludtak úgy, mint az emberek. A test maga tudja, hogyan regenerálódjon, ha levesszük róla a terhet, amely pusztította.',
    'Am văzut oameni care tratau ani de zile plângeri „fără rezolvare" — și care în câteva săptămâni și-au recăpătat forțele, au dormit prima dată după mult timp ca niște oameni. Corpul știe singur cum să se refacă, dacă îi luăm de pe el povara care îl distrugea.')
rep('Dr. Szabó Ilona gyógynövényes formulájának köszönhetően Magyarországon több ezer ember tisztította meg a szervezetét a parazitáktól.\n          Íme néhány eset:',
    'Datorită formulei pe bază de plante a dr. Mioara Zaharia, mii de oameni din România și-au curățat organismul de paraziți.\n          Iată câteva cazuri:')

# ---------- четыре подписи ----------
rep('<figcaption>Férfi, 65 éves. Évekig „gyomorhurut” és krónikus fáradtság. HELMIRON kúra: megszűnt a puffadás, visszatért az energia, normalizálódott az emésztés.</figcaption>',
    '<figcaption>Bărbat, 65 de ani. Ani de zile „gastrită" și oboseală cronică. Cura HELMIRON: a dispărut balonarea, a revenit energia, s-a normalizat digestia.</figcaption>')
rep('<figcaption>Nő, 58 éves. „Allergia” és bőrkiütés évek óta. Kúra után: tiszta bőr, viszketés megszűnt, megszűntek az „allergiás” reakciók.</figcaption>',
    '<figcaption>Femeie, 58 de ani. „Alergie" și erupții pe piele de ani de zile. După cură: piele curată, mâncărimile au dispărut, au dispărut reacțiile „alergice".</figcaption>')
rep('<figcaption>Nő, 72 éves. Vérszegénység, amely még vas pótlására sem szűnt meg. Kúra után: a vérkép javult, a fáradtság és sápadtság megszűnt.</figcaption>',
    '<figcaption>Femeie, 72 de ani. Anemie care nu a trecut nici la suplimentarea cu fier. După cură: hemoleucograma s-a îmbunătățit, oboseala și paloarea au dispărut.</figcaption>')
rep('<figcaption>Férfi, 70 éves. Állandó puffadás, álmatlanság, fogcsikorgatás. Kúra után: nyugodt alvás, normális székletürítés, visszanyert súly.</figcaption>',
    '<figcaption>Bărbat, 70 de ani. Balonare permanentă, insomnie, scrâșnit din dinți. După cură: somn liniștit, scaun normal, greutate recâștigată.</figcaption>')
rep('— Pályafutásom során végig néztem a paraziták testre gyakorolt hosszú távú hatásait. Ezért érintenek meg ezek az esetek: amint ezt a terhet levesszük a testről, az magától regenerálódik. Erős vegyszerek nélkül. Olyan tabletták nélkül, amelyek a májat támadják. <b>Az emberi test erős — csak időben le kell venni róla azt, ami belülről pusztítja.</b>',
    '— În toată cariera mea am privit efectele de lungă durată ale paraziților asupra corpului. De aceea mă ating cazurile acestea: în clipa în care luăm povara asta de pe corp, el se reface singur. Fără substanțe chimice puternice. Fără pastile care atacă ficatul. <b>Corpul omenesc este puternic — trebuie doar să luăm de pe el, la timp, ceea ce îl distruge din interior.</b>')

# ---------- оффер ----------
rep('Miért nem kapható a HELMIRON a gyógyszertárakban? És hogyan lehet beszerezni?',
    'De ce nu se găsește HELMIRON în farmacii? Și cum poate fi procurat?')
rep('<p>A HELMIRON gyártása lassú és gondos folyamat. Amint dr. Szabó elmagyarázta, a gyógynövényeket a megfelelő időben kell begyűjteni, és pontos arányban összekeverni — üröm, bogáncs, szegfűszeg, fekete dió, tök mag. Minden kis mennyiségben, kézzel készül, és nem lehet kielégíteni a teljes keresletet.</p>',
    '<p>Producția HELMIRON este un proces lent și atent. Cum a explicat dr. Zaharia, plantele trebuie culese la momentul potrivit și amestecate în proporții exacte — pelin, vetricea, cuișoare, nuc negru, semințe de dovleac. Totul se face în cantități mici, manual, și nu se poate acoperi toată cererea.</p>')
rep('<p>Legalább 2-3 évre van szükség ahhoz, hogy a HELMIRON a gyógyszertárakba kerüljön. Addig a termék kizárólag online, a támogatási program keretében érhető el. Mindazonáltal,\n      <font class="red-txt">a kedvezmény akár 50% is lehet</font>\n      — ami óriási jelentőséggel bír a nyugdíjasok számára.\n    </p>',
    '<p>Sunt necesari cel puțin 2-3 ani pentru ca HELMIRON să ajungă în farmacii. Până atunci, produsul este disponibil exclusiv online, în cadrul programului de sprijin. Cu toate acestea,\n      <font class="red-txt">reducerea poate ajunge până la 50%</font>\n      — ceea ce are o importanță uriașă pentru pensionari.\n    </p>')
rep('Kérem Önöket: NE SZALASSZÁK EL A TÁMOGATÁSI PROGRAMOT. Ne csak magukért — hanem a szeretteikért is, akik talán évekig nem azt kezelik, amit kellene, anélkül, hogy sejtenék a valódi okot. Tisztítsák meg magukat — és segítsenek azokon, akik számítanak Önöknek.',
    'Vă rog: NU RATAȚI PROGRAMUL DE SPRIJIN. Nu numai pentru dumneavoastră — ci și pentru cei dragi, care poate tratează ani de zile altceva decât ar trebui, fără să bănuiască cauza reală. Curățați-vă — și ajutați-i pe cei care contează pentru dumneavoastră.')
rep('<b>A rendelés leadásához használják az alábbi űrlapot.</b>', '<b>Pentru a plasa comanda, folosiți formularul de mai jos.</b>')
rep('Az utolsó lehetőség idén, hogy HELMIRON-t szerezzenek — maguknak vagy szeretteiknek, akik évek óta szenvednek a helyes válasz nélkül',
    'Ultima ocazie în acest an de a procura HELMIRON — pentru dumneavoastră sau pentru cei dragi, care suferă de ani de zile fără răspunsul corect')
rep('— Kizárólag ennek a portálnak az olvasói számára 20 000 dobozt különítettek el. Minden 40 év feletti magyar állampolgár <font class="red-txt">akár 50% kedvezményt</font> kaphat, de a program <span>',
    '— Exclusiv pentru cititorii acestui portal au fost puse deoparte 20 000 de cutii. Orice cetățean român de peste 40 de ani poate primi <font class="red-txt">o reducere de până la 50%</font>, dar programul durează până la <span>')
rep('      </span>-ig tart.\n    </p>', '      </span>.\n    </p>')
rep('<p>Ne várják meg, amíg a fáradtság, a bőrproblémák és az emésztési panaszok a mindennapok részévé válnak. Amíg pénzt költenek rossz diagnózisokra. Emlékezzenek: az állatokat évente kétszer féregtelenítjük, magunkat egyszer sem. A HELMIRON-t elegendő egy kúra formájában átvenni, majd évente kétszer megismételni — profilaktikusan, pontosan úgy, mint az állatoknál.</p>',
    '<p>Nu așteptați până când oboseala, problemele de piele și tulburările digestive devin parte din fiecare zi. Până când dați bani pe diagnostice greșite. Țineți minte: animalele le deparazităm de două ori pe an, pe noi niciodată. HELMIRON este suficient să fie luat sub formă de cură, apoi repetat de două ori pe an — profilactic, exact ca la animale.</p>')
rep('<p>Írják be a nevüket és telefonszámukat. Szakértőnk felveszi Önökkel a kapcsolatot, kiválasztja a megfelelő programot, és megszervezi a kiszállítást futárral vagy postán 2-3 napon belül, közvetlenül a címükre.</p>',
    '<p>Scrieți numele și numărul de telefon. Specialistul nostru vă va contacta, va alege programul potrivit și va organiza livrarea prin curier sau prin poștă în 2-3 zile, direct la adresa dumneavoastră.</p>')
rep('<b>Reménnyel és tisztelettel — dr. Kovács Gábor, patológus. 35 év után a boncasztalnál az egyetlen, amit ajánlok: tisztítsák meg magukat időben. A testük nem fogja elfelejteni.</b>',
    '<b>Cu speranță și respect — dr. Octavian Brezeanu, patolog. După 35 de ani la masa de autopsie, singurul lucru pe care îl recomand este: curățați-vă la timp. Corpul dumneavoastră nu va uita.</b>')
rep('<span class="ramka-title">Frissítés: <span>', '<span class="ramka-title">Actualizare: <span>')
rep('A hatalmas érdeklődés miatt a készletek korábban elfogyhatnak, mint várható! Ma —',
    'Din cauza interesului uriaș, stocurile se pot epuiza mai repede decât era de așteptat! Astăzi —')
rep('        </span> — a program utolsó napja</font> vagy a készletek kimerüléséig.',
    '        </span> — este ultima zi a programului</font> sau până la epuizarea stocurilor.')
rep('Figyelem! Ne zárják be és ne frissítsék az oldalt, ellenkező esetben az Ön számára lefoglalt HELMIRON doboz egy másik személyhez kerül!',
    'Atenție! Nu închideți și nu reîmprospătați pagina, altfel cutia de HELMIRON rezervată pentru dumneavoastră va ajunge la o altă persoană!')
rep('Használják ki az ajánlatot — az Ön helye le van foglalva:', 'Profitați de ofertă — locul dumneavoastră este rezervat:')

# ---------- форма ----------
rep('<b>Hivatalos rendelési űrlap</b>', '<b>Formular oficial de comandă</b>')
rep('A <b>50% kedvezmény</b> igénybevételéhez írják be a nevüket és telefonszámukat az alábbi mezőkbe, majd nyomják meg a „MEGRENDELEM" gombot.',
    'Pentru a beneficia de <b>reducerea de 50%</b>, scrieți numele și numărul de telefon în câmpurile de mai jos, apoi apăsați butonul „COMAND ACUM".')
rep('Elérhetőség:', 'Disponibilitate:')
rep('<span class="price_old">19800 HUF</span>', '<span class="price_old">198 lei</span>')
rep('<span class="price_main">9900 HUF</span>', '<span class="price_main">99 lei</span>')
rep('<input type="hidden" name="country" value="HU">', '<input type="hidden" name="country" value="RO">')
rep('<label for="name-input">Név</label>', '<label for="name-input">Nume</label>')
rep('placeholder="Az Ön neve"', 'placeholder="Numele dumneavoastră"', 2)
rep('<label for="phone-input">Telefonszám</label>', '<label for="phone-input">Număr de telefon</label>')
rep('placeholder="Az Ön telefonszáma"', 'placeholder="Numărul dumneavoastră de telefon"')
rep('<button class="button-submit" type="submit">MEGRENDELEM</button>', '<button class="button-submit" type="submit">COMAND ACUM</button>')
rep('✔️ A szállítást a Nemzeti Közegészségügyi Központ végzi<br> közvetlenül a megadott címre',
    '✔️ Livrarea este efectuată de Institutul Național de Sănătate Publică<br> direct la adresa indicată')

# ---------- комментарии: имена ----------
for hu, ro in [('Kovács Mária','Tudorița Dobrescu'), ('Nagy Erzsébet','Catinca Ivașcu'),
               ('Varga Anna','Lucreția Răducanu'), ('Kiss János','Ioan Chirilă'),
               ('Szabó Péter','Grigore Lixandru'), ('Tóth Alexandra','Alexandra Stănilă'),
               ('Horváth Judit','Steluța Burlacu'), ('Nagy Kázmér','Costache Hurdubei'),
               ('Molnár Katalin','Profira Tănăsescu'), ('Farkas Erzsébet','Safta Gîrbea'),
               ('Papp József','Iosif Rotărescu'), ('Balogh Tádé','Anghel Mocanu'),
               ('Gábor Ibolya','Zamfira Grigoraș'), ('Kiss Zsuzsanna','Smaranda Nistor'),
               ('Nagy Gergely','Toader Vasilescu')]:
    rep('<p class="comments__item-name">%s</p>' % hu, '<p class="comments__item-name">%s</p>' % ro)

# ---------- комментарии: тексты ----------
rep('Sírtam, amikor ezt a cikket olvastam. Anyukám 76 éves, és évek óta „gyomorhuruttal” és „allergiával” kezelteti magát — és senki sem említette soha a parazitákat. Minden stimmel, abszolút minden. Rendeltem neki HELMIRON-t. Hogy nem jutott ez hamarabb eszembe?',
    'Am plâns când am citit articolul acesta. Mama are 76 de ani și de ani de zile se tratează de „gastrită" și „alergie" — și nimeni nu a pomenit vreodată de paraziți. Totul se potrivește, absolut totul. I-am comandat HELMIRON. Cum nu mi-a trecut mai devreme prin minte?')
rep('A múlt héten megjött a HELMIRON. Reggel és este szedem a kapszulákat. 5 nap után — a puffadás, ami évekig gyötört, majdnem teljesen eltűnt, a gyomrom könnyebb, mint valaha. Ennek a patológusnak a története késztetett a rendelésre. Bárcsak tudnák, milyen jól érzem magam.',
    'Săptămâna trecută mi-a venit HELMIRON. Iau capsulele dimineața și seara. După 5 zile — balonarea care m-a chinuit ani de zile a dispărut aproape complet, stomacul îmi e mai ușor ca niciodată. Povestea patologului acesta m-a făcut să comand. Dacă ați ști ce bine mă simt.')
rep('69 éves vagyok. Hét évig kezeltek „allergiával” — krémek, tabletták, cseppek. A bőröm égett és viszketett. 3 hét HELMIRON kapszula után — a bőröm először nyugodott meg ennyi év után. Magam járok piacra, főzök, normálisan élek. Visszatértem önmagamhoz.',
    'Am 69 de ani. Șapte ani m-au tratat de „alergie" — creme, pastile, picături. Pielea îmi ardea și mă mânca. După 3 săptămâni de capsule HELMIRON — pielea mi s-a liniștit prima dată după atâția ani. Merg singură la piață, gătesc, trăiesc normal. M-am întors la mine însămi.')
rep('Napi 10 órát dolgozom. Állandó fáradtság, köd a fejben, édesség utáni vágy, amit nem tudtam kontrollálni. Azt hittem — életkor, stressz. Kipróbáltam a HELMIRON-t. 4 hét után — visszatért az energia, tiszta a fejem. Hatalmas tisztelet ennek az állatorvosnak, azt az igazságot mondja, amit senki más nem mond.',
    'Lucrez 10 ore pe zi. Oboseală permanentă, ceață în cap, poftă de dulce pe care nu o puteam controla. Credeam — vârsta, stresul. Am încercat HELMIRON. După 4 săptămâni — a revenit energia, am capul limpede. Respect uriaș pentru veterinarul acesta, spune adevărul pe care nu îl spune nimeni altcineva.')
rep('Rendeltem 3 dobozt — magamnak, a feleségemnek (állandó bőrproblémák) és az apósomnak. Az állatokat évente kétszer féregtelenítjük, magunkat soha — amikor ezt elolvastam, minden világossá vált. Köszönöm a cikket, felnyitotta a szemem.',
    'Am comandat 3 cutii — pentru mine, pentru soția mea (probleme permanente de piele) și pentru socrul meu. Animalele le deparazităm de două ori pe an, pe noi niciodată — când am citit asta, totul s-a limpezit. Mulțumesc pentru articol, mi-a deschis ochii.')
rep('Gondolkodom a rendelésen az apukámnak. 78 éves, évek óta panaszkodik az emésztésre és fáradtságra, az orvosok nem találnak semmit. Szerintetek a HELMIRON segíthet ebben a korban is?',
    'Mă gândesc să comand pentru tata. Are 78 de ani, se plânge de ani de zile de digestie și de oboseală, doctorii nu găsesc nimic. Credeți că HELMIRON poate ajuta și la vârsta asta?')
rep('Alexandra, az én anyukám 82 éves! Évek óta vérszegénység, ami még vas pótlására sem szűnt meg. Egy hónapig szedte a HELMIRON-t — javult a vérképe, elmúlt a fáradtság. Nem túlzok. Rendelj nyugodtan, az apukád megérdemli az esélyt.',
    'Alexandra, mama mea are 82 de ani! Anemie de ani de zile, care nu a trecut nici la suplimentarea cu fier. A luat HELMIRON o lună — i s-a îmbunătățit hemoleucograma, i-a trecut oboseala. Nu exagerez. Comandă liniștită, tatăl dumitale merită șansa asta.')
rep('Alexandra, rendelj nyugodtan. 78 évesen állandó gyomorproblémáim voltak — senki nem tudta, mi az. A HELMIRON egy hónap alatt talpra állított. Az apukádnak jobban szüksége van erre, mint gondolnád.',
    'Alexandra, comandă fără frică. La 78 de ani aveam probleme permanente cu stomacul — nimeni nu știa ce e. HELMIRON m-a pus pe picioare într-o lună. Tatăl dumitale are mai mare nevoie de asta decât crezi.')
rep('Egy hete szedem a kapszulákat. Reggelre már nem puffadok, mint egy dob, megszűnt az evés utáni nehézség. És jobban alszom — már nem ébredek hajnali 3-kor. Rendeltem a szomszédasszonynak is, ő is évek óta szenved, mint én.',
    'Iau capsulele de o săptămână. Dimineața nu mai sunt balonată ca o tobă, a trecut greutatea de după masă. Și dorm mai bine — nu mă mai trezesc la 3 dimineața. Am comandat și pentru vecina mea, suferă și ea de ani de zile ca mine.')
rep('68 évesen azt hittem, normális, hogy állandóan fáradt vagyok. A HELMIRON kúra után — idén felástam az egész kertet, először hosszú idő után. Ez a történet mélyen megrázott. Még vannak becsületes emberek, akik igazat mondanak.',
    'La 68 de ani credeam că e normal să fiu obosită tot timpul. După cura cu HELMIRON — anul acesta am săpat toată grădina, prima dată după mult timp. Povestea asta m-a zguduit adânc. Mai există oameni cinstiți care spun adevărul.')
rep('82 éves vagyok. Tavaly alig funkcionáltam — fáradtság, rossz emésztés, gyenge immunrendszer, állandóan beteg. Kipróbáltam a HELMIRON-t nagy remények nélkül. És működik! Van energiám, normálisan eszem, nem betegszem meg minden huzatnál. A legnagyobb öröm ezekben az években.',
    'Am 82 de ani. Anul trecut aproape nu mai funcționam — oboseală, digestie proastă, imunitate slabă, bolnav tot timpul. Am încercat HELMIRON fără mari speranțe. Și funcționează! Am energie, mănânc normal, nu mă îmbolnăvesc la fiecare curent. Cea mai mare bucurie din anii aceștia.')
rep('A feleségem évekig szenvedett — bőr, fáradtság, „neurózis”. Attól féltem, hogy valami komolyabb dologról van szó. Rendeltem HELMIRON-t a kedvezménnyel. 4 hét után — tegnap magától ment a piacra, és virágokkal tért vissza! Olyan mosolygós volt, mint régen. Szívből köszönöm.',
    'Soția mea a suferit ani de zile — pielea, oboseala, „nevroza". Mă temeam că e vorba de ceva mai serios. Am comandat HELMIRON cu reducere. După 4 săptămâni — ieri s-a dus singură la piață și s-a întors cu flori! Era zâmbitoare ca pe vremuri. Vă mulțumesc din suflet.')
rep('Rendeltem 4 dobozt — anyukámnak, apukámnak és 2-t magamnak. A cikkben szereplő történetek lesújtottak. Ennyi évig mindannyian nem azt kezeltük, amit kellett volna. Már régen meg kellett volna tennem. Véget a kifogásoknak.',
    'Am comandat 4 cutii — pentru mama, pentru tata și 2 pentru mine. Poveștile din articol m-au doborât. Atâția ani am tratat toți altceva decât ar fi trebuit. Trebuia să o fac de mult. S-a terminat cu scuzele.')
rep('Megkaptam a HELMIRON-t — a futár 2 nap alatt kiszállította! Rögtön elkezdtem szedni a kapszulákat. Szívből drukkolok. Elküldöm ezt a cikket a nővéremnek is — ő is évek óta szenved az emésztéssel, és senki sem segít neki.',
    'Am primit HELMIRON — curierul l-a livrat în 2 zile! Am început imediat să iau capsulele. Țin din tot sufletul. Trimit articolul acesta și surorii mele — și ea suferă de ani de zile cu digestia, și nimeni nu o ajută.')
rep('Kerestem a HELMIRON-t a gyógyszertárban — nincs. Azt mondták, csak erről az oldalról lehet rendelni. Remélem, még elérhető. Az apukámnak sürgősen szüksége van rá — évek óta szenved, az orvosok csak széttárják a kezüket.',
    'Am căutat HELMIRON la farmacie — nu este. Mi-au spus că se poate comanda numai de pe pagina asta. Sper că mai este disponibil. Tatăl meu are nevoie urgentă — suferă de ani de zile, doctorii doar ridică din umeri.')

# ---------- форма комментария, trust, футер ----------
rep('<p class="comments__header-title">HOZZÁSZÓLÁSOK</p>', '<p class="comments__header-title">COMENTARII</p>')
rep('Profilkép</label>', 'Poză de profil</label>')
rep('placeholder="Az Ön hozzászólása"', 'placeholder="Comentariul dumneavoastră"')
rep('<label class="custom-form__photo-label" for="photo">Kép hozzáadása</label>',
    '<label class="custom-form__photo-label" for="photo">Adaugă o imagine</label>')
rep('<button disabled class="custom-form__btn">KÜLDÉS</button>', '<button disabled class="custom-form__btn">TRIMITE</button>')
rep('Tanúsított minőség</div>', 'Calitate certificată</div>')
rep('Szállítás 2–3 napon belül</div>', 'Livrare în 2–3 zile</div>')
rep('Vény nélkül</div>', 'Fără rețetă</div>')
rep('Biztonságos rendelés</div>', 'Comandă securizată</div>')
rep('— különjelentés<br>', ' — raport special<br>')
rep('Az oldalon található adatok tájékoztató jellegűek, és nem helyettesítik az orvosi konzultációt.',
    'Datele prezentate pe această pagină au caracter informativ și nu înlocuiesc consultul medical.')

# ---------- применяем ----------
for a, b, n in R:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

# alt-атрибуты врача (после основных замен)
for a, b, n in [('alt="Dr. Kovács Gábor"', 'alt="Dr. Octavian Brezeanu"', 1),
                ('Dr. Kovács Gábor\n          <small>', 'Dr. Octavian Brezeanu\n          <small>', 1),
                ('alt="Dr. Kovács Gábor, patológus"', 'alt="Dr. Octavian Brezeanu, patolog"', 1),
                ('<p><b>Dr. Kovács Gábor:</b></p>', '<p><b>Dr. Octavian Brezeanu:</b></p>', 9),
                ('<p><b>Dr. Szabó Ilona:</b></p>', '<p><b>Dr. Mioara Zaharia:</b></p>', 1)]:
    c = t.count(a)
    assert c == n, "ОЖИДАЛОСЬ %d, НАЙДЕНО %d: %r" % (n, c, a[:90])
    t = t.replace(a, b)

open(DST, "w", encoding="utf-8").write(t)
print("записано:", DST, len(t), "знаков")
