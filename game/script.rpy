# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define i = Character ('Увядающее Тело', color="#8a8a8a") 
define g = Character ('Гиря', color="#062C06")
define c = Character ('Отцовские часы', color="#AC4C4C") 
define n = Character ('Забвенная Записная книжка', color="#F4FA1C")
define h = Character ('Эпатажная шляпа', color="#A05B1B")
define m = Character ('Менеджер', color="#FF0000")
define a = Character ('Анна', color="#00E5FF") 
define f = Character ('Опустошенный Холодильник', color="#80C8BA")
define p = Character ('Сиплый телефон', color="#D380DA")
define x = Character ('Обреченное тело', color="#8a8a8a")
define y = Character ('Исцелившееся тело', color="#8a8a8a")

#переменные
define hatmad = False
define hat_lost = False
define anna_love = False
define getjob = False




# Игра начинается здесь:
label start:
    scene bg divan
    i "В этом чертовом городе всегда идет дождь?"
    i "Если бы не ты я бы добежал быстрее и не промок."
    show girya
    g "Ты винишь меня во всех своих злоключениях…"
    g "Ничего, я потерплю если тебе так становится проще."
    i "Они не перезвонят, я уже миллион раз видел такой взгляд."
    i "'Да-да, выметайся уже поскорее, еще кучу таких как ты надо отшить, преждем чем можно будет идти домой.'"
    g "Тебе не нужна их поганая работа, надо найти что-то, что позволит тебе запереться дома."
    i "Аргхх, я устал, этот мир поставил мне цуцванг, что не делай, становится хуже, чем вчера."
    g "Всё хорошо, пока мы можем быть здесь в тепле, одни."
    i "Мать сказала, что в этом месяце она отправляет мне деньги последний раз." 
    i "Если не найду работу в ближайшее время, всё пропало, я пропал."
    g "Не верю! Не верю что она тебя просто бросит вот так"
    hide girya
    c "Вы просто жалкие, слушать вас сущее мучение. Твой отец будь рассмеялся бы над тобой."
    c "Только сидишь и скулишь как шавка какая."
    c "Сделай уже что-нибудь, вложись в акции, открой свой бизнес, пройди курсы адвокатуры." 
    c "Столько возможностей проходит мимо, пока ты бесцельно пялешься в потолок."
    i "Ну ты прав, лежать так просто не дело."
    i "Нужно пожевать чего."
    f "Ты правда подумал, что найдешь здесь что-то съедобное?" 
    f "Совсем спятил. Ты используешь меня исключительно в качестве подставки для бутылок последние пару лет." 
    f "Я пустой, вечно пустой! Я уже забыл, какого это иметь внутри еду... о это далекое дивное чувство!"    
    i "Не дребезжи, вон я вижу что-то, так-так давай это сюда!"
    f "Да ты шутишь! Не говори мне, что собираешься это съесть." 
    f "Я даже не помню как оно выглядело и чем являлось раньше до того, как испортиться в первый раз."
    i "Не драматизируй, я всеядный, а это моё все"

    show girya
    g "Мне больно осозновать, но завтра нужно сходить за покупками, только недалеко… и сразу же назад."
    i "Сходить говорит! Да ты хоть представляешь как утомительно волочить тебя по земле каждый раз."     
    i "Раньше ты был не таким тяжелым."
    i "Как мне вообще искать работу с такой обузой."
    i "Ты портишь мне жизнь, ведёшь меня на эшафот, что тебе от вообще нужно, сколько это будет продолжаться."
    g "Какими грубостями ты меня обливаешь, это тебе нужен я, а не наоборот." 
    g "без меня где бы ты был уже? На дне реки или, скорее, бутылки?"
    c "Не слушай его, с самого момента его появления всё идет по низходящему тренду." 
    g "Зачем тебе вообще искать работу. Ты можешь продать часы, они точно стоят кучу денег." 
    g "А дальше… дальше всё само как-нибудь наладится."
    i "Забудь, это подарок отца в честь выпуска, семейная реликвия, считай." 
    i "Он с того свет явится и вытрясет из меня душу за такое."
    c "Хотя бы что-то человеческое в тебе осталось."
    i "Всё замолчите, я хочу спать, спать и не просыпаться."
    
    i "Скажите мне, что прошла уже тысяча лет, и людям больше не нужно работать, и желательно  двигаться."
    g "Это было бы прекрасное будущее"
    i "Во сне было так легко…"
    f "Я не прощу тебя, если ты вернешься с пустыми руками или с пакетом грохочащего стекла."
    n "Ты алчный кусок холодного металла, человек должен думать о сытости духовной, а не как бы набить брюхо."
    i "О, это же мой творческий блокнот, когда-то я всегда носил тебя с собой, записывал свои идеи, стихотворения."
    i "Я думал, что потерял тебя уже лет сто назад."  
    f "Положи его обратно, а лучше закинь подальше."
    f "Он только трепаться и горазд, а нам жратва нужна, ЖРАТВА!"
    i "Всё, иду я иду, "
    "Может быть, если бы ты по ночам не мешал мне спать своим рычанием, я бы чаще к тебе прислушивался."
    c "Не злись так на него, с момента как его собрали, две страны уже рухнуло, а он всё еще пашет."
    h "Хэй, босс. Решил проветриться, это круто. Сегодня довольно солнечно, цепляй меня и погнали."
    i "Ты не подходишь такой развалине, я и храню тебя то как напоминание о своей молодости."
    h "Брехня, ты еще не истлел, стряхни только пыль с меня и полетели/"
    i "Ты видишь, что у меня на ноге? С такой штукой не полетаешь."
    i "Так, лучше скажи, сколько там у меня деньжат осталось?"
    h "Эй, эй я тебе копилка что ли? На то чтобы взорвать разок - точно хватит!"
    i "Деньги взял, телефон взял, ключи…."

    "Внутри меня засело какое-то тревожное чувство, будто я что-то забыл, мне нужно унять его, иначе я не смогу выйти наружу."
    label choise1:
    menu:
    
        "Надеть шляпу":
            h "Hell yeah baby! Давненько мы не отрывались, эта красотка уже вечером будет у наших ног."
            jump hat1
            
        "Взять блокнот": 
            n "Каждый твой выход на улицу - это событие, которое должно быть задокументировано, выдолблено в мраморе…. ну или в бумаге."
            $ anna_love = True
            jump notepad1
            
        "Надеть отцовские часы":
            c "Отлично, купим в магазине поблизости, продадим на рынке с наценкой, затем возьмем в долг еще партию побольше, так пока не выйдем на серьезные масштабы."
            jump clock1
            
