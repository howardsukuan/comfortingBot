#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for domestic_violence

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_domestic_violence = True
userDefinedDICT = {}

familyLIST = ["爸爸","媽媽","家裡的人","弟弟","男友","我"]
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_domestic_violence:
        print("[domestic_violence] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[媽媽]因為我成績退步[一直]打[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST):
            resultDICT["source"] = "domestic_violence"         
        pass

    if utterance == "[弟]把[我]壓在[地][上]說要打死[我]":
        # write your code here
        pass

    if utterance == "[我]被[家人]揍到流血":
        # write your code here
        
        pass

    if utterance == "[我]被[爸爸]打":
        # write your code here
        pass

    if utterance == "[爸爸][一直]揍[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST):
            resultDICT["source"] = "domestic_violence" 
        pass

    if utterance == "[爸爸][喝醉酒]回來就打[媽]":
        # write your code here
        pass

    if utterance == "[爸爸]打[我]":
        # write your code here
        pass

    if utterance == "[爸爸]毆打[媽媽]":
        # write your code here
        pass

    if utterance == "[男友]對[我]動手":
        # write your code here
        pass

    return resultDICT