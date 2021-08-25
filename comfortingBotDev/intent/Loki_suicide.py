#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for suicide

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
#list1: 自殺行為
suicideLIST = ["安眠藥","世界","意義","人生","了結","死一死","不想活","消失","想死","不要醒","用我的命換","結束生命","死","活著","自殺","結束","去死","離開","登出","淡出","好累","痛苦"] 


DEBUG_suicide = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一", "計畫"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便", "寫論文"], "asAdverb": ["很", "好", "太", "超", "蠻", "有點"], "asAdjective": ["雷", "舒服", "好多", "可怕"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_suicide:
        print("[suicide] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]不想活了":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"
        pass

    if utterance == "[我]不知道活著的意義是什麼":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想去死":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想去死一死":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想吃[一堆]安眠藥":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想吞整罐安眠藥":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想把整罐安眠藥吃下去":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想死一死":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想消失":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想登出世界":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想登出人生":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想結束生命":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想結束這一生":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想自殺":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想逃離這個世界":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]想離開這個世界":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]找不到生命的意義":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]的人生沒[什麼]意義":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[我]的人生沒意義":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "[永遠][都]不要醒":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "世界不需要[我]":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "世界好像不需要[我]":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "死了算了":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "活得好痛苦":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "活著好累":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    if utterance == "活著還有什麼":
        # write your code here
        if any(e in inputSTR for e in suicideLIST):
            resultDICT["source"] = "suicide"        
        pass

    return resultDICT