label notepad1: 

        g "Мне здесь не нравится, может произойти всё что угодно. Нужно было попросить кого-нибудь принести еды."
        n "Я шел по узким городским улицам столь привычным для прохожих, что они даже не замечают изменений вокруг."
        n "Не замечают меня, растворенного в городском пейзаже." 
        i "Я шел в магазин, запятая, а потом пойду домой, точка."
        n "Важность моей миссии была бесконечна, ибо от неё завесила моя жизнь"
        "...."
        a "Ой, прошу прощения, Вы в порядке."
        a "Ох, неужели это ты?" 
        i "Анна?"
        a "Да, ну точно ты, невероятно. Я думала, ты переехал! Кого не спрашивала, никто не знает, что ты да как."
        g "Ты её знаешь? Такая ухоженная, такая яркая... откуда такому как ты её знать."
        n "Ну конечно знает, у меня даже стихотворение есть:"
        """Ах, Анна, Анна, но как же так случилось,
        Что мысли все мои лишь только о тебе,
        Ах, Анна, Анна, неужто мне приснилось,
        Как…"""
        i "НЕ СМЕЙ ПРОДОЛЖАТЬ, А ТО Я ТЕБЯ ВМЕСТО ТУАЛЕТНОЙ БУМАГИ ИСПОЛЬЗУЮ."
        g "Не отвечай ей, сделай вид, что обозналась."
        a "Тук-тук, здесь есть кто-нибудь?"
        i "Хах, ахахах, прости, просто я поражен тем, как ты изменилась."
        a "И как же?"
        i "Стала еще прекраснее, мне нравится твой новый стиль."
        a "Мммм, ты всё так же мил как и раньше."
        a "Слушай, у меня как раз есть свободное время, я шла выпить кофе, не хочешь со мной?"
        a "Ну… если ты не занят, конечно."
        g "Я ПРОТЕСТУЮ!"
        g "куда, куда, куда…. в незнакомое место… Ты же её не видел уже столько лет, она красотка, а ты на себя посмотри."
        n "Внешне она выглядит иначе, но я уверен, что она всё та же добрая, веселая Анна, которая вытирала салфеткой крем от эклера у тебя со щеки во время обеда и так звонко хихикала при это." 
        i "С радостью, я тут просто прогуливаюсь за покупками."
        '''
        {color=#0EA3C9}"Не так уж много почти окрыленных шагов спустя."
        '''
        a "Так ты живешь где-то неподалеку."
        i  "Да, почти сразу же за углом снимаю студию"
        a "Ух ты, тут такие милые домики, наверное, она очень уютная."
        i "Была, пока в ней не поселился я."
        a "Ты всегда был неряхой тем ещё, хе-хе."
        a "Надо же, столько лет прошло, а ты почти не изменился."
        i "Это получается, что я стою на месте?"
        a "Нет, я не в плохом смысле."
        a "Просто все в моём окружении стали такими душными, постоянно говорят о делах."
        a "Даже время свободное провести не с кем, потому я обычно и хожу сюда одна."
        a "Но рядом с тобой я этого не чувствую, с тобой как и раньше можно поговорить о другом."
        n "Ваша связь с годами не ослабла, она и правда скучает по вашему общению."
        a "Мы тут так заседелись, пора уже идти."
        i "Было приятно встретить тебя после стольких лет."
        a "Ммм, а что это у тебя записная книжка."
        i "Хех, да, тоже со времен университета еще, почитать не дам и посомтреть тоеж!"
        a "Секретики-секретики, хе-хе."
        a "Ну а для моего телефона там место найдется?"
        i "Ну если только где-нибудь с краю."
        n "Половина страниц пустует и желтеет за ненадобностью."
        n "Можешь писать хоть по цифре на страницу!"
        '''
        {color=#0EA3C9}11 неразборчиво выведенных закорючек спустя.
        '''
        g "Ты вообще в меню заглядывал? Мы разорены!"
        a "О, не переживай, я заплачу, всё-таки я тебя пригласила."
        g "Я же говорил, она думает, что ты нищеброд вонючий, решила угостить тебя сладким из жалости."         
        i "Ты же не думаешь, что я сам за себя заплатить не могу…"
        a "Конечно, нет. Но если хочешь вернуть мне должок, придется встретиться еще раз."
        g "Не позволяй ей тобой манипулировать, очевидно, что она хочет от тебя чего-то."
        n "Абсурд не иначе. У тебя нет ничего кроме драгоценного, но поблекшего камня души. Который сиять лишь может будучи другому преподнесённым." 
        a "Пока-пока."
        n "Будь ты чутким и галантным, мог бы проводить её до дома, но какой уж ты есть."
        g "Пускай лучше проводит себя до нашего дома." 
        i "Еще не поздно купить продуктов."
        jump event_job
