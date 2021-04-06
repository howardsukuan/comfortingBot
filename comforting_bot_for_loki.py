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
from comfortingREF import SexualHarassmentLIST
from comfortingREF import SexualHarassmentReactionLIST
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    from intent import Loki_feeling
    from intent import Loki_asking_for_help
    from intent import Loki_complainingSentences
    from intent import Loki_domestic_violence
except:
    from .intent import Loki_feeling   
    from .intent import Loki_asking_for_help
    from .intent import Loki_complainingSentences
    from .intent import Loki_domestic_violence


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
                
                # domestic_violence
                if lokiRst.getIntent(index, resultIndex) == "domestic_violence":
                    resultDICT = Loki_domestic_violence.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)                

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
    
 
suicideLIST = ["活著還有什麼","我死一死","不想活","好想消失","好想死","永遠都不要醒","用我的命換","結束生命","死了算了","活著有什麼","活著的意義是什麼","自殺","結束這一生","想去死","想離開世界","登出人生","淡出人生","活著好累","活得好痛苦","活著好痛苦","淡出世界","登出世界"]  

endingLIST = ["謝謝你", "感謝有你", "太感謝你了", "還好有你的聆聽", "好", "好的", "好吧", "先這樣", "我知道了", "沒其他的事了", "我好多了", "我好很多了", "我的心情好很多了", "嗯嗯", "大概就這樣", "我會加油的", "掰掰", "拜拜", "bye bye", "bye"]
endingReactionLIST = ["真的很謝謝你和我分享！"]
def HandleReasons(inputSTR):
    resultDICT = runLoki([inputSTR])
    reactionDICT  = {"source" : ""}
    if any(e in inputSTR for e in SexualHarassmentLIST):
        return random.choice(SexualHarassmentReactionLIST)
    elif any(e in inputSTR for e in suicideLIST):
        reactionDICT["source"] = "suicide"
    elif any(e == inputSTR for e in endingLIST):
        return random.choice(endingReactionLIST)        
    else:   
        try:
            SourceSTR = resultDICT["source"]
            for e in handleSoruceDICT.keys():
                if SourceSTR in handleSoruceDICT[e]:
                    reactionDICT["source"] = e  
        except:
            pass
    if reactionDICT["source"] == "":
        for e in handleSoruceDICT.keys():
            for x in handleSoruceDICT[e]:
                if x in inputSTR:
                    reactionDICT["source"] = e
                else:
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
    inputSTR = "我覺得我好胖"
    reactionSTR = HandleReasons(inputSTR)
    print(reactionSTR)
    
    