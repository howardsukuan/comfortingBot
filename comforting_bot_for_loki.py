#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""
import random
import requests
from account_info import accountInfoDICT
from comfortingREF import EmotionRactionDICT
from comfortingREF import handleSoruceDICT
from comfortingREF import sourceReactionDICT
from comfortingREF import PlainFeelingLIST
from comfortingREF import BadFeelingReactionLIST
from comfortingREF import GoodFeelingReactionLIST
from comfortingREF import PlainReactionLIST
from comfortingREF import OtherReactionLIST

try:
    from intent import Loki_feeling
    from intent import Loki_asking_for_help
    from intent import Loki_complainingSentences
except:
    from .intent import Loki_feeling
    from .intent import Loki_asking_for_help
    from .intent import Loki_complainingSentences


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountInfoDICT["USERNAME"]
LOKI_KEY = accountInfoDICT["LOKI_KEY"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []

        try:
            result = requests.post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": INTENT_FILTER
            })

            if result.status_code == requests.codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # feeling
                if lokiRst.getIntent(index, resultIndex) == "feeling":
                    resultDICT = Loki_feeling.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # asking_for_help
                if lokiRst.getIntent(index, resultIndex) == "asking_for_help":
                    resultDICT = Loki_asking_for_help.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # complainingSentences
                if lokiRst.getIntent(index, resultIndex) == "complainingSentences":
                    resultDICT = Loki_complainingSentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

#1st self defined function: 去除標點
punctuationSTR = "!@#$%^&*()_+<>?:.,;。，！～~"  # add whatever you want
def str_normalization(inputSTR):
    for w in inputSTR:
        if w in punctuationSTR:
            return inputSTR.replace(w, "").strip()
        else:
            return inputSTR
    


##2nd self defined function: check the mood
#EmotionRactionDICT = {"BadMood":["差","不好","很糟糕","badmood","爛","很悶","低潮","好難","難過","低落","空虛","寂寞","黑暗","不太開心","不太妙","很難過"],"GoodMood":["好","不錯","很好","很棒","棒"]}
#PlainFeelingLIST = ["普通","還好","還行","沒什麼特別","一樣","好無聊","跟平常差不多"]

#BadFeelingReactionLIST = ["還好嗎 \n想說說為什麼嗎?",
                          #"還好嗎?\n跟我談談嗎?",
                          #"我都在這,你如果願意談談可以跟我說\n你說,我聽"]
#GoodFeelingReactionLIST = ["好替你開心!! 那你願意跟我分享一下嗎~",
                          #"感覺很棒! 是發生什麼事情嗎~"]
#PlainReactionLIST = ["那想聊的時候再跟我聊聊\n我都在", "好~ 有什麼想分享的事情再說喔!"]
#OtherReactionLIST = ["那要談談嗎?", "那要分享一下嗎?"]
def HandleFeelings(inputSTR):
    inputSTR = str_normalization(inputSTR) 
    resultDICT = runLoki([inputSTR])
    feelingDICT = {"feeling" : ""}
    try:
        feelingSTR = resultDICT["feeling"]
        for e in EmotionRactionDICT.keys():
            if feelingSTR in EmotionRactionDICT[e]:
                feelingDICT["feeling"] = e
    except:
        pass
    try:
        feelingSTR = "不"+resultDICT["neg_feeling"]
        for e in EmotionRactionDICT.keys():
            if feelingSTR in EmotionRactionDICT[e]:
                feelingDICT["feeling"] = e 
    except:
        pass
    if feelingDICT["feeling"] == "" and any (e in inputSTR for e in PlainFeelingLIST):
        feelingDICT["feeling"] = "Plain"
    else:
        feelingDICT["feeling"] = "Other"
    if  feelingDICT["feeling"] == "BadMood":
        return random.choice(BadFeelingReactionLIST )
    elif feelingDICT["feeling"] == "GoodMood":
        return random.choice(GoodFeelingReactionLIST)
    elif feelingDICT["feeling"] == "Plain":
        return random.choice(PlainReactionLIST )
    elif feelingDICT["feeling"] == "Other":
        return random.choice(OtherReactionLIST)