label hat1:
    
        i "Ладно, ты и правда уже запылился тут."
        h "Ты не пожалеешь, ковбой."
        i "Охлади свой пыл, мы только в магазин и обратно."
        g "Зря ты его взял, поверь мне, опять ввяжешься в историю."

        h "Палящие солнце, ритм мегаполиса, как я соскучился по всему этому."
        h "Столько всего происходит вокруг, может быть, и с нами произойдёт что-то?"
        g "И не надейся, скоро мы уже будем дома, скором будем дома, скоро будем…"
        h "Эй, босс, скажи зачем ты эту тяжеленную штуку с собой таскаешь?"
        i "Как будто я по своей воли это делаю, тебя я могу снять и положить на полку до лучших времен, а это… Это преследует меня повсюду."
        a "Ай, прошу прощения."
        i "Всё в порядке..."
        a "Мммм, неужели это ты!"
        i "Ты... ты ведь Анна?"
        a "Бинго!"
        a "Ах, подожди, это у тебя в руках та самая легендарная шляпа?"
        h "Она самая детка, я знал, что моя слава ещё не померкла."
        g "Отдай ей шляпу как сувенир из прошлого и пойдем, мне тревожно."
        i "Не такая уж и легендарная."
        a "Еще какая! Ты ведь выиграл её в покер у самого декана во время празднования юбилея университета." 
        a "Я думала он скорее съест её, чем тебе отдаст."
        h "Мне этот старый маразматик никогда не нравился, это так к слову."
        h "Лысина его потела чудовищно просто."
        i "А что ты здесь делаешь, кстати говоря?"
        a "Это мои слова, я то тут работаю, а вот ты…"
        a "Столько лет ни слуху ни духу, я думала, ты в родной город решил вернуться."
        h "Какой вернуться, мадам. Ковбой идёт только вперед."
        i "Я еще с этим городом не закончил."
        a "Рада, что твой огонь ещё не погас."
        a "Слушай, у меня как раз есть свободное время, я шла выпить кофе, не хочешь со мной?"
        a "Ну… если ты не занят, конечно."
        g "Я ПРОТЕСТУЮ!"
        g "куда, куда, куда…. в незнакомое место… Ты же её не видел уже столько лет, она красотка, а ты на себя посмотри."
        n "Внешне она выглядит иначе, но я уверен, что она всё та же добрая, веселая Анна, которая вытирала салфеткой крем от эклера у тебя со щеки во время обеда и так звонко хихикала при это." 
        i "С радостью, я тут просто шатаюсь без дела, ищу чем заняться."
        '''
        {color=#0EA3C9}"Не так уж много шагов спустя."
        '''
        
        a "Уютно здесь правда, моё любимое место."
        h "Слишком спокойно, шороху не наведешь."
        a "Так, я пожалуй возьму себе ванильный латте на кокосовом молоке и фирменный чизкейк. Рекомендую, выпечка у них здесь просто класс."
        h "Тебе бы текиллы взять для начала, а не вот это всё."
        a "У меня есть свой стиль, я возьму себе фламбе и двойной эспрессо."
        '''
        {color=#0EA3C9}"Спустя два выпитых кофе."
        '''
        g "Мы влипли, мы так влипли, боюсь даже представить сколько денег ты потратил."
        g "Что ты потом делать будешь?"
        h "Брехня, кто же деньги считает в кафе с такой чумовой цыпой."
        i "Слушай, не хочешь прогуляться?"
        i "Просто выпить кофе мне недостаточно после стольких лет разлуки."
        a "Мой вечер в твоём распоряжении."
        h "Вот это выстрел меткий, достойно."
        g "Катастрофа! Ты что же еще за неё и заплатил? ЕЩЕ И ОФИЦИАНТУ НА ЧАЙ ОСТАВИЛ, СКОЛЬКО ОСТАВИЛ?"
        g "Да ты же нищий! Будешь завтра варить кашу из отвалившейся со стен штукатурки." 
        h "Не сбавляй темпа, амиго. Сегодня она точно станет твоей."
        g "Шумно, здесь так шумно, столько людей, домой, скорее домой!"
        h "Подожди, ни в коем случае, никаких домой. Такой шанс, пригласи её в бар, всё так гладко идет."
        i "Анна, не устала ходить? Ты ведь после работы."
        a "Ммм... предположим устала, а есть предложения?"
        g "Нету, нету у тебя никаких предложений, хотя... Нет есть одно, Можешь предложить ей попращаться!"
        h "Ну чего ждешь, действуй!"
        i "Я не уверен... Я чувствую себя таким уставшим."
        h "За то я полон сил, давай, надевай меня."
        i "Что? Да засмеют же. Я и раньше не без смущения шляпу носил. и вообще, я без понятия зачем тебя с собой взял."
        h "Засмеют? Да я весь город на уши поставлю, а эту красотку посажу тебе на колени."
        h "Такой момент, такая встреча, нужно только еще немного нажать на педаль."
        g "Чтобы оказаться в овраге! Он угробит тебя, столько раз пытался, ты только вспомни, Я прошу тебя, пошли домой, купим еды и пойдем домой, и так столько денег уже потратили, так и правда придется побираться ходить скоро"
        
