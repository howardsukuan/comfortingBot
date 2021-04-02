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
        if "不做事" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
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
        if "大雷人" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]放槍":
        # write your code here
        if "放槍" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]有夠廢":
        # write your code here
        if "有夠廢" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]無敵廢":
        # write your code here
        if "無敵廢" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]耍廢":
        # write your code here
        if "耍廢" or "耍腦" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]耍腦":
        # write your code here
        if "耍腦" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]超級雷":
        # write your code here
        if "超級雷" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass

    if utterance == "[同事]超雷":
        # write your code here
        if "超雷" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
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
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"        
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
            resultDICT["source"] = "competition"            
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
        if "今天很遭" in inputSTR:
            resultDICT["source"] = "mood"
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
            resultDICT["source"] = "toilet"
        pass

    if utterance == "家[裡]大掃除[一直]做不完很煩":
        # write your code here
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"
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
            resultDICT["source"] = "toilet"
        pass

    if utterance == "想[大]便":
        # write your code here
        if "大便" in inputSTR:
            resultDICT["source"] = "toilet"
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
            resultDICT["source"] = "competition"
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
    
    if utterance == "被[人]誤會":
        # args []   
        if "誤會" in inputSTR:
            resultDICT["source"] = "misunderstood"
        pass
    
    if utterance == "[事情]好無聊":
        # args []   
        if "無聊" in inputSTR:
            resultDICT["source"] = "boringWork"
        pass
    
    if utterance == "踩到[狗]大便":
        # args []  
        if "大便" in inputSTR:
            resultDICT["source"] = "stepInPoop"
        pass
    
    if utterance == "掃除做不完":
        # args []
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"        
        pass
    
    if utterance == "踩到大便":
          # args []
        if "大便" in inputSTR:
            resultDICT["source"] = "stepInPoop"
        pass
    
    if utterance == "覺得[自己]很廢":
        if "廢" in inputSTR:
            resultDICT["source"] = "useless"
        pass
    
    if utterance == "長得醜":
        if "長得醜" in inputSTR:
            resultDICT["source"] = "appearance"
        pass
    
    if utterance == "[大家]都好厲害":
        if "好厲害" in inputSTR:
            resultDICT["source"] = "wit"
        pass
    
    if utterance == "[自己]就是[一個][廢物]":
        resultDICT["source"] = args[2]
        pass
    
    if utterance == "[同事]很煩":
        resultDICT["source"] = args[0]
        pass 
    
    if utterance == "要我解釋[問題]":
        resultDICT["source"] = args[0]
        pass    
    
    if utterance == "又問我同樣的[東西]":
        resultDICT["source"] = args[0]
        pass  
    
    if utterance == "不知道要怎麼辦":
        if "不知道要怎麼辦" in inputSTR:
            resultDICT["source"] = "whattodo"
        pass
    
    if utterance == "不知道該怎麼辦":
        if "不知道該怎麼辦" in inputSTR:
            resultDICT["source"] = "whattodo"
        pass
    
    if utterance == "[常常]生病":
        if "生病" in inputSTR:
            resultDICT["source"] = "sick"
        pass
    
    if utterance == "[進度]就會延遲":
        resultDICT["source"] = args[0]
        pass  
    
    if utterance == "就是惡性循環":
        if "惡性循環" in inputSTR:
            resultDICT["source"] = "progress"
        pass
    
    if utterance == "要讀[好多][書]":
        resultDICT["source"] = args[1]
        pass        
        
    if utterance == "做不完的感覺":
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"
        pass
    
    if utterance == "有好多[事情]要做":
        resultDICT["source"] = args[0]
        pass  
    
    if utterance == "時間感覺都不夠用":
        if "時間" in inputSTR:
            resultDICT["source"] = "timemanagement"
        pass
    
    if utterance == "想留[一點]時間給自己":
        if "時間" in inputSTR:
            resultDICT["source"] = "timemanagement"
        pass
    
    if utterance == "想留點時間給自己":
        if "時間" in inputSTR:
            resultDICT["source"] = "timemanagement"
        pass
    
    if utterance == "[周圍]的人都很努力進修":
        if "周圍的人" in inputSTR:
            resultDICT["source"] = "otherpeople"
        pass
    
    if utterance == "身邊的人都很聰明":
        if "身邊的人" in inputSTR:
            resultDICT["source"] = "otherpeople"
        pass
    
    if utterance == "存不到什麼錢":
        if "錢" in inputSTR:
            resultDICT["source"] = "money"
        pass
    
    if utterance == "[薪水]下來[一下子]就沒了":
        resultDICT["source"] = args[0]
        pass  
    
    if utterance == "都不能存錢":
        if "錢" in inputSTR:
            resultDICT["source"] = "money"
        pass
    
    if utterance == "給爸媽生活費":
        if "生活費" in inputSTR:
            resultDICT["source"] = "money"
        pass
    
    if utterance == "朋友都說他很忙":
        if "朋友都說他很忙" in inputSTR:
            resultDICT["source"] = "friend"
        pass
    
    if utterance == "朋友說他很忙":
        if "朋友說他很忙" in inputSTR:
            resultDICT["source"] = "friend"
        pass
    
    if utterance == "都說很忙":
        if "都說很忙" in inputSTR:
            resultDICT["source"] = "friend"
        pass
    
    if utterance == "都說沒空":
        if "沒空" in inputSTR:
            resultDICT["source"] = "timemanagement"
        pass
    
    if utterance == "忘記我的[生日]":
        if "忘記我的生日" in inputSTR:
            resultDICT["source"] = "forgetYou"
        pass
    
    if utterance == "忘記我[生日]":
        if "忘記我生日" in inputSTR:
            resultDICT["source"] = "forgetYou"
        pass
    
    if utterance == "都不會忘記":
        if "都不會忘記" in inputSTR:
            resultDICT["source"] = "forgetYou"
        pass
    
    if utterance == "[任務]很難做":
        resultDICT["source"] = args[0]
        pass         
        
    if utterance == "不給我任何方向":
        if "不給我任何方向" in inputSTR:
            resultDICT["source"] = "schoolwork"
        pass
    
    if utterance == "不給我方向":
        if "不給我方向" in inputSTR:
            resultDICT["source"] = "schoolwork"
        pass
    
    if utterance == "[事情]做不好":
        if "做不好" in inputSTR:
            resultDICT["source"] = "perfection"
        pass
    
    if utterance == "如果做不好":
        if "做不好" in inputSTR:
            resultDICT["source"] = "perfection"
        pass
    
    if utterance == "壓力很大":
        if "壓力" in inputSTR:
            resultDICT["source"] = "progress"
        pass
    
    if utterance == "沒有任何人可以訴苦":
        if "訴苦" in inputSTR:
            resultDICT["source"] = "complainToYou"
        pass
    
    if utterance == "很不快樂":
        if "不快樂" in inputSTR:
            resultDICT["source"] = "others"
        pass
        
    if utterance == "沒生活品質":
        if "沒生活品質" in inputSTR:
            resultDICT["source"] = "lifequality"
        pass
    
    if utterance == "[一直]碎碎念":
        if "碎碎念" in inputSTR:
            resultDICT["source"] = "complainToYou"
        pass
    
    if utterance == "不接受":
        if "不接受" in inputSTR:
            resultDICT["source"] = "complainToYou"
        pass
    
    if utterance == "[男友]不愛我":
        resultDICT["source"] = args[0]
        pass          
    
    if utterance == "起了口角":
        if "起了口角" in inputSTR:
            resultDICT["source"] = "quarrel"
        pass
    
    if utterance == "[同學]好虛偽":
        if "虛偽" in inputSTR:
            resultDICT["source"] = "friend"
        pass 
    
    if utterance == "報告要同[一組]":
        if "報告" in inputSTR:
            resultDICT["source"] = "colleagueLEI"
        pass 
    
    if utterance == "祝福都沒有收到":
        if "祝福都沒有收到" in inputSTR:
            resultDICT["source"] = "forgetYou"
        pass
    
    if utterance == "利用我":
        if "利用我" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass
    
    if utterance == "予取予求":
        if "予取予求" in inputSTR:
            resultDICT["source"] = "friend"        
        pass
    
    if utterance == "說我壞話":
        if "壞話" in inputSTR:
            resultDICT["source"] = "friend"        
        pass
        
    if utterance == "好偏心":
        if "偏心" in inputSTR:
            resultDICT["source"] = "negMood"        
        pass
    
    if utterance == "吃力不討好的工作":
        if "吃力不討好的工作" in inputSTR:
            resultDICT["source"] = "colleagueLEI"        
        pass
    
    if utterance == "要我背黑鍋":
        if "背黑鍋" in inputSTR:
            resultDICT["source"] = "colleagueLEI"                
        pass
    
    if utterance == "常消失不見":
        if "消失不見" in inputSTR:
            resultDICT["source"] = "others"                
        pass
    
    if utterance == "我覺得[媽媽]討厭我":
           # args [媽媽]
        resultDICT["source"] = args[0]
    
    if utterance == "我心好累":
        # args []
        if "心好累" in inputSTR:
            resultDICT["source"] = "mood"
    
    if utterance == "我覺得很煩":
        # args []
        if "覺得很煩" in inputSTR:
            resultDICT["source"] = "mood" 
    
    if utterance == "我不太確定論文的方向":
        # args []
        if "不太確定論文的方向" in inputSTR:
            resultDICT["source"] = "thesis" 
    if utterance == "[今天]好多事情要做，好煩":
        # args [今天]
        if "好煩" in inputSTR:
            resultDICT["source"] = "notDone" 
    if utterance == "事情太多了不知道要怎麼辦":
        # args []
        if "事情太多了" in inputSTR:
            resultDICT["source"] = "notDone" 
        
    if utterance == "我很胖":
        # args [] 
        if "胖" in inputSTR:
            resultDICT["source"] = "appearance"

    if utterance == "我覺得別人不喜歡我":
        # args []
        if "別人不喜歡我" in inputSTR:
            resultDICT["source"] = "otherpeople" 
    if utterance == "有人說我很貪心":
        # args [] 
        if "有人說我很貪心" in inputSTR:
            resultDICT["source"] = "otherpeople"
    if utterance == "事情都不順我的意很討厭":
        # args []
        if "事情都不順" in inputSTR:
            resultDICT["source"] = "rough"
    if utterance == "同學同組都不說話":
        # args []
        if "同組都不說話" in inputSTR:
            resultDICT["source"] = "badTeamMate"
    if utterance == "[同學]做報告都沒有貢獻怎麼辦":
        # args [同學]
        if "做報告都沒有貢獻" in inputSTR:
            resultDICT["source"] = "badTeamMate"
    if utterance == "[同學]只想從我這邊拿成果":
        # args [同學]
        if "只想從我這邊拿成果" in inputSTR:
            resultDICT["source"] = "badTeamMate"
    if utterance == "我在[小組][裡面]很自卑 ":
        # args [小組, 裡面]
        if "很自卑" in inputSTR:
            resultDICT["source"] = "lowSelfEsteem"        
        
            
            
        

    return resultDICT