##3rd self defined function: respond to the reason    
#handleSoruceDICT = {"appearance":["下巴","嘴唇","屁股","手","appearance","皮膚","皺紋","肚子","腿","膚色","臉","身高","額頭","髮質","髮際線","鼻子"],
                    #"negMood":["mood","心","很自私"],
                    #"score":["低空","分數","score"],
                    #"work":["工作","work","會議"],
                    #"schoolwork":["作業","作品","schoolwork"],
                    #"colleagueRelation":["做事","同事"],
                    #"colleagueLEI":["colleagueLEI"],
                    #"weather":["天氣","weather"],
                    #"family": ["爸爸","媽媽","父親","母親","老公","老婆","親戚們"],
                    #"money":["存款","錢"],
                    #"death":["death"],
                    #"sick":["sick",],
                    #"self":["我"],
                    #"stranger":["人","stranger"],
                    #"food":["food","食物"],
                    #"nothing":["nothing"],
                    #"relationship": ["男友","男朋友","女朋友","女友","另一半","伴侶","閃光","relationship"],
                    #"receipt":["發票"],
                    #"ticket":["票"],
                    #"teacher":["老師","教授"],
                    #"boss":["老闆","boss","主管"],
                    #"thesis":["論文"],
                    #"sthbroken":["broken"],
                    #"school":["schoolLesson"],
                    #"shop":["店"],
                    #"toilet":["toilet"],
                    #"future":["未來"],
                    #"suicide":["suicide"],
                    #"sexualHarassment":["sexualHarassment"],
                    #"hunger":["hunger"],
                    #"motivation":["力氣","動力"],
                    #"noFriend":["朋友"],
                    #"listen":["listen"],
                    #"exchange":["exchange"],
                    #"test":["test"],
                    #"bully":["bully"],
                    #"afraid":["afraid"],
                    #"missOpportunity":["missOpportunity"],
                    #"end":["end"],
                    #"nightmare":["nightmare","惡夢"],
                    #"complainToYou":["complain","抱怨","牢騷"],
                    #"competition":["competition"],
                    #"cheerup":["cheerup"],
                    #"notOpen":["notOpen"],
                    #"misunderstood":["misunderstood"],
                    #"notDone":["notDone"],
                    #"boringWork":["boringWork"],
                    #"stepInPoop":["stepInPoop"]
                    #}