label choise1_5:
        menu:
          
            "Нацепить шляпу и устроить рок-н-ролл":
                $ hatmad = True
                $ hat_lost = True
                i "Может быть, в этот раз всё пройдет не как обычно."
                i "Детка, сегодня мы идем в бар и напьемся как раньше в хлам, и будет нам весело как Греческим Богам."
                a "Хи-хи, на пару бокалов зайти и правда можно."
                jump event_job
            "Нажать на тормоза":
                i "Нет уж, я знаю куда ведёт этот путь и идти по нему, а точнее ползти я не хочу"
                i "Эм.. да нет, особых предложений нет."
                a "Знаешь что? Может, запишишь мой телефон?" 
                a "Я бы хотела встретиться еще"
                p "Ах, неужели!"
                p "Неужели, я наконец-то смогу вспомнить, какого это звонить другим людям!"
                g "Он звонит иногда маме, а она даём ему деньги, и он живет дальше. Это всегда было более чем достаточно."
                i "Конечно, было бы здорово."
                '''
        {color=#0EA3C9}"Спустя 27 неловких нажатий на кнопки спустя"
                '''
                
                a "Ну тогда спокойной ночи, еще увидимся"
                i "Был рад с тобой повидаться."
                h "ну-ну, был рад повидаться, а если бы послушал меня, мог бы с ней и не только повидаться, но и покувыркаться."
                g "ДОМОЙ, УРА НАКОНЕЦ ДОМОЙ."
                i "Кажется, мне придется научиться жить без еды."
                $ anna_love = True
                jump event_job
            
