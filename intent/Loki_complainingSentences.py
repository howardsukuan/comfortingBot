#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for complainingSentences

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_complainingSentences = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_complainingSentences:
        print("[complainingSentences] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[下巴]太圓":
        # write your code here
        resultDICT["source"] = args[0]
        
        pass

    if utterance == "[世界][上]沒有我也可以":
        resultDICT["source"] = "mood"
        # write your code here
        pass
    if utterance == "[低空]飛過":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作品]被退件了":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業]不會寫":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業]不知道怎麼寫":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業]寫不出來":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業]想不出怎麼做":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業]想不出該怎麼做":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[分數]不理想":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[分數]很難看":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]不做事":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]不出現":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]做事不負責任但領的錢比我多":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]告我的狀":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]和我借錢不還":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]大雷人":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]放槍":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]有夠廢":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]無敵廢":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]耍廢":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]耍腦":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]超級雷":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]超雷":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[同事]難相處":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[嘴唇]很薄":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[天氣]不好":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[天氣]好冷":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[天氣]很糟":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[好窮]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[媽媽][一直]逼我婚":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[媽媽]覺得我吃太多":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[存款]太少":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[家人]過世了":
        # write your code here
        if "過世" in inputSTR:
            resultDICT["source"] = "death"
        pass

    if utterance == "[寵物]死掉了":
        # write your code here
        if "死掉" in inputSTR:
            resultDICT["source"] = "death"        
        pass

    if utterance == "[寵物]生病了":
        # write your code here
        resultDICT["source"] = "sick"
        pass

    if utterance == "[屁股]好大":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[工作]做不完":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[心]好累":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[我][很好]":
        # write your code here
        pass

    if utterance == "[我]好沒用":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[我]是廢物":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[我]被分手":
        # write your code here
        if "分手" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "[我]還[好]":
        # write your code here
        pass

    if utterance == "[手]超粗":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[旁邊]有噁心的[人]":
        # write your code here
        resultDICT["source"] = args[1]
        pass

    if utterance == "[旁邊]的[人][好臭]":
        # write your code here
        resultDICT["source"] = args[1]
        pass

    if utterance == "[月經]來":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[朋友]說我長得很醜":
        # write your code here
        if "我長得很醜" in inputSTR:
            resultDICT["source"] = "appearance"
        pass

    if utterance == "[東西]很難吃":
        # write your code here
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "[東西]超噁心":
        # write your code here
        if "噁心" in inputSTR:
            resultDICT["source"] = "food"        
        pass

    if utterance == "[比賽]輸了":
        # write your code here
        if "輸" in inputSTR:
            resultDICT["source"] = "lose"            
        pass

    if utterance == "[沒事]":
        # write your code here
        if "沒事" in inputSTR:
            resultDICT["source"] = "nothing"
        pass

    if utterance == "[男友]亂來":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]劈腿":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]垃圾":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]很渣":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]提分手":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]是渣":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]甩了我":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]說要分手":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]說要跟我分手":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男友]超渣":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[男朋友]怎麼可以這麼小氣":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]又槓龜":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]又沒[中]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]沒[中]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]沒有中獎":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[皮膚]好差":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[皺紋]長出來了":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[眼睛]太小":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[票]好少":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[票]好難搶":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[票]沒了":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[票]賣光了":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[票]超難買":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[老師]上課好無聊":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[老師]誤會我":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[老闆]叫我加班":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[肚子]咕嚕咕嚕叫":
        # write your code here
        if "咕嚕" in inputSTR:
            resultDICT["source"] = "hunger"
        pass

    if utterance == "[肚子]好餓":
        # write your code here
        if "餓" in inputSTR:
            resultDICT["source"] = "hunger"
        pass

    if utterance == "[肚子]很圓":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[肚子]餓了":
        # write your code here
        if "餓" in inputSTR:
            resultDICT["source"] = "hunger"
        pass

    if utterance == "[肩膀]痠痛":
        # write your code here
        if "痠痛" in inputSTR:
            resultDICT["source"] = "sick"        
        pass

    if utterance == "[胃]痛":
        # write your code here
        if "痛" in inputSTR:
            resultDICT["source"] = "sick"
        pass

    if utterance == "[腰痠]":
        # write your code here
        if "痠" in inputSTR:
            resultDICT["source"] = "sick"
        pass

    if utterance == "[腿]短":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[膚色]好黑":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[臉]非常長":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫不完":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫得不夠精細":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫得很爛":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[身高]太矮":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[錢]不夠用":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[電腦]壞掉了":
        # write your code here
        if "壞掉" in inputSTR:
            resultDICT["source"] = "broken"
        pass

    if utterance == "[頭]好痛":
        # write your code here
        if "痛" in inputSTR:
            resultDICT["source"] = "sick"        
        pass

    if utterance == "[額頭]很高":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[食物]好臭":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[髮質]很糟糕":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[髮際線]太[後面]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "[鼻子]不夠挺":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "一切正常":
        # write your code here
        if "一切正常" in inputSTR:
            resultDICT["source"] = args[0]
        pass

    if utterance == "上課[超累]":
        # write your code here
        if "上課" in inputSTR:
            resultDICT["source"] = "schoolLesson"
        pass

    if utterance == "上課很煩":
        # write your code here
        if "上課" in inputSTR:
            resultDICT["source"] = "schoolLesson"
        pass

    if utterance == "不想上班":
        # write your code here
        if "上班" in inputSTR:
            resultDICT["source"] = "work" 
        pass

    if utterance == "不知道該做什麼":
        # write your code here
        if "上班" in inputSTR:
            resultDICT["source"] = "work"
        pass

    if utterance == "什麼事都不想做":
        # write your code here
        if "什麼事" in inputSTR:
            resultDICT["source"] = "mood"        
        pass

    if utterance == "什麼事都做不好":
        # write your code here
        if "什麼事" in inputSTR:
            resultDICT["source"] = "mood"             
        pass

    if utterance == "到[店][裡]才發現[店]休息":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "只得[第二名]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "吃到[香菜]好可怕":
        # write your code here
        if "吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "吃到難吃的[東西]":
        # write your code here
        if "吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "喜歡的[人]不喜歡我":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的[人]對我無感":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的[人]有伴侶了":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的[人]有戀人了":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的[偶像]結婚了":
        # write your code here
        if "喜歡的偶像" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人不想談戀愛":
        # write your code here
        if "喜歡的偶像" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人拒絕我的告白":
        # write your code here
        if "喜歡的偶像" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人有[男朋友]了":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人說我們是[好閨密]":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人說我們是好哥們":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "喜歡的人說我們當[朋友]就好":
        # write your code here
        if "喜歡的人" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "嗯哼":
        # write your code here
        if "嗯哼" in inputSTR:
            resultDICT["source"] = "nothing"
        pass

    if utterance == "天氣爆差":
        # write your code here
        if "天氣" in inputSTR:
            resultDICT["source"] = "weather"
        pass

    if utterance == "失戀了":
        # write your code here
        if "失戀" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "好不想[工作]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "好低分不及格":
        # write your code here
        if "低分" in inputSTR:
            resultDICT["source"] = "score"
        pass

    if utterance == "好想下班":
        # write your code here
        if "下班" in inputSTR:
            resultDICT["source"] = "work"
        pass

    if utterance == "好想拉屎":
        # write your code here
        if "拉屎" in inputSTR:
            resultDICT["source"] = "tiolet"
        pass

    if utterance == "家[裡]大掃除[一直]做不完很煩":
        # write your code here
        if "大掃除" in inputSTR:
            resultDICT["source"] = "houseChore"
        pass

    if utterance == "對[未來]好迷茫":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "就覺得很煩":
        # write your code here
        if "煩" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "想[上]廁所":
        # write your code here
        if "廁所" in inputSTR:
            resultDICT["source"] = "tiolet"
        pass

    if utterance == "想[大]便":
        # write your code here
        if "大便" in inputSTR:
            resultDICT["source"] = "tiolet"
        pass

    if utterance == "想消失":
        # write your code here
        if "消失" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "感到不受重視":
        # write your code here
        if "不受重視" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "感到很有[壓力]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "感覺努力沒有被看見":
        # write your code here
        if "被看見" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "我[一直]交不到[男朋友]":
        # write your code here
        resultDICT["source"] = args[1]
        pass

    if utterance == "我好想自殺但又怕痛":
        # write your code here
        if "自殺" in inputSTR:
            resultDICT["source"] = "suicide"
        pass

    if utterance == "我搶不到[票]":
        # write your code here
        resultDICT["source"] = args[1]
        pass

    if utterance == "我被性騷擾":
        # write your code here
        if "性騷擾" in inputSTR:
            resultDICT["source"] = "sexualHarassment"
        pass

    if utterance == "我討厭自己":
        # write your code here
        if "自己" in inputSTR:
            resultDICT["source"] = "self"
        pass

    if utterance == "所有的[同事]都加薪了但沒有我":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "找不到[工作]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "提不起勁":
        # write your code here
        if "不起勁" in inputSTR:
            resultDICT["source"] = "cheerup" 
        pass

    if utterance == "有人性騷擾我":
        # write your code here
        if "性騷擾" in inputSTR:
            resultDICT["source"] = "sexualHarassment"
        pass

    if utterance == "沒人懂我":
        # write your code here
        if "懂我" in inputSTR:
            resultDICT["source"] = "mood" 
        pass

    if utterance == "沒什麼":
        # write your code here
        if "沒什麼" in inputSTR:
            resultDICT["source"] = "nothing" 
        pass

    if utterance == "沒吃飽":
        # write your code here
        if "沒吃飽" in inputSTR:
            resultDICT["source"] = "hunger" 
        pass

    if utterance == "沒得到[名次]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "沒有":
        # write your code here
        if "沒有" in inputSTR:
            resultDICT["source"] = "nothing"
        pass

    if utterance == "沒有[力氣]做事":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "沒有[朋友]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "沒有人聽我說話":
        # write your code here
        if "聽我說話" in inputSTR:
            resultDICT["source"] = "listen"
        pass

    if utterance == "沒有什麼事":
        # write your code here
        if "沒有" in  inputSTR:
            resultDICT["source"] = "nothing"
        pass

    if utterance == "沒有得名":
        # write your code here
        if "得名" in  inputSTR:
            resultDICT["source"] = "lose"
        pass

    if utterance == "沒有考[上]喜歡的[學校]":
        # write your code here
        if "考上" in  inputSTR:
            resultDICT["source"] = "score"
        pass

    if utterance == "生理[期]":
        # write your code here
        if "生理期" in inputSTR:
            resultDICT["source"] = "sick"
        pass

    if utterance == "申請了交換但[一直]沒有收到回音":
        # write your code here
        if "申請" in inputSTR:
            resultDICT["source"] = "exchange"
        pass

    if utterance == "腳踏[兩條]船":
        # write your code here
        if "腳踏" in inputSTR:
            resultDICT["source"] = "relationship"
        pass
        pass

    if utterance == "碰到噁男":
        # write your code here
        if "噁男" in inputSTR:
            resultDICT["source"] = "stranger"
        pass

    if utterance == "票秒殺":
        # write your code here
        if "票" in inputSTR:
            resultDICT["source"] = "ticket"
        pass

    if utterance == "老闆說我的能力不夠":
        # write your code here
        if "老闆" in inputSTR:
            resultDICT["source"] = "boss"
        pass

    if utterance == "考試[一大堆]不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"
        pass

    if utterance == "考試[一大堆]都不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試全部不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試全部都不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試大部分不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試大部分都不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試好多不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試好多都不會寫":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "考試考超差的":
        # write your code here
        if "考試" in inputSTR:
            resultDICT["source"] = "test"        
        pass

    if utterance == "自己[好渺小]":
        # write your code here
        if "渺小" in inputSTR:
            resultDICT["source"] = "mood"        
        pass

    if utterance == "莫名覺得憂鬱":
        # write your code here
        if "憂鬱" in inputSTR:
            resultDICT["source"] = "mood"              
        pass

    if utterance == "被[主管]罵了":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "被[主管]臭罵[一頓]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "被[主管]訓話":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "被[主管]說表現很差":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "被[男朋友]分手":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "被怪叔叔性騷擾":
        # write your code here
        if "性騷擾" in inputSTR:
            resultDICT["source"] = "sexualHarassment"
        pass

    if utterance == "被排擠":
        # write your code here
        if "排擠" in inputSTR:
            resultDICT["source"] = "bully"
        pass

    if utterance == "被甩了":
        # write your code here
        if "被甩" in inputSTR:
            resultDICT["source"] = "relationship"
        pass

    if utterance == "被說[很自私]":
        # write your code here
        if "被說" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "被說沒[禮貌]":
        # write your code here
        if "被說沒" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "被說目中無人":
        # write your code here
        if "被說" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "被說自我中心":
        # write your code here
        if "被說" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "要上班":
        # write your code here
        if "上班" in inputSTR:
            resultDICT["source"] = "work"
        pass

    if utterance == "要打[預防針]":
        # write your code here
        if "要打" in inputSTR:
            resultDICT["source"] = "afraid"
        pass

    if utterance == "覺得[孤單]":
        # write your code here
        if "覺得" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "覺得[工作]很累":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "覺得[我]不夠好":
        # write your code here
        if "不夠好" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "覺得很難吃":
        # write your code here
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "覺得微不足道":
        # write your code here
        if "微不足道" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "覺得被忽略":
        # write your code here
        if "忽略" in inputSTR:
            resultDICT["source"] = "mood"
        pass

    if utterance == "買不到[票]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "追的定[番]結束了":
        # write your code here
        if "結束" in inputSTR:
            resultDICT["source"] = "end"          
        pass

    if utterance == "遇到奇怪的人":
        # write your code here
        if "人" in inputSTR:
            resultDICT["source"] = "stranger"          
        pass

    if utterance == "那是廚餘吧":
        # write your code here
        if "廚餘" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "長[痘痘]":
        # write your code here
        resultDICT["source"] = args[0]
        pass

    if utterance == "限定[商品]沒有買到":
        # write your code here
        if "沒買到" in inputSTR:
            resultDICT["source"] = "stranger"          
        pass

    if utterance == "隔壁坐了[一個]莫名其妙的人":
        # write your code here
        if "人" in inputSTR:
            resultDICT["source"] = "stranger"          
        pass

    if utterance == "隔壁的人很吵":
        # write your code here
        if "人" in inputSTR:
            resultDICT["source"] = "stranger"  
        pass
    if utterance == "做惡夢":
        # args []
        if "惡夢" in inputSTR:
            resultDICT["source"] = "nightmare"  
        pass
    if utterance == "向我發牢騷":
        # args []
        if "牢騷" in inputSTR:
            resultDICT["source"] = "complain"  
        pass
    if utterance == "[早餐店]沒開":
        # args []
        if "沒開" in inputSTR:
            resultDICT["source"] = "notOpen"      
        pass

    return resultDICT