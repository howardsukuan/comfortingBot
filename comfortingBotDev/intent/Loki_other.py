#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for other

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_other = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一", "計畫"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便", "寫論文"], "asAdverb": ["很", "好", "太", "超", "蠻", "有點"], "asAdjective": ["雷", "舒服", "好多"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_other:
        print("[other] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]沒有收到交換申請的回音":
        if "交換" in inputSTR:
            resultDICT["source"] = "exchange"
        pass

    if utterance == "[事情][無聊]到[不行]":
        if "無聊" in inputSTR:
            resultDICT["source"] = "boringWork"
        pass

    if utterance == "[事情][無聊]死了":
        if "無聊" in inputSTR:
            resultDICT["source"] = "boringWork"
        pass
    
    if utterance == "[事情]太多了不知道要怎麼辦":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[事情]好多，[好]煩":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[今天][天氣][好][冷]":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[今天][天氣][好]煩":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[今天][天氣]不好":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[今天][好][冷]":
        resultDICT["source"] = args[2]
        pass

    if utterance == "[今天]好多[事情]要做":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[作業][我][一直]拖":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業][我][一直]拖延":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[作業][我]不想面對":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[分數][很]難看":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[分數]不理想":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[分數]爆了":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[大掃除][一直]做不完":
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"
        pass

    if utterance == "[大掃除][一直]做不完[很]煩":
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone"
        pass

    if utterance == "[天氣][好][冷]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[工作]做不完":
        if "做不完" in inputSTR:
            resultDICT["source"] = "notDone" 
        pass

    if utterance == "[我][一直]拖延":
        if "拖延" in inputSTR:
            resultDICT["source"] = "notDone"          
        pass

    if utterance == "[我][筆電][最近]壞了":
        if "壞了" in inputSTR:
            resultDICT["source"] = "sthBroken"   
        pass

    if utterance == "[我][筆電][最近]壞掉了":
        if "壞掉了" in inputSTR:
            resultDICT["source"] = "sthBroken"  
        pass

    if utterance == "[我][筆電]壞了":
        if "壞了" in inputSTR:
            resultDICT["source"] = "sthBroken"   
        pass

    if utterance == "[我][筆電]壞掉了":
        if "壞掉了" in inputSTR:
            resultDICT["source"] = "sthBroken"   
        pass

    if utterance == "[我]不太確定[論文]的方向":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[我]不想寫[作業]":
        if "不想" in inputSTR:
            resultDICT["source"] = "notDone"   
        pass

    if utterance == "[我]不想面對[作業]":
        if "不想" in inputSTR:
            resultDICT["source"] = "notDone"   
        pass

    if utterance == "[我]不知道[我]的實驗在做什麼":
        if "實驗" in inputSTR:
            resultDICT["source"] = "thesis"   
        pass

    if utterance == "[我]不知道[我]的實驗在幹嘛":
        if "實驗" in inputSTR:
            resultDICT["source"] = "thesis"   
        pass

    if utterance == "[我]不知道[該]怎麼辦":
        if "該怎麼辦" in inputSTR:
            resultDICT["source"] = "whatToDo"  
        pass

    if utterance == "[我]不知道要怎麼辦":
        if "要怎麼辦" in inputSTR:
            resultDICT["source"] = "whatToDo"  
        pass

    if utterance == "[我]搶不到[演唱會][票]":
        resultDICT["source"] = args[2]
        pass

    if utterance == "[我]是[月光族]":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[我]每個月[都][月光]":
        resultDICT["source"] = args[2]
        pass

    if utterance == "[我]的[信用卡]帳單爆了":
        if "帳單爆了" in inputSTR:
            resultDICT["source"] = "poor"  
        pass

    if utterance == "[我]的[信用卡費]爆了":
        if "爆了" in inputSTR:
            resultDICT["source"] = "poor" 
        pass

    if utterance == "[我]的[存款][好]少":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[我]要吃土了":
        if "吃土" in inputSTR:
            resultDICT["source"] = "poor" 
        pass

    if utterance == "[我]買不到[票]":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[我]踩到[大][便]":
        if "大便" in inputSTR:
            resultDICT["source"] = "stepInPoop" 
        pass

    if utterance == "[我]踩到[屎]":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[我]踩到[狗][大][便]":
        if "大便" in inputSTR:
            resultDICT["source"] = "stepInPoop" 
        pass

    if utterance == "[我們]沒有[緣份]":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[早餐店][今天]休息":
        if "今天休息" in inputSTR:
            resultDICT["source"] = "notOpen" 
        pass

    if utterance == "[早餐店][今天]沒開":
        if "今天沒開" in inputSTR:
            resultDICT["source"] = "notOpen" 
        pass

    if utterance == "[早餐店]休息":
        if "休息" in inputSTR:
            resultDICT["source"] = "notOpen" 
        pass

    if utterance == "[早餐店]沒開":
        if "沒開" in inputSTR:
            resultDICT["source"] = "notOpen" 
        pass

    if utterance == "[東西][很]難吃":
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "[東西][超]噁心":
        if "噁心" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "[根本]是廚餘吧":
        if "廚餘" in inputSTR:
            resultDICT["source"] = "food" 
        pass

    if utterance == "[演唱會][票][好]難搶":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[演唱會][票][好]難買":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[演唱會][票]沒了":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[演唱會][票]沒搶到":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[演唱會][票]賣光了":
        resultDICT["source"] = args[1]
        pass

    if utterance == "[發票]又槓龜":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]又沒[中]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]沒[中]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[發票]沒有中獎":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[緣份]盡了":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[股票]丟了[好多]錢":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[股票]損失了[好多]錢":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[股票]虧了":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[股票]虧了[好多]錢":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[薪水]下來[一下子]就沒了":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[計畫][都]沒有進步":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫不完":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫得[不夠][細]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[論文]寫得[有點][爛]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[買一送一]沒有跟到":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[進度][都]趕不[上]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[進度]有點[落後]":
        if "落後" in inputSTR:
            resultDICT["source"] = args[0] 
        pass

    if utterance == "[進度]有點耽[誤]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "[都]沒辦法存錢":
        if "沒辦法存錢" in inputSTR:
            resultDICT["source"] = "noSavings"         
        # write your code here
        pass

    if utterance == "[錢][不夠][用]":
        if "不夠用" in inputSTR:
            resultDICT["source"] = "poor"  
        pass

    if utterance == "[電腦]壞了":
        if "壞了" in inputSTR:
            resultDICT["source"] = "sthBroken"  
        pass

    if utterance == "[電腦]壞掉了":
        if "壞掉了" in inputSTR:
            resultDICT["source"] = "sthBroken"  
        pass

    if utterance == "上課[好][累]":
        if "上課" in inputSTR:
            resultDICT["source"] = "school"  
        pass

    if utterance == "上課[很]煩":
        if "上課" in inputSTR:
            resultDICT["source"] = "school"  
        pass

    if utterance == "不想寫[作業]":
        if "不想" in inputSTR:
            resultDICT["source"] = "notDone"  
        pass

    if utterance == "不知道[該]怎麼辦":
        if "該怎麼辦" in inputSTR:
            resultDICT["source"] = "whatToDo"  
        pass

    if utterance == "不知道要怎麼辦":
        if "要怎麼辦" in inputSTR:
            resultDICT["source"] = "whatToDo"  
        pass

    if utterance == "交換[可能]不[會]上":
        if "交換" in inputSTR:
            resultDICT["source"] = "exchange"
        pass

    if utterance == "交換[可能]沒[機會]":
        if "交換" in inputSTR:
            resultDICT["source"] = "exchange"
        pass

    if utterance == "到[店][才]發現[今天]休息":
        if "休息" in inputSTR:
            resultDICT["source"] = args[0]
        pass

    if utterance == "吃到[香菜][好][可怕]":
        if "吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "吃到難吃的[東西]":
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "好多[事情]要做":
        resultDICT["source"] = args[0]
        pass

    if utterance == "存不到什麼[錢]":
        if "存不到" in inputSTR:
            resultDICT["source"] = "noSavings"
        pass

    if utterance == "實習[好][累]":
        if "實習" in inputSTR:
            resultDICT["source"] = "internship"
        pass

    if utterance == "實習[好]廢":
        if "實習" in inputSTR:
            resultDICT["source"] = "internship"
        pass

    if utterance == "實習[很]煩":
        if "實習" in inputSTR:
            resultDICT["source"] = "internship"
        pass

    if utterance == "我沒錢":
        if "沒錢" in inputSTR:
            resultDICT["source"] = "poor"
        pass

    if utterance == "投資失利了":
        if "失利" in inputSTR:
            resultDICT["source"] = "loseMoney"
        pass

    if utterance == "沒有考[上]喜歡的[學校]":
        if "考上" in inputSTR:
            resultDICT["source"] = "score"
        pass

    if utterance == "考試[好]低分":
        if "低分" in inputSTR:
            resultDICT["source"] = "score"
        pass

    if utterance == "考試不[及格]":
        if "不及格" in inputSTR:
            resultDICT["source"] = "score"
        pass

    if utterance == "要吃土了":
        if "吃土" in inputSTR:
            resultDICT["source"] = "poor"
        pass

    if utterance == "要看好多[論文]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "要讀好多[書]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "覺得[寫論文]壓力[很][大]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "覺得[很]難吃":
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "課[好]廢":
        if "課" in inputSTR:
            resultDICT["source"] = "school"
        pass

    if utterance == "跟[機會]擦肩而過":
        resultDICT["source"] = args[0]
        pass

    if utterance == "這個月[只][能]吃[吐司]了":
        if "吃吐司" in inputSTR:
            resultDICT["source"] = "poor"
        pass

    if utterance == "這個月要吃[吐司]了":
        if "吃吐司" in inputSTR:
            resultDICT["source"] = "poor"
        pass

    if utterance == "這家[店][東西][很]難吃":
        if "難吃" in inputSTR:
            resultDICT["source"] = "food"
        pass

    if utterance == "這次[發票]又沒[中]":
        resultDICT["source"] = args[0]
        pass

    if utterance == "還在等交換申請的[結果]":
        if "交換" in inputSTR:
            resultDICT["source"] = "exchange"
        pass

    if utterance == "錯過這次的[機會]了":
        resultDICT["source"] = args[0]
        pass

    if utterance == "限定[商品]沒有買到":
        resultDICT["source"] = args[0]
        pass

    return resultDICT