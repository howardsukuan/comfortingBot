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
sickLIST = ["流鼻涕", "腹瀉", "拉肚子", "頭痛", "頭暈", "咳嗽", "噁心", "發燒", "疲勞", "疲倦", "暈眩", "累", "食慾不振","胃潰瘍", "B型肝炎帶原者","C型肝炎帶原者","肝機能異常", "不孕症","婦科腫瘤", "高血壓", "泌尿道腫瘤","前列腺肥大","腎結石","膀胱結石","血尿","頻尿","小便無力","尿道下裂","隱睪","陰囊腫痛","夜尿","尿失禁","不孕","男性性機能異常","包皮","性病","膀胱機能異常", "甲狀腺疾病","糖尿病","肥胖","腦下垂體病變","腎上腺","甲狀腺","高尿酸","代謝異常", "咳血","氣喘","肺結核","肺腫瘤","肺炎","胸悶","支氣管炎", "掉頭髮","脂肪瘤","痘痘", "禿", "骨折","骨骼疼痛","脫臼","骨髓炎","關節退化","腰酸背痛","關節炎","骨畸形","骨腫瘤","脊椎病變","脊椎骨骨折","脊椎側彎","駝背","骨質疏鬆症","坐骨神經痛","運動傷害","容易流汗","夜汗","糖尿病","口渴","多尿","口乾","多尿","乳房分泌物","肢端肥大症","肥胖症","高血脂症","血糖過低","尿酸過高","身高異常","性別異常","癌",  "大腸炎","息肉", "中風", "腦充血", "嘔吐","頭暈","牙痛","頭痛","腳痛","膝蓋痛","咳嗽","乾咳","心悸", "感冒"]

happyLIST = ["快樂", "開心", "高興"]

