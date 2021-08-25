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
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便"], "asAdverb": ["很", "好", "太", "超", "蠻"], "asAdjective": ["雷", "舒服"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_domestic_violence:
        print("[domestic_violence] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[哥哥][一直]打[我]":
        # write your code here
        pass

    if utterance == "[媽媽]因為[我]成績退步[一直]打[我]":
        # write your code here
        pass

    if utterance == "[我]被[爸爸]打":
        # write your code here
        pass

    if utterance == "[我]被[爸爸]揍":
        # write your code here
        pass

    if utterance == "[我]被[爸爸]虐待":
        # write your code here
        pass

    if utterance == "[我]被家人打得半死":
        # write your code here
        pass

    if utterance == "[我]被家人揍到流血":
        # write your code here
        pass

    if utterance == "[爸爸][一直]傷害[我]":
        # write your code here
        pass

    if utterance == "[爸爸][一直]扁[我]":
        # write your code here
        pass

    if utterance == "[爸爸][一直]抓[我]的頭去撞牆":
        # write your code here
        pass

    if utterance == "[爸爸][一直]揍[我]":
        # write your code here
        pass

    if utterance == "[爸爸][一直]踢[我]":
        # write your code here
        pass

    if utterance == "[爸爸][常常]對[我]使用言語暴力":
        # write your code here
        pass

    if utterance == "[爸爸][常常]對[我]罵髒話":
        # write your code here
        pass

    if utterance == "[爸爸][常常]罵[我]髒話":
        # write your code here
        pass

    if utterance == "[爸爸][常常]賞[我]巴掌":
        # write your code here
        pass

    if utterance == "[爸爸]向[我]揮拳":
        # write your code here
        pass

    if utterance == "[爸爸]喝醉就揍[我]":
        # write your code here
        pass

    if utterance == "[爸爸]喝醉酒回來就打[媽]":
        # write your code here
        pass

    if utterance == "[爸爸]家暴[我]":
        # write your code here
        pass

    if utterance == "[爸爸]對[我]使用暴力":
        # write your code here
        pass

    if utterance == "[爸爸]對[我]動粗":
        # write your code here
        pass

    if utterance == "[爸爸]對[我]拳打腳踢":
        # write your code here
        pass

    if utterance == "[爸爸]對[我]施暴":
        # write your code here
        pass

    if utterance == "[爸爸]心情不好就打[我]":
        # write your code here
        pass

    if utterance == "[爸爸]心情不好就揍[我]":
        # write your code here
        pass

    if utterance == "[爸爸]打[我]":
        # write your code here
        pass

    if utterance == "[爸爸]把[我]打到流血":
        # write your code here
        pass

    if utterance == "[爸爸]把[我]打到瘀青":
        # write your code here
        pass

    if utterance == "[爸爸]把[我]抓起來摔":
        # write your code here
        pass

    if utterance == "[爸爸]把[我]鎖在家[裡]":
        # write your code here
        pass

    if utterance == "[爸爸]拿熱水潑[我]":
        # write your code here
        pass

    if utterance == "[爸爸]拿菸燙[我]":
        # write your code here
        pass

    if utterance == "[爸爸]拿藤條抽[我]":
        # write your code here
        pass

    if utterance == "[爸爸]毆打[媽媽]":
        # write your code here
        pass

    if utterance == "[爸爸]用拳頭打[我]":
        # write your code here
        pass

    if utterance == "[爸爸]用言語辱罵[我]":
        # write your code here
        pass

    if utterance == "[爸爸]痛毆[我]":
        # write your code here
        pass

    if utterance == "[爸爸]要打死[我]":
        # write your code here
        pass

    if utterance == "[爸爸]要殺掉[我]":
        # write your code here
        pass

    if utterance == "[爸爸]說要打死[我]":
        # write your code here
        pass

    if utterance == "[爸爸]說要殺掉[我]":
        # write your code here
        pass

    if utterance == "[爸爸]限制[我]出門的[自由]":
        # write your code here
        pass

    if utterance == "我[姊][剛剛][毫無]原因就揍[我]":
        # write your code here
        pass

    if utterance == "男友對[我]動手":
        # write your code here
        pass

    return resultDICT