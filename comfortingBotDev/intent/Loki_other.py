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
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便"], "asAdverb": ["很", "好", "太", "超", "蠻"], "asAdjective": ["雷", "舒服"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_other:
        print("[other] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]沒有收到交換申請的回音":
        # write your code here
        pass

    if utterance == "[事情]太多了不知道要怎麼辦":
        # write your code here
        pass

    if utterance == "[今天]天氣不好":
        # write your code here
        pass

    if utterance == "[今天]天氣好[冷]":
        # write your code here
        pass

    if utterance == "[今天]天氣好煩":
        # write your code here
        pass

    if utterance == "[今天]天氣很[糟]":
        # write your code here
        pass

    if utterance == "[今天]好[冷]":
        # write your code here
        pass

    if utterance == "[今天]好多事情要做":
        # write your code here
        pass

    if utterance == "[分數]不理想":
        # write your code here
        pass

    if utterance == "[分數]很難看":
        # write your code here
        pass

    if utterance == "[天氣]好[冷]":
        # write your code here
        pass

    if utterance == "[工作]做不完":
        # write your code here
        pass

    if utterance == "[我][一直]拖延":
        # write your code here
        pass

    if utterance == "[我]不太確定論文的方向":
        # write your code here
        pass

    if utterance == "[我]不想寫[作業]":
        # write your code here
        pass

    if utterance == "[我]不想面對作業":
        # write your code here
        pass

    if utterance == "[我]不知道[我]的實驗在做什麼":
        # write your code here
        pass

    if utterance == "[我]不知道[我]的實驗在幹嘛":
        # write your code here
        pass

    if utterance == "[我]不知道[該]怎麼辦":
        # write your code here
        pass

    if utterance == "[我]不知道要怎麼辦":
        # write your code here
        pass

    if utterance == "[我]搶不到演唱會票":
        # write your code here
        pass

    if utterance == "[我]是月光族":
        # write your code here
        pass

    if utterance == "[我]每個月[都][月光]":
        # write your code here
        pass

    if utterance == "[我]的[筆電][最近]壞掉了":
        # write your code here
        pass

    if utterance == "[我]的信用卡帳單爆了":
        # write your code here
        pass

    if utterance == "[我]的信用卡費爆了":
        # write your code here
        pass

    if utterance == "[我]的存款太少":
        # write your code here
        pass

    if utterance == "[我]的存款好少":
        # write your code here
        pass

    if utterance == "[我]筆電[最近]壞了":
        # write your code here
        pass

    if utterance == "[我]筆電[最近]壞掉了":
        # write your code here
        pass

    if utterance == "[我]筆電壞了":
        # write your code here
        pass

    if utterance == "[我]筆電壞掉了":
        # write your code here
        pass

    if utterance == "[我]要吃土了":
        # write your code here
        pass

    if utterance == "[我]買不到票":
        # write your code here
        pass

    if utterance == "[我]踩到[大][便]":
        # write your code here
        pass

    if utterance == "[我]踩到屎":
        # write your code here
        pass

    if utterance == "[我]踩到狗[大][便]":
        # write your code here
        pass

    if utterance == "[我]踩到狗屎":
        # write your code here
        pass

    if utterance == "[我們]沒有緣份":
        # write your code here
        pass

    if utterance == "[早餐店]沒開":
        # write your code here
        pass

    if utterance == "[東西]很難吃":
        # write your code here
        pass

    if utterance == "[發票]又槓龜":
        # write your code here
        pass

    if utterance == "[發票]又沒[中]":
        # write your code here
        pass

    if utterance == "[發票]沒[中]":
        # write your code here
        pass

    if utterance == "[發票]沒有中獎":
        # write your code here
        pass

    if utterance == "[緣份]盡了":
        # write your code here
        pass

    if utterance == "[股票]虧了":
        # write your code here
        pass

    if utterance == "[薪水]下來[一下子]就沒了":
        # write your code here
        pass

    if utterance == "[論文]寫不完":
        # write your code here
        pass

    if utterance == "[都]沒有進步":
        # write your code here
        pass

    if utterance == "[都]沒辦法存錢":
        # write your code here
        pass

    if utterance == "[錢][不夠][用]":
        # write your code here
        pass

    if utterance == "[電腦]壞掉了":
        # write your code here
        pass

    if utterance == "上課好[累]":
        # write your code here
        pass

    if utterance == "上課很煩":
        # write your code here
        pass

    if utterance == "上課超[累]":
        # write your code here
        pass

    if utterance == "不想寫[作業]":
        # write your code here
        pass

    if utterance == "不知道[該]怎麼辦":
        # write your code here
        pass

    if utterance == "不知道要怎麼辦":
        # write your code here
        pass

    if utterance == "事情[無聊]到[不行]":
        # write your code here
        pass

    if utterance == "事情[無聊]死了":
        # write your code here
        pass

    if utterance == "事情好多，好煩":
        # write your code here
        pass

    if utterance == "交換[可能]不[會]上":
        # write your code here
        pass

    if utterance == "交換[可能]沒機會":
        # write your code here
        pass

    if utterance == "作業[我][一直]拖":
        # write your code here
        pass

    if utterance == "作業[我][一直]拖延":
        # write your code here
        pass

    if utterance == "作業[我]不想面對":
        # write your code here
        pass

    if utterance == "做不完的感覺":
        # write your code here
        pass

    if utterance == "分數爆了":
        # write your code here
        pass

    if utterance == "到店[裡][才]發現[今天]休息":
        # write your code here
        pass

    if utterance == "吃到難吃的[東西]":
        # write your code here
        pass

    if utterance == "吃到香菜好[可怕]":
        # write your code here
        pass

    if utterance == "大掃除[一直]做不完":
        # write your code here
        pass

    if utterance == "大掃除[一直]做不完很煩":
        # write your code here
        pass

    if utterance == "天氣好[熱]":
        # write your code here
        pass

    if utterance == "好多事情要做":
        # write your code here
        pass

    if utterance == "存不到什麼[錢]":
        # write your code here
        pass

    if utterance == "實習好[累]":
        # write your code here
        pass

    if utterance == "實習好廢":
        # write your code here
        pass

    if utterance == "實習很煩":
        # write your code here
        pass

    if utterance == "實習超[累]":
        # write your code here
        pass

    if utterance == "我沒錢":
        # write your code here
        pass

    if utterance == "投資失利了":
        # write your code here
        pass

    if utterance == "早餐店[今天]休息":
        # write your code here
        pass

    if utterance == "早餐店[今天]沒開":
        # write your code here
        pass

    if utterance == "早餐店休息":
        # write your code here
        pass

    if utterance == "東西超噁心":
        # write your code here
        pass

    if utterance == "沒有考[上]喜歡的[學校]":
        # write your code here
        pass

    if utterance == "演唱會票好難搶":
        # write your code here
        pass

    if utterance == "演唱會票好難買":
        # write your code here
        pass

    if utterance == "演唱會票沒了":
        # write your code here
        pass

    if utterance == "演唱會票沒搶到":
        # write your code here
        pass

    if utterance == "演唱會票賣光了":
        # write your code here
        pass

    if utterance == "考試不[及格]":
        # write your code here
        pass

    if utterance == "考試好低分":
        # write your code here
        pass

    if utterance == "股票丟了好多錢":
        # write your code here
        pass

    if utterance == "股票損失了好多錢":
        # write your code here
        pass

    if utterance == "股票虧了好多錢":
        # write your code here
        pass

    if utterance == "要吃土了":
        # write your code here
        pass

    if utterance == "要看好多論文":
        # write your code here
        pass

    if utterance == "要讀好多書":
        # write your code here
        pass

    if utterance == "覺得寫論文[壓力]很[大]":
        # write your code here
        pass

    if utterance == "覺得很難吃":
        # write your code here
        pass

    if utterance == "課好廢":
        # write your code here
        pass

    if utterance == "論文[不夠][精緻]":
        # write your code here
        pass

    if utterance == "論文寫得[不夠][細]":
        # write your code here
        pass

    if utterance == "論文寫得有[點][爛]":
        # write your code here
        pass

    if utterance == "買一送一沒有跟到":
        # write your code here
        pass

    if utterance == "跟[機會]擦肩而過":
        # write your code here
        pass

    if utterance == "這個月[只][能]吃[吐司]了":
        # write your code here
        pass

    if utterance == "這個月要吃[吐司]了":
        # write your code here
        pass

    if utterance == "這家店[東西]很難吃":
        # write your code here
        pass

    if utterance == "這次發票又沒[中]":
        # write your code here
        pass

    if utterance == "進度[都]趕不[上]":
        # write your code here
        pass

    if utterance == "進度有[點][落後]":
        # write your code here
        pass

    if utterance == "進度有[點]耽[誤]":
        # write your code here
        pass

    if utterance == "還在等交換申請的結果":
        # write your code here
        pass

    if utterance == "那是廚餘吧":
        # write your code here
        pass

    if utterance == "錯過這次的[機會]了":
        # write your code here
        pass

    if utterance == "限定[商品]沒有買到":
        # write your code here
        pass

    if utterance == "電腦壞了":
        # write your code here
        pass

    return resultDICT