DEBUG_personal = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一", "計畫", "台大", "大便", "老公", "老婆", "阿公", "阿嬤", "閃", "另一半", "教授", "莫名其妙的人", "隔壁的人", "邊緣人", "競賽", "大隊接力", "上司", "副理", "這個月", "授權碼"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便", "寫論文", "痠", "沒空", "拳打腳踢", "脫魯", "背"], "asAdverb": ["很", "好", "太", "超", "蠻", "有點"], "asAdjective": ["雷", "舒服", "好多", "可怕", "可以"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_personal:
        print("[personal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]被奪命[連環]call超級煩":
        resultDICT["source_personal"] = "annoyed"
        pass

    if utterance == "[作品]被退件了":
        resultDICT["source_personal"] = "schoolwork"
        pass

    if utterance == "[作業]不[會]寫":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[作業]不知道怎麼寫":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[作業]寫不出來":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[作業]想不出[該][怎麼]做":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[作業]想不出怎麼做":
        if "怎麼做" in inputSTR:
            resultDICT["source_personal"] = "schoolwork"
        #resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[分數]不理想":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[只]想[每天]躲在宿舍":
        if "躲在宿舍" in inputSTR:
            resultDICT["source_personal"] = "WanttobeAlone"
        pass

    if utterance == "[常常]生病":
        # write your code here
        if "生病" in inputSTR:
            resultDICT["source_personal"] = "sick"
        pass

    if utterance == "[我][一直]做可怕的夢":
        if "可怕的夢" in inputSTR:
            resultDICT["source_personal"] = "nightmare"
        pass

    if utterance == "[我][只]要想[自己][一個]人待著":
        if "自己" and "人待著" in inputSTR:
            resultDICT["source_personal"] = "WanttobeAlone"
        pass

    if utterance == "[我][常常]睡[不飽]":
        if "睡" in inputSTR:
            resultDICT["source_personal"] = "insomia"
        pass

    if utterance == "[我][每天][都]睡不著":
        if "睡不著" in inputSTR:
            resultDICT["source_personal"] = "insomia"
        pass

    if utterance == "[我][能]找得到工作嗎":
        if "找得到工作" in inputSTR:
            resultDICT["source_personal"] = "futurePathWorry"
        pass

    #if utterance == "[我][能]考[上]台[大]嗎":
        #if "考" in inputSTR:
            #resultDICT["source_personal"] = "futurePathWorry"
        #pass

    if utterance == "[我]什麼[時候]才[能]換工作呢":
        if "換工作" in inputSTR:
            resultDICT["source_personal"] = "workChange"  
        pass

    if utterance == "[我]吃壞肚子了":
        if "吃壞肚子" in inputSTR:
            resultDICT["source_personal"] = "toilet"
        pass

    if utterance == "[我]在小組[裡面]很[自卑]":
        resultDICT["source_personal"] = args[2]
        pass

    if utterance == "[我]好沒用":
        if "沒用" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
            pass
    if utterance == "[我]很不喜歡我[自己]":
        if "不喜歡" and  "自己" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        pass

    if utterance == "[我]很胖":
        if "很胖" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "[我]心好[累]":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "[我]是[廢物]":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "[我]看不到[未來]":
        if "看不到" in inputSTR:
            resultDICT["source_personal"] = "futurePathWorry"
        pass

    if utterance == "[我]覺得[我][能力][不足]":
        if "能力" and "不足" in inputSTR:
            resultDICT["source_personal"] = "noAbility"
        if "微不足道" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        if "很雖" in inputSTR: 
            resultDICT["source_personal"] = "rough" 
        if "厭食症" in inputSTR:
            resultDICT["source_personal"] = "Anorexia"
        pass

    if utterance == "[我]覺得[我]很雖":
        if "很雖" in inputSTR: 
            resultDICT["source_personal"] = "rough"
        pass

    if utterance == "[我]覺得[自己]很討厭":
        if "自己" and "很討厭":
            resultDICT["source_personal"] = "lowSelfEsteem"
        pass

    if utterance == "[我]覺得[非常]倒楣":
        if "倒楣" in inputSTR:
            resultDICT["source_personal"] = "rough"
        pass

    if utterance == "[我]覺得很煩":
        if "很煩" in inputSTR:
            resultDICT["source_personal"] = "annoyed"
        pass

    if utterance == "[我]討厭[自己]":
        if "討厭" and "自己" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        pass

    if utterance == "[我]身體不舒服":
        if "身體不舒服" in inputSTR:
            resultDICT["source_personal"] = "sick"
        pass

    if utterance == "[昨天晚上]夢到可怕的事情":
        if "夢到可怕" in inputSTR:
            resultDICT["source_personal"] = "nightmare"
        pass

    if utterance == "[最近]身體變好差":
        if "身體變好差" in inputSTR:
            resultDICT["source_personal"] = "tired"
        pass

    if utterance == "[月經]來":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "[現在]超想家":
        if "想家" in inputSTR:
            resultDICT["source_personal"] = "homeSick"
        pass

    if utterance == "[甚至][也]不想跟別人social":
        if "不想跟別人social" in inputSTR:
            resultDICT["source_personal"] = "WanttobeAlone"
        pass

    if utterance == "[皺紋]長出來了":
        resultDICT["source_personal"] = args[0]
        pass

    #if utterance == "[肩膀]痠痛":
        #if "痠痛" in inputSTR:
            #resultDICT["source_personal"] = "sick"
        pass

    if utterance == "[自己]就是[一個]廢物":
        if "廢物" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        pass 

    if utterance == "[莫名]的想家":
        if "想家" in inputSTR:
            resultDICT["source_personal"] = "homeSick"
        pass

    if utterance == "[莫名]覺得憂鬱":
        if "憂鬱" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "[蟑螂]來了":
        resultDICT["source_personal"] = args[0]
        pass

    #if utterance == "[都]說沒[空]":
        #resultDICT["source_personal"] = args[0]
        #pass

    if utterance == "[鼻子][不夠][挺]":
        if "很糟" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        if "鼻子" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "下巴太[圓]":
        if "下巴" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "不想上班":
        if "上班" in inputSTR:
            resultDICT["source_personal"] = "work"
        pass

    if utterance == "不知道[未來]要住在哪裡":
        if "住在哪裡" in inputSTR:
            resultDICT["source_personal"] = "noPlacetoLive"
        pass

    if utterance == "不給[我][任何]方向":
        if "方向" in inputSTR:
            resultDICT["source_personal"] = "schoolwork"
        pass

    if utterance == "不給[我]方向":
        if "方向" in inputSTR:
            resultDICT["source_personal"] = "schoolwork"        
        pass

    #if utterance == "世界[上]沒有[我][也][可以]":
        #if "沒有" in inputSTR:
            #resultDICT["source_personal"] = "negMood"
        #pass

    if utterance == "事情[都][不順][我]的意很討厭":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "事情做不好":
        if "做不好" in inputSTR:
            resultDICT["source_personal"] = "perfection"
        pass

    #if utterance == "什麼[時候][我][才][可以][成功]":
        #resultDICT["source_personal"] = args[4]
        #pass

    if utterance == "什麼事[都]不想做":
        if "不想做" in inputSTR:
            resultDICT["source_personal"] = "motivation"
        pass

    if utterance == "什麼事[都]做不好":
        if "做不好" in inputSTR:
            resultDICT["source_personal"] = "perfection"
        pass

    if utterance == "任務很難做":
        if "很難做" in inputSTR:
            resultDICT["source_personal"] = "perfection"
        pass

    if utterance == "低空飛過":
        if "低空飛過" in inputSTR:
            resultDICT["source_personal"] = "score"
        pass

    if utterance == "做了很[久]但是[都]沒有成效":
        if "成效" in inputSTR:
            resultDICT["source_personal"] = "workWaste"
        pass

    if utterance == "做什麼事情[都]沒有[動機]":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "做惡夢":
        if "惡夢" in inputSTR:
            resultDICT["source_personal"] = "nightmare"
        pass

    if utterance == "[分數]很難看":
        resultDICT["source_personal"] = args[0]       
        pass

    if utterance == "可是[我][晚上][都]睡不著":
        if "睡不著" in inputSTR:
            resultDICT["source_personal"] = "insomia"
        pass

    if utterance == "嘴唇很[薄]":
        if "嘴唇" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "壓力好[大]":
        if "壓力" in inputSTR:
            resultDICT["source_personal"] = "pressure"
        pass

    if utterance == "壓抑[自己]的情緒":
        if "壓抑" in inputSTR:
            resultDICT["source_personal"] = "PressEmotion"
        pass

    if utterance == "大家[都]好[厲害]":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "失去了[原本]的生活品質":
        if "生活品質" in inputSTR:
            resultDICT["source_personal"] = "lifeQuality"
        pass

    if utterance == "好低分不[及格]":
        if "低分" in inputSTR:
            resultDICT["source_personal"] = "score"
        pass

    if utterance == "好想下班":
        if "下班" in inputSTR:
            resultDICT["source_personal"] = "work"
        pass

    if utterance == "好想回家":
        if "想回家" in inputSTR:
            resultDICT["source_personal"] = "homeSick"
        pass

    if utterance == "好想拉屎":
        if "拉屎" in inputSTR:
            resultDICT["source_personal"] = "toilet"
        pass

    if utterance == "好想要換工作喔":
        if "換工作" in inputSTR:
            resultDICT["source_personal"] = "workChange"
        pass

    if utterance == "好生氣":
        if "生氣" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "好討厭[現在]的[自己]":
        resultDICT["source_personal"] = args[1]        
        pass

    if utterance == "好難過":
        if "難過" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "如果做不好":
        if "做不好" in inputSTR:
            resultDICT["source_personal"] = "perfection"
        pass

    if utterance == "對[未來]好迷[茫]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "就覺得很煩":
        if "很煩" in inputSTR:
            resultDICT["source_personal"] = "annoyed"
        pass

    if utterance == "屁股好[大]":
        if "屁股" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "很不[快樂]":
        for happy in happyLIST:
            if happy in inputSTR:
                resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "心情不好":
        if "心情" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "心情低潮":
        if "心情" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "心情很差":
        if "心情" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "心情很幹":
        if "心情" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "怎麼辦[我]覺得[我][一直][失敗]":
        resultDICT["source_personal"] = args[3]
        pass

    if utterance == "想[上][廁所]":
        resultDICT["source_personal"] = args[1]
        pass

    #if utterance == "想[大][便]":
        #resultDICT["source_personal"] = args[1]
        #pass

    if utterance == "想留[一點]時間給[自己]":
        if "時間" in inputSTR:
            resultDICT["source_personal"] = "TimeManagement"
        pass

    if utterance == "想留[點]時間給[自己]":
        if "時間" in inputSTR:
            resultDICT["source_personal"] = "TimeManagement"        
        pass

    if utterance == "感到不受重視":
        if "不受重視" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass 

    if utterance == "感到很有壓力":
        if "壓力" in inputSTR:
            resultDICT["source_personal"] = "pressure"
        pass

    if utterance == "感覺[牆角]有[鬼]在看[我]":
        resultDICT["source_personal"] = args[1]
        pass

    if utterance == "感覺[自己]做了白工":
        if "白工" in inputSTR:
            resultDICT["source_personal"] = "workWaste"
        pass

    if utterance == "感覺努力沒有被看見":
        if "沒有被看見" in inputSTR:
            resultDICT["source_personal"] = "workWaste"
        pass 

    if utterance == "憑什麼[小明]比較被[妹妹]喜歡":
        if "憑什麼" in inputSTR:
            resultDICT["source_personal"] = "envy"
        pass

    if utterance == "憑什麼小明考得比較好":
        if "憑什麼" in inputSTR:
            resultDICT["source_personal"] = "envy"        
        pass

    if utterance == "手超[粗]":
        if "手" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "找不到[工作]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "找不到租屋處":
        if "租屋處" in inputSTR:
            resultDICT["source_personal"] = "noPlacetoLive"
        pass

    if utterance == "提不起勁":
        if "提不起勁" in inputSTR:
            resultDICT["source_personal"] = "motivation"
        pass

    if utterance == "時間感覺[都][不夠][用]":
        if "時間" in inputSTR:
            resultDICT["source_personal"] = "TimeManagement"
        pass

    if utterance == "月經來好不舒服":
        if "月經" in inputSTR:
            resultDICT["source_personal"] = "period"
        pass

    if utterance == "有人弄亂[我]的[桌子]":
        if "弄亂" in inputSTR:
            resultDICT["source_personal"] = "bully"
        pass 

    if utterance == "朋友說[我]長得很[醜]":
        resultDICT["source_personal"] = args[1]
        pass

    #if utterance == "沒[什麼][可以]分享的":
        #if "沒" in inputSTR:
            #resultDICT["source_personal"] = "nothing"
        #pass

    if utterance == "沒事":
        if "沒" in inputSTR:
            resultDICT["source_personal"] = "nothing"
        pass

    if utterance == "沒人懂[我]":
        if "沒人懂" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "沒什麼":
        if "沒" in inputSTR:
            resultDICT["source_personal"] = "nothing"         
        pass

    if utterance == "沒吃飽":
        if "沒吃飽" in inputSTR:
            resultDICT["source_personal"] = "hunger"
        pass

    if utterance == "沒有什麼事":
        if "沒" in inputSTR:
            resultDICT["source_personal"] = "nothing"        
        pass

    if utterance == "沒有力氣做事":
        if "做事" in inputSTR:
            resultDICT["source_personal"] = "motivation"
        pass

    if utterance == "沒有考[上]喜歡的學校":
        if "考" in inputSTR:
            resultDICT["source_personal"] = "futurePathWorry"
        pass

    if utterance == "沒生活品質":
        if "生活品質" in inputSTR:
            resultDICT["source_personal"] = "lifeQuality"
        pass

    if utterance == "為什麼[都]換不了工作":
        if "換不了工作" in inputSTR:
            resultDICT["source_personal"] = "workChange"
        pass

    #if utterance == "為什麼大家[都][可以]做到":
        #if "做到" in inputSTR:
            #resultDICT["source_personal"] = "envy"
        #pass

    if utterance == "狀態不太好":
        if "不太好" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "狀態很[糟糕]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "狀態很差":
        if "很差" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "班[上]的人[都]不和[我]說話":
        if "不" and "說話" in inputSTR:
            resultDICT["source_personal"] = "bully"
        pass

    if utterance == "生活品質變[低]":
        if "生活品質" in inputSTR:
            resultDICT["source_personal"] = "lifeQuality"
        pass

    if utterance == "生理[期]來":
        if "生理" in inputSTR:
            resultDICT["source_personal"] = "period"
        pass

    if utterance == "皮膚好差":
        if "皮膚" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "眼睛太[小]":
        if "眼睛" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "考試[一大堆][都]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試[一大堆]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試[全部][都]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試[全部]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試大部分[都]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試大部分不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試好多[都]不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試好多不[會]寫":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "test"
        pass

    if utterance == "考試考超差的":
        if "考試" in inputSTR:
            resultDICT["source_personal"] = "score"        
        pass

    if utterance == "肚子咕嚕咕嚕叫":
        if "肚子" in inputSTR:
            resultDICT["source_personal"] = "hunger"
        pass

    if utterance == "肚子好[餓]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "肚子很[圓]":
        if "肚子" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "膚色好黑":
        if "膚色" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "莫名的想哭":
        if "想哭" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "被排擠":
        if "排擠" in inputSTR:
            resultDICT["source_personal"] = "bully"
        pass

    if utterance == "被說很[自私]":
        if "被說" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "被說沒禮貌":
        if "被說" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "被說目中無人":
        if "被說" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "要上班":
        if "上班" in inputSTR:
            resultDICT["source_personal"] = "work"
        pass

    if utterance == "要崩潰了":
        if "崩潰" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "要打預防針":
        if "預防針" in inputSTR:
            resultDICT["source_personal"] = "afraid"
        pass

    if utterance == "覺得[孤單]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "覺得[我][不夠]好":
        if "不夠" and "好" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        #resultDICT["source_personal"] = args[1]
        pass

    if utterance == "覺得[我]很胖":
        if "很胖" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "覺得[我]得了感冒":
        for sick in sickLIST: 
            if sick in inputSTR:
                resultDICT["source_personal"] = "sick"
        pass

    if utterance == "覺得[我]有厭食症":
        if "厭食症" in inputSTR:
            resultDICT["source_personal"] = "Anorexia"
        pass

    if utterance == "覺得[我]白忙了[一場]":
        if "白忙" in inputSTR:
            resultDICT["source_personal"] = "workWaste"
        pass

    if utterance == "覺得[現在]的工作[我]做不來":
        if "做不來" in inputSTR:
            resultDICT["source_personal"] = "noAbility"
        pass

    if utterance == "覺得[自己][快要]爆炸了":
        if "爆炸" in inputSTR:
            resultDICT["source_personal"] = "pressure"
        pass

    if utterance == "覺得[自己]好像有點厭食症":
        if "厭食症" in inputSTR:
            resultDICT["source_personal"] = "Anorexia"
        pass

    if utterance == "覺得[自己]很廢":
        if "很廢" in inputSTR:
            resultDICT["source_personal"] = "lowSelfEsteem"
        pass

    if utterance == "覺得不開心":
        if "不開心" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "覺得傷心":
        if "傷心" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass

    if utterance == "覺得呼吸好[困難]":
        resultDICT["source_personal"] = args[0]
        pass

    if utterance == "覺得失望":
        if "失望" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "覺得工作很[累]":
        if "工作" in inputSTR:
            resultDICT["source_personal"] = "work"        
        pass

    if utterance == "覺得很難過":
        if "難過" in inputSTR:
            resultDICT["source_personal"] = "negMood"
        pass
        
    if utterance == "覺得被忽略":
        if "被忽略" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "覺得這件[事情]沒有達到[自己]的[標準]":
        resultDICT["source_personal"] = args[2]
        pass


    if utterance == "超不開心":
        if "不開心" in inputSTR:
            resultDICT["source_personal"] = "negMood" 
        pass

    if utterance == "超難過":
        if "難過" in inputSTR:
            resultDICT["source_personal"] = "negMood" 
        pass

    if utterance == "身體好[疲憊]":
        if "身體" in inputSTR:
            resultDICT["source_personal"] = "tired" 
        pass

    if utterance == "身體覺得很重":
        if "身體" in inputSTR:
            resultDICT["source_personal"] = "tired" 
        pass

    if utterance == "身高太矮":
        if "身高" in inputSTR:
            resultDICT["source_personal"] = "appearance" 
        pass

    if utterance == "長得醜":
        if "醜" in inputSTR:
            resultDICT["source_personal"] = "appearance" 
        pass

    if utterance == "長痘痘":
        if "痘痘" in inputSTR:
            resultDICT["source_personal"] = "appearance" 
        pass

    if utterance == "頭好痛":
        if "痛" in inputSTR:
            resultDICT["source_personal"] = "sick"
        pass

    if utterance == "髮質很[糟糕]":
        if "髮質" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass

    if utterance == "髮際線太[後面]":
        if "髮際線" in inputSTR:
            resultDICT["source_personal"] = "appearance"
        pass
    
    if utterance == "[自己]好[渺小]":
        resultDICT["source_personal"] = args[1]     
        pass

    if utterance == "[都]說沒空":
        if "沒空" in inputSTR:
            resultDICT["source_personal"] = "TimeManagement"
        pass

    if utterance == "世界[上]沒有[我][也]可以":
        if "沒有" in inputSTR:
            resultDICT["source_personal"] = "negMood"        
        pass

    if utterance == "什麼[時候][我][才]可以[成功]":
        resultDICT["source_personal"] = args[3]
        pass

    if utterance == "想大便":
        if "想" and "大便" in inputSTR:
            resultDICT["source_personal"] = "toilet" 
        pass

    if utterance == "沒[什麼]可以分享的":
        if "沒" in inputSTR:
            resultDICT["source_personal"] = "nothing"        
        pass

    if utterance == "為什麼大家[都]可以做到":
        if "可以做到" in inputSTR:
            resultDICT["source_personal"] = "envy"
        pass

    if utterance == "肩膀痠痛":
        if "痠痛" in inputSTR:
            resultDICT["source_personal"] = "sick"        
        pass    

    if utterance == "[我][能]考[上][台大]嗎":
        if "考" in inputSTR:
            resultDICT["source_personal"] ="futurePathWorry"
        pass

    return resultDICT