with open('/root/.claude/uploads/f65f0cab-92ee-59ef-9c6b-94a4c2e4666c/ffb2d01a-HUsustnew.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Normalize Hungarian right double quotation mark (U+201D) to straight quote
# so old_strings written with " (U+0022) can match source text content
c = c.replace('”', '"')

r = [
    ('html lang="hu"', 'html lang="sw"'),

    # title
    ('„Azokhoz járok, akiket a saját családjuk is kezd elengedni" — a fiatal magyar orvos, aki visszaadja az\n    időseknek a járást és a helyüket a családban</title>',
     '„Ninawatembelea wale ambao familia zao zinaanza kuwaacha" — daktari mchanga wa Tanzania anayewarudishia\n    wazee kutembea na nafasi yao katika familia</title>'),

    # meta description
    ('Hogyan mondott le egy 31 éves orvos a budapesti karrierjéről, hogy a vidéki idős embereknek segítsen visszanyerni az önállóságukat — műtét és életfogytig tartó tabletták nélkül.',
     'Jinsi daktari mwenye umri wa miaka 31 alivyoacha kazi yake ya Dar es Salaam ili kusaidia wazee wa vijijini kupata uhuru wao tena — bila upasuaji wala dawa za maisha yote.'),

    # topbar
    ('EgészségHír Magyarország', 'AfyaHabari Tanzania'),
    ('Különleges riport · Egészség és Társadalom', 'Ripoti Maalum · Afya na Jamii'),

    # kicker
    ('Riport · Vidéki egészségügy', 'Ripoti · Afya vijijini'),

    # H1
    ('„Amikor már nem tudsz felállni, lassan a saját családodnak is teher leszel."',
     '„Ukishindwa kusimama, utakuwa mzigo kwa familia yako mwenyewe."'),

    # lead
    ('A fiatal magyar orvos, aki Borsod és Szabolcs elfeledett idős embereihez jár — és visszaadja nekik\n      azt, amit más senki: a járást, az önállóságot és a helyüket a családban.',
     'Daktari mchanga wa Tanzania anayewatembelea wazee waliosaahauliwa wa Morogoro na Dodoma — na kuwarudishia\n      kile ambacho hakuna mwingine awezaye: kutembea, uhuru, na nafasi yao katika familia.'),

    # byline
    ('Megjelent: <span id="pubdate"></span>, 09:36 · Szerző: szerkesztőségünk\n      munkatársa',
     'Imechapishwa: <span id="pubdate"></span>, 09:36 · Mwandishi: mhariri wetu'),

    # alt texts
    ('alt="Fiatal orvos segít felállni egy idős asszonynak otthonában"',
     'alt="Daktari mchanga akimsaidia mzee mwanamke kusimama nyumbani kwake"'),
    ('alt="Dr. Kovács Gergő, ortopéd-traumatológus"',
     'alt="Dk. Baraka Mwamba, daktari wa mifupa na majeraha"'),
    ('alt="Egészséges és tönkrement ízület összehasonlítása"',
     'alt="Ulinganisho wa kiungo chenye afya na kilichoharibiwa"'),
    ('alt="Idős asszony tönkrement ízületekkel"',
     'alt="Mzee mwanamke mwenye viungo vilivyoharibiwa"'),
    ('alt="Idős férfi bottal a konyhában"',
     'alt="Mzee mwanaume na fimbo jikoni"'),
    ('alt="Idős asszony előtte-utána"',
     'alt="Mzee mwanamke kabla na baada"'),
    ('alt="HondroDin ízületi krém"',
     'alt="HondroDin krimu ya viungo"'),
    ('alt="Olvasói fénykép"',
     'alt="Picha ya msomaji"'),

    # first figcaption
    ('Dr. Kovács Gergő egy idős betegét segíti otthonában, egy borsodi faluban. „Ezeknek az embereknek van\n        rám a legnagyobb szükségük — épp azért, mert máshoz nem jön senki."',
     'Dk. Baraka Mwamba anamhudumia mgonjwa wake mzee nyumbani kwake, katika kijiji cha Morogoro. „Watu hawa ndio wanaohitaji msaada wangu zaidi — hasa kwa sababu hakuna mwingine anayekuja."'),

    # paragraph 1
    ('Egy keddi reggelen érkeztünk meg egy apró faluba Borsod-Abaúj-Zemplén megyében. A földút régi kerítések és ugató\n      kutyák mellett vezet. „A fiatal orvost keresik?" — kérdezte tőlünk egy asszony a vegyesbolt előtt. „Minden\n      csütörtökön jön. Az öregek a kapuban várják. Van, aki sír, amikor meglátja."',
     'Tulifika asubuhi ya Jumanne katika kijiji kidogo cha mkoa wa Morogoro. Njia ya udongo inapita karibu na uzio wa zamani na mbwa wanaobweka. „Mnamtafuta daktari mchanga?" — aliuliza mama mmoja mbele ya duka. „Anakuja kila Alhamisi. Wazee wanambakia mlangoni. Wengine wanalia wamwona."'),

    # paragraph 2
    ('Így hallottunk először dr. Kovács Gergőről — a 31 éves orvosról, aki otthagyta a jól fizető állását egy budapesti\n      magánklinikán, hogy azt csinálja, amit más orvos nem akart: bejárja Kelet-Magyarország falvait, és olyan idős\n      embereket kezeljen, akiket lassan a saját családjuk is kezd elengedni.',
     'Hivyo ndivyo tulivyosikia kwanza kuhusu dk. Baraka Mwamba — daktari mwenye miaka 31, aliyeacha kazi yake yenye mshahara mzuri katika kliniki ya kibinafsi ya Dar es Salaam, ili afanye kile ambalo daktari mwingine hakutaka: kuzunguka vijiji vya Tanzania Mashariki, na kutibu wazee ambao familia zao zinaanza polepole kuwaacha.'),

    # paragraph 3
    ('Az ok majdnem mindig ugyanaz: az ember egyszer csak nem tud többé felállni. A térde felmondja a szolgálatot. A\n      háta meggörnyed. A keze úgy remeg, hogy a kanalat sem bírja megfogni. És pontosan abban a pillanatban — amikor a\n      legnagyobb szüksége lenne a segítségre — válik azzá, amitől egész életében a legjobban rettegett: teherré.',
     'Sababu ni ile ile karibu kila wakati: mtu anashindwa tena kusimama. Magoti yake yanashindwa kufanya kazi. Mgongo wake unainamia. Mikono yake inatetemeka kiasi kwamba hawezi kushika kijiko. Na katika wakati huo huo — wakati anahitaji msaada zaidi — anakuwa kile alichokiogopa maisha yake yote: mzigo.'),

    # blockquote 1
    ('„A fiam azt mondta: «Anya, már nem bírlak minden alkalommal felemelni a székről. Nem megy tovább.» Nem\n      haragszom rá. Dolgozik, családja van. De azóta alig jön. És én csak ülök, és várom, hogy valaki rám gondoljon."\n      <span class="src">— Margit néni, 79 éves, Edelény</span>',
     '„Mwanangu alisema: «Mama, siwezi kukuinua kutoka kwenye kiti kila wakati. Haiwezekani tena.» Sikasirikii. Ana kazi, ana familia. Lakini tangu wakati huo anakuja mara chache. Nami naketi tu, nasubiri mtu anifikirie."\n      <span class="src">— Mama Fatuma, miaka 79, Morogoro</span>'),

    # blockquote 2
    ('„Egész életemben én voltam, aki vitte-hozta az unokákat, aki főzött, aki ott volt, ha baj volt. Amikor a\n      térdeim leálltak, egyszerre én lettem az, akit ellátni kell. És láttam a lányom szemén a fáradtságot. Ez fáj a\n      legjobban — nem a térd. Az, hogy teher lettem."\n      <span class="src">— Ferenc, 73 éves, Ózd</span>',
     '„Maisha yangu yote mimi ndiye niliyepeleka na kuleta wajukuu, niliyepika, niliyekuwepo wakati wa shida. Magoti yangu yaliposhindwa, ghafla mimi nikawa mtu anayehitaji kutunzwa. Na niliona uchovu machoni mwa binti yangu. Hiyo ndiyo inayoumiza zaidi — si magoti. Ukweli kwamba nimekuwa mzigo."\n      <span class="src">— Baba Juma, miaka 73, Dodoma</span>'),

    # H2 first
    ('„Láttam, mit jelent feleslegessé válni. És eldöntöttem, hogy nem nézhetem tétlenül"',
     '„Niliona maana ya kuwa si wa lazima. Na niliamua kwamba siwezi kukaa bila kufanya chochote"'),

    # lead under H2
    ('Exkluzív interjú dr. Kovács Gergővel — az orvossal, aki lemondott a havi másfél milliós fizetésről,\n      hogy azoknak segítsen, akiknek már nincs senkijük.',
     'Mahojiano ya kipekee na dk. Baraka Mwamba — daktari aliyeacha mshahara wa shilingi milioni 3.4 kwa mwezi,\n      ili awasaidie wale ambao hawana mtu yeyote tena.'),

    # doctor figcaption
    ('Dr. Kovács Gergő, ortopéd-traumatológus. A Semmelweis Egyetemen végzett, részben Németországban\n        szakosodott. Mielőtt belekezdett vidéki munkájába, egy budapesti magánklinikán dolgozott.',
     'Dk. Baraka Mwamba, daktari wa mifupa na majeraha. Alisomea katika Chuo Kikuu cha Muhimbili, na akajiboresha kwa sehemu nchini Afrika Kusini. Kabla ya kuanza kazi yake vijijini, alifanya kazi katika kliniki ya kibinafsi huko Dar es Salaam.'),

    # doctor first speech
    ('<p><b>Dr. Kovács Gergő:</b> „Először önkéntesként léptem be egy idős asszony otthonába, 28 éves koromban. Nem voltam\n      felkészülve arra, amit láttam. Egy 76 éves nő ült az ágy szélén, feldagadt lábakkal, térdekkel, amelyek már nem\n      hajlottak be. Négy hónapja ki sem mozdult a szobájából. Megfogta a kezem, és azt mondta: «Doktor úr, a gyerekeim\n      akkor hagytak magamra, amikor már nem tudtam felmenni a lépcsőn.» Abban a pillanatban értettem meg: ezeknek az\n      embereknek van rám a legnagyobb szükségük."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Mara ya kwanza niliingia nyumbani kwa mzee mwanamke kama mwanaojitolea, nilipokuwa na miaka 28. Sikuwa tayari kwa kile nilichokiona. Mwanamke wa miaka 76 alikuwa ameketi ukingoni mwa kitanda, miguu iliyovimba, na magoti ambayo hayakuweza kuinama. Miezi minne hakutoka chooni. Alinishika mkono na kusema: «Daktari, watoto wangu waliniacha wakati niliposhindwa kupanda ngazi.» Katika wakati huo ndipo nilielewa: watu hawa ndio wanaohitaji msaada wangu zaidi."</p>'),

    # doctor travels paragraph
    ('<p>Dr. Kovács Gergő nyugodtan beszél, de van a hangjában egy feszültség, amit nem lehet figyelmen kívül hagyni. Két\n      éve\n      járja Kelet-Magyarország falvait — Borsodtól Szabolcsig —, és mindenhol ugyanazzal a képpel találkozik: tönkrement\n      ízületű idős emberekkel, akik semmilyen valódi kezelést nem kapnak, csak gyulladáscsökkentőket, amelyek\n      tönkreteszik a gyomrukat és a veséjüket.</p>',
     '<p>Dk. Baraka Mwamba anazungumza kwa utulivu, lakini kuna nguvu katika sauti yake ambayo haiwezi kupuuzwa. Kwa miaka miwili amekuwa akizunguka vijiji vya Tanzania Mashariki — kutoka Morogoro hadi Dodoma —, na kila mahali anakutana na picha ile ile inayosumbua: wazee wenye viungo vilivyoharibiwa, wasiopata matibabu yoyote ya kweli, ni dawa za kupunguza uvimbe tu, ambazo zinaharibu tumbo na figo zao.</p>'),

    # pull quote
    ('      <p>„Magyarországon a nagyszülő gyakran a család <strong>tartóoszlopa</strong>. Ő viszi és hozza a gyereket az\n        iskolából, ő főz, ő vigyáz az unokákra, amíg a lánya vagy a fia dolgozik. Amikor egy idős embernek felmondanak\n        az ízületei, nemcsak a járást veszíti el. Elveszíti a <strong>szerepét</strong> a családban. Már nem tud\n        segíteni, nem tud hasznos lenni. Ezt a szót hallom a leggyakrabban a betegeimtől: «teher». A saját szüleiket\n        nevezik tehernek."</p>',
     '      <p>„Katika Tanzania, babu au bibi mara nyingi ndiye <strong>nguzo ya familia</strong>. Yeye hupeleka na kuleta watoto shuleni, yeye hupika, yeye hutunza wajukuu wakati binti au mwana wake anafanya kazi. Mzee anapopata tatizo la viungo, hupoteza zaidi ya kutembea. Anapoteza <strong>nafasi yake</strong> katika familia. Hawezi tena kusaidia, hawezi tena kuwa na manufaa. Neno hili ndilo ninalolosikia mara nyingi zaidi kutoka kwa wagonjwa wangu: «mzigo». Wanawita wazazi wao wenyewe kuwa mzigo."</p>'),

    # blockquote 3
    ('„Nem azért hagytak magamra, mert nem szeretnek. Hanem mert hajnali háromkor felüvöltöttem a fájdalomtól\n      a térdemben, és senki nem tudott aludni. A menyem azt mondta: vagy ő, vagy én. A fiam őt választotta."\n      <span class="src">— Gyula, 71 éves, Sajószentpéter</span>',
     '„Hawakuacha kwa sababu hawanipendi. Bali kwa sababu usiku wa manane nilipiga kelele kwa maumivu ya goti langu, na hakuna aliyeweza kulala. Mkwewe alisema: au yeye, au mimi. Mwanangu alimchagua yeye."\n      <span class="src">— Baba Hassan, miaka 71, Iringa</span>'),

    # H2 tablets
    ('„A tabletták semmit nem oldanak meg — csak elfedik a pusztulást"',
     '„Dawa za kumeza hazisaidii chochote — zinafunika tu uharibifu"'),

    ('<p>Dr. Kovács Gergő elmagyarázza, miért vall kudarcot a megszokott kezelés.</p>',
     '<p>Dk. Baraka Mwamba anaeleza kwa nini matibabu ya kawaida yanashindwa.</p>'),

    # tablets speech
    ('<p><b>Dr. Kovács Gergő:</b> „Őszinte leszek: amit ezekben a házakban láttam, az megrémített. 55–80 éves emberek,\n      akiknek évek óta ugyanazokat a gyulladáscsökkentő tablettákat adják — tablettákat, amelyek néhány órára elnyomják\n      a fájdalmat, de az okot nem szüntetik meg. A porcuk tovább pusztul. Az ízületi folyadék elfogy. Az ízület csontig\n      kopik. A tablettákban lévő vegyszer pedig napról napra rombolja a gyomrukat, a májukat és a veséjüket."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Nitakuwa mkweli: nilichokiona katika nyumba hizi kilinisogeza. Watu wenye miaka 55–80, ambao kwa miaka wamepewa dawa zile zile za kupunguza uvimbe — dawa ambazo zinazima maumivu kwa masaa machache, lakini hazishughulikii sababu. Cartilage yao inaendelea kuharibiwa. Maji ya viungo yanaisha. Kiungo kinakoromea mpaka mfupa. Na kemikali za dawa hizo zinaharibu tumbo, ini na figo zao siku baada ya siku."</p>'),

    # vicious cycle
    ('<p>Ez egy ördögi kör: fájdalom → tabletta → a fájdalom erősebben tér vissza → erősebb tabletta → a gyomor felmondja\n      → jönnek a gyomorgyógyszerek → a vese felmondja. És senki nem mondja meg nekik az igazat: hogy létezik mód az\n      ízület belülről történő helyreállítására, nem csak a fájdalom tompítására.</p>',
     '<p>Huu ni mzunguko mbaya: maumivu → dawa → maumivu yanarudika kwa nguvu zaidi → dawa kali zaidi → tumbo linashindwa → dawa za tumbo → figo zinashindwa. Na hakuna anayewaambia ukweli: kwamba kuna njia ya kurejesha kiungo kutoka ndani, si tu kupunguza maumivu.</p>'),

    # joint comparison figcaption
    ('Balra: egészséges ízület megőrzött porccal és elegendő ízületi folyadékkal. Jobbra: tönkrement ízület\n        — lekopott porc, krónikus gyulladás, csont a csonton. A gyulladáscsökkentő tabletták nem építik újra a porcot.\n      ',
     'Kushoto: kiungo chenye afya chenye cartilage nzima na maji ya kutosha ya viungo. Kulia: kiungo kilichoharibiwa — cartilage iliyokoromea, uvimbe wa kudumu, mfupa kwa mfupa. Dawa za kupunguza uvimbe hazijengi upya cartilage.\n      '),

    # pull 70-90
    ('      <p><b>Dr. Kovács Gergő:</b> „Sok idős embernél a porc a térdben, a gerincben vagy a csípőben 70–90%-ban\n        tönkrement. Ha még járnak egyáltalán, csontot csonton járnak. Minden lépés kínszenvedés. <strong>A megszokott\n          tabletták nem tudják újraépíteni a porcot — csak elfedik a fájdalmat, miközben minden tönkremegy.</strong>"\n      </p>',
     '      <p><b>Dk. Baraka Mwamba:</b> „Kwa wazee wengi, cartilage katika goti, mgongo au kiuno imeharibiwa kwa 70–90%. Wakitembea hata kidogo, wanaendesha mfupa kwa mfupa. Kila hatua ni mateso. <strong>Dawa za kawaida haziwezi kujenga upya cartilage — zinafunika tu maumivu wakati kila kitu kinaendelea kuharibika.</strong>"\n      </p>'),

    # H2 stories
    ('Történetek, amelyeket minden héten a saját szememmel látok',
     'Hadithi ninazoziona kila wiki kwa macho yangu mwenyewe'),

    ('<p><b>Dr. Kovács Gergő:</b> „Engedjék meg, hogy elmondjam, mit látok. Nem számokat. Embereket. Embereket, akiknek\n      nevük van, történetük, és gyerekeik, akik már nem jönnek."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Niruhusu niwaambie ninachokiona. Si nambari. Watu. Watu wenye majina, wenye hadithi, na watoto ambao hawaji tena."</p>'),

    # Irén néni figcaption
    ('Irén néni, 77 éves. Mindkét kezét reumás ízületi gyulladás támadta meg — nem tud bögrét tartani,\n        egyedül felöltözni sem. „Reggel ránézek a kezemre, és nem ismerem meg. Mintha nem is az enyém lenne."\n      ',
     'Mama Zawadi, miaka 77. Mikono yake yote miwili imeshambuliwa na ugonjwa wa viungo wa baridi yabisi — hawezi kushika kikombe, hawezi kujivisha peke yake. „Asubuhi ninaangalia mikono yangu, nisiyoijua. Kana kwamba si yangu."\n      '),

    # Piroska blockquote
    ('„Három gyereket neveltem fel. Negyven évig dolgoztam a földeken. Amikor a térdeim felmondtak, és már a\n      fürdőszobába sem jutottam el egyedül, egyszerűen… egyre ritkábban jöttek. Mintha már nem is léteznék a számukra."\n      <span class="src">— Piroska, 82 éves, Encs</span>',
     '„Niliwalea watoto watatu. Nilifanya kazi mashambani kwa miaka arobaini. Magoti yangu yaliposhindwa, na sikuweza kwenda chooni peke yangu, polepole… walikuja mara chache zaidi. Kana kwamba mimi sijawahi kuwepo kwao."\n      <span class="src">— Mama Amina, miaka 82, Kilosa</span>'),

    # Zoltán figcaption
    ('Zoltán, 75 éves. Porckorongsérv, kétoldali csípőkopás. Nyolc hónapja nem áll a lábán. „Azt mondták,\n        túl öreg vagyok a műtéthez. Azt mondták, nyugodjak bele."',
     'Baba Ramadhani, miaka 75. Mshikamano wa diski ya mgongo, uharibifu wa kiuno pande zote mbili. Miezi minane hajasimama. „Walisema mzee sana kwa upasuaji. Walisema, nikubali tu hali."'),

    # H3 symptoms
    ('Ezeket a tüneteket látom a leggyakrabban — és milliók hagyják figyelmen kívül:',
     'Dalili hizi ndizo ninazoziona mara nyingi zaidi — na mamilioni wanazipuuza:'),

    # symptom list
    ('      <li>Erős fájdalom a térdben lépcsőn fel- vagy lefelé menet — vagy minden mozdulatnál;</li>\n      <li>Reggeli merevség — a test „fából van", 30–60 percig nem mozdul ébredés után;</li>\n      <li>Krónikus hátfájás — nem tud lehajolni, nem tud felkelni az ágyból;</li>\n      <li>Bedagadt térd, boka vagy ujjak;</li>\n      <li>Ropogás és recsegés az ízületekben minden mozdulatnál;</li>\n      <li>Csípőfájás, amely a combba sugárzik — nem tud 50 méternél többet menni;</li>\n      <li>Eldeformálódott, csomós ujjak — nem tudja megfogni a tárgyakat;</li>\n      <li>Zsibbadó láb vagy kéz — porckorongsérv vagy becsípődött ideg jele;</li>\n      <li>„Kés" érzése a derékban kiegyenesedéskor;</li>\n      <li>Görnyedő hát, ferde testtartás — fokozódó gerincferdülés;</li>\n      <li>Éjszakai fájdalom, amely nem hagy aludni — 4–5-ször ébred fel éjjel;</li>',
     '      <li>Maumivu makali katika goti wakati wa kupanda au kushuka ngazi — au kila unapotembea;</li>\n      <li>Ugumu wa asubuhi — mwili „kama mbao", hauwezi kutembea kwa dakika 30–60 baada ya kuamka;</li>\n      <li>Maumivu ya kudumu ya mgongo — hawezi kuinama, hawezi kutoka kitandani;</li>\n      <li>Kuvimba kwa goti, kifundo cha mguu au vidole;</li>\n      <li>Mlio wa mifupa katika viungo kila unaposogea;</li>\n      <li>Maumivu ya kiuno yanayoenea mpaka paja — hawezi kutembea zaidi ya mita 50;</li>\n      <li>Vidole vilivyopinda na kuvimba — hawezi kushika vitu;</li>\n      <li>Ganzi katika mguu au mkono — ishara ya mshikamano wa diski au ujasiri ulionaswa;</li>\n      <li>Hisia ya „kisu" kiunoni wakati wa kunyoosha;</li>\n      <li>Mgongo ulioinamia, mkao mbaya — kiinamia kinachozidi;</li>\n      <li>Maumivu ya usiku yasiyomruhusu kulala — anaamka mara 4–5 usiku;</li>'),

    # alarm
    ('Ezeknek a tüneteknek a figyelmen kívül hagyása 45–50 éves kor után egyetlen végkifejlet felé\n      vezet: TELJES MOZGÁSKÉPTELENSÉG, KEREKESSZÉK, TELJES KISZOLGÁLTATOTTSÁG — ÉS A LEGTÖBB ESETBEN AZ, HOGY A CSALÁD\n      LASSAN ELENGED.',
     'Kupuuza dalili hizi baada ya umri wa miaka 45–50 kunasababisha matokeo moja tu:\n      KUTOWEZA KUTEMBEA KABISA, KITI CHA MAGURUDUMU, KUTEGEMEA WENGINE KABISA — NA MARA NYINGI, FAMILIA YAKO KUANZA KUKUACHA POLEPOLE.'),

    # family slow abandon
    ('Először ritkábban jönnek. Aztán a lányod az asztalra teszi az idősotthon papírjait. Aztán az unokáid kezdenek\n      elkerülni, mert nem tudják, mit mondjanak annak, aki már fel sem tud állni. <b>Cselekedjen most — magáért vagy a\n        szeretteiért —, mielőtt késő lenne.</b>',
     'Kwanza wanakuja mara chache. Kisha binti yako anaweka karatasi za nyumba ya wazee mezani. Kisha wajukuu wako wanaanza kukuepuka, hawajui waambie nini mtu ambaye hata kusimama hawezi. <b>Fanya sasa — kwa ajili yako au wapendwa wako — kabla hujachelewa.</b>'),

    # H2 decision
    ('„Eldöntöttem, hogy léteznie kell módnak az ízületek helyreállítására — nem csak a fájdalom tompítására"',
     '„Niliamua lazima kuwe na njia ya kurejesha viungo — si tu kupunguza maumivu"'),

    # research decision
    ('<p><b>Dr. Kovács Gergő:</b> „Egy év vidéki munka után rájöttem egy fájdalmas dologra: gyulladáscsökkentő\n      tablettákkal senkit nem mentek meg. Valami egészen másra volt szükségem: egy módszerre, amely belülről építi újra\n      a porcot, helyreállítja az ízületi folyadékot, és sejtszinten állítja meg a gyulladást."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Baada ya mwaka mmoja wa kazi vijijini, niligundua ukweli mchungu: dawa za kupunguza uvimbe hazimwokoi mtu yeyote. Nilihitaji kitu tofauti kabisa: njia inayojenga upya cartilage kutoka ndani, inayorejesha maji ya viungo, na inayosimamisha uvimbe katika kiwango cha seli."</p>'),

    # research institute
    ('<p>„Felvettem a kapcsolatot egy kutatóintézettel, amellyel a szakosodásom alatt dolgoztam együtt. Megmutattam nekik\n      a betegeim eseteit, a felvételeket, a leleteket. És megdöbbentek. Több mint 10 hónapon át dolgoztunk együtt. Több\n      mint 180 kombinációt teszteltünk. Végül megtaláltuk a pontos formulát — egy krémet, amely a megtámadott ízületre\n      kenve sejtszintig hatol, és aktiválja a porc természetes regenerációját."</p>',
     '<p>„Niliwasiliana na taasisi ya utafiti ambayo nilifanya nayo kazi wakati wa utaalamu wangu. Niliwaonyesha kesi za wagonjwa wangu, picha, matokeo ya vipimo. Na wakashangaa. Tulifanya kazi pamoja kwa zaidi ya miezi 10. Tulijaribu mchanganyiko zaidi ya 180. Hatimaye tulipata formula sahihi — krimu ambayo inapakiwa kwenye kiungo kilichoshambuliwa, inachomeka hadi kiwango cha seli, na inawasha upyaisho wa asili wa cartilage."</p>'),

    # H3 ingredients
    ('A formula hatóanyagai:', 'Viambato vya formula:'),

    # ingredients list
    ('      <li><b>Boswellia serrata kivonat</b>Természetes gyulladáscsökkentő, megállítja a porc pusztulását.</li>\n      <li><b>Glükozamin és kondroitin aktív formában</b>Az ízületi porc építőkövei — táplálék a sejteknek.</li>\n      <li><b>Kis molekulájú hialuronsav</b>Újraépíti az ízületi folyadékot — az ízület természetes „kenőanyagát".</li>\n      <li><b>II-es típusú kollagén és MSM</b>Erősítik az ízületet körülvevő szalagokat és inakat.</li>\n      <li><b>Kámfor és hegyi árnika</b>Azonnali enyhülés a fájdalomra és a duzzanatra.</li>',
     '      <li><b>Dondoo la Boswellia serrata</b>Kizuia uvimbe cha asili, kinachosimamisha uharibifu wa cartilage.</li>\n      <li><b>Glucosamine na chondroitin katika hali hai</b>Vifaa vya ujenzi wa cartilage ya viungo — chakula kwa seli.</li>\n      <li><b>Asidi ya hyaluronic ya molekuli ndogo</b>Inajenga upya maji ya viungo — „mafuta" ya asili ya kiungo.</li>\n      <li><b>Collagen aina ya II na MSM</b>Zinaimarisha mishipa na tendons zinazozunguka kiungo.</li>\n      <li><b>Camphor na arnica ya mlima</b>Pumziko la haraka kutoka kwa maumivu na uvimbe.</li>'),

    # formula note
    ('<p>A formula további 14 ritka kivonatot tartalmaz, pontosan kiszámított arányban. Mindössze 0,1% eltérés, és a krém\n      már nem hatol elég mélyre.</p>',
     '<p>Formula ina dondoo 14 nyingine adimu, katika uwiano uliohesabiwa kwa usahihi. Tofauti ya 0.1% tu, na krimu haitaingia kwa kina cha kutosha.</p>'),

    # H2 HondroDin born
    ('Így született meg a HondroDin — az egyetlen krém, amely sejtszinten, közvetlenül a megtámadott ízületen hat',
     'Hivyo ndivyo HondroDin ilivyozaliwa — krimu pekee inayofanya kazi katika kiwango cha seli, moja kwa moja kwenye kiungo kilichoshambuliwa'),

    # product figcaption
    ('A HondroDin kizárólag külső használatra készült krém, amelyet közvetlenül a fájó ízületre kell\n        felvinni.',
     'HondroDin ni krimu inayotumika nje peke yake, ambayo inapakiwa moja kwa moja kwenye kiungo chenye maumivu.'),

    # doctor product description
    ('<p><b>Dr. Kovács Gergő:</b> „A kutatóintézettel közösen sikerült előállítanunk ezt a terméket: egy külsőleg\n      használható krémet, amelyet közvetlenül a megtámadott ízületre kennek — térd, hát, csípő, kéz, nyak. A neve\n      HondroDin. Naponta kétszer kell használni, reggel és este, 2–3 perces gyengéd masszírozással. A hatóanyagok\n      közvetlenül az ízületbe jutnak, megkerülve a gyomrot és a májat — így a tabletták minden mellékhatása kiesik."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Pamoja na taasisi ya utafiti tuliweza kutengeneza bidhaa hii: krimu ya matumizi ya nje, ambayo inapakiwa moja kwa moja kwenye kiungo kilichoshambuliwa — goti, mgongo, kiuno, mkono, shingo. Inaitwa HondroDin. Inatumika mara mbili kwa siku, asubuhi na jioni, kwa upole wa kukanda kwa dakika 2–3. Viambato vya kazi vinaingia moja kwa moja kwenye kiungo, vikizunguka tumbo na ini — kwa hivyo madhara yote ya dawa za kumeza hayatokei."</p>'),

    # technology
    ('<p>A titok a „Mély Transzdermális Behatolás Technológiájában" rejlik, amelyet a laborban dolgoztunk ki. Ez a módszer\n      lehetővé teszi, hogy a hatóanyagok közvetlenül az ízületi tokba jussanak — oda, ahol a porc pusztul — ötször\n      nagyobb hatékonysággal, mint bármely hagyományos krém.</p>',
     '<p>Siri iko katika „Teknolojia ya Kupenya kwa Kina ya Transdermal", ambayo tulitengeneza katika maabara. Njia hii inaruhusu viambato vya kazi kufikia moja kwa moja kwenye kifuko cha kiungo — pale ambapo cartilage inaharibika — kwa ufanisi mara tano zaidi ya krimu yoyote ya kawaida sokoni.</p>'),

    # pull first patients
    ('      <p><b>Dr. Kovács Gergő:</b> „Az első betegeim a falvak idős emberei voltak. Olyanok, akiket a családjuk magára\n        hagyott. Felkentem a krémet a feldagadt térdekre, hátakra, csípőkre. És vártam. A harmadik napon egy asszony,\n        aki négy hónapja nem kelt fel az ágyból, megtette az első lépéseit egyedül. Mindketten sírtunk."</p>',
     '      <p><b>Dk. Baraka Mwamba:</b> „Wagonjwa wangu wa kwanza walikuwa wazee wa vijiji. Wale ambao familia zao waliwaacha. Nilipaka krimu kwenye magoti yaliyovimba, migongo, viuno. Na nikasubiri. Siku ya tatu, mwanamke aliyekuwa hajaondoka kitandani kwa miezi minne, alitembea peke yake kwa mara ya kwanza. Wote wawili tulilia."</p>'),

    # H2 4 mechanisms
    ('Négy mód, ahogyan a HondroDin helyreállítja az ízületeket — bármely életkorban',
     'Njia nne ambazo HondroDin inavyorejesha viungo — katika umri wowote'),

    # effect 1
    ('<div><b>A fájdalom és a gyulladás megszüntetése</b><br>Már az első 15–30 percben a Boswellia, az árnika és a\n        kámfor komplexe enyhíti a fájdalmat és csökkenti a gyulladást — nem az idegjel blokkolásával (ahogy a tabletták\n        teszik), hanem a gyulladásos folyamat forrásánál való megállításával.</div>',
     '<div><b>Kuondoa maumivu na uvimbe</b><br>Tayari katika dakika 15–30 za kwanza, mchanganyiko wa Boswellia, arnica na camphor hupunguza maumivu na kupunguza uvimbe — si kwa kuzuia ishara ya ujasiri (kama dawa za kumeza zinavyofanya), bali kwa kusimamisha mchakato wa uvimbe chanzo chake.</div>'),

    # effect 2
    ('<div><b>Az ízületi porc regenerációja</b><br>A glükozamin, a kondroitin és a II-es típusú kollagén bejut az\n        ízületi tokba, és aktiválja a porcsejteket, serkentve az új porcszövet termelődését. Ez a folyamat 3–5 nap\n        rendszeres használat után indul be.</div>',
     '<div><b>Kuzaliwa upya kwa cartilage ya kiungo</b><br>Glucosamine, chondroitin na collagen aina ya II zinaingia kwenye kifuko cha kiungo, na kuamsha seli za cartilage, zikichochea uzalishaji wa tishu mpya za cartilage. Mchakato huu huanza siku 3–5 za matumizi ya kawaida.</div>'),

    # effect 3
    ('<div><b>Az ízületi folyadék helyreállítása</b><br>A kis molekulájú hialuronsav transzdermálisan hatol be, és\n        újraépíti az ízületi folyadékot — az ízület természetes „kenőanyagát". Így a csontok többé nem dörzsölődnek\n        egymáshoz, a mozgás pedig folyamatossá és fájdalommentessé válik.</div>',
     '<div><b>Kurudisha maji ya viungo</b><br>Asidi ya hyaluronic ya molekuli ndogo inaingia kwa njia ya transdermal, na kujenga upya maji ya viungo — „mafuta" ya asili ya kiungo. Kwa hivyo mifupa haingurumiani tena, na mwendo unakuwa laini na bila maumivu.</div>'),

    # effect 4
    ('<div><b>Hosszú távú védelem és megelőzés</b><br>Az MSM és az ásványi komplex erősíti az ízületet körülvevő\n        szalagokat és inakat, megelőzve a jövőbeni károsodást. 30–60 nap használat után az ízület tartós védelmet kap.\n      </div>',
     '<div><b>Ulinzi wa muda mrefu na kuzuia</b><br>MSM na mchanganyiko wa madini huziimarisha mishipa na tendons zinazozunguka kiungo, ikizuia uharibifu wa siku zijazo. Baada ya siku 30–60 za matumizi, kiungo hupata ulinzi wa kudumu.\n      </div>'),

    # H2 stories hope
    ('Történetek, amelyek megtanítottak rá, hogy soha nem késő',
     'Hadithi zilizonionyesha kwamba kamwe si kuchelewa'),

    ('<p><b>Dr. Kovács Gergő:</b> „Íme néhány ember, akiket minden héten a saját szememmel látok. Olyanok, akiknek senki\n      nem adott esélyt. Olyanok, akik most újra járnak."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Hawa hapa ni watu wachache ninaowaona kila wiki kwa macho yangu mwenyewe. Wale ambao hakuna aliyewapa nafasi. Wale ambao sasa wanatembea tena."</p>'),

    # Margit figcaption
    ('Margit néni, 82 éves. Négy hónapig nem kelt fel az ágyból. Három nap használat után önállóan megtette\n        az első lépéseit. „Senki nem várta. Még én sem."',
     'Mama Fatuma, miaka 82. Miezi minne hakuondoka kitandani. Baada ya siku tatu za matumizi, alitembea peke yake kwa mara ya kwanza. „Hakuna aliyetarajia. Hata mimi."'),

    # Piroska casebox
    ('      <b>Piroska, 82 éves</b> — négy hónapig nem kelt fel az ágyból. 3 nap után az első lépések, 30 nap után egyedül\n      megy ki az udvarra.\n      <div class="res">Eredmény 30 nap után: önálló járás, megszűnt a reggeli merevség, a fájdalom 9/10-ről 2/10-re\n        csökkent.</div>',
     '      <b>Mama Amina, miaka 82</b> — miezi minne hakuondoka kitandani. Baada ya siku 3 hatua za kwanza, baada ya siku 30 anatoka nje peke yake.\n      <div class="res">Matokeo baada ya siku 30: kutembea kwa uhuru, ugumu wa asubuhi umeisha, maumivu yamepungua kutoka 9/10 hadi 2/10.</div>'),

    # Gyula casebox
    ('      <b>Gyula, 71 éves</b> — porckorongsérv, isiász, 5 percnél tovább nem tudott egyenesen állni. 6 hét után visszatért\n      a kertjébe.\n      <div class="res">Eredmény 45 nap után: megszűnt a heves derékfájás, visszatért a mozgásképesség, 4 év óta először\n        aludt át egy éjszakát.</div>',
     '      <b>Baba Hassan, miaka 71</b> — mshikamano wa diski, maumivu ya sciatic, hakuweza kusimama wima zaidi ya dakika 5. Baada ya wiki 6 alirudi bustanini.\n      <div class="res">Matokeo baada ya siku 45: maumivu makali ya kiuno yameisha, uwezo wa kutembea ulirejea, aliweza kulala usiku mzima kwa mara ya kwanza kwa miaka 4.</div>'),

    # H2 pharmacy
    ('Miért nem kapható a HondroDin a gyógyszertárakban? És hogyan lehet hozzájutni?',
     'Kwa nini HondroDin haipatikani katika maduka ya dawa? Na jinsi ya kuipata?'),

    ('<p><b>Dr. Kovács Gergő:</b> „Sajnos a HondroDin gyártása bonyolult és költséges folyamat. Az alapanyagok ritkák — a\n      kis molekulájú hialuronsav, a tisztított II-es típusú kollagén, a tömény Boswellia-kivonat —, és nehéz a szükséges\n      mennyiségben beszerezni őket. Nem tudjuk a teljes keresletet kielégíteni."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Kwa bahati mbaya, utengenezaji wa HondroDin ni mchakato mgumu na ghali. Malighafi ni adimu — asidi ya hyaluronic ya molekuli ndogo, collagen ya aina ya II iliyosafishwa, dondoo la Boswellia lenye nguvu —, na ni vigumu kuvipata katika kiasi kinachohitajika. Hatuwezi kukidhi mahitaji yote."</p>'),

    ('<p>Legalább 2–3 évre lenne szükség ahhoz, hogy a HondroDin a gyógyszertárakba kerüljön. Addig a terméket kizárólag\n      online, támogatási programok keretében forgalmazzuk, évente kétszer. A kedvezmény akár az 50%-ot is elérheti — ami\n      az idős embereknek rendkívül fontos.</p>',
     '<p>Itachukua angalau miaka 2–3 kabla HondroDin haijafika katika maduka ya dawa. Hadi wakati huo, bidhaa inasambazwa mtandaoni peke yake, ndani ya programu za usaidizi, mara mbili kwa mwaka. Punguzo linaweza kufikia hadi 50% — jambo ambalo ni muhimu sana kwa wazee.</p>'),

    ('<p>„Amikor a forgalmazók megértették, milyen hatékony a formula, 33 500 forintért akarták árulni tubusonként.\n      Visszautasítottam. Nem a pénzért csinálom — hanem azokért az idős emberekért, akik 160 ezer forintos nyugdíjból\n      élnek, és választaniuk kell a gyógyszer és a kenyér között."</p>',
     '<p>„Wasambazaji walipoelewa jinsi formula inavyofaa, walitaka kuiuza kwa shilingi 75,000 kwa kila bomba. Nilikataa. Sifanyi hii kwa pesa — bali kwa ajili ya wazee wale wanaoishi kwa pensheni ya shilingi 350,000, na wanaolazimika kuchagua kati ya dawa na mkate."</p>'),

    # price table cells
    ('          <td class="lbl">Ár, amit a forgalmazók kértek</td>\n          <td class="val">33 500 HUF</td>',
     '          <td class="lbl">Bei iliyotakiwa na wasambazaji</td>\n          <td class="val">75,000 TZS</td>'),
    ('          <td class="lbl">Ár más európai országokban</td>\n          <td class="val">19 900 HUF</td>',
     '          <td class="lbl">Bei katika nchi nyingine za Afrika</td>\n          <td class="val">45,000 TZS</td>'),
    ('          <td class="lbl">Mai teljes ár</td>\n          <td class="val">22 800 HUF</td>',
     '          <td class="lbl">Bei kamili ya leo</td>\n          <td class="val">52,000 TZS</td>'),
    ('          <td class="lbl">Olvasói kedvezménnyel ma</td>\n          <td class="val">11 400 HUF</td>',
     '          <td class="lbl">Bei ya wasomaji leo</td>\n          <td class="val">26,000 TZS</td>'),

    # do not miss
    ('<p><b>Kérem: NE HAGYJA KI A TÁMOGATÁSI PROGRAMOT.</b> Ne csak magáért — a szüleiért, nagyszüleiért, szeretteiért is,\n      akik talán csendben szenvednek. Legyen Ön az, aki változást hoz.</p>',
     '<p><b>Tafadhali: USIKOSE PROGRAMU YA USAIDIZI.</b> Si kwa ajili yako tu — bali pia kwa wazazi wako, babu na bibi wako, wapendwa wako, ambao labda wanateseka kimya kimya. Kuwa wewe mtu anayebadilisha hali.</p>'),

    ('<p>A rendeléshez kérjük, használja az alábbi űrlapot.</p>',
     '<p>Ili kuagiza, tafadhali tumia fomu iliyo hapa chini.</p>'),

    # H2 last chance
    ('Utolsó esély, hogy idén hozzájusson a HondroDin termékhez — magának vagy egy szerettének',
     'Nafasi ya mwisho kupata HondroDin mwaka huu — kwako au kwa mpendwa wako'),

    ('<p><b>Dr. Kovács Gergő:</b> „20 000 tubust foglaltam le kizárólag ennek a portálnak az olvasói számára. Minden 40 év\n      feletti magyar állampolgár akár 50% kedvezményt kaphat, de a program hamarosan lezárul."</p>',
     '<p><b>Dk. Baraka Mwamba:</b> „Nimehifadhi bomba 20,000 kwa ajili ya wasomaji wa tovuti hii peke yao. Kila raia wa Tanzania mwenye umri zaidi ya miaka 40 anaweza kupata punguzo la hadi 50%, lakini programu inafungwa hivi karibuni."</p>'),

    ('<p>Ne várjon, amíg már nem tud felmenni a lépcsőn. Amíg a térde végleg felmondja a szolgálatot. És főleg — ne\n      várjon, amíg „teherré" válik a szerettei szemében. A HondroDin hatása halmozódó, és elég évente egyszer használni\n      megelőzésként.</p>',
     '<p>Usisubiri hadi ushindwe kupanda ngazi. Hadi magoti yako yashindwe kabisa. Na hasa — usisubiri hadi uwe „mzigo" machoni mwa wapendwa wako. Athari ya HondroDin inajikusanyika, na inatosha kuitumia mara moja kwa mwaka kama kinga.</p>'),

    # counter
    ('<div>A program a mai napon zárul:</div>', '<div>Programu inafungwa leo:</div>'),
    ('<div class="big">Az Ön számára fenntartva: Nr <span id="resnum">19 974</span></div>',
     '<div class="big">Imehifadhiwa kwako: Nr <span id="resnum">19 974</span></div>'),
    ('<div>Elérhető: <b><span id="stock">27</span></b> / 1000</div>',
     '<div>Zinazopatikana: <b><span id="stock">27</span></b> / 1000</div>'),
    ('<span class="was">22 800 HUF</span><span class="is">11 400 HUF</span>',
     '<span class="was">52,000 TZS</span><span class="is">26,000 TZS</span>'),
    ('<a href="#" class="cta" style="margin-top:8px">LEFOGLALOM A KEDVEZMÉNYT</a>',
     '<a href="#" class="cta" style="margin-top:8px">HIFADHI PUNGUZO LANGU</a>'),
    ('<p style="font-size:.8rem;color:#bbb;margin:10px 0 0">Figyelem! Kérjük, ne zárja be és ne frissítse az oldalt,\n        különben a fenntartott tubust felajánljuk valaki másnak.</p>',
     '<p style="font-size:.8rem;color:#bbb;margin:10px 0 0">Tahadhari! Tafadhali usifunge au kuonyesha upya ukurasa,\n        vinginevyo bomba lililohifadhiwa litatolewa kwa mtu mwingine.</p>'),

    # order form
    ('<h3>Hivatalos megrendelőlap</h3>', '<h3>Fomu rasmi ya kuagiza</h3>'),
    ('<input type="hidden" name="country" value="HU">', '<input type="hidden" name="country" value="TZ">'),
    ('placeholder="Az Ön neve"', 'placeholder="Jina lako"'),
    ('placeholder="Telefonszám"', 'placeholder="Nambari ya simu"'),
    ('<button type="submit" class="cta">MEGRENDELEM MOST</button>',
     '<button type="submit" class="cta">NINAAGIZA SASA</button>'),
    ('<p style="font-size:.85rem;color:var(--muted);margin-bottom:0">✔️ A kiszállítást a futárszolgálat végzi, 2–3 napon\n        belül, közvetlenül a megadott címre.</p>',
     '<p style="font-size:.85rem;color:var(--muted);margin-bottom:0">✔️ Utoaji unafanywa na huduma ya courier, ndani ya siku 2–3, moja kwa moja kwenye anwani iliyotolewa.</p>'),

    # closing quote
    ('<p style="font-family:Georgia,serif;font-style:italic;color:#333">Reménnyel és tisztelettel — dr. Kovács Gergő.\n      Kérem, viselje gondját a szeretteinek. Talán csak annyira van szükségük, hogy tudják: Ön nem feledkezett meg\n      róluk.</p>',
     '<p style="font-family:Georgia,serif;font-style:italic;color:#333">Kwa matumaini na heshima — dk. Baraka Mwamba.\n      Tafadhali wajali wapendwa wako. Labda wachohitaji tu ni kujua kwamba hukuwasahau.</p>'),

    # badges
    ('      <span>🛡️ Tanúsított minőség</span>\n      <span>🚚 Kiszállítás 2–3 nap</span>\n      <span>⚕️ Vény nélkül</span>\n      <span>🔒 Biztonságos rendelés</span>',
     '      <span>🛡️ Ubora uliothibitishwa</span>\n      <span>🚚 Utoaji siku 2–3</span>\n      <span>⚕️ Bila dawa ya daktari</span>\n      <span>🔒 Agizo salama</span>'),

    # comments header
    ('<h3 style="font-family:Georgia,serif">HOZZÁSZÓLÁSOK</h3>',
     '<h3 style="font-family:Georgia,serif">MAONI</h3>'),

    # comment 1 Bognár Marianna
    ('            <div class="nm">Bognár Marianna</div>\n            <div class="tm">2 órája</div>',
     '            <div class="nm">Msongo Mariamu</div>\n            <div class="tm">Masaa 2 iliyopita</div>'),
    ('<p class="bd">Az anyósom a kapuban várt, amikor megérkeztem. Le kellett fényképeznem. Egész úton sírtam.</p>',
     '<p class="bd">Mama mkwe wangu alisubiri mlangoni nilipofika. Nilimpigia picha. Nililia njia yote nikienda nyumbani.</p>'),

    # comment 2 Kovács Mária
    ('            <div class="nm">Kovács Mária</div>\n            <div class="tm">4 órája</div>',
     '            <div class="nm">Kamala Maria</div>\n            <div class="tm">Masaa 4 iliyopita</div>'),
    ('<p class="bd">Sírtam, amikor ezt olvastam. Anyám 76 éves, két éve idősotthonban van — pont azért, mert\n          felmondtak a térdei, és én már nem tudtam ellátni. Ez életem legnagyobb bűntudata. Megrendeltem neki a\n          HondroDin-t. Talán még nem késő. Istenem, csak hasson.</p>',
     '<p class="bd">Nililia nilipoisoma hii. Mama yangu ana miaka 76, amekuwa nyumbani kwa wazee kwa miaka miwili — hasa kwa sababu magoti yake yalishindwa, na mimi sikuweza kumhudumia. Hii ndiyo hatia kubwa zaidi ya maisha yangu. Nimemwagazia HondroDin. Labda bado si kuchelewa. Mungu, naomba isaidie.</p>'),

    # comment 3 Tóth Erika
    ('            <div class="nm">Tóth Erika</div>\n            <div class="tm">5 órája</div>',
     '            <div class="nm">Temu Erika</div>\n            <div class="tm">Masaa 5 iliyopita</div>'),
    ('<p class="bd">Múlt pénteken kaptam meg. Reggel-este kenem a térdemre. 5 nap után sokkal kevesebb a fájdalom,\n          lépcsőn is le tudok menni anélkül, hogy a korlátba kapaszkodnék! Az orvos története győzött meg, hogy\n          megrendeljem. Rendkívüli ember.</p>',
     '<p class="bd">Nilipokea Ijumaa iliyopita. Ninapaka magotini asubuhi na jioni. Baada ya siku 5 maumivu ni kidogo sana, ninaweza kushuka ngazi bila kushikamana na reli! Hadithi ya daktari ilinishawishi kuagiza. Mtu wa ajabu.</p>'),

    # comment 4 Kiss László
    ('            <div class="nm">Kiss László</div>\n            <div class="tm">7 órája</div>',
     '            <div class="nm">Kisava Lazaro</div>\n            <div class="tm">Masaa 7 iliyopita</div>'),
    ('<p class="bd">Napi 10 órát ülök az irodában. A hátam és a nyakam felmondta. Az orvos azt mondta: „vagy\n          munkahelyet vált, vagy műtét." A HondroDin-t választottam. 5 hét után a fájdalomnak nyoma sincs. És óriási\n          tisztelet dr. Kovács Gergőnek — egy olyan világban, ahol mindenki pénzt akar, ő az elfeledett öregekhez jár.\n        </p>',
     '<p class="bd">Ninakaa ofisini kwa masaa 10 kila siku. Mgongo na shingo yangu vimeshindwa. Daktari alisema: „au ubadilishe kazi, au upasuaji." Nilichagua HondroDin. Baada ya wiki 5 maumivu hayapo kabisa. Na heshima kubwa kwa dk. Baraka Mwamba — katika ulimwengu ambapo kila mtu anataka pesa, yeye anakwenda kwa wazee waliosaahauliwa.\n        </p>'),

    # comment 5 Németh Anikó
    ('            <div class="nm">Németh Anikó</div>\n            <div class="tm">9 órája</div>',
     '            <div class="nm">Ngowi Anika</div>\n            <div class="tm">Masaa 9 iliyopita</div>'),
    ('<p class="bd">69 éves vagyok. A hátam négy éve kínzott — porckorongsérv és isiász. Nem tudtam lehajolni, hogy\n          bekössem a cipőmet. Az orvosok gyulladáscsökkentőt adtak, ami tönkretette a gyomromat. 3 hét HondroDin után a\n          fájdalom szinte eltűnt. Egyedül járok vásárolni, főzök. Visszakaptam az életemet.</p>',
     '<p class="bd">Nina miaka 69. Mgongo wangu ulikuwa ukinidhulumu kwa miaka minne — mshikamano wa diski na maumivu ya sciatic. Sikuweza kuinama kufunga viatu vyangu. Madaktari walitoa dawa za kupunguza uvimbe, ambazo ziliharibu tumbo langu. Baada ya wiki 3 za HondroDin maumivu yamepotea karibu kabisa. Ninaenda kununua peke yangu, ninapika. Nimepata tena maisha yangu.</p>'),

    # comment 6 Varga Gergely
    ('            <div class="nm">Varga Gergely</div>\n            <div class="tm">11 órája</div>',
     '            <div class="nm">Mwanga Geremo</div>\n            <div class="tm">Masaa 11 iliyopita</div>'),
    ('<p class="bd">3 tubust rendeltem — magamnak (térd), a feleségemnek (kéz, ízületi gyulladás) és az apósomnak, aki\n          idősotthonban van. Nem tudjuk gyakran látogatni, de legalább elküldjük neki, amire szüksége van. Remélem, nála\n          is így hat. Köszönöm ezt a cikket.</p>',
     '<p class="bd">Niliagiza bomba 3 — kwangu (goti), mke wangu (mkono, arthritis) na baba mkwe wangu, aliye nyumbani kwa wazee. Hatuwezi kumtembelea mara nyingi, lakini angalau tunamtumia anahohitaji. Natumaini itamsaidia pia. Asante kwa makala hii.</p>'),

    # comment 7 Lukács Éva
    ('            <div class="nm">Lukács Éva</div>\n            <div class="tm">13 órája</div>',
     '            <div class="nm">Lukia Eva</div>\n            <div class="tm">Masaa 13 iliyopita</div>'),
    ('<p class="bd">Megígértem, hogy felteszem a képet. Édesanyám 80 éves, fél éve ki sem mozdult a házból. Tegnap a\n          kertben fotóztam le — egyedül sétál. Köszönöm, dr. Kovács Gergő!</p>',
     '<p class="bd">Niliahidi nitaweka picha. Mama yangu ana miaka 80, kwa miezi sita hakutoka nyumbani. Jana nilimpiga picha bustanini — anatembea peke yake. Asante, dk. Baraka Mwamba!</p>'),

    # comment 8 Farkas Piroska
    ('            <div class="nm">Farkas Piroska</div>\n            <div class="tm">15 órája</div>',
     '            <div class="nm">Farida Amina</div>\n            <div class="tm">Masaa 15 iliyopita</div>'),
    ('<p class="bd">Őszintén szólva először nem hittem benne. Annyi mindent reklámoznak az interneten, hogy már nem\n          hiszek nekik. Csak azért olvastam el ezt a cikket, mert az anyósom nem tud járni, és kétségbe vagyok esve.\n          Megrendeltem azzal, hogy „ha nem hat, elbuktam 11 400 forintot". Eltelt 3 hét. Az anyósom tegnap magától\n          felállt a fotelből. Az anyósom! Aki 8 hónapja nem állt fel egyedül. Csak azoknak írom ezt, akik kételkednek —\n          mint én.</p>',
     '<p class="bd">Kwa uaminifu mwanzoni sikuamini. Kuna matangazo mengi sana mtandaoni, kiasi kwamba siiamini tena. Nilisoma makala hii tu kwa sababu mama mkwe wangu hawezi kutembea, na nimekuwa na wasiwasi mkubwa. Niliagiza nikisema „kama haisaidii, nimepoteza shilingi 26,000". Wiki 3 zilipita. Jana mama mkwe wangu alisimama peke yake kutoka kwenye kiti. Mama mkwe wangu! Aliyekuwa hajasimama peke yake kwa miezi 8. Ninaandika hii kwa wale wanaoshuku tu — kama mimi.</p>'),

    # comment 9 Pataki Dezső
    ('            <div class="nm">Pataki Dezső</div>\n            <div class="tm">17 órája</div>',
     '            <div class="nm">Mfaume Dezio</div>\n            <div class="tm">Masaa 17 iliyopita</div>'),
    ('<p class="bd">A feleségem már nem tudott lemenni a lépcsőn. A falba kapaszkodott és sírt a fájdalomtól. Azt\n          hittem, elveszítem — nem a betegségtől, hanem a kétségbeeséstől. Megrendeltem a HondroDin-t kedvezménnyel. 4\n          hét után — tegnap egyedül lement a boltba, és virággal jött vissza. Virággal! Hálás vagyok a szívem mélyéből.\n        </p>',
     '<p class="bd">Mke wangu hakuweza tena kushuka ngazi. Alishikamana na ukuta akilia kwa maumivu. Nilidhani nitampoteza — si kwa ugonjwa, bali kwa kukata tamaa. Niliagiza HondroDin kwa punguzo. Wiki 4 baadaye — jana alishuka peke yake hadi dukani, na alirudi na maua. Maua! Nina shukrani kubwa kutoka moyoni.\n        </p>'),

    # comment 10 Juhász Teréz
    ('            <div class="nm">Juhász Teréz</div>\n            <div class="tm">19 órája</div>',
     '            <div class="nm">Jumanne Tereza</div>\n            <div class="tm">Masaa 19 iliyopita</div>'),
    ('<p class="bd">Azon gondolkodom, hogy rendelek az édesapámnak. 3 éve idősotthonban van — a térdei egyáltalán nem\n          működnek. Feladta, alig beszél. Szerintetek 78 évesen segíthet a HondroDin?</p>',
     '<p class="bd">Ninafikiri kuagiza kwa baba yangu. Amekuwa nyumbani kwa wazee kwa miaka 3 — magoti yake hayafanyi kazi kabisa. Amejisalimu, anazungumza kidogo sana. Je, mnaamini HondroDin inaweza kumsaidia akiwa na miaka 78?</p>'),

    # reply Balogh Zsuzsanna
    ('          <div class="nm" style="font-size:.9rem">Balogh Zsuzsanna · 18 órája</div>\n          <p class="bd" style="margin-top:6px">Teréz, az én anyám 82 éves! Súlyos kopás mindkét térdben, nem kelt fel az\n            ágyból. 2 hónapja használja — most magától kimegy az udvarra. Nem túlzok. És a legszebb: amikor\n            meglátogattam, a kapuban várt, a lábán. Mindketten elsírtuk magunkat. Rendeld meg nyugodtan, az édesapád\n            megérdemli az esélyt.</p>',
     '          <div class="nm" style="font-size:.9rem">Bakari Zuwena · Masaa 18 iliyopita</div>\n          <p class="bd" style="margin-top:6px">Tereza, mama yangu ana miaka 82! Uharibifu mkubwa katika magoti yote mawili, hakuondoka kitandani. Amekuwa akitumia kwa miezi 2 — sasa anatoka nje peke yake. Sisizidishi. Na jambo zuri zaidi: nilipomtembelea, alisubiri mlangoni, akiwa amesimama. Wote wawili tulilia. Agiza bila wasiwasi, baba yako anastahili nafasi.</p>'),

    # comment 11 Simon Ildikó
    ('            <div class="nm">Simon Ildikó</div>\n            <div class="tm">22 órája</div>',
     '            <div class="nm">Simoni Ildiko</div>\n            <div class="tm">Masaa 22 iliyopita</div>'),
    ('<p class="bd">4 tubust rendeltem — anyámnak (idősotthon, térd), apámnak (otthon, hát) és 2-t magamnak (kéz,\n          ujjak ízületi gyulladása, már írni sem tudtam). A cikk történetei összetörtek. Már rég meg kellett volna\n          tennem. Nincs több kifogásom.</p>',
     '<p class="bd">Niliagiza bomba 4 — mama yangu (nyumba ya wazee, goti), baba yangu (nyumbani, mgongo) na 2 kwangu (mkono, arthritis ya vidole, sikuweza tena kuandika). Hadithi za makala zilinionya. Nilipaswa kufanya hivi zamani. Sina tena udhuru.</p>'),

    # comment 12 Deák Tibor
    ('            <div class="nm">Deák Tibor</div>\n            <div class="tm">1 napja</div>',
     '            <div class="nm">Daud Tibor</div>\n            <div class="tm">Siku 1 iliyopita</div>'),
    ('<p class="bd">Két hónap után készült ez a kép édesapámról. Már bottal sem jár. Aki kételkedik, nézze meg a saját\n          szemével.</p>',
     '<p class="bd">Picha hii ya baba yangu ilipigwa baada ya miezi miwili. Hata fimbo haitumii tena. Yule anayeshuku, aione kwa macho yake mwenyewe.</p>'),

    # footer — EgészségHír Magyarország is replaced by pair 16 above, so match the remainder
    ('AfyaHabari Tanzania — különleges riport\n      <p class="disc">Az ezen az oldalon bemutatott információk tájékoztató jellegűek, és nem helyettesítik az orvosi\n        konzultációt. A nevek megváltoztathatók a szereplők személyiségi jogainak védelmében. Az eredmények egyénenként\n        eltérhetnek.</p>',
     'AfyaHabari Tanzania — ripoti maalum\n      <p class="disc">Taarifa zilizotolewa kwenye ukurasa huu ni za kuelimisha tu, na hazibadilishi ushauri wa daktari. Majina yanaweza kubadilishwa ili kulinda haki za watu wanaohusika. Matokeo yanaweza kutofautiana kwa kila mtu.</p>'),

    # JS months array
    ('var months = ["január", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember", "október", "november", "december"];',
     'var months = ["Januari", "Februari", "Machi", "Aprili", "Mei", "Juni", "Julai", "Agosti", "Septemba", "Oktoba", "Novemba", "Desemba"];'),

    # JS date format: "2026. Juni 23." → "23 Juni 2026"
    ('el.textContent = d.getFullYear() + ". " + months[d.getMonth()] + " " + d.getDate() + ".";',
     'el.textContent = d.getDate() + " " + months[d.getMonth()] + " " + d.getFullYear();'),
]

for old, new in r:
    c = c.replace(old, new)

with open('/home/user/claudenewone/landing-example/landing-TZ.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done")
