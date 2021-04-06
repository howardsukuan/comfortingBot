#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for feeling

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_feeling = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_feeling:
        print("[feeling] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "心情[很好]":
        # write your code here
        resultDICT["feeling"] = args[0]
        pass

    if utterance == "心情不[好]":
        # write your code here
        resultDICT["neg_feeling"] = args[0]
        pass

    if utterance == "心情很[差]":
        # write your code here
        resultDICT["feeling"] = args[0]
        pass

    if utterance == "狀態不[太好]":
        # write your code here
        resultDICT["neg_feeling"] = args[0]
        pass

    if utterance == "覺得[很難過]":
        # write your code here
        resultDICT["feeling"] = args[0]
        pass

    if utterance == "過得[不錯]":
        # write your code here
        resultDICT["feeling"] = args[0]
        pass
    if utterance == "狀態很[差]":
        # args [差]
        resultDICT["feeling"] = args[0]
    if utterance == "狀態[很糟糕]":
        # args [很糟糕]
        resultDICT["feeling"] = args[0]
    if utterance == "要崩潰了":
        # args []
        if "崩潰" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "好想哭":
        # args []
        if "想哭" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "好難過":
        # args []
        if "難過" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "好生氣":
        # args []
        if "生氣" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "心情很幹":
        # args []
        if "幹" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "[心情][爛]到爆":
        # args [狀態, 爛] 
        resultDICT["feeling"] = args[1]
    if utterance == "莫名的想哭":
        # args []
        if "想哭" in inputSTR:
            resultDICT["feeling"] = "badmood"
        if "躲在宿舍" in inputSTR:
            resultDICT["source"] = "WanttobeAlone"        
    if utterance == "[心情][低潮]":
        # args [心情, 低潮] 
        if "甚至也不想跟別人social" in inputSTR:
            resultDICT["source"] = "WanttobeAlone"
        if "很少陪我" in inputSTR:
            resultDICT["source"] = "noPartner"
        else:
            resultDICT["feeling"] = args[1]
    if utterance == "[人生][好難]":
        # args [人生, 好難]
        resultDICT["feeling"] = args[1]
    if utterance == "該怎麼辦":
        # args []
        if "怎麼辦" in inputSTR:
            resultDICT["feeling"] = "badmood"  
    if utterance == "該怎麼做":
        # args []
        if "怎麼做" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "好煩":
        # args []
        if "煩" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "還不是[都][一樣]":
        # args [都, 一樣]
        if "還不是" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "覺得傷心":
        # args []
        resultDICT["feeling"] = "badmood"        
    if utterance == "很生氣":
        # args []
        if "生氣" in inputSTR:
            resultDICT["feeling"] = "badmood"
        if "我是不是生病了" in inputSTR:
            resultDICT['source'] = "tired"
    if utterance == "覺得失望":
        # args []   
        if "失望" in inputSTR:
            resultDICT["feeling"] = "badmood" 
    if utterance == "覺得[空虛][寂寞]":
        # args [空虛, 寂寞]
        resultDICT["feeling"] = args[1]
    if utterance == "[一片][黑暗]":
        # args [一片, 黑暗] 
        resultDICT["feeling"] = args[1]
    if utterance == "沒人懂我":
        # args []
        if "沒人懂我" in inputSTR:
            resultDICT["feeling"] = "badmood"         
    if utterance == "覺得不開心":
        # args []
        if "不開心" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "不爽":
        # args []
        if "不爽" in inputSTR:
            resultDICT["feeling"] = "badmood" 
    if utterance == "不[太開心]":
        # args [太開心]
        resultDICT["neg_feeling"] = args[0]
    if utterance == "[不太]爽":
        # args [不太]
        if "不太爽" in inputSTR:
            resultDICT["feeling"] = "badmood"
    if utterance == "[超]難過":
        # args [超]
        if "難過" in inputSTR:
            resultDICT["feeling"] = "badmood"   
    if utterance == "很沮喪":
        # args []
        if "沮喪" in inputSTR:
            resultDICT["feeling"] = "badmood"  
    if utterance == "超不開心":
        # args []
        if "不開心" in inputSTR:
            resultDICT["feeling"] = "badmood"          
    if utterance == "超不[好]":
            # args [好]
        resultDICT["neg_feeling"] = args[0]
    if utterance == "超不好的":
        # args []
        if "不好" in inputSTR:
            resultDICT["feeling"] = "badmood" 
    if utterance == "覺得[很難過]":
        # args [很難過]
        resultDICT["feeling"] = args[0]
    
    
    return resultDICT