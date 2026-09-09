# -*- coding: utf-8 -*-
# 20 хуков к лендингу PLzhele.html (Arthrovia, PL, суставы, «sztuczka z żelatyną»).
# Поля: (группа, заголовок, RU, PL, на что лендинга передаёт, что должен сделать первый экран)

H = [
# ================= A. Желатин как абсурд =================
("A", "Холодец каждую неделю",
 "Свекровь варит холодец каждую неделю с самого января. Праздников за это время не было ни одного, а ест она его сама, по полтарелки, каждый вечер.",
 "Teściowa od stycznia gotuje galaretę co tydzień. Żadnego święta w tym czasie nie było, a zjada ją sama, po pół talerza, każdego wieczoru.",
 "Заголовок «Sztuczka z żelatyną» + блок «zwykła żelatyna ze sklepu to po prostu białko»",
 "Читатель приходит с вопросом «зачем ей столько холодца» и на первом экране получает: она делала правильную вещь неправильным способом."),

("A", "Десять пачек",
 "Отец покупает в магазине желатин пачками, по десять штук за раз. Кассирша спросила, не пекарня ли у него, и он ответил ей, что почти.",
 "Ojciec kupuje w sklepie żelatynę paczkami po dziesięć sztuk. Kasjerka zapytała, czy ma piekarnię, a on odpowiedział, że prawie.",
 "Тот же блок: «w Biedronce czy Auchan nie znajdziesz tych składników w terapeutycznych stężeniach»",
 "Первый экран обязан объяснить, почему десять пачек из магазина не заменяют одну правильную пропорцию."),

("A", "Желе на ужин",
 "Я застала мать у открытого холодильника: она ела желе ложкой прямо из чашки, стоя. Ей шестьдесят четыре, и она сказала мне, что это ужин.",
 "Zastałam mamę przy otwartej lodówce: jadła galaretkę łyżeczką prosto z kubka, na stojąco. Ma sześćdziesiąt cztery lata i powiedziała, że to kolacja.",
 "Раздел про желатин + возрастная отсечка «po 50. roku życia»",
 "Снять с матери вид чудачки: она не сходит с ума, она угадала направление и промахнулась в форме."),

("A", "Рецепт без лекарств",
 "Ортопед выписал ей на листке рецепт, в котором не было ни одного лекарства. Три слова, и все три продаются в обычном продуктовом магазине.",
 "Ortopeda wypisał jej na kartce receptę, w której nie było ani jednego leku. Trzy słowa, i wszystkie trzy można kupić w spożywczym.",
 "«żelatyna, imbir i kurkuma w precyzyjnych proporcjach» — три компонента названы прямо",
 "Назвать три слова сразу. Хук обещает список — статья обязана его отдать в первых абзацах."),

("A", "Один телефонный звонок",
 "«Я забыла о боли в суставах. Благодаря желатину.» Так начался тот телефонный разговор, после которого она отменила себе операцию.",
 "„Zapomniałam o bólu stawów. Dzięki galaretce.” Tak zaczęła się rozmowa telefoniczna, po której odwołała sobie zaplanowaną operację.",
 "Сцена звонка в блоке Агаты + «Pomyślałam, że żartuje»",
 "Читателя встречает та же реакция, что была у героини: «она шутит». Совпадение реакций — это доверие."),

# ================= B. Три метода и деньги =================
("B", "Сто тридцать тысяч",
 "Сто тридцать тысяч злотых, три врача и семь лет. А по утрам она по-прежнему сидит на краю кровати и ждёт, прежде чем встать на ноги.",
 "Sto trzydzieści tysięcy złotych, trzech lekarzy, siedem lat. A rano nadal siada na brzegu łóżka i czeka, zanim wstanie na nogi.",
 "Заголовок раздела «Wydałam 130 000 zł na 3 lekarzy» + разбивка 40 000 / 40 zabiegów / 90 000",
 "Разбить сумму на три чека сразу. Цифра без разбивки читается как выдумка, с разбивкой — как чужая бухгалтерия."),

("B", "Полгода и три недели",
 "Укол за три тысячи держит полгода. Потом за три недели всё возвращается, и колено оказывается в худшем состоянии, чем до этого укола.",
 "Zastrzyk za trzy tysiące działa pół roku. Potem w trzy tygodnie wszystko wraca, a kolano jest w gorszym stanie niż przed zastrzykiem.",
 "«Metoda 3: Zastrzyki» + «to nie leczenie — to abonament na zależność»",
 "Объяснить механизм отскока: укол не учит организм, он замещает. Это единственное, чего читатель раньше не слышал."),

("B", "Приходите через полгода",
 "Врач сказал ей: «Принимайте и приходите через полгода». Она принимала четыре года и приходила к нему за это время ровно восемь раз.",
 "Lekarz powiedział jej: „Proszę brać i przyjść za pół roku”. Brała cztery lata i przychodziła do niego przez ten czas osiem razy.",
 "«ludzie przychodzą do mnie po latach bezskutecznego leczenia» — прямая речь Гавела",
 "Восемь визитов — это не невезение, это схема. Показать, что схема одинаковая у всех, кто это читает."),

("B", "Блистер в сумке",
 "Мать носит блистер в сумке и по дороге считает, сколько таблеток у неё осталось до воскресенья. Считает она вслух, сама с собой.",
 "Mama nosi blister w torebce i po drodze liczy, ile tabletek zostało jej do niedzieli. Liczy na głos, sama do siebie, idąc ulicą.",
 "«Metoda 1: Tabletki» + метафора с пожарной сигнализацией",
 "Перевести стрелку с зависимости на разрушение: пока она считает таблетки, сустав разрушается именно потому, что не болит."),

# ================= C. Кадмий и снятие вины =================
("C", "Ни одного пропуска",
 "За четыре года она не пропустила ни одного назначения. Делала ровно то, что ей говорили, и с каждым годом ей становилось только хуже.",
 "Przez cztery lata nie opuściła ani jednego zalecenia. Robiła dokładnie to, co jej kazali, i z każdym rokiem było jej tylko gorzej.",
 "«Wszystkie te metody walczą z objawem. Żadna nie dotyka przyczyny»",
 "Снять вину в первых же строках. Это самый сильный ход лендинга, и хук обязан отдавать его немедленно."),

("C", "9,7 раза",
 "Есть вещество, из-за которого хрящ разрушается в девять и семь десятых раза быстрее. Оно попадает в вас с едой и с водой ежедневно.",
 "Jest substancja, przez którą chrząstka niszczy się 9,7 raza szybciej. Trafia do Was z jedzeniem i wodą, każdego dnia, przez lata.",
 "Блок с исследованием Annals of the Rheumatic Diseases + разбор хлорида кадмия",
 "Назвать вещество и источник. Хук выдаёт цифру, статья обязана выдать имя — иначе обещание не закрыто."),

("C", "Батарейка из сигнализации",
 "Обезболивающее — это как вынуть батарейку из пожарной сигнализации. Тихо, спокойно, никто не кричит, а огонь при этом горит дальше.",
 "Tabletka przeciwbólowa to jak wyjęcie baterii z czujnika dymu. Cicho, spokojnie, nikt już nie krzyczy — a ogień nadal się pali.",
 "Метафора стоит в лендинге дословно, в разделе «Metoda 1»",
 "Метафора уже узнана — первый экран должен идти дальше неё, к вопросу «что тогда горит»."),

("C", "Труба с дырой",
 "Сустав с этим внутри — это как труба с дырой. Можно лить воду сколько угодно долго, но пока дыра не заделана, она будет вытекать.",
 "Staw z tym w środku to jak rura z dziurą. Możesz lać wodę bez końca, ale dopóki nie załatasz tej dziury, będzie wyciekać. Zawsze.",
 "Метафора из раздела про кадмий, стоит перед блоком с исследованием",
 "Сразу сказать, что такое «это». Метафора без разгадки в первом экране раздражает, а не тянет."),

# ================= D. Отказ аптекам =================
("D", "Полторы тысячи",
 "Аптечные сети предложили ему полторы тысячи злотых за одну упаковку. Он положил трубку и с тех пор ни разу им больше не перезвонил.",
 "Sieci aptek zaproponowały mu tysiąc pięćset złotych za jedno opakowanie. Odłożył słuchawkę i od tamtej pory już nigdy nie oddzwonił.",
 "Раздел «Dlaczego Arthrovia nie ma w aptekach» + цена 147 zł",
 "Дать причину отказа его словами, а не рекламными. Цена должна прозвучать как следствие поступка, а не как акция."),

("D", "Компенсировать потери",
 "«Пан доктор, люди перестанут покупать хондропротекторы и делать уколы. Нам придётся как-то компенсировать себе эти потери.» Так ему сказали.",
 "„Panie doktorze, ludzie przestaną kupować chondroprotektory i robić zastrzyki. Musimy sobie jakoś zrekompensować te nasze straty.” Tak mu powiedziano.",
 "Дословная реплика сети аптек в лендинге",
 "Не комментировать реплику. Она сама себя объясняет, и первый экран должен только назвать, кто это сказал и когда."),

("D", "Между уколом и едой",
 "Двадцать лет он смотрит у себя в кабинете на людей, которые выбирают между уколом и едой. Они приходят к нему с пенсией в кармане.",
 "Od dwudziestu lat patrzy w gabinecie na ludzi, którzy wybierają między zastrzykiem a jedzeniem. Przychodzą z emeryturą w kieszeni.",
 "«Od 20 lat patrzę na ludzi... z emeryturą w kieszeni i bólem w oczach»",
 "Самый мягкий по модерации заход. Первый экран держит эту же интонацию и не переходит на давление."),

# ================= E. Тело-свидетель =================
("E", "Минута молчания",
 "Ортопед смотрел на её снимок и молчал целую минуту. Потом он сказал ей, что операция, к которой её готовили, больше уже не нужна.",
 "Ortopeda patrzył na jej zdjęcie i milczał całą minutę. Potem powiedział, że operacja, do której ją przygotowywano, nie jest już potrzebna.",
 "Цитата пациентки: «Mój ortopeda patrzył na MRI i milczał przez minutę» + комментарий Ewy Woźniak",
 "Отдать сцену целиком и сразу назвать срок: сколько прошло между снимками. Без срока сцена не работает."),

("E", "Посреди коридора",
 "Она дошла до кухни и не подумала о боли. Остановилась посреди коридора и заплакала, потому что поняла, что только что произошло.",
 "Doszła do kuchni i nie pomyślała o bólu. Zatrzymała się pośrodku korytarza i rozpłakała się, bo zrozumiała, co się właśnie stało.",
 "Финал блока Агаты: «Zatrzymałam się pośrodku korytarza i rozpłakałam się»",
 "Не объяснять слёзы. Первый экран должен дать день, на который это случилось, — десятый."),

("E", "Туфли из шкафа",
 "Она достала из шкафа туфли на каблуке, которых не надевала три года. Надела их и прошла в них через комнату и обратно, до самой двери.",
 "Wyjęła z szafy buty na obcasie, których nie zakładała od trzech lat. Włożyła je i przeszła w nich przez cały pokój i z powrotem.",
 "«Wyciągnęłam buty na obcasie, których nie wkładałam od 3 lat» + «Dzień 14»",
 "Три года — это срок болезни, а не срок хранения обуви. Первый экран обязан это перевернуть."),

("E", "Сад через четыре недели",
 "Муж не вставал с кровати, и мы уже говорили про сиделку. Через четыре недели он сам вышел работать в сад, и никто в доме этого не обсуждал.",
 "Mąż nie wstawał z łóżka i rozmawialiśmy już o opiekunce. Po czterech tygodniach sam wyszedł pracować w ogrodzie, i nikt w domu tego nie komentował.",
 "Комментарий Elżbiety Wieczorek под статьёй, почти дословно",
 "Хук взят из комментария — первый экран должен вести к комментариям, а не к формуле. Это другая точка входа."),
]