#sourceReactionDICT = {"appearance":["大家對外表可能會有一定的要求,但是重點還是在你身上,如果你喜歡這樣的自己,那又何嘗不可?"," 外表只是一時的，只要健康就好","美醜其實都是自己定義的！所以抬頭挺胸，做自信的自己！我相信你可以！","比起皮囊，我更喜歡那裡頭的靈魂。", "不論身心靈各方面，多愛自己一點是基本呀!!!"],
                    #"negMood":["雖說自己的努力不用別人去定義，但現在這個受委屈的心情是真實的，我懂你的不舒服，但現在的繼續努力，未來我相信一定會成為支持你的力量", "遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","你會練習跟自己相處，聽到自己內心的聲音。","我不會叫你加油，因為我知道你已經很努力了。"],
                    #"score":[" 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分", "如果你已經盡力了，那就不愧對自己了。","等到以後，你會明白分數不是一切，那只是數字海中的其中幾個。"],
                    #"work":["(抱) 辛苦了，想想你原本的目標，覺得不行了也要休息一下","世上最遙遠的距離，不是我和你，而是公司到家裡。","努力工作，也要努力花錢，讓這份精神補償金變成喜歡的形狀。"],
                    #"schoolwork":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"," 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分"," 辛苦了，就算是再喜愛的工作都會有累的時候，不和你說加油，因為你已經夠努力了", "要不要試試看換一個新方法呢?", "人生也有許多沒有正確答案的事，正因為每個人答題方式不同，才會有不同的結果。"],
                    #"colleagueRelation":["真的辛苦你了！看著同事的情況，一定心裡有點不舒服。或許現況不一定很好改變，但是穩紮穩打，未來一定有人可以看的到你的光芒。","真是辛苦了，不被同事理解感覺一定很不好受。只要你現在做事無愧於心，我覺得未來一定會有欣賞你的人出現。","雖然同為工作上的夥伴，但是並不是事事都可以和同事都可以處的這麼好，先暫時緩緩再看看怎麼樣調適心情吧 。"],
                    #"colleagueLEI":["啊!這麼早遇到超級大boss的你打怪辛苦了。"],
                    #"weather":["♪其實我，不是因為好天氣才這麼說，牽著你走過大雨盛開水花的路口，也是我一樣喜歡的夢♪","因為天氣好，因為天氣不好，因為天氣剛剛好，每一天都很美好。","有時我會聽聽雨的聲音，嘈雜中帶點規律，聽著這規律的節拍，心好像也慢慢平靜下來。"],
                    #"family": ["與家人的溝通需要智慧，有時候需要時間來思考下一步，加油加油。","家人和你生活這麼久都不見得很懂你，有話別憋在心裡，試著說出來吧。","和家人的相處其實也會有摩擦，尤其又是和自己最親近的人，遇到這樣的事情真的很不舒服！先休息一下，沉澱一下。","雖然或許家人也有他們的理由，但是其實不管怎麼樣，心裡覺得受傷的事實也不能忽略。謝謝你和我分享這些事情，我們先休息一下，再看看怎麼解決吧~"],
                    #"money":["生活帶走了錢，但是他帶不走你的快樂!!","好巧，我也覺得錢錢沒有夠用的一天呢，它總是離家出走，好淘氣！","雖然錢變成了你喜歡的形狀，但是這是不可逆的魔法，購物前還是先分清楚想要和需要吧。","你聽過財務管理的631法則嗎? 將薪水分成60%生活費、30%儲蓄、10%備用或投資，推薦給你試試看!"],
                    #"death":["想說什麼我都會聽你說，我也會一直陪著你","相信他會以另一種形式好好地繼續陪伴你。","形體消失了，但精神和回憶會一直一直存在在你的心裡。","和熟悉的人告別真的很不容易，謝謝你和我說，如果你想要更多陪伴我都在這裡。"],
                    #"sick":["傾聽身體的聲音，找一天做個健康檢查吧!","有強大的心靈，也要有強壯的身體，沒有什麼比健康更重要了。"],
                    #"self":["發現別人的光芒很容易，但記得也要好好沉澱自己，發現自己的光芒。","人一生相處最久的不是別人，是自己。記得善待自己，別忘了要溫柔，別忘了要快樂。"],
                    #"stranger":[],
                    #"food":["如果你吐出來了！Good Job! 如果沒有，沒關係，這樣不好吃的東西會用另外一種形式排出體外！","吃到可怕的東西的感覺真的很糟啊！我完全可以理解！","天啊！吃到這樣的東西真的有點難過，快快去吃你喜歡的東西來平衡一下！(我推薦水果，我最喜歡吃了~)","就像有人喜歡芋頭，有人不喜歡。不喜歡的就不要勉強自己去接受。"],
                    #"nothing":["生活比海還深，陷溺後便是流沙，你無法徒手拔出流沙裡的人，在拯救溺水者之前，你必須先呼吸。"],
                    #"relationship": ["你一定現在非常難過， 好好給自己一點時間好好休息吧！","會走的人你留不住，該來的人你擋不了，一切都是緣分。","切勿過度怪罪自己，因為在這之中誰都沒有錯，而誰也都有錯。","理智上可以理解，心情上過不去，也是某種成長痛","要好好長大，會有人愛你。願我們都成為逐漸完整的自己。"],
                    #"receipt":[ "換個角度想，你的壞運氣都用在這裡了，接下來都會好運的。","沒關係的，至少你是個監督商家有沒有乖乖繳稅的好公民啊。"],
                    #"ticket":[ "有時候運氣也是實力的一種，下次組一支搶票小隊幫忙吧。","可以問問有沒有人想讓票或換票，但切記不要跟黃牛買喔！"],
                    #"teacher":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！","他們都曾是學生，理當能理解這時期的困惑與躊躇。"],
                    #"boss":["先給你一個擁抱(抱)，真的辛苦你了，現在先好好從工作中休息再看看下一步怎麼做吧！","工作很累吧！先好好休息一下，聽個音樂，再重新出發。","如果是沒來由地指責，那就不要太往心裡去，因為那不是你的錯。"],
                    #"thesis":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！","每個人都有自己的路和步調，沒有所謂最正確或最快速，只有最適合自己的那種。"],
                    #"sthbroken":["舊的不去，新的不來，雖然和舊的物品說在件很難過，但是也會迎接新的夥伴啊！"],
                    #"school":["枯燥乏味之事存在的意義有兩個，一個是凸顯其他有趣的事，另一個是讓你從重複中變成大師。","學校不是唯一可以學習的地方，試著自學一些東西，你會發現其中的樂趣。","學校有時候可能會帶給你一些不開心的心情，辛苦了，先轉換心情，釐清一下自己喜歡什麼吧～～"],
                    #"shop":["或許現在不是一個好的時機啊！等時機對了，機會就會來臨"],
                    #"toilet":["還好嗎，要不要去一趟廁所?" ],
                    #"future":["人對未知都是恐懼的，練習正視自己的恐懼，慢慢來就好。","我記得有人這樣說過: 「未來早已發生，只是在現在這個當下，它們只是尚未集結的片段。」","如果未來很遠的話，那要不要試試看專注做好當下的每一件事情。","很多時候會覺得未來很難捉摸，因為都還沒有發生，也不確定會發生什麼，這個時候不妨好好感受和把握當下，然後遇到喜歡的事情就記錄起來。或許這些喜歡的小東西集結起來就可以成為未來規畫的靈感。"],
                    #"suicide":["想聊聊嗎？要不要打給張老師 1980","你會願意和我聊聊嗎? 那怕是一點點也好，或許我能幫忙。","或許你想逃離的不是世界，而是這一切複雜難解的問題和痛苦。如果你願意的話，說說好嗎? 我陪你一起梳理打結的思緒。"],
                    #"sexualHarassment":["謝謝你願意和我分享，我覺得你非常勇敢，你沒有任何的錯！和你分享這個連結\nhttp://womany.net/read/article/1777"],
                    #"hunger":["每天最困難的問題大概就是三餐吃什麼了吧! 我懂！","不要照著時間吃東西，而是覺得餓的時候再吃。想好要吃什麼了嗎? 有的話就去吃吧!","飢餓有兩種，一種是來自生理的渴望，一種是對於意義追尋的渴求。或許你現在需要一點新的東西~","不知道要吃什麼真的是個難題，有時候真的找不到靈感，要不然換個新問題，回想之前吃過覺得不錯吃的東西，來找找看靈感吧！"],
                    #"motivation":["遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","感到停滯的時候，不要急著逼自己往前。休息一下充飽電再出發。","很多都會有這種累的時候，其實正是告訴你需要休息一下。看看是不是先讓自己放鬆一些，再繼續～","失去動力了，不代表要放棄，很多時候只是需要休息。而放棄也沒什麼，如果你確定這不是你想要的。那換一件事情也好。"],
                    #"noFriend":["你會練習跟自己相處，聽到自己內心的聲音。","自己是自己最好的朋友，傾聽內心，相信直覺，善待自己。","很多時候和自己相處真的很不容易，這也是需要學習的！不過覺得寂寞的心情其實也不用掩藏，一起來想想看你喜歡做什麼事情吧！","其實我有時候想到只有自己一人真的覺得難過，謝謝你和我說你的心情。有我在這邊陪你。"],
                    #"listen":["你會練習跟自己相處，聽到自己內心的聲音。"],
                    #"exchange":["先把結果交給上天吧！我相信你一定為了出國交換付出了很多努力，你真的已經盡力了，相信上天一定會為你預備最好的結果。","準備交換或許不如自己所想，你已經很努力了！","我覺得這樣的結果真的很難過，雖然這次的交換結果不如自己的預期，但或許這次沒有出國反而會有一些新的機會產生也說不定！你很優秀又願意努力，新的機會就會上門。"],
                    #"test":[ "如果你已經盡力了，那就不愧對自己了。","考試不是目的而是手段，為的是看看你對某個觀念的熟悉程度，並不是要把你考倒，放寬心~~別太執著。"],
                    #"bully":["Alert"],
                    #"afraid":["辛苦你了，碰到這樣可怕的事情，謝謝你願意和我分享"],
                    #"missOpportunity":["沒關係，如果它是屬於你的，就會是你的，總有一天會得到它的","機會是留給準備好的人，錯過了沒關係，相信努力又有實力的你，絕對可以把握住下一次。","我相信你一定可以把握下一次的機會！所以休息一下，就把這次的經驗當成學習機會！","我覺得我理解你現在的心情，我想應該是不甘心。辛苦了，先好好休息一下，我想信你一定可以把這次的經驗轉化成你的動力！"],
                    #"end":["舊的不去，新的不來，會找到更多喜歡的東西的。","要揮別過的事情和東西真的很不容易，因為裡面滿滿都是回憶。","不會有不散的筵席，其實東西也是，不過這樣的感覺是真的很難過。"],
                    #"others":["那你覺得怎麼樣?"],
                    #"nightmare":["還好嗎? 感覺很可怕...別怕，我陪你。","做惡夢的感覺很不好，不過不用擔心，因為我聽說夢境中不好的東西都和現實相反，所以那些可怕的東西都不會發生。","先給你拍拍，別怕，你已經醒了。","別怕！你已經醒了！現在先喝口水，或許可以走一走，然後安心去睡覺吧～"],
                    #"complainToYou":["那你一定是一個溫暖的人，但真的很不舒服的話，也可以試著跟他們說看看","當一個溫柔的人不容易，當你好好地接住他人的情緒，別忘了也好好照顧你內心的孩子。","當你也覺得負荷不來的時候，可以說給我聽，換我接住你。","辛苦了，遇到這些事情的你真的很不容易，謝謝你和我分享！"],
                    #"competition": ["盡力就是最棒的結果","學到更多的人才是最後的贏家。","不可能凡事都是第一名，但只求在這過程中，你享受、你開心。","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。","競賽其實最後都是和以前的自己做比較，每個人狀態不一樣，所以如果你享受這全心全意的準備和付出，你就贏了！我知道你很棒！你也要知道！","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。"],
                    #"cheerup":["在哪裡跌倒，就在哪裡躺下，休息一下再出發。","凡事有起有落，到谷底時正是最佳的觸底反彈時機。","謝謝你和我分享你的感覺，雖然知道挫折有時候真的是可以讓自己成長的，但有這樣的感覺真的不好受。先好好休息一下，再出發，相信一定會否極泰來。","不想和你說加油，因為我知道你已經很努力了。我只想和你說你要相信你很棒！所以要相信自己可以度過難關。"],
                    #"notOpen":["可能是個可以發掘新東西的機會喔!","雖然喜歡的東西沒有買到，但或許有別的好東西～","我覺得我可以理解這種期待落空的感覺！這樣的感覺真的很不爽！"],
                    #"misunderstood":["不用怕! 行得正，坐得端，就什麼都不用怕別人的眼光。","謝謝你把你的心情和我分享，被誤會的感覺真的很討厭，先逃離那個環境，再想想看怎麼解開這些誤會。","我覺得被誤會真的很討厭，真的辛苦了，先喝杯茶，先沉澱一下心情，再出發！","我自己也是最討厭被誤會了，那種不被相信的感覺真的很不好受。","真是辛苦了，不被理解感覺一定很不好受。只要你現在做事無愧於心，我覺得未來一定會有欣賞你的人出現。"],
                    #"notDone":["一步一步就可以把手上的工作都做完了！","雖然看似超級多，但一點一點做，一定可以完成的~","我也很討厭工作做不完這種感覺，因為覺得壓力很大啊！但我想和你說，我相信你的能力，按部就班，可以做完的！再不然，先檢視一下時間表，好好做個調整！","工作繁雜的時候真的很不好受，好擔心你，記得要適度休息喔！現在就先喝口水吧！"],
                    #"boringWork":["可以試著把枯燥乏味的事情遊戲化，當作一個個任務來破解或許就會比較有趣了。","其實工作總是會有無聊或是不喜歡的時候，覺得工作起來很無力的時候，或許休息一下轉換一下心情是好方法！","工作起來真的會有這些比較繁瑣、無趣的時候，相信這樣的感覺應該真的有點啊雜！我知道！謝謝你和我分享 ， 我被你度過這個無聊的時光。"],
                    #"stepInPoop":["天啊，可以去買張樂透了!"]
                    #}
  
def HandleReasons(inputSTR):
    resultDICT = runLoki([inputSTR])
    reactionDICT  = {"source" : ""}
    try:
        SourceSTR = resultDICT["source"]
        for e in handleSoruceDICT.keys():
            if SourceSTR in handleSoruceDICT[e]:
                reactionDICT["source"] = e  
    except:
        pass
    if reactionDICT["source"] == "":
        reactionDICT["source"] = "others"
    return random.choice(sourceReactionDICT[reactionDICT["source"]]) 
            
            

#def Result(inputSTR):
    #if HandleFeelings(inputSTR) != None:
        #return HandleFeelings(inputSTR) 
    #elif HandleReasons(inputSTR) != None:
        #return HandleReasons(inputSTR) 
    #else:
        #return "謝謝你願意跟我說這些"

        
    

if __name__ == "__main__":
    #inputSTR = "心情爆爆爆爆好"
    #reactionSTR = HandleFeelings(inputSTR)
    #print(reactionSTR)
    inputSTR = "踩到狗大便"
    reactionSTR = HandleReasons(inputSTR)
    print(reactionSTR)
    
    