label event_job:
        '''
        {color=#0EA3C9}"Мгновение спустя"
        '''
        if hatmad:
            i "Аргхххх, голова…" 
            i "Всё-таки прошло как обычно…"
            i "Что же я такого наделал, я же пару бокалов только выпил."
            g "Как удобно тебе, что ты не помнишь, я тоже хотел бы забыть."
            g "Это был сущий кошмар."
            i "Рассказывай, давай."
            g "Уверен? Это может оказаться болезненным, не хочу ранить тебя."
            i "Одна боль, другая... и так башка гудит, давай уже, коли!"
            g "Ну… ты напялил это гнездо на голову и понеслось…."
            g "Поначалу всё шло неплохо, вы с Анной болтали как в старые времена."
            g "Между вами даже была какая-то химия."
            g "Вы уже почти поцеловались, но твой разум не смог вынести этой демонической энергии."
            g "Сначала ты попытался её облапать, потом полез в драку на бармена, а затем и вовсе заблевал всё вокруг."
            i "Мда... она точно не это имела в виду, когда говорила, что хочет потусоваться как в былые времена."
            g "По крайней мере ты добрался домой, я думал, ты собираешься спать под лавкой."
            i "...."
            p "Сэр, прошу прощения, но у Вас есть одно новое сообщение, я посчитал, что оно достаточно важное."
            g "Не читай, вдруг это тебя ищут после вчерашнего, хотят расквитаться."
            i "Ну говори, что там написано?"
            p "Кхе-кхе, судя по всему, это приглашение на собеседование от крупной компании на должность, которую Вы так хотели получить всё это время."
            p "Написано, что к ним в отдел кадров попало Ваше резюме, и они очень заинтересованы." 
            i "Шутишь!?"
            i "Ко-когда, когда собеседование."
            p "Сегодня, сэр."
            i "СЕЕЕЕЕГОДНЯЯ???"
            i "ЧТОООО ЗНААААЧИИИИИИИТ СЕГООООООДНЯ???"
            i "ВО СКОЛЬКО?"
            p "Через сорок минут, сэр."
            i "ТО ЕСТЬ ПРЯМО, МАТЬ ТВОЮ, СЕЙЧАС!!!" 
            i "КАКОГО ЧЕРТА! Ты бесполезный кирпич, мог бы разбудить меня пораньше."
            p "Я делал всё что было в моих силах! Но Вы же знаете, голос у меня уже не тот что раньше."
            p "А Вы вдобавок были так мертвецки пьяны."
            i "Сраная шляпа, опять за старое, чего молчишь? Это твоих полей дело."
            f "Да забудь про шляпу, главное ты опять без ЖРАТВЫ вернулся."
            c "И без денег. Это предприятие стремительно идёт к финансовому коллапсу."
            f "Сведёшь так себя в могилу, а новый хозяин точно выкинет меня на свалку."
            i "Так, время... Сколько времени мне нужно чтобы добраться до туда?"
            g "Ты ведь не всерьез да? У тебя ноги трясутся словно холодец, а выглядишь ну прямо матёрый бомж, тебя и в офис то не пустят."
            c "Не вздумай слушать эту черную кляксу, возможность сгорит в любом случае, а если попытаешься, то хотя бы совесть твоя будет чиста."
            g "И опять выставишь себя на посмешище, ты и в лучшей форме ничего не добился, а сейчас на что рассчитывать?"   
            i "Он прав, Гиря. Я сам себя до такого состояния довел, поэтому если облажаюсь, то хотя бы и винить кроме себя будет некого." 
            n "История о превозмогании, о силе воли. У меня тут кое-что записано:"
            n "Можно кинуть камень в волка, но не волка в камень!"
            n "Простите, это не то…"
            n "Успех - это способность терпеть поражение за поражением, не теряя энтузиазма."
            c "Жаль только, что не ты это придумал."
            i "Так, я почти собрался, носки.... Где носки, ладно и без них нормально."
            i "Всё, нужно лететь... Бежать... Прыгать... ползти, что угодно но успеть." 
        else: 
            '''
            {color=#0EA3C9}Несколько тревожных снов спустя.
            '''
            i "Снова проснулся один в своей одиночной квартире." 
            p "Сэр, прошу прощения, но у Вас есть одно новое сообщение, я посчитал, что оно достаточно важное."
            g "Не читай, вдруг это опять те цыгане или мошенники."
            i "Вот уж нашли, на кого время тратить."
            i "Ну говори, что там написано?"
            p "Кхе-кхе, судя по всему, это приглашение на собеседование от крупной компании на должность, которую Вы так хотели получить всё это время."
            p "Написано, что к ним в отдел кадров попало Ваше резюме, и они очень заинтересованы." 
            i "Шутишь!?"
            i "Ко-когда, когда собеседование."
            p "Сегодня, сэр."
            i "СЕЕЕЕЕГОДНЯЯ???"
            i "ВО СКОЛЬКО?"
            p "Через два часа, сэр."
            i "Фух, время есть чтобы привезти себя в порядок."
            c "Вселенная даёт тебе шанс, не упусти его."
            g "Вселенная в очередной раз насмехается, выманивает тебя как крота в игровом автомате, чтобы дать молотком по голове."
            n "Тот, кто зарывает голову в песок не видит страданий, но и счастья не видит тоже." 
            i "Ладно, я готов к новой схватке."
            jump choise22

label choise22:
    "На самом деле сердце буквально выпрыгивает из груди, нужно взять что-то в качестве талисмана" 
    menu:
        "Часы":
            c "Хо-хо, наконец-то я вижу перед собой мужчину."
            i "Я всегда это отрицал, но в этот раз не помешает взять немного папиной удачи с собой."
            $ getjob = True
            jump Clock2

        "Записная книжка":
            i "Мне не стоило забывать о тебе, я думал все мои неудачи, из-за этой творческой меланхоличности."
            i "Но без этого от меня осталось ещё меньше." 
            n "Не сомневаюсь, ты поразишь их высотой полета своей мысли."
            n "И ты напишешь наконец в своей жизни счастливую главу."
            if hatmad:
                $ getjob = False
            else: 
                $ getjob = True
            jump notepad2

        "Шляпа":
            if hat_lost:
                i "Хмм... а куда я вчера шляпу закинул?"
                f "Когда ты приполз домой, ты был с непокрытой головой." 
                g "Ты её оставил в баре, разумеется. И это к лучшему однозначно."
                i "Да жалко как-то, может, вернуться как-нибудь забрать."
                g "Не вздумай показываться там снова, тем более ты под конец использовал её вместо пакета для блевотины."
                i "Значит... Это конец наших отношений, прощай"
                jump choise22
            else:
                h "Эти вонючие офисные крысы в кой-то веки взбодрятся, едва завидят тебя!" 
                i "Нет уж, я хочу увеличить свои шансы, а не умножить на ноль."  
                jump choise22

label Clock2:
#sound of clock tic-tac fast
    play sound "audio/tick-tock.ogg"
#highpitch sound in the head
    play sound "audio/high_pitch.ogg"
