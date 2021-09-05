#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sexual_harassment

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
#list1
sexualHarassmentLIST = ["觸碰","毛手毛腳","抱","發生關係","黃腔","黃色笑話","聊色", "偷拍", "胸部", "裸照", "廁所", "跟他睡","屁股", "生殖器","貼著","口交","騷擾","摸","侵犯","接吻","偷看","打手槍","露鳥","奶","洗澡","屌","下海","霸王硬上弓","變態","做愛","強暴","腿","腰","肩","手心","自己","身體"]


DEBUG_sexual_harassment = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一", "計畫", "台大", "大便", "老公", "老婆", "阿公", "阿嬤", "閃", "另一半", "教授", "莫名其妙的人", "隔壁的人", "邊緣人", "競賽", "大隊接力", "上司", "副理", "這個月", "授權碼"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便", "寫論文", "痠", "沒空", "拳打腳踢", "脫魯", "背"], "asAdverb": ["很", "好", "太", "超", "蠻", "有點"], "asAdjective": ["雷", "舒服", "好多", "可怕", "可以"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sexual_harassment:
        print("[sexual_harassment] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[同學][一直]傳裸照給[我]":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"             
        pass

    if utterance == "[同學][一直]聊色":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學][一直]說黃色笑話":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學][一直]開黃腔":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]對[我]露鳥":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]對著[我]撫摸[他]的生殖器":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]拍[我]屁股":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]要[我]和[他]發生關係":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]要[我]跟[他]睡":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[同學]觸碰到[我]":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[我]被[人]亂摸":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]亂摸[我]":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]偷摸[我]的屁股":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]對[我]性騷擾":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]對[我]毛手毛腳":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]想跟[我][一起]洗澡":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[爸爸]想跟[我]發生關係":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[男友]對[我]霸王硬上弓":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[男友]逼迫[我]跟[他]接吻":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[男生]抱著[我]不放":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[老師]摳[我]的手心":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    if utterance == "[路人]對[我]露屌":
        # write your code here
        if any(e in inputSTR for e in sexualHarassmentLIST):
            resultDICT["source_sexual_harassment"] = "sexualHarassment"         
        pass

    return resultDICT