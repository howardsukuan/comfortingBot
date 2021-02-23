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
    


#2nd self defined function: check the mood
EmotionRactionDICT = {"BadMood":["差","不好","很糟糕","badmood","爛","很悶","低潮","好難","難過","低落","空虛","寂寞","黑暗","不太開心","不太妙","很難過"],"GoodMood":["好","不錯","很好","很棒","棒"]}
PlainFeelingLIST = ["普通","還好","還行","沒什麼特別","一樣","好無聊","跟平常差不多"]

BadFeelingReactionLIST = ["還好嗎 \n想說說為什麼嗎?",
                          "還好嗎?\n跟我談談嗎?",
                          "我都在這,你如果願意談談可以跟我說\n你說,我聽"]
GoodFeelingReactionLIST = ["好替你開心!! 那你願意跟我分享一下嗎~",
                          "感覺很棒! 是發生什麼事情嗎~"]
PlainReactionLIST = ["那想聊的時候再跟我聊聊\n我都在", "好~ 有什麼想分享的事情再說喔!"]
OtherReactionLIST = ["那要談談嗎?", "那要分享一下嗎?"]
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

#3rd self defined function: respond to the reason    
handleSoruceDICT = {"appearance":["下巴","嘴唇","屁股","手","appearance","皮膚","皺紋","肚子","腿","膚色","臉","身高","額頭","髮質","髮際線","鼻子"],
                    "negMood":["mood","心","很自私"],
                    "score":["低空","分數","score"],
                    "work":["工作","work","會議"],
                    "schoolwork":["作業","作品","schoolwork"],
                    "colleague":["做事","同事"],
                    "weather":["天氣","weather"],
                    "family": ["爸爸","媽媽","父親","老公","親戚們"],
                    "money":["存款","錢"],
                    "death":["death"],
                    "sick":["sick",],
                    "self":["我"],
                    "stranger":["人","stranger"],
                    "food":["food","食物"],
                    "lose":["lose","名次"],
                    "nothing":["nothing"],
                    "relationship": ["男友","男朋友","女朋友","女友","relationship"],
                    "receipt":["發票"],
                    "ticket":["票"],
                    "teacher":["老師","教授"],
                    "boss":["老闆","boss","主管"],
                    "thesis":["論文"],
                    "sthbroken":["broken"],
                    "school":["schoolLesson"],
                    "shop":["店"],
                    "toilet":["toilet"],
                    "houseChore":["houseChore"],
                    "future":["未來"],
                    "suicide":["suicide"],
                    "sexualHarassment":["sexualHarassment"],
                    "hunger":["hunger"],
                    "motivation":["力氣","動力"],
                    "friend":["朋友"],
                    "listen":["listen"],
                    "exchange":["exchange"],
                    "test":["test"],
                    "bully":["bully"],
                    "afraid":["afraid"],
                    "missOpportunity":["missOpportunity"],
                    "end":["end"],
                    "nightmare":["nightmare","惡夢"],
                    "complainToYou":["complain","抱怨","牢騷"],
                    "competition":["competition"],
                    "cheerup":["cheerup"],
                    "notOpen":["notOpen"]
                    }