#tense music
    c "Осталось 15 минут, нужно торопиться."
    i  "Невозможно, с этой хреновиной невыносимо бежать."
    g "Снова я виноват, не нужно было вчера ужираться, пошел бы домой, сейчас было бы всё иначе." 
    g "А если мы опоздаем? Тогда лучше не приходить вообще."
    c "Нытьё отставить, назад пути нет, ты будешь прорываться даже через закрытые двери."
    i "уф, хах, не могу больше бежать, нужно отдышаться."
    c "Каждая секунда, потраченная бездеятельно - это еще один шаг к дефолту." 
    i "Аргхх, если умру от остановки сердца, надеюсь, тебя закопают со мной."
    '''
    {color=#0EA3C9}"Двадцать триллионов шагов спустя"
    '''

    c "Молодец, ты добрался."
    c "Теперь, позволь мне разобраться с этим."
    i "А ты сможешь?"
    c "Ты сколько собеседований уже провалил? Доверься мне."
    i "Ты прав, хуже точно не будет."
    m "Следующий кандидат, входите!"
    g "Такой низкий тяжелый голос, как раскат грома."
    g "Он раздавит тебя, расплющит колоссальным пальцем саму твою суть."
    i "Одним провалом больше, одним меньше. Я уже привык, так что я иду."
    g "........"
    i "У тебя ведь всё равно нет выбора, раз уж ты прицепился."
    m "У меня не так много времени, быстрее, пожалуйста!"
    g "Ты только вглядись, он же сторониться тебя, твоего мерзотного запаха, твоей жалкой натуры."
    "СПУСТЯ 26 ТЫСЯЧ ВОПРОСОВ ИНТЕРВЬЮЕРА."
    c "Я же говорил, что всё пройдет как надо."
    i "Он же еще не сказал, что меня взяли."
    c "Это уже решенный вопрос, ты же заметил, КАК он это сказал?"
    c "Не это дежурное: 'Мы свяжемся с Вами', которое слышит каждый неудачник."
    c "Нет, это было: 'Мы В СКОРОМ ВРЕМЕНИ свяжемся с вами.'"
    i "Разница и правда есть."
    i "Теперь можно со спокойной душой возвращаться домой."
    c "Отдыхай, пока можешь, скорее в твоей жизни появится столько всего, что уже не продохнешь."
    g "Это ведь просто ужасно, столько стресса, как ты это выдержишь." 
    i "Это уже будет другая история."
    jump ending
    
label notepad2:
        if hatmad:
            n "Твоя голова идёт круг, пытаясь найти выход из болезненного лабиринта."
            n "Но неважно сколько усилий ты прилагаешь, всё тщетно."
            n "Ты и головная боль - одно отвратительное целое."
            g "Вот именно, и так всё очень плохо, так ты еще поперся на галгофу."  
            n "Ты полон ненависти к себе, хочешь разорвать себя на куски и бросить псам."
            n "Поэтому ты идешь туда, где от тебя не оставят и кусочка."
            i "Да... Иду прямо в пасть к этим корпоротивным ублюдкам."
            i "Чтобы они еще раз вытерли об меня ноги, что я не закончил университет."
            i "Что я без опыта работы, что без связей."
            g "Хватит, это так страшно, пойдем назад, немедленно пойдем назад!"
            n "Назад идти было уже поздно, ведь на тебя уже упал взор Черной Башни."
            i "Чтож, это не займет много времени, я либо разорву их от ярости, либо паду к ногам от отчаяния."
            jump ending
        
        else:
    
            $ getjob = True
            n "Ты идешь по улице, не замечая прохожих."
            n "Ты пробуешь на вкус, какого это быть в делах, спешить куда-то."
            n "Ты должен прийти на собеседование будучи таким же как они."
            n "Дыши их воздухом, смотри их глазами, чувствуй их сердцами."
            g "Я чувствую тревогу, ты не готов ни разу к собеседованию, просто взял и пошел."
            i "А что, я уже в поисках работы будто на самой работе."
            g "Не ври, я знаю, что ты боишься, что ты трясешься внутри."
            i "И всё равно иду, и всё равно приду."
            n "Стеклянное здание возвышается надо мной, у его подножия я чувствую свою незначительность."
            n "Я трепещу перед людьми, что взирают на меня из глазниц этого гиганта."
            n "Трепещу и втайне желаю однажды так же смотреть свысока на других."
            g "Он прав, как ты будешь заходить внутрь? Ты же совершенно не похож на них, они прогонят тебя, или того хуже - сожрут!"
            i "Пускай подавятся тогда моим гнилым мясом"
        jump ending


label clock1:

