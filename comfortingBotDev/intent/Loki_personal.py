#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for personal

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_personal = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便"], "asAdverb": ["很", "好", "太", "超", "蠻"], "asAdjective": ["雷", "舒服"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_personal:
        print("[personal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]被奪命[連環]call[超級]煩":
        # write your code here
        pass

    if utterance == "[下巴]太圓":
        # write your code here
        pass

    if utterance == "[今天]很遭":
        # write your code here
        pass

    if utterance == "[作品]被退件了":
        # write your code here
        pass

    if utterance == "[作業]不[會]寫":
        # write your code here
        pass

    if utterance == "[作業]不知道怎麼寫":
        # write your code here
        pass

    if utterance == "[作業]寫不出來":
        # write your code here
        pass

    if utterance == "[作業]想不出[該][怎麼]做":
        # write your code here
        pass

    if utterance == "[作業]想不出怎麼做":
        # write your code here
        pass

    if utterance == "[分數]不理想":
        # write your code here
        pass

    if utterance == "[分數]很難看":
        # write your code here
        pass

    if utterance == "[只]想[每天]躲在宿舍":
        # write your code here
        pass

    if utterance == "[嘴唇]很薄":
        # write your code here
        pass

    if utterance == "[常常]生病":
        # write your code here
        pass

    if utterance == "[我][一直]做[可怕]的夢":
        # write your code here
        pass

    if utterance == "[我][只]要想[自己][一個]人待著":
        # write your code here
        pass

    if utterance == "[我][常常]睡[不飽]":
        # write your code here
        pass

    if utterance == "[我][每天][都]睡不著":
        # write your code here
        pass

    if utterance == "[我][總是]在人[前]壓抑[自己]的情[緒然][後]在人[後]又[獨自][悲傷]":
        # write your code here
        pass

    if utterance == "[我][能]找得到工作嗎":
        # write your code here
        pass

    if utterance == "[我][能]考[上]台[大]嗎":
        # write your code here
        pass

    if utterance == "[我]什麼[時候]才[能]換工作呢":
        # write your code here
        pass

    if utterance == "[我]吃壞肚子了":
        # write your code here
        pass

    if utterance == "[我]在小組[裡面]很自卑":
        # write your code here
        pass

    if utterance == "[我]好[醜]":
        # write your code here
        pass

    if utterance == "[我]好沒用":
        # write your code here
        pass

    if utterance == "[我]很不喜歡我[自己]":
        # write your code here
        pass

    if utterance == "[我]心好[累]":
        # write your code here
        pass

    if utterance == "[我]是[廢物]":
        # write your code here
        pass

    if utterance == "[我]看不到[未來]":
        # write your code here
        pass

    if utterance == "[我]覺得[很]煩":
        # write your code here
        pass

    if utterance == "[我]覺得[我][能力][不足]":
        # write your code here
        pass

    if utterance == "[我]覺得[我]很雖":
        # write your code here
        pass

    if utterance == "[我]覺得[自己][很]討厭":
        # write your code here
        pass

    if utterance == "[我]覺得[非常]倒楣":
        # write your code here
        pass

    if utterance == "[我]討厭[自己]":
        # write your code here
        pass

    if utterance == "[我]身體不舒服":
        # write your code here
        pass

    if utterance == "[昨天晚上]夢到[可怕]的事情":
        # write your code here
        pass

    if utterance == "[最近]身體變好差":
        # write your code here
        pass

    if utterance == "[月經]來":
        # write your code here
        pass

    if utterance == "[現在]超想家":
        # write your code here
        pass

    if utterance == "[甚至][也]不想跟別人social":
        # write your code here
        pass

    if utterance == "[皺紋]長出來了":
        # write your code here
        pass

    if utterance == "[眼睛]太小":
        # write your code here
        pass

    if utterance == "[肚子]很圓":
        # write your code here
        pass

    if utterance == "[肩膀]痠痛":
        # write your code here
        pass

    if utterance == "[胃]痛":
        # write your code here
        pass

    if utterance == "[腿]短":
        # write your code here
        pass

    if utterance == "[自己]就是[一個]廢物":
        # write your code here
        pass

    if utterance == "[莫名]的想家":
        # write your code here
        pass

    if utterance == "[莫名]覺得憂鬱":
        # write your code here
        pass

    if utterance == "[蟑螂]來了":
        # write your code here
        pass

    if utterance == "[超]不開心":
        # write your code here
        pass

    if utterance == "[身高]太矮":
        # write your code here
        pass

    if utterance == "[都]說沒[空]":
        # write your code here
        pass

    if utterance == "[髮質]很糟糕":
        # write your code here
        pass

    if utterance == "[髮際線]太[後面]":
        # write your code here
        pass

    if utterance == "[鼻子][不夠][挺]":
        # write your code here
        pass

    if utterance == "不小心起了衝突":
        # write your code here
        pass

    if utterance == "不想上班":
        # write your code here
        pass

    if utterance == "不知道[未來]要住在哪裡":
        # write your code here
        pass

    if utterance == "不給[我][任何]方向":
        # write your code here
        pass

    if utterance == "不給[我]方向":
        # write your code here
        pass

    if utterance == "世界[上]沒有[我][也][可以]":
        # write your code here
        pass

    if utterance == "事情[都][不順][我]的意[很]討厭":
        # write your code here
        pass

    if utterance == "事情做不好":
        # write your code here
        pass

    if utterance == "什麼[時候][我][才][可以][成功]":
        # write your code here
        pass

    if utterance == "什麼事[都]不想做":
        # write your code here
        pass

    if utterance == "什麼事[都]做不好":
        # write your code here
        pass

    if utterance == "任務很難做":
        # write your code here
        pass

    if utterance == "低空飛過":
        # write your code here
        pass

    if utterance == "做了很久但是[都]沒有[成效]":
        # write your code here
        pass

    if utterance == "做什麼事情[都]沒有[動機]":
        # write your code here
        pass

    if utterance == "做惡夢":
        # write your code here
        pass

    if utterance == "可是[我][晚上][都]睡不著":
        # write your code here
        pass

    if utterance == "和朋友吵架了":
        # write your code here
        pass

    if utterance == "壓力好[大]":
        # write your code here
        pass

    if utterance == "壓抑[自己]的情緒":
        # write your code here
        pass

    if utterance == "大家[都]好[厲害]":
        # write your code here
        pass

    if utterance == "失去了[原本]的生活品質":
        # write your code here
        pass

    if utterance == "好低分不[及格]":
        # write your code here
        pass

    if utterance == "好偏心":
        # write your code here
        pass

    if utterance == "好想下班":
        # write your code here
        pass

    if utterance == "好想回家":
        # write your code here
        pass

    if utterance == "好想拉屎":
        # write your code here
        pass

    if utterance == "好想要換工作喔":
        # write your code here
        pass

    if utterance == "好生氣":
        # write your code here
        pass

    if utterance == "好討厭[現在]的[自己]":
        # write your code here
        pass

    if utterance == "好難過":
        # write your code here
        pass

    if utterance == "如果做不好":
        # write your code here
        pass

    if utterance == "對[未來]好迷[茫]":
        # write your code here
        pass

    if utterance == "就覺得[很]煩":
        # write your code here
        pass

    if utterance == "屁股好[大]":
        # write your code here
        pass

    if utterance == "很不[快樂]":
        # write your code here
        pass

    if utterance == "得了厭食症":
        # write your code here
        pass

    if utterance == "心好[累]":
        # write your code here
        pass

    if utterance == "心情[很]幹":
        # write your code here
        pass

    if utterance == "心情不好":
        # write your code here
        pass

    if utterance == "心情低潮":
        # write your code here
        pass

    if utterance == "心情很[差]":
        # write your code here
        pass

    if utterance == "怎麼辦[我]覺得[我][一直][失敗]":
        # write your code here
        pass

    if utterance == "想[上][廁所]":
        # write your code here
        pass

    if utterance == "想[大][便]":
        # write your code here
        pass

    if utterance == "想消失":
        # write your code here
        pass

    if utterance == "想留[一點]時間給[自己]":
        # write your code here
        pass

    if utterance == "想留[點]時間給[自己]":
        # write your code here
        pass

    if utterance == "感到[很]有[壓力]":
        # write your code here
        pass

    if utterance == "感到不受重視":
        # write your code here
        pass

    if utterance == "感覺[牆角]有[鬼]在看[我]":
        # write your code here
        pass

    if utterance == "感覺[自己]做了白工":
        # write your code here
        pass

    if utterance == "感覺努力沒有被看見":
        # write your code here
        pass

    if utterance == "憑什麼[小明]比較被[妹妹]喜歡":
        # write your code here
        pass

    if utterance == "憑什麼小明考得比較好":
        # write your code here
        pass

    if utterance == "我很胖":
        # write your code here
        pass

    if utterance == "手超粗":
        # write your code here
        pass

    if utterance == "找不到[工作]":
        # write your code here
        pass

    if utterance == "找不到租屋處":
        # write your code here
        pass

    if utterance == "提不起勁":
        # write your code here
        pass

    if utterance == "時間感覺[都][不夠][用]":
        # write your code here
        pass

    if utterance == "月經來好不舒服":
        # write your code here
        pass

    if utterance == "有人弄亂[我]的[桌子]":
        # write your code here
        pass

    if utterance == "朋友說[我]長得很醜":
        # write your code here
        pass

    if utterance == "沒[什麼][可以]分享的":
        # write your code here
        pass

    if utterance == "沒事":
        # write your code here
        pass

    if utterance == "沒人懂[我]":
        # write your code here
        pass

    if utterance == "沒什麼":
        # write your code here
        pass

    if utterance == "沒吃飽":
        # write your code here
        pass

    if utterance == "沒有什麼事":
        # write your code here
        pass

    if utterance == "沒有力氣做事":
        # write your code here
        pass

    if utterance == "沒有考[上]喜歡的學校":
        # write your code here
        pass

    if utterance == "沒生活品質":
        # write your code here
        pass

    if utterance == "為什麼[都]換不了工作":
        # write your code here
        pass

    if utterance == "為什麼大家[都][可以]做到":
        # write your code here
        pass

    if utterance == "狀態不太好":
        # write your code here
        pass

    if utterance == "狀態很差":
        # write your code here
        pass

    if utterance == "狀態很糟糕":
        # write your code here
        pass

    if utterance == "班[上]的人[都]不和[我]說話":
        # write your code here
        pass

    if utterance == "生活品質變[低]":
        # write your code here
        pass

    if utterance == "生理[期]來":
        # write your code here
        pass

    if utterance == "皮膚好差":
        # write your code here
        pass

    if utterance == "考試[一大堆][都]不[會]寫":
        # write your code here
        pass

    if utterance == "考試[一大堆]不[會]寫":
        # write your code here
        pass

    if utterance == "考試[全部][都]不[會]寫":
        # write your code here
        pass

    if utterance == "考試[全部]不[會]寫":
        # write your code here
        pass

    if utterance == "考試大部分[都]不[會]寫":
        # write your code here
        pass

    if utterance == "考試大部分不[會]寫":
        # write your code here
        pass

    if utterance == "考試好多[都]不[會]寫":
        # write your code here
        pass

    if utterance == "考試好多不[會]寫":
        # write your code here
        pass

    if utterance == "考試考超差的":
        # write your code here
        pass

    if utterance == "肚子咕嚕咕嚕叫":
        # write your code here
        pass

    if utterance == "肚子好[餓]":
        # write your code here
        pass

    if utterance == "腰痠":
        # write your code here
        pass

    if utterance == "膚色好黑":
        # write your code here
        pass

    if utterance == "莫名的想哭":
        # write your code here
        pass

    if utterance == "被排擠":
        # write your code here
        pass

    if utterance == "被說很自私":
        # write your code here
        pass

    if utterance == "被說沒禮貌":
        # write your code here
        pass

    if utterance == "被說目中無人":
        # write your code here
        pass

    if utterance == "要上班":
        # write your code here
        pass

    if utterance == "要崩潰了":
        # write your code here
        pass

    if utterance == "要打預防針":
        # write your code here
        pass

    if utterance == "覺得[孤單]":
        # write your code here
        pass

    if utterance == "覺得[我][不夠]好":
        # write your code here
        pass

    if utterance == "覺得[我]很胖":
        # write your code here
        pass

    if utterance == "覺得[我]得了感冒":
        # write your code here
        pass

    if utterance == "覺得[我]有厭食症":
        # write your code here
        pass

    if utterance == "覺得[我]白忙了[一場]":
        # write your code here
        pass

    if utterance == "覺得[現在]的工作[我]做不來":
        # write your code here
        pass

    if utterance == "覺得[空虛][寂寞]":
        # write your code here
        pass

    if utterance == "覺得[自己][很]廢":
        # write your code here
        pass

    if utterance == "覺得[自己][快要]爆炸了":
        # write your code here
        pass

    if utterance == "覺得[自己]好像有[點]厭食症":
        # write your code here
        pass

    if utterance == "覺得不開心":
        # write your code here
        pass

    if utterance == "覺得傷心":
        # write your code here
        pass

    if utterance == "覺得呼吸好[困難]":
        # write your code here
        pass

    if utterance == "覺得失望":
        # write your code here
        pass

    if utterance == "覺得工作很累":
        # write your code here
        pass

    if utterance == "覺得很難過":
        # write your code here
        pass

    if utterance == "覺得微不足道":
        # write your code here
        pass

    if utterance == "覺得被忽略":
        # write your code here
        pass

    if utterance == "覺得這件[事情]沒有達到[自己]的[標準]":
        # write your code here
        pass

    if utterance == "起了口角":
        # write your code here
        pass

    if utterance == "超難過":
        # write your code here
        pass

    if utterance == "身體好[疲憊]":
        # write your code here
        pass

    if utterance == "身體覺得很重":
        # write your code here
        pass

    if utterance == "長得醜":
        # write your code here
        pass

    if utterance == "長痘痘":
        # write your code here
        pass

    if utterance == "頭好痛":
        # write your code here
        pass

    return resultDICT