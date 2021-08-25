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

from requests import post
from requests import codes
import math
try:
    from intent import Loki_domestic_violence
    from intent import Loki_interpersonal
    from intent import Loki_sexual_harassment
    from intent import Loki_personal
    from intent import Loki_suicide
    from intent import Loki_other
except:
    from .intent import Loki_domestic_violence
    from .intent import Loki_interpersonal
    from .intent import Loki_sexual_harassment
    from .intent import Loki_personal
    from .intent import Loki_suicide
    from .intent import Loki_other


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
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

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
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

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # domestic_violence
                if lokiRst.getIntent(index, resultIndex) == "domestic_violence":
                    resultDICT = Loki_domestic_violence.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # interpersonal
                if lokiRst.getIntent(index, resultIndex) == "interpersonal":
                    resultDICT = Loki_interpersonal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # sexual_harassment
                if lokiRst.getIntent(index, resultIndex) == "sexual_harassment":
                    resultDICT = Loki_sexual_harassment.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # personal
                if lokiRst.getIntent(index, resultIndex) == "personal":
                    resultDICT = Loki_personal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # suicide
                if lokiRst.getIntent(index, resultIndex) == "suicide":
                    resultDICT = Loki_suicide.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # other
                if lokiRst.getIntent(index, resultIndex) == "other":
                    resultDICT = Loki_other.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # domestic_violence
    print("[TEST] domestic_violence")
    inputLIST = ['爸爸打我','我被爸爸打','我被爸爸揍','爸爸家暴我','爸爸痛毆我','哥哥一直打我','我被爸爸虐待','爸爸一直扁我','爸爸一直揍我','爸爸一直踢我','爸爸向我揮拳','爸爸對我動粗','爸爸對我施暴','爸爸拿菸燙我','爸爸毆打媽媽','爸爸要打死我','爸爸要殺掉我','男友對我動手','爸爸一直傷害我','爸爸喝醉就揍我','爸爸拿熱水潑我','爸爸拿藤條抽我','爸爸用拳頭打我','爸爸說要打死我','爸爸說要殺掉我','我被家人打得半死','我被家人揍到流血','爸爸對我使用暴力','爸爸對我拳打腳踢','爸爸常常罵我髒話','爸爸常常賞我巴掌','爸爸把我打到流血','爸爸把我打到瘀青','爸爸把我抓起來摔','爸爸把我鎖在家裡','爸爸用言語辱罵我','爸爸常常對我罵髒話','爸爸心情不好就打我','爸爸心情不好就揍我','爸爸喝醉酒回來就打媽','爸爸限制我出門的自由','我姊剛剛毫無原因就揍我','爸爸一直抓我的頭去撞牆','爸爸常常對我使用言語暴力','媽媽因為我成績退步一直打我']
    testLoki(inputLIST, ['domestic_violence'])
    print("")

    # interpersonal
    print("[TEST] interpersonal")
    inputLIST = ['失戀了','被甩了','同事放槍','同事耍廢','同事耍腦','同事超雷','好想脫魯','我被分手','比賽輸了','沒有得名','沒有朋友','男友亂來','男友劈腿','男友垃圾','男友很渣','男友是渣','男友超渣','碰到噁男','被人誤會','阿公很煩','一直碎碎念','同事不做事','同事不出現','同事大雷人','同事有夠廢','同事無敵廢','同事超級雷','同事難相處','同學好虛偽','向我發牢騷','好想交男友','家人生病了','家人過世了','寵物死掉了','寵物生病了','我是邊緣人','我男友好摳','朋友吵架了','男友提分手','男友甩了我','老師誤會我','腳踏兩條船','被主管訓話','別人不喜歡我','同事告我的狀','對男友沒感覺','忘記我的生日','我身體不舒服','朋友予取予求','朋友說他很忙','朋友說我壞話','沒人找我一組','狗狗亂大小便','狗狗都不吃飯','男友說要分手','老闆叫我加班','遇到奇怪的人','遠距離好痛苦','隔壁的人很吵','女友有嚴重潔癖','媽媽一直逼我婚','教授觀念很保守','有人說我很貪心','朋友鬧得不愉快','沒有人聽我說話','祝福都沒有收到','老師上課好無聊','被主管臭罵一頓','跟爸媽很難溝通','同事和我借錢不還','同組同學都不說話','喜歡的人不喜歡我','喜歡的人對我無感','喜歡的人有伴侶了','喜歡的人有戀人了','媽媽覺得我吃太多','我覺得媽媽討厭我','男友相處時間變少','男友說要跟我分手','被主管說表現很差','身邊的人都很聰明','喜歡的人不想談戀愛','喜歡的人有男朋友了','我的寵物最近生病了','沒有任何人可以訴苦','男友最近都很少陪我','男朋友怎麼這麼小氣','老闆說我的能力不夠','分組報告組員都在擺爛','同學做報告都沒有貢獻','周圍的人都很努力進修','喜歡的人拒絕我的告白','最近跟家裡的人吵架了','同學只想從我這邊拿成果','喜歡的人說我們是好哥們','喜歡的人說我們是好閨密','我什麼時候才能換女友呢','喜歡的人說我們當朋友就好','隔壁坐了一個莫名其妙的人','同事做事不負責任但領的錢比我多']
    testLoki(inputLIST, ['interpersonal'])
    print("")

    # sexual_harassment
    print("[TEST] sexual_harassment")
    inputLIST = ['我被人亂摸','爸爸亂摸我','同學一直聊色','同學對我露鳥','同學拍我屁股','同學觸碰到我','路人對我露屌','同學一直開黃腔','同學要我跟他睡','爸爸對我性騷擾','男生抱著我不放','老師摳我的手心','爸爸偷摸我的屁股','爸爸對我毛手毛腳','同學一直傳裸照給我','同學一直說黃色笑話','爸爸想跟我一起洗澡','爸爸想跟我發生關係','男友對我霸王硬上弓','男友逼迫我跟他接吻','同學要我和他發生關係','同學對著我撫摸他的生殖器']
    testLoki(inputLIST, ['sexual_harassment'])
    print("")

    # personal
    print("[TEST] personal")
    inputLIST = ['沒事','胃痛','腰痠','腿短','做惡夢','好偏心','好生氣','好難過','心好累','想大便','想消失','我好醜','我很胖','手超粗','月經來','沒什麼','沒吃飽','被排擠','要上班','超難過','長得醜','長痘痘','頭好痛','下巴太圓','不想上班','今天很遭','低空飛過','嘴唇很薄','壓力好大','好想下班','好想回家','好想拉屎','屁股好大','常常生病','很不快樂','心情不好','心情低潮','心情很差','心情很幹','想上廁所','我好沒用','我心好累','我是廢物','提不起勁','沒人懂我','狀態很差','生理期來','皮膚好差','眼睛太小','肚子好餓','肚子很圓','肩膀痠痛','膚色好黑','蟑螂來了','要崩潰了','覺得傷心','覺得失望','覺得孤單','起了口角','超不開心','身高太矮','都說沒空','不給我方向','事情做不好','任務很難做','作業不會寫','分數不理想','分數很難看','如果做不好','就覺得很煩','得了厭食症','我覺得很煩','我討厭自己','找不到工作','沒有什麼事','沒生活品質','狀態不太好','狀態很糟糕','現在超想家','自己好渺小','莫名的想哭','莫名的想家','被說很自私','被說沒禮貌','要打預防針','覺得不開心','覺得很難過','覺得我很胖','覺得被忽略','身體好疲憊','髮質很糟糕','鼻子不夠挺','作品被退件了','作業寫不出來','和朋友吵架了','大家都好厲害','好低分不及格','對未來好迷茫','感到不受重視','感到很有壓力','我吃壞肚子了','我常常睡不飽','我看不到未來','我覺得我很雖','我身體不舒服','找不到租屋處','沒有力氣做事','生活品質變低','皺紋長出來了','考試考超差的','莫名覺得憂鬱','被說目中無人','被說自我中心','覺得工作很累','覺得微不足道','覺得我不夠好','覺得空虛寂寞','覺得自己很廢','身體覺得很重','髮際線太後面','不小心起了衝突','不給我任何方向','什麼事都不想做','什麼事都做不好','壓抑自己的情緒','好想要換工作喔','我每天都睡不著','我能考上台大嗎','我覺得非常倒楣','最近身體變好差','月經來好不舒服','考試全部不會寫','考試好多不會寫','肚子咕嚕咕嚕叫','覺得呼吸好困難','覺得我得了感冒','覺得我有厭食症','作業不知道怎麼寫','作業想不出怎麼做','只想每天躲在宿舍','好討厭現在的自己','想留點時間給自己','感覺自己做了白工','我一直做可怕的夢','我很不喜歡我自己','我能找得到工作嗎','我覺得我能力不足','我覺得自己很討厭','時間感覺都不夠用','有人弄亂我的桌子','朋友說我長得很醜','沒什麼可以分享的','考試一大堆不會寫','考試全部都不會寫','考試大部分不會寫','考試好多都不會寫','自己就是一個廢物','覺得我白忙了一場','世界上沒有我也可以','作業想不出該怎麼做','可是我晚上都睡不著','想留一點時間給自己','感覺努力沒有被看見','感覺牆角有鬼在看我','我在小組裡面很自卑','沒有考上喜歡的學校','為什麼都換不了工作','考試一大堆都不會寫','考試大部分都不會寫','覺得自己快要爆炸了','不知道未來要住在哪裡','什麼時候我才可以成功','做什麼事情都沒有動機','失去了原本的生活品質','憑什麼小明考得比較好','為什麼大家都可以做到','班上的人都不和我說話','甚至也不想跟別人social','事情都不順我的意很討厭','做了很久但是都沒有成效','怎麼辦我覺得我一直失敗','我什麼時候才能換工作呢','我只要想自己一個人待著','昨天晚上夢到可怕的事情','覺得現在的工作我做不來','覺得自己好像有點厭食症','一直被奪命連環call超級煩','憑什麼小明比較被妹妹喜歡','覺得這件事情沒有達到自己的標準','我總是在人前壓抑自己的情緒然後在人後又獨自悲傷']
    testLoki(inputLIST, ['personal'])
    print("")

    # suicide
    print("[TEST] suicide")
    inputLIST = ['我想去死','我想消失','我想自殺','死了算了','活著好累','我不想活了','我想死一死','活得好痛苦','世界不需要我','我想去死一死','我想登出世界','我想登出人生','我想結束生命','永遠都不要醒','活著還有什麼','我想結束這一生','我的人生沒意義','世界好像不需要我','我想吃一堆安眠藥','我想吞整罐安眠藥','我想逃離這個世界','我想離開這個世界','我找不到生命的意義','我的人生沒什麼意義','我想把整罐安眠藥吃下去','我不知道活著的意義是什麼']
    testLoki(inputLIST, ['suicide'])
    print("")

    # other
    print("[TEST] other")
    inputLIST = ['我沒錢','課好廢','上課好累','上課很煩','上課超累','今天好冷','今天好熱','分數爆了','天氣好冷','天氣好熱','實習好廢','實習好累','實習很煩','實習超累','我沒錢了','我踩到屎','發票沒中','緣份盡了','股票虧了','要吃土了','錢不夠用','錢不夠花','電腦壞了','不想寫作業','事情好無聊','分數不理想','分數很難看','工作做不完','我一直拖延','我是月光族','我筆電壞了','我要吃土了','我買不到票','我踩到大便','我踩到狗屎','投資失利了','早餐店休息','早餐店沒開','東西很難吃','東西超噁心','發票又槓龜','發票又沒中','考試不及格','考試好低分','要讀好多書','覺得很難吃','論文寫不完','那是廚餘吧','都沒有進步','電腦壞掉了','事情無聊死了','今天天氣不好','今天天氣好冷','今天天氣好煩','今天天氣好熱','今天天氣很糟','作業我一直拖','做不完的感覺','好多事情要做','存不到什麼錢','我不想寫作業','我們沒有緣份','我的存款太少','我的存款好少','我的筆電壞了','我筆電壞掉了','我踩到狗大便','演唱會票沒了','發票沒有中獎','要看好多論文','論文不夠精緻','進度有點耽誤','進度有點落後','進度都趕不上','都沒辦法存錢','不知道要怎麼辦','不知道該怎麼辦','事情好多，好煩','事情無聊到不行','交換可能不會上','交換可能沒機會','作業我一直拖延','作業我不想面對','吃到難吃的東西','吃到香菜好可怕','我不想面對作業','我每個月都月光','我的筆電壞掉了','我筆電最近壞了','早餐店今天休息','早餐店今天沒開','演唱會票好難搶','演唱會票好難買','演唱會票沒搶到','演唱會票賣光了','股票丟了好多錢','股票虧了好多錢','論文寫得不夠細','論文寫得有點爛','跟機會擦肩而過','這次發票又沒中','今天好多事情要做','大掃除一直做不完','我不知道要怎麼辦','我不知道該怎麼辦','我搶不到演唱會票','我的信用卡費爆了','我的筆電最近壞了','我筆電最近壞掉了','股票損失了好多錢','買一送一沒有跟到','這個月要吃吐司了','這家店東西很難吃','錯過這次的機會了','限定商品沒有買到','我的信用卡帳單爆了','我的筆電最近壞掉了','沒有考上喜歡的學校','覺得寫論文壓力很大','這個月只能吃吐司了','到店裡才發現今天休息','大掃除一直做不完很煩','我不太確定論文的方向','薪水下來一下子就沒了','還在等交換申請的結果','我不知道我的實驗在幹嘛','事情太多了不知道要怎麼辦','我不知道我的實驗在做什麼','一直沒有收到交換申請的回音']
    testLoki(inputLIST, ['other'])
    print("")

    # 輸入其它句子試看看
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    #filterLIST = []
    #resultDICT = runLoki(inputLIST, filterLIST)
    #print("Result => {}".format(resultDICT))