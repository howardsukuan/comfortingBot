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
#list1: familyLIST
familyLIST = ["爸媽","父母","父母親","我爸","爸爸","父親","我媽","媽媽","母親",
              "兄弟姐妹","兄弟姊妹","我哥","哥哥","我姐","我姊","姊姊","姐姐","我弟","弟弟","我妹","妹妹",
              "祖父母","阿公","阿嬤","爺爺","奶奶","外公","外婆","祖父","祖母","長輩","老人家","阿祖",
              "親戚","叔叔","叔","舅舅","舅","伯","姨丈","姑丈","阿姨","姨","姑姑","姑","嬸嬸","嬸","舅媽",
              "表兄弟姊妹","表兄弟姐妹","表哥","表弟","表姊","表姐","表妹",
              "堂兄弟姐妹","堂兄弟姊妹","堂哥","堂弟","堂姊","堂姐","堂妹","外甥","外甥女","姪子","姪女",
              "家裡的人","親人","家人","同居人","老公","老婆","夜間部同學","先生","太太","公婆","公公","婆婆","岳父","岳母",
              "兒子","女兒","孫子","孫女","曾孫","曾孫女","大嫂","嫂子","嫂","姊夫","姐夫","弟媳","妹婿","女婿","媳婦","妹夫"]
#list2: petLIST
petLIST = ["寵物","狗","狗狗","拉不拉多","黃金獵犬","鬥牛犬","巴哥","貴賓","馬爾濟斯","土狗","博美","柴犬","哈士奇","約克夏",
           "吉娃娃","牧羊犬","獵犬","秋田犬","米格魯","比熊犬","沙皮","鬆獅","臘腸狗","大麥町","雪納瑞","蝴蝶犬","聖伯納","藏獒",
           "貓","貓貓","摺耳貓","短毛貓","反耳貓","波絲貓","黑貓","橘貓","花貓",
           "鼠","寵物鼠","黃金鼠","天竺鼠","三線鼠",
           "魚","犬","鳥","龜","鼬","蛇"]
#list3: friendLIST
friendLIST = ["朋友","朋朋","麻吉","閨密","兄弟","同學","姊妹","姐妹"]
#list4: partnerLIST
partnerLIST = ["男友","男朋友","女友","女朋友","閃光","閃","伴侶","另一半"]
#list5: colleagueLIST
colleagueLIST = ["同事","組員","工作夥伴","前輩","後輩","新人","助理","同組同學"]

### 因為entity眾多，故列出以上的LIST
### 在寫對應的句型時，若遇到以上的entity，請用對應類別去對(e.g. "family","pet","friend","partner", "colleague")，不要用args[0]
### 因為在創REF的時候，是把LIST member 和 handle source DICT分開

### 例如 if any(e in args[0] for e in colleagueLIST) and ("難相處" in inputSTR):
###            resultDICT["source_interpersonal"] = "colleague"
###        pass

### 後來有再將member list 裡的 entities 補回 handle source dict，做為沒有對到句型的補救措施