sourceReactionDICT = {"appearance":["大家對外表可能會有一定的要求,但是重點還是在你身上,如果你喜歡這樣的自己,那又何嘗不可?"," 外表只是一時的，只要健康就好","美醜其實都是自己定義的！所以抬頭挺胸，做自信的自己！我相信你可以！","比起皮囊，我更喜歡那裡頭的靈魂。", "不論身心靈各方面，多愛自己一點是基本呀!!!"],
                    "negMood":["雖說自己的努力不用別人去定義，但現在這個受委屈的心情是真實的，我懂你的不舒服，但現在的繼續努力，未來我相信一定會成為支持你的力量", "遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","你會練習跟自己相處，聽到自己內心的聲音。","我不會叫你加油，因為我知道你已經很努力了。"],
                    "score":[" 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分", "如果你已經盡力了，那就不愧對自己了。"],
                    "work":["(抱) 辛苦了，想想你原本的目標，覺得不行了也要休息一下","世上最遙遠的距離，不是我和你，而是公司到家裡。"],
                    "schoolwork":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"," 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分"," 辛苦了，就算是再喜愛的工作都會有累的時候，不和你說加油，因為你已經夠努力了", "要不要試試看換一個新方法呢?", "人生也有許多沒有正確答案的事，正因為每個人答題方式不同，才會有不同的結果。"],
                    "colleague":["不用怕! 行的正，坐的端，就什麼都不用怕","真的辛苦你了！看著這樣不公平的事情，一定心裡有點不舒服。或許現況不一定很好改變，但是穩紮穩打，未來一定有人可以看的到你的光芒。","真是辛苦了，這樣的感覺一定很不好受。只要你現在做事無愧於心，我覺得未來一定會有欣賞你的人出現", "啊!這麼早遇到超級大boss的你打怪辛苦了。"],
                    "weather":["♪其實我，不是因為好天氣才這麼說，牽著你走過大雨盛開水花的路口，也是我一樣喜歡的夢♪"],
                    "family": ["家人的溝通需要智慧，還有時間，加油加油"],
                    "money":["生活帶走了錢，但是他帶不走你的快樂!!","好巧，我也覺得錢錢沒有夠用的一天呢。" ],
                    "death":["想說什麼我都會聽你說，我也會一直陪著你","相信他會以另一種形式好好地繼續陪伴你。"],
                    "sick":["傾聽身體的聲音，找一天做個健康檢查吧!"],
                    "self":["發現別人的光芒很容易，但記得也要好好沉澱自己，發現自己的光芒。"],
                    "stranger":[],
                    "food":["如果你吐出來了！Good Job! 如果沒有，沒關係他會用另外一種形式排出體外！"],
                    "lose":[ "學到更多的人才是最後的贏家。"],
                    "nothing":["生活比海還深，陷溺後便是流沙，你無法徒手拔出流沙裡的人，在拯救溺水者之前，你必須先呼吸。"],
                    "relationship": ["你一定現在非常難過， 好好給自己一點時間好好休息吧！","不是你不好，是那些人都看不到你的好。","不管怎麼樣，你現在受委屈的心情我懂！辛苦你了！","我懂你的難過，辛苦了，讓我先給你一個擁抱","理智上可以理解，心情上過不去，也是某種成長痛","要好好長大，會有人愛你。願我們都成為逐漸完整的自己。"],
                    "receipt":[ "換個角度想，你的壞運氣都用在這裡了，接下來都會好運的。"],
                    "ticket":[ "有時候運氣也是實力的一種，下次組一支搶票小隊幫忙吧。"],
                    "teacher":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"],
                    "boss":["先給你一個擁抱(抱)，真的辛苦你了，現在先好好休息再看看下一步怎麼做吧！"],
                    "thesis":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"],
                    "sthbroken":["舊的不去，新的不來，雖然和舊的物品說在件很難過，但是也會迎接新的夥伴啊！"],
                    "school":["枯燥乏味之事存在的意義有兩個，一個是凸顯其他有趣的事，另一個是讓你從重複中變成大師。"],
                    "shop":["或許現在不是一個好的時機啊！等時機對了，機會就會來臨"],
                    "tiolet":["還好嗎，要不要去一趟廁所?" ],
                    "houseChore":["一步一步就可以把手上的工作都做完了！"],
                    "future":["人對未知都是恐懼的，練習正視自己的恐懼，慢慢來就好。"],
                    "suicide":["想聊聊嗎？要不要打給張老師 1980"],
                    "sexualHarassment":["謝謝你願意和我分享，我覺得你非常勇敢，你沒有任何的錯！和你分享這個連結\nhttp://womany.net/read/article/1777"],
                    "hunger":["每天最困難的問題大概就是三餐吃什麼了吧!"],
                    "motivation":["遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!"],
                    "friend":["你會練習跟自己相處，聽到自己內心的聲音。"],
                    "listen":["你會練習跟自己相處，聽到自己內心的聲音。"],
                    "exchange":["先把結果交給上天吧！我相信你一定為此付出了很多努力，你真的已經盡力了，相信上天一定會為你預備最好的道路","先把結果交給上天吧！我相信你一定為此付出了很多努力，你真的已經盡力了，相信上天一定會為你預備最好的道路"],
                    "test":[ "如果你已經盡力了，那就不愧對自己了。"],
                    "bully":["Alert"],
                    "afraid":["辛苦你了，碰到這樣可怕的事情，謝謝你願意和我分享"],
                    "missOpportunity":["沒關係，如果它是屬於你的，就會是你的，總有一天會得到它的"],
                    "end":["舊的不去，新的不來，會找到新愛的"],
                    "others":["那你覺得怎麼樣?"],
                    "nightmare":["還好嗎? 感覺很可怕..."],
                    "complainToYou":["那你一定是一個溫暖的人\n但真的很不舒服的話\n也可以試著跟他們說看看"],
                    "competition": ["盡力就是最棒的結果"],
                    "cheerup":["在哪裡跌倒，就在哪裡躺下，會很快樂的!"],
                    "notOpen":["是個可以發掘新東西的機會!"]
                    }
  
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
    inputSTR = "心情爆爆爆爆好"
    reactionSTR = HandleFeelings(inputSTR)
    print(reactionSTR)
    inputSTR = "早餐店沒開"
    reactionSTR = HandleReasons(inputSTR)
    print(reactionSTR)
    