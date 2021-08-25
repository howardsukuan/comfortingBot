#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for interpersonal

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_interpersonal = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便"], "asAdverb": ["很", "好", "太", "超", "蠻"], "asAdjective": ["雷", "舒服"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_interpersonal:
        print("[interpersonal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]碎碎念":
        # write your code here
        pass

    if utterance == "[同事][無敵]廢":
        # write your code here
        pass

    if utterance == "[同事][超]雷":
        # write your code here
        pass

    if utterance == "[同事][難]相處":
        # write your code here
        pass

    if utterance == "[同事]不做事":
        # write your code here
        pass

    if utterance == "[同事]不出現":
        # write your code here
        pass

    if utterance == "[同事]做事不負責任但領的[錢]比[我]多":
        # write your code here
        pass

    if utterance == "[同事]告[我]的狀":
        # write your code here
        pass

    if utterance == "[同事]和[我]借錢不還":
        # write your code here
        pass

    if utterance == "[同事]大雷人":
        # write your code here
        pass

    if utterance == "[同事]放槍":
        # write your code here
        pass

    if utterance == "[同事]有夠廢":
        # write your code here
        pass

    if utterance == "[同事]耍廢":
        # write your code here
        pass

    if utterance == "[同事]耍腦":
        # write your code here
        pass

    if utterance == "[同事]超級雷":
        # write your code here
        pass

    if utterance == "[同學][只]想從[我]這邊拿成果":
        # write your code here
        pass

    if utterance == "[同學]做報告[都]沒有貢獻":
        # write your code here
        pass

    if utterance == "[同學]好虛偽":
        # write your code here
        pass

    if utterance == "[同組同學][都]不說話":
        # write your code here
        pass

    if utterance == "[周圍的人][都][很]努力進修":
        # write your code here
        pass

    if utterance == "[喜歡的人]不喜歡[我]":
        # write your code here
        pass

    if utterance == "[喜歡的人]不想談戀愛":
        # write your code here
        pass

    if utterance == "[喜歡的人]對[我]無感":
        # write your code here
        pass

    if utterance == "[喜歡的人]拒絕[我]的告白":
        # write your code here
        pass

    if utterance == "[喜歡的人]有[男朋友]了":
        # write your code here
        pass

    if utterance == "[喜歡的人]有伴侶了":
        # write your code here
        pass

    if utterance == "[喜歡的人]有戀人了":
        # write your code here
        pass

    if utterance == "[喜歡的人]說[我們]是好哥們":
        # write your code here
        pass

    if utterance == "[喜歡的人]說[我們]是好閨密":
        # write your code here
        pass

    if utterance == "[喜歡的人]說[我們]當朋友就[好]":
        # write your code here
        pass

    if utterance == "[女友]有[嚴重]潔癖":
        # write your code here
        pass

    if utterance == "[媽媽][一直]逼[我]婚":
        # write your code here
        pass

    if utterance == "[媽媽]覺得[我]吃太多":
        # write your code here
        pass

    if utterance == "[家人]生病了":
        # write your code here
        pass

    if utterance == "[家人]過世了":
        # write your code here
        pass

    if utterance == "[寵物]死掉了":
        # write your code here
        pass

    if utterance == "[我][男友]好摳":
        # write your code here
        pass

    if utterance == "[我]什麼[時候]才[能]換[女友]呢":
        # write your code here
        pass

    if utterance == "[我]是邊緣人":
        # write your code here
        pass

    if utterance == "[我]的[寵物][最近]生病了":
        # write your code here
        pass

    if utterance == "[我]被分手":
        # write your code here
        pass

    if utterance == "[我]覺得[媽媽]討厭[我]":
        # write your code here
        pass

    if utterance == "[我]身體不舒服":
        # write your code here
        pass

    if utterance == "[教授]觀念很保守":
        # write your code here
        pass

    if utterance == "[最近]跟[家裡的人]吵架了":
        # write your code here
        pass

    if utterance == "[朋友]予取予求":
        # write your code here
        pass

    if utterance == "[朋友]吵架了":
        # write your code here
        pass

    if utterance == "[朋友]說[他][很]忙":
        # write your code here
        pass

    if utterance == "[朋友]說[我]壞話":
        # write your code here
        pass

    if utterance == "[朋友]鬧得不[愉快]":
        # write your code here
        pass

    if utterance == "[比賽]輸了":
        # write your code here
        pass

    if utterance == "[狗狗][都]不吃飯":
        # write your code here
        pass

    if utterance == "[狗狗]亂大小便":
        # write your code here
        pass

    if utterance == "[男友][最近][都]很少陪[我]":
        # write your code here
        pass

    if utterance == "[男友]亂來":
        # write your code here
        pass

    if utterance == "[男友]劈腿":
        # write your code here
        pass

    if utterance == "[男友]垃圾":
        # write your code here
        pass

    if utterance == "[男友]很渣":
        # write your code here
        pass

    if utterance == "[男友]提分手":
        # write your code here
        pass

    if utterance == "[男友]是渣":
        # write your code here
        pass

    if utterance == "[男友]甩了[我]":
        # write your code here
        pass

    if utterance == "[男友]相處時間變少":
        # write your code here
        pass

    if utterance == "[男友]說要分手":
        # write your code here
        pass

    if utterance == "[男友]說要跟[我]分手":
        # write your code here
        pass

    if utterance == "[男友]超渣":
        # write your code here
        pass

    if utterance == "[男朋友]怎麼這麼小氣":
        # write your code here
        pass

    if utterance == "[老師]上課好無聊":
        # write your code here
        pass

    if utterance == "[老師]誤會[我]":
        # write your code here
        pass

    if utterance == "[老闆]叫[我]加班":
        # write your code here
        pass

    if utterance == "[老闆]說[我]的能力[不夠]":
        # write your code here
        pass

    if utterance == "[身邊的人][都]很聰明":
        # write your code here
        pass

    if utterance == "[遠距離]好痛苦":
        # write your code here
        pass

    if utterance == "[阿公][很]煩":
        # write your code here
        pass

    if utterance == "分組報告[組員][都]在擺爛":
        # write your code here
        pass

    if utterance == "別人不喜歡[我]":
        # write your code here
        pass

    if utterance == "向我發牢騷":
        # write your code here
        pass

    if utterance == "失戀了":
        # write your code here
        pass

    if utterance == "好想交[男友]":
        # write your code here
        pass

    if utterance == "好想脫魯":
        # write your code here
        pass

    if utterance == "對[男友]沒感覺":
        # write your code here
        pass

    if utterance == "忘記[我]的[生日]":
        # write your code here
        pass

    if utterance == "有人說[我]很貪心":
        # write your code here
        pass

    if utterance == "沒人找[我][一組]":
        # write your code here
        pass

    if utterance == "沒有[任何]人[可以]訴苦":
        # write your code here
        pass

    if utterance == "沒有[朋友]":
        # write your code here
        pass

    if utterance == "沒有人聽[我]說話":
        # write your code here
        pass

    if utterance == "沒有得名":
        # write your code here
        pass

    if utterance == "碰到[噁男]":
        # write your code here
        pass

    if utterance == "祝福[都]沒有收到":
        # write your code here
        pass

    if utterance == "腳踏[兩條]船":
        # write your code here
        pass

    if utterance == "被[主管]臭罵[一頓]":
        # write your code here
        pass

    if utterance == "被[主管]訓話":
        # write your code here
        pass

    if utterance == "被[主管]說表現很差":
        # write your code here
        pass

    if utterance == "被[人]誤會":
        # write your code here
        pass

    if utterance == "被甩了":
        # write your code here
        pass

    if utterance == "跟[爸媽]很[難]溝通":
        # write your code here
        pass

    if utterance == "遇到[奇怪的人]":
        # write your code here
        pass

    if utterance == "隔壁坐了[一個]莫名其妙的[人]":
        # write your code here
        pass

    if utterance == "隔壁的[人]很吵":
        # write your code here
        pass

    return resultDICT