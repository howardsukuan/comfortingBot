#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for asking_for_help

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_asking_for_help = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_asking_for_help:
        print("[asking_for_help] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "想要建議":
        # write your code here
        if "建議" in inputSTR:
            resultDICT["advise"] = "suggestion"
        pass

    if utterance == "想要有[人]幫忙":
        # write your code here
        if "幫忙" and "想要" in inputSTR:
            resultDICT["advise"] = "suggestion"
        pass

    if utterance == "需要幫助":
        # write your code here
        if "需要" and "幫助" in inputSTR:
            resultDICT["advise"] = "suggestion"
        pass

    return resultDICT