g "Мне здесь не нравится, может произойти, всё что угодно. Нужно было попросить кого-нибудь принести еды."
a "АУЧ"
a "Ой, прошу прощения, Вы в порядке."
a "Ах, неужели это ты?" 
i "Анна?"
a "Да, ну точно ты, невероятно. Я думала, ты переехал! Кого не спрашивала, никто не знает, что ты да как." 
g "Ты её знаешь? Такая ухоженная, такая яркая... откуда такому как ты её знать."
c "Они учились с этой девушкой в университете, она из богатой влиятельной семьи." 
g "Не отвечай ей, сделай вид, что обозналась."
a "Тук-тук, здесь есть кто-нибудь?"
i "Хах, ахахах, прости, просто я поражен тем, как ты изменилась."
a "И как же?"
i "Выгялидшь дорого, отличное сочетание денег и стиля."
a "Правда? Мне казалось, что я одеваюсь достаточно скромно."
c "Скромно как же, да каждое её движение кричит: 'Смотрите у меня куча ДЕНЕГ!'"
c "А вот у тебя всё прямо наоборот." 
a "Слушай, у меня как раз есть свободное время, я шла выпить кофе, не хочешь со мной?"
a "Ну… если ты не занят, конечно."
g "Я ПРОТЕСТУЮ!"
g "куда, куда, куда…. в незнакомое место… Ты же её не видел уже столько лет, она красотка, а ты на себя посмотри."
c "Я бы честно предпочел, чтобы ты занялся более продуктивными делами, но иметь статную женщину всегда было престижно, её связи также могут иметь ценность в дальнейшем."
c "так что я помогу тебе составить заманчивое коммерческое предложение."
i "Вообще-то я тут по делам, но на тебя могу уделить часок."

'''
{color=#0EA3C9}"Не так уж много шагов спустя."
'''

a "Так ты живешь где-то неподалеку."
i  "Да, почти сразу же за углом у меня апартаменты."
a "Ух ты, тут такие милые домики, наверное, она очень уютная."
i "Настоящий дворец, не хватает только королевы."
a "Вот как. Я очень рада, что у тебя дела идут хорошо."
a "А то ходили разные слухи… ну знаешь как это бывает."
c "Разузнай у неё побольше, информация самое ценное на рынке."
g "Иди скорее домой, здесь страшно, она видит тебя насквозь, видит какой ты неудачник на самом деле." 
i "Что именно говорят? Ты же не веришь во всякие глупости, я надеюсь."
a "Ты знаешь, мне никогда не было это интересно, просто слышала некоторое, то тут, то там."
c "Как же, её семья информационные магнаты, они знают всё обо всех, тебе нужно завладеть этой информацией и превратить её в золото!"
i "Ты же всегда была в центре внимания, наверняка тебе есть что рассказать."
i "После учебы у тебя точно карьера пошла в гору, работаешь в одном из этих роскошных офисах в кабинете на семидесятом этаже с панорамными окнами?" 
a "Ну… даже не знаю, мой кабинет не такой большой, а здание не такое высокое..."
c "Точно работает, корпоративная этика." 
i "..."
a "..."
g "Чувствуешь неловкое молчание? Это она думает, зачем она вообще тебя позвала куда-то, такого червяка."
a "Эм... подождешь меня минутку? Я отойду ненадолго"
i "Конечно, я пока позвоню своему партнеру по бизнесу, не торопись."
g "Отлично, пока её нет надо валить, пока она не начала над тобой смеятся, пока все не начали."
c "Нельзя уходить посреди переговоров."
i "Зря я пришел сюда, глупо делать вид, что всё как раньше. Между нами пропасть, социальная пропасть."
c "Хм, я тоже почувствовал, не хочется признавать, но, вряд ли, ты чего-то добьешься здесь. Никто в здравом уме не станет вкладываться в такой ушербный проект."
g "Эти дурацкие часы впервые говорят что-то верное, пойдем скорее."
c "Если ты уходишь, то сохрани свой капитал, будем считать это небольшой финансовой аферой."
c "В результате которой, тебе достанется бесплатный кофе с эклером."
g "БЫСТРЕЕ ИДИ ДОМОЙ, ПОКА ОНА НЕ ВЕРНУЛАСЬ!" 
i "Не могу поверить, что я действительно это делаю."
i "Но для неё это и правда должны быть копейки."
i "Прощай Анна, живи дальше в своём дворце, лучше бы ты просто прошла мимо."   
g "Только не оборачивайся, вдруг она заметила, будет так стыдно."   
'''
{color=#0EA3C9}"Семь наполненных стыдом минут спустя."
'''     
i "Насколько же низко я опустился, за каких-то пять лет?"
c "Не вижу трагедии, ты остался в профите от этой встречи. Почувствовал запах нормальной жизни, побывал в кой-то веке в приличном месте, а твой баланс остался нетронутым."
i "Больше никогда не появлюсь на этом проспекте, чтобы не встретиться с ней случайно."
i "Если бы не папаня, то мы бы могли каждый день обедать вместе в люксовых заведениях."
c "Твой отец был хорошим человеком и гениальным бизнесменом, он дал своей семье всё."  
i "Только вот бизнес его прогорел, а мы с мамой остались банкротами с кучей долгов."
i "Ладно бы это, но он еще и помереть через полгода умудрился, так и не проплатив до конца за моё обучение, куда сам же и отправил."
i "И вот теперь где я оказался, сбегаю из кафе, чтобы не отдавать свои последние копейки и не умереть с голоду"
c "Не смей винить в этом своего отца! Он высылал тебе столько денег все эти годы, что на них уже целое состояние можно было сколотить. Но ты всё спускал в трубу."
c "А эта девушка? Она предлагала попросить за тебя свою семью, чтобы оплатить твой последний год учебы, но ты отказался." 
c "И это было бы достойным поступком, если бы у тебя был какой-то план, но твой план это оказаться в глубоком дерьме с еще более глубокодерьмовыми перспективами."
i "Я хотел, чтобы они видели во мне равного. Тогда я поступил так, как мой отец хотел бы чтобы я поступил."  
c "И он бы восстал как феникс, а ты просто бледная тень! И вместо унизительных десяти минут тогда, ты выбрал десять тысяч сейчас."
g "Не говори так, он живет спокойную и безопасною жизнь, это является главной ценностью, а не твои отравляющие грёзы."
g "Какой смысл воротить прошлое, от него нужно держаться подальше."
jump event_job

