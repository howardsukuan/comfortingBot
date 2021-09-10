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
#from collections import defaultdict
import random
from interpersonalREF import handleSourceInterDICT
from interpersonalREF import sourceReactionInterDICT
from otherREF import handleSourceOtherDICT
from otherREF import sourceReactionOtherDICT
from personalREF import handleSourcePersonalDICT
from personalREF import sourceReactionPersonalDICT
from seriousSituationREF import handleSourceSeriousDICT
from seriousSituationREF import sourceReactionSeriousDICT
from requests import post
from requests import codes
from account_info import accountInfoDICT
import math

from intent import Loki_domestic_violence
from intent import Loki_interpersonal
from intent import Loki_sexual_harassment
from intent import Loki_personal
from intent import Loki_suicide
from intent import Loki_other
#except:
    #from .intent import Loki_domestic_violence
    #from .intent import Loki_interpersonal
    #from .intent import Loki_sexual_harassment
    #from .intent import Loki_personal
    #from .intent import Loki_suicide
    #from .intent import Loki_other


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
                
                # suicide
                if lokiRst.getIntent(index, resultIndex) == "suicide":
                    resultDICT = Loki_suicide.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                    
                # sexual_harassment
                if lokiRst.getIntent(index, resultIndex) == "sexual_harassment":
                    resultDICT = Loki_sexual_harassment.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)                
        

                # interpersonal
                if lokiRst.getIntent(index, resultIndex) == "interpersonal":
                    resultDICT = Loki_interpersonal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                 # other
                if lokiRst.getIntent(index, resultIndex) == "other":
                    resultDICT = Loki_other.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # personal
                if lokiRst.getIntent(index, resultIndex) == "personal":
                    resultDICT = Loki_personal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)    

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

#def testLoki(inputLIST, filterLIST):
    #INPUT_LIMIT = 20
    #for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        #resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

        
        
######主要修改區######
        
#先將字典合併
handleSourceLIST = [handleSourceSeriousDICT,handleSourceInterDICT,handleSourceOtherDICT,handleSourcePersonalDICT]
sourceReactionLIST = [sourceReactionSeriousDICT,sourceReactionInterDICT,sourceReactionOtherDICT,sourceReactionPersonalDICT]
handleSourceDICT = dict()
sourceReactionDICT = dict()
for d in handleSourceLIST :
    handleSourceDICT.update(d)
for d in sourceReactionLIST :
    sourceReactionDICT.update(d)
    

#偵測結束
endingLIST = ["謝謝你我沒事了","好 謝謝你","謝謝你", "感謝有你", "太感謝你了", "還好有你的聆聽", "好", "好的", "好吧", "先這樣", "我知道了", "沒其他的事了", "我好多了", "我好很多了", "我的心情好很多了", "嗯嗯", "大概就這樣", "我會加油的", "掰掰", "拜拜", "bye bye", "bye","好喔謝謝你","好的謝謝你"]
endingReactionLIST = ["真的很謝謝你和我分享！","說出來會好一點，謝謝你願意說給我聽，這也是我存在的理由。","如果我能帶給你一點點的療癒，那就足夠了，謝謝你跟我分享!"]


def HandleReasons(inputSTR):   
    resultDICT = runLoki([inputSTR])

    #print(resultDICT)
    reactionDICT  = {"source_suicide" : "","source_sexual_harassment":"","source_domestic_violence":"","source_interpersonal":"","source_other":"","source_personal":""}
    #suicide
    try:
        for e in handleSourceDICT.keys():
            if resultDICT["source_suicide"] in handleSourceDICT[e]:
                reactionDICT["source_suicide"]= e        
        
    except:
        pass
    #sexual harassment    
    try:
        for e in handleSourceDICT.keys():
            if resultDICT["source_sexual_harassment"]  in handleSourceDICT[e]:
                reactionDICT["source_sexual_harassment"]= e        
        
    except:
        pass
    #domestic violence    
    try:
        for e in handleSourceDICT.keys():
            if resultDICT["source_domestic_violence"] in handleSourceDICT[e]:
                reactionDICT["source_domestic_violence"]= e           
    except:
        pass
    #others
    try:
        for e in handleSourceOtherDICT.keys():
            #print(e + "other") #測試用
            if resultDICT["source_other"]  in handleSourceOtherDICT[e]:
                reactionDICT["source_other"]= e 
                #print(e + "ver1")
    except:
        pass
    
    #interpersonal  
    try:
        for e in handleSourceDICT.keys():
            if resultDICT["source_interpersonal"]  in handleSourceDICT[e]:
                reactionDICT["source_interpersonal"]= e 
    except:
        pass
        
    #personal 
    try:
        for e in handleSourcePersonalDICT.keys():
            #print(e) #測試用
            if resultDICT["source_personal"]  in handleSourcePersonalDICT[e]:
                reactionDICT["source_personal"]= e 
    except:
        pass
    # matching reaction 
    try:
        #when the input can be detected by loki
        reactionSTR = [e for e in [reactionDICT[i] for i in reactionDICT.keys()] if len(e) > 0][0]
        #print(reactionDICT)
        return random.choice(sourceReactionDICT[reactionSTR]), reactionDICT #可以看配對狀況
    except:
        #when the sentence cannot be detected by loki...
        #condition 1: sentence with ending marker
        if any(e == inputSTR for e in endingLIST):
            return random.choice(endingReactionLIST)
        #condition 2: can be solved using keyword method
        else:
            for e in handleSourceDICT.keys():
                for x in handleSourceDICT[e]:
                    if x in inputSTR:
                        return random.choice(sourceReactionDICT[e])
                    else: #condition3: still not matched
                        return random.choice(sourceReactionDICT["others"]) 
    
if __name__ == "__main__":

    inputSTR = "覺得微不足道"
    reactionSTR = HandleReasons(inputSTR)
    print(reactionSTR)
   
    #爸爸家暴我
    #功課寫不完

    # 輸入其它句子試看看
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    #filterLIST = []
    #resultDICT = runLoki(inputLIST, filterLIST)
    #print("Result => {}".format(resultDICT))