DEBUG_interpersonal = True
userDefinedDICT = {"asNoun": ["家裡的人", "奇怪的人", "喜歡的人", "哥們", "身體", "周圍的人", "身邊的人", "大掃除", "天氣", "黃色笑話", "信用卡費", "東西", "遠距離", "月光族", "買一送一"], "asVerb": ["毛手毛腳", "發生關係", "開黃腔", "霸王硬上弓", "秒殺", "吃土", "錯過", "大小便"], "asAdverb": ["很", "好", "太", "超", "蠻"], "asAdjective": ["雷", "舒服"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_interpersonal:
        print("[interpersonal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]碎碎念":
        if "碎碎念" in inputSTR:
            resultDICT["source_interpersonal"] = "complainToYou"
        pass

    if utterance == "[同事][無敵]廢":
        if any(e in args[0] for e in colleagueLIST) and ("廢" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同事][超]雷":
        if any(e in args[0] for e in colleagueLIST) and ("雷" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同事][難]相處":
        if any(e in args[0] for e in colleagueLIST) and ("難相處" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

    if utterance == "[同事]不做事":
        if any(e in args[0] for e in colleagueLIST) and ("不做事" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同事]不出現":
        if any(e in args[0] for e in colleagueLIST) and ("不出現" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

    if utterance == "[同事]告[我]的狀":
        if any(e in args[0] for e in colleagueLIST) and ("告" and "狀" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

    if utterance == "[同事]和[我]借錢不還":
        if "借錢不還" in inputSTR:
            resultDICT["source_interpersonal"] = "moneyFight"
        pass

    if utterance == "[同事]大雷人":
        if any(e in args[0] for e in colleagueLIST) and ("雷人" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同事]放槍":
        if any(e in args[0] for e in colleagueLIST) and ("放槍" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同事]耍廢":
        if any(e in args[0] for e in colleagueLIST) and ("耍廢" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

#這句對不到，可能被"同事耍廢"蓋住
#    if utterance == "[同事]耍腦":
#        if any(e in args[0] for e in colleagueLIST) and ("耍腦" in inputSTR):
#            resultDICT["source_interpersonal"] = "badTeamMate"
#        pass

    if utterance == "[同組同學][只]想拿成果":
        if any(e in args[0] for e in colleagueLIST) and ("拿成果" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同學]做報告[都]沒有貢獻":
        if "沒有貢獻" in inputSTR:
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[同學]好虛偽":
        if any(e in args[0] for e in friendLIST) and ("虛偽" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        elif any(e in args[0] for e in colleagueLIST) and ("虛偽" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        pass

    if utterance == "[同組同學][都]不說話":
        if any(e in args[0] for e in colleagueLIST) and ("不說話" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[周圍的人][都][很]努力進修":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]不喜歡[我]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]不想談戀愛":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]對[我]無感":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]拒絕[我]的告白":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]有[男朋友]了":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]有伴侶了":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[喜歡的人]有戀人了":
        resultDICT["source_interpersonal"] = args[0]
        pass

#    if utterance == "[喜歡的人]說[我們]是好哥們":
#        resultDICT["source_interpersonal"] = args[0]
#        pass

#    if utterance == "[喜歡的人]說[我們]是好閨密":
#        resultDICT["source_interpersonal"] = args[0]
#        pass

    if utterance == "[喜歡的人]說[我們]當朋友就[好]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[女友]有[嚴重]潔癖":
        if any(e in args[0] for e in partnerLIST) and ("潔癖" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        pass

    if utterance == "[媽媽][一直]逼[我]婚":
        if any(e in args[0] for e in familyLIST) and ("逼" and "婚" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        pass

    if utterance == "[媽媽]覺得[我]吃太多":
        if any(e in args[0] for e in familyLIST) and ("吃太多" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        pass

    if utterance == "[家人]生病了":
        if any(e in args[0] for e in familyLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick"
        elif any(e in args[0] for e in friendLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick"
        elif any(e in args[0] for e in partnerLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick"  
        elif any(e in args[0] for e in petLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "petSick"       
        pass

    if utterance == "[家人]過世了":
        if "過世" in inputSTR:
            resultDICT["source_interpersonal"] = "death"
        pass

    if utterance == "[寵物]死掉了":
        if "死掉" in inputSTR:
            resultDICT["source_interpersonal"] = "death"
        pass

    if utterance == "[我][男友]好摳":
        if "摳" in inputSTR:
            resultDICT["source_interpersonal"] = "moneyFight"
        pass

    if utterance == "什麼[時候]才[能]換[女友]":
        if any(e in args[2] for e in familyLIST) and ("換" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        pass

    if utterance == "[我]是邊緣人":
        if "邊緣人" in inputSTR:
            resultDICT["source_interpersonal"] = "noFriend"
        pass

    if utterance == "[我]的[寵物][最近]生病了":
        if any(e in args[1] for e in familyLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick"
        elif any(e in args[1] for e in friendLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick" 
        elif any(e in args[1] for e in partnerLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "familySick" 
        elif any(e in args[1] for e in petLIST) and ("生病" in inputSTR):
            resultDICT["source_interpersonal"] = "petSick"       
        pass

    if utterance == "[我]被分手":
        if "被分手" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "[我]覺得[媽媽]討厭[我]":
        if any(e in args[1] for e in familyLIST) and ("討厭" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        elif any(e in args[1] for e in friendLIST) and ("討厭" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        elif any(e in args[1] for e in partnerLIST) and ("討厭" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        elif any(e in args[1] for e in colleagueLIST) and ("討厭" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

# 這個應該在personal
#    if utterance == "[我]身體不舒服":
#        if "身體不舒服" in inputSTR:
#            resultDICT["source_interpersonal"] = "familySick"
#        pass

    if utterance == "[教授]觀念很保守":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[最近]跟[家裡的人]吵架了":
        if any(e in args[1] for e in familyLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "familyFight"
        elif any(e in args[1] for e in friendLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"  
        elif any(e in args[1] for e in partnerLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "partnerFight"     
        elif any(e in args[1] for e in colleagueLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        elif "吵架" in inputSTR:
            resultDICT["source_interpersonal"] = "otherFight"
        pass

    if utterance == "[朋友]予取予求":
        if any(e in args[0] for e in friendLIST) and ("予取予求" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        pass

    if utterance == "[朋友]說[他][很]忙":
        if any(e in args[0] for e in friendLIST) and ("忙" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        pass

    if utterance == "[朋友]說[我]壞話":
        if any(e in args[0] for e in friendLIST) and ("壞話" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        elif any(e in args[0] for e in familyLIST) and ("壞話" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        elif any(e in args[0] for e in partnerLIST) and ("壞話" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        elif any(e in args[0] for e in colleagueLIST) and ("壞話" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

    if utterance == "[朋友]鬧得不[愉快]":
        resultDICT["source_interpersonal"] = "otherFight"
        pass

    if utterance == "[比賽]輸了":
        if "輸" in inputSTR:
            resultDICT["source_interpersonal"] = "competition"
        pass

    if utterance == "[狗狗][都]不吃飯":
        if any(e in args[0] for e in petLIST) and ("不吃飯" in inputSTR):
            resultDICT["source_interpersonal"] = "pet"
        pass

    if utterance == "[狗狗]亂大小便":
        if any(e in args[0] for e in petLIST) and ("亂大小便" in inputSTR):
            resultDICT["source_interpersonal"] = "pet"
        pass

    if utterance == "[男友][最近][都]很少陪[我]":
        if "很少陪我" in inputSTR:
            resultDICT["source_interpersonal"] = "feelLonely"
        pass

    if utterance == "[男友]亂來":
        if any(e in args[0] for e in partnerLIST) and ("亂來" in inputSTR):
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "[男友]劈腿":
        if any(e in args[0] for e in partnerLIST) and ("劈腿" in inputSTR):
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "[男友]垃圾":
        if any(e in args[0] for e in partnerLIST) and ("垃圾" in inputSTR):
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "[男友]很渣":
        if any(e in args[0] for e in partnerLIST) and ("渣" in inputSTR):
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "[男友]提分手":
        if "提分手" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "[男友]是渣":
        if any(e in args[0] for e in partnerLIST) and ("是渣" in inputSTR):
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "[男友]甩了[我]":
        if any(e in args[0] for e in partnerLIST) and ("甩了" in inputSTR):
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "[男友]相處時間變少":
        if "相處時間變少" in inputSTR:
            resultDICT["source_interpersonal"] = "feelLonely"
        pass

    if utterance == "[男友]說要分手":
        if "說要分手" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "[男友]說要跟[我]分手":
        if "分手" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "[男朋友]怎麼這麼小氣":
        if "小氣" in inputSTR:
            resultDICT["source_interpersonal"] = "moneyFight"
        pass

    if utterance == "[老師]上課好無聊":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[老師]誤會[我]":
        if "誤會" in inputSTR:
            resultDICT["source_interpersonal"] = "misunderstood"
        pass

    if utterance == "[老闆]叫[我]加班":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[老闆]說[我]的能力[不夠]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[身邊的人][都]很聰明":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[遠距離]好痛苦":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "[阿公][很]煩":
        if any(e in args[0] for e in familyLIST) and ("煩" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        elif any(e in args[0] for e in friendLIST) and ("煩" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        elif any(e in args[0] for e in partnerLIST) and ("煩" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        elif any(e in args[0] for e in colleagueLIST) and ("煩" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        elif any(e in args[0] for e in petLIST) and ("煩" in inputSTR):
            resultDICT["source_interpersonal"] = "pet"
        pass

    if utterance == "[組員][都]在擺爛":
        if any(e in args[0] for e in colleagueLIST) and ("擺爛" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"

    if utterance == "別人不喜歡[我]":
        if "別人" in inputSTR:
            resultDICT["source_interpersonal"] = "otherPeople"
        pass

    if utterance == "向我發牢騷":
        if "發牢騷" in inputSTR:
            resultDICT["source_interpersonal"] = "complainToYou"
        pass

    if utterance == "失戀了":
        if "失戀" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "想交[男朋友]":
        if any(e in args[0] for e in partnerLIST) and ("交" in inputSTR):
            resultDICT["source_interpersonal"] = "noPartner"
        pass

    if utterance == "想脫魯":
        if "想脫魯" in inputSTR:
            resultDICT["source_interpersonal"] = "noPartner"
        pass

    if utterance == "對[男友]沒感覺":
        if any(e in args[0] for e in partnerLIST) and ("沒感覺" in inputSTR):
            resultDICT["source_interpersonal"] = "relationship"
        pass

    if utterance == "忘記[我]的[生日]":
        resultDICT["source_interpersonal"] = "forgetYou"
        pass

    if utterance == "有人說[我]很貪心":
        if "有人" in inputSTR:
            resultDICT["source_interpersonal"] = "otherPeople"
        pass

    if utterance == "沒人找[我][一組]":
        resultDICT["source_interpersonal"] = "noFriend"
        pass

    if utterance == "沒有[任何]人[可以]訴苦":
        resultDICT["source_interpersonal"] = "listen"
        pass

    if utterance == "沒有[朋友]":
        resultDICT["source_interpersonal"] = "noFriend"
        pass

    if utterance == "沒有人聽[我]說話":
        resultDICT["source_interpersonal"] = "listen"
        pass

    if utterance == "沒有得名":
        resultDICT["source_interpersonal"] = "competition"
        pass

    if utterance == "碰到[噁男]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "祝福[都]沒有收到":
        resultDICT["source_interpersonal"] = "forgetYou"
        pass

    if utterance == "腳踏[兩條]船":
        if "腳踏" and "船" in inputSTR:
            resultDICT["source_interpersonal"] = "loveBetrayal"
        pass

    if utterance == "被[主管]臭罵[一頓]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "被[主管]訓話":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "被[主管]說表現很差":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "被[人]誤會":
        if "誤會" in inputSTR:
            resultDICT["source_interpersonal"] = "misunderstood"
        pass

    if utterance == "被甩了":
        if "被甩" in inputSTR:
            resultDICT["source_interpersonal"] = "breakup"
        pass

    if utterance == "跟[家人][難]溝通":
        if any(e in args[0] for e in familyLIST) and ("難溝通" in inputSTR):
            resultDICT["source_interpersonal"] = "family"
        elif any(e in args[0] for e in friendLIST) and ("難溝通" in inputSTR):
            resultDICT["source_interpersonal"] = "friend"
        elif any(e in args[0] for e in partnerLIST) and ("難溝通" in inputSTR):
            resultDICT["source_interpersonal"] = "partner"
        elif any(e in args[0] for e in colleagueLIST) and ("難溝通" in inputSTR):
            resultDICT["source_interpersonal"] = "colleague"
        pass

    if utterance == "遇到[奇怪的人]":
        resultDICT["source_interpersonal"] = args[0]
        pass

    if utterance == "隔壁坐了[一個]莫名其妙的[人]":
        if "莫名其妙的人" in inputSTR:
            resultDICT["source_interpersonal"] = "otherPeople"
        pass

    if utterance == "隔壁的[人]很吵":
        if "隔壁的人" in inputSTR:
            resultDICT["source_interpersonal"] = "otherPeople"
        pass

    if utterance == "[同事]做事不負責任但領的[錢]比[我]多":
        if any(e in args[0] for e in colleagueLIST) and ("不負責任" in inputSTR):
            resultDICT["source_interpersonal"] = "badTeamMate"
        pass

    if utterance == "[朋友]吵架了":
        if any(e in args[0] for e in familyLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "familyFight"
        elif any(e in args[0] for e in partnerLIST) and ("吵架" in inputSTR):
            resultDICT["source_interpersonal"] = "partnerFight"
        elif "吵架" in inputSTR:
            resultDICT["source_interpersonal"] = "otherFight"
        pass

    return resultDICT