label ending:
    '''
    {color=#0EA3C9}"Две недели спустя"
    '''
    if anna_love:
        "В комнате больше никиго не было"
        "Один за одним голоса замолчали" 
        jump goodending1
    else: 
        "В комнате больше никиго не было."
        "Один за одним голоса замолчали." 
        "Нет, кто-то в ней всё же был."
        i "В последнее время я слышу только тебя."
        g "Я не оставлю тебя одного, покуда ты во мне нуждаешься"
        g "Каким бы жалким, слабым ты себя не считал, я люблю тебя."
        i "Я знаю... Я знаю. С самого начала это был я, кто прицепил гирю к своей ноге."
        i "Чтобы иметь оправдание, чтобы не испытывать больше боли."
        i "Спрятаться от всего на самом дне."
        jump normalend
    
     
label goodending1:
    "Я всё еще привыкал, что дома было так светло."
    "Всё потому, что я помыл окна, выкинул старые затхлые шторы, и свету больше ничего не препятствовало."
    "Ему больше не препятствовало моё желание жить во мраке."
    "Стук в дверь"
    "Внезапный звук не пугает меня, наоборот я его предвкушал"
    "Уверенно дергаю ручку, по ту сторону ожидаемо оказывается блистательная девушка."
    i "Я как раз варю нам кофе, заходи."
    a "Вау, с каких пор ты не лежишь еще в трусах в это время?"
    i "Примерно со вчера, если тебя интересует точно время."
    a "Пахнет здорово, ты ведь раньше часто варил кофе, когда мы компанией выбиралсь в загородний дом моих родителей."
    i "Да, но я делаю это только для кого-то. Ради себя мне стоять у плиты сторожить его слишком лениво."
    a "Знаешь, я люблю тебя."
    a "Знаю, это немного внезапно... мы не так давно снова начали общаться, но когда ты рядом всё совсем по-другому."
    a "Я не могу перестать улыбаться как полня дура!"
    i "Я тоже тебя люблю, если бы ты видела, что я из себя представлял пока не встретил тебю, что творилось у меня в голове - ты бы ужаснулась."
    
    
    if getjob:
        y "Знаешь, я последние пять лет ходил с огромной гирей на ноге."
        y "И только вчера когда я проснулся её не было рядом."
        y "Сколько бы я не искал, она исчезла."
        y "Исчезла навсегда."
        y "Пей свой кофе и поедем на работу, это ты вся такая важная можешь позволить себе хоть в полдень заявиться."
        y "А я не хочу начать свою карьеру с такого аккорда."
        a "Ого, ты всё же действительно повзрослел."
        a "Значит я всё-таки не откопала артефакт из прошлого."
        
        y "Я так долго просто сидел и сжег спички, пока бежали дни."
        y "Но для меня наконец наступил завтрашний день."
    else:
        y "Знаешь, я последние пять лет ходил с огромной гирей на ноге."
        y "Она и сейчас где-то прячется, ждёт когда я снова буду в ней нуждаться."
        y "Но надже если такой день настанет, я больше не буду просто прятаться за ней от мира."
        y "Я буду волочить её за собой даже в самую крутую гору."
        a "Красиво сказано, а теперь давай собирайся уже."
        a "Я подброшу тебя, у тебя же собеседование в здании напротив моего офиса?"
        "Точно, снова собеседование, снова отказы."
        "Но с каждым разом я всё ближе к цели." 
        "Я больше не боюсь."

return
        
        
label normalend:
    if getjob:
        i "Но теперь всё не так очевидно, мне одиноко, но я больше не презираю себя."
        i "У меня появилась хорошая работа, и я с ней справляюсь."
        g "Но тебе тяжело, ты всё еще с опаской позволяешь себе мечтать о чем-то."
        g "Ты слишком привык сидеть в болоте, ведь здесь спокойно, тихо."
        i "Однажды ты мне больше будешь не нужен."
        g "Или однажды только я у тебя и останусь." 
        i "Пора идти, служебная машина уже приехала."
        i "Мне больше не тяжело, я буду волочить тебя за собой даже в самую крутую гору."
    else:
        g "Это конец."
        i "Это конец."
        g "Я больше никогда не хочу выходить из этой комнаты."
        i "Я больше никогда не хочу выходить из этой комнаты."
        
        x "Я клянусь, что остаток своих дней проведу в самом темном углу."
        x "Где свет не сможет больше обжечь меня."
        x "Где... Не будет... Меня."
     
return

