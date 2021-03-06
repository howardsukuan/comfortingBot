#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#2nd self defined function: check the mood
EmotionRactionDICT = {
    "BadMood":["差","不好","很糟糕","badmood","爛","很悶","低潮","好難","難過","低落","空虛","寂寞","黑暗","不太開心","不太妙","很難過"],
    "GoodMood":["好","不錯","很好","很棒","棒"]}
PlainFeelingLIST = ["普通","還好","還行","沒什麼特別","一樣","好無聊","跟平常差不多"]

#性騷擾LIST
SexualHarassmentLIST = ["觸碰到我","毛手毛腳","抱著我不放","發生關係","黃腔","黃色笑話","開黃腔","講黃色笑話","開黃色笑話","聊色", "偷拍", "用胸部擠我", "傳裸照", "叫我開門讓他進去上廁所", "跟他睡","拍我屁股", "有人拍了我的屁股","貼在我的胸部上","撫摸他的生殖器","有甚麼東西貼著","要我和他發生關係","說我胸部小","幫他口交","騷擾","被人摸了","侵犯","逼迫我跟他接吻","亂摸","偷看","打手槍","露鳥","偷摸我奶","想跟我一起洗澡","露屌","偷摸屁股","下海","霸王硬上弓","變態","不做愛就是不愛他","性騷擾","摸我","強暴","捏屁股","摸屁股","摸胸部","摸腿","摟腰","勾肩","摳手心","覺得自己好髒","自己身體好骯髒"]

#Reaction 回應LIST
BadFeelingReactionLIST = ["還好嗎 \n想說說為什麼嗎?",
                          "還好嗎?\n跟我談談嗎?",
                          "我都在這,你如果願意談談可以跟我說\n你說,我聽"]
GoodFeelingReactionLIST = ["好替你開心!! 那你願意跟我分享一下嗎~",
                          "感覺很棒! 是發生什麼事情嗎~"]
PlainReactionLIST = ["那想聊的時候再跟我聊聊\n我都在", "好~ 有什麼想分享的事情再說喔!"]
OtherReactionLIST = ["那要談談嗎?", "那要分享一下嗎?"]
SexualHarassmentReactionLIST = ["下次如果有遇到類似的狀況，請向信任的人說出自己的遭遇，請人幫忙，不要讓自己的權益睡著了。這個給你參考，衛服部保護司性騷擾防治法令規章 https://dep.mohw.gov.tw/DOPS/lp-1287-105-xCat-item005.html", "這邊提供你一個連結，如果有需要可以參考看看。【法律小常識】性騷擾，怎麼辦？http://womany.net/read/article/1777", "這樣已經算是性騷擾的行為了，建議你聯繫衛生福利部 (02)8590-6666 (轉保護服務司第三科)", "別害怕!不要因為受到威脅而妥協。這個提供給你參考: 現代婦女基金會 (02)2351-2811", "別怕拒絕別人，勇於說不，避免持續被騷擾才是唯一的法則。或許你可以打這個專線，讓專業的人為你服務: 勵馨基金會 (02)8911-8595", "附近有監視器嗎?有沒有目擊者看到偷拍的人的長相?下次要記得不要打草驚蛇，偷偷報警，讓其他人牽制色狼的行動!", "千萬不要自責，之後盡量避免獨處或是有任何的肢體接觸，如果有覺得不對勁，一定要偷偷蒐證保護好自己! \n衛服部保護司性騷擾防治法令規章 https://dep.mohw.gov.tw/DOPS/lp-1287-105-xCat-item005.html", "性騷擾不分性別，如果有感受到不當的身體觸碰，一定要請在場的人作證，不能姑息這樣的行為。", "當下一定很錯愕但又不知道怎麼辦，這裡有個連結給你參考，自己的權益自己維護! 衛服部保護司性騷擾防治法令規章 https://dep.mohw.gov.tw/DOPS/lp-1287-105-xCat-item005.html","只要有不舒服的感受，一定要義正嚴詞的說不，讓對方知道事情的嚴重性! \n【法律小常識】性騷擾，怎麼辦？http://womany.net/read/article/1777"]




#3rd self defined function: respond to the reason    
handleSoruceDICT = {"appearance":["appearance","身體","顏值","身高","體重","額頭","髮質","髮際","髮際線","臉","眼袋","眉毛","鼻子","嘴唇","下巴","雙下巴","耳朵","脖子","手","手臂","手肘","胸部","皮膚","皺紋","斑","痣","肚子大","肚子凸","小腹","腰","肚臍","腿","大腿","小腿","膚色","屁股"],
                    "negMood":["mood","心","心情","內心","身心","感覺","感受","情緒","厭世","悲觀","累","懶","疲憊","疲乏","疲倦","負能量","憂慮","憂鬱","擔憂","抑鬱","陰鬱","鬱悶","哀傷","悶悶不樂","害怕","恐懼","生氣","易怒","怒氣沖沖","惱羞成怒","惱羞","惱怒","抓狂","發狂","煩躁","緊張","壓迫","擔心","受傷","悲傷","挫折","挫敗","討厭","噁心","心情低落","氣餒","喪氣","落魄","可悲","尷尬","罪惡感","卑微","受辱","嘲弄","懊悔","懊惱","感到抱歉","愚蠢","無力","笨","無能","無用","墮落","自甘墮落","疏遠","空虛","痛苦","哭","想哭","大哭","偷哭","嫉妒","忌妒","不安","不在乎","不高興","不開心","不愉快","不滿意","不耐煩","不爽","心情不好","心情不優","不夠格","不受歡迎","不被愛","不被喜歡","不被重視","不被看重","不知所措","不信任","沒面子","被忽略","被騙","責備","責罵","辱罵","誤解","誤會‘","羞辱","操弄","壓榨","威脅","欺負","忍受","好痛苦"],
                    "score":["分數","score","成績","表現","考","考試","評量","模擬考","學測","指考","會考","托福","雅思","多益","學科","證照","低分","差","不及格","不理想","差強人意","失望","失足"],
                    "whattodo":["whattodo","如何是好","徬徨","沒有方向","該怎麼辦","該如何是好","可以怎麼做","要怎麼做","該何去何從","該怎麼做","無助","手足無措","聊不起來"],
                    "work":["工作","工作量","work","會議","業務","專案","廠商","加班","報表","開會","簡報","考績","年終","職場","業界"],
                    "schoolwork":["作品","schoolwork","homework","分組","報告","分工","呈現","期中","期末"],
                    "colleagueRelation":["同事","同事們","夥伴","前輩","新鮮人","相處","共事"],
                    "colleagueLEI":["colleagueLEI","雷同事","馬屁精","雙面人","小人","偷懶","不做事","被幹掉","被做掉","講壞話","八卦","拍馬屁","來陰的","被弄","豬隊友"],
                    "weather":["天氣","weather","大太陽","颳風","下雨","毛毛雨","暴雨","午後雷陣雨","打雷","陰陰的","霧霾","濕氣","酷熱","熱","冷"],
                    "family": ["family","趕出家門","爸爸","爸","媽媽","媽","父親","母親","哥哥","哥","大哥","姊姊","姊","姐姐","姐","大姊","大姐","弟弟","弟","小弟","妹妹","妹","小妹","親戚","親戚們","外公","外婆","爺爺","奶奶","公公","婆婆","公婆","兒子","女兒","阿公","阿嬤","被家人氣死","被爸媽氣死","氣死", "男朋友", "女朋友", "家裡的人","女友","男友","家人","阿公","阿嬤","叔","阿姨","舅","舅媽","伯","姑","先生","太太","老公","老婆","同居人"],
                    "money":["錢","money","薪水","薪資","投資","股票","基金","花錢","存錢","存款","存不到錢","月光","信用卡費","帳單","紅利"],
                    "death":["death","死了","死亡","死掉","過世","去世","死翹翹","不在了","考試","喪禮","法會","頭七"],
                    "sick":["sick","生病","嘔吐","頭暈","痠痛","痠","痛","牙痛","頭痛","腳痛","膝蓋痛","咳嗽","乾咳","心悸","身體不舒服"],
                    "self":["自己","個人","一個人"],
                    "stranger":["stranger","陌生人","路人","有人"],
                    "food":["food","減肥餐","吃到的東西","難吃","東西很難吃"],
                    "nothing":["nothing","價值","不知道","無助","迷惘","困惑","廢","弱","沒用","渾渾噩噩","無所事事","原地踏步","沈淪","後退","退步"],
                    "relationship": ["relationship","出軌","男友","男朋友","女朋友","女友","另一半","伴侶","老公","丈夫","老婆","太太","跨國戀","遠距離","約會","在一起","被閃","閃光","分手","分了"],
                    "receipt":["發票","收據","兌獎","對獎","中獎"],
                    "ticket":["票","買票","搶票","換票","門票"],
                    "teacher":["老師","教授","教師","導師","指導教授","口委"],
                    "boss":["老闆","boss","主管","上司","主任","經理","副理","慣老闆"],
                    "thesis":["論文","書","thesis","project","paper","碩論","博論","研究","經費","實驗","受試者","口考","大綱口試","proposal","defense","畢業"],
                    "sthbroken":["broken","壞掉","破掉","碎掉","裂掉","壞了","破了","碎了","裂了","丟了","不見","弄丟"],
                    "school":["schoolLesson","廢課","爛課","課程","統計","微積分,""軍訓","服務學習","力學","實驗","化學","科學","通識","概論","導論","實務"],
                    "shop":["店","購物","買","採購","周年慶","特價","買一送一","貴","出清","促銷","特賣"],
                    "toilet":["toilet","肚子痛","脹氣","緊張","想吐","吃壞肚子","胃痛","絞痛","肚子悶","消化不良"],
                    "future":["未來","將來","以後","之後","生涯","職涯","理想","夢想","目標","前途","前景","願景"],
                    "suicide":["suicide","自殺","消失","不想活","結束生命","用我的命換","永遠都不要醒","活著還有什麼意義","跳樓","跳海","上吊","割腕","燒炭","臥軌","輕生"],
                    "sexualHarassment":["sexualHarassment","性騷擾","毛手毛腳","開黃腔","傳裸照","偷拍","捏屁股","摸屁股","摸胸部","摸腿","摟腰","勾肩","摳手心"],
                    "hunger":["hunger","吃啥","食物","食慾","餓","飽","美食沙漠","嘴饞","小鳥胃","午餐吃什麼","晚餐吃什麼","早餐吃什麼","午餐要吃什麼","晚餐要吃什麼","早餐要吃什麼","午餐吃甚麼","晚餐吃甚麼","早餐吃甚麼"],
                    "motivation":["力氣","動力","心力","狀態差","低潮","無力","心累","懶","不想動","瓶頸"],
                    "noFriend":["朋友","麻吉","兄弟","閨密","社交","social","孤單","寂寞","孤獨","邊緣","角落生物","一個人"],
                    "listen":["listen","心事","垃圾桶","傾聽","傾訴"],
                    "exchange":["exchange","交換","留學","遊學","海外實習"],
                    "test":["test","考試","測驗","小考","隨堂考","期中","期末","升學考","學測","統測","指考","口試","筆試","甄試","乙級","甲級","多益","英檢"],
                    "bully":["bully","霸凌","排擠","嘲笑","嘲諷","污辱","汙衊","抹黑","辱罵","毆打","圍毆","勒索"],
                    "afraid":["afraid","可怕","害怕","恐怖","危險","尾隨","跟蹤","變態","色狼","神經病","車禍","生死一瞬間","人生跑馬燈","好害怕","受夠","不想再忍"],
                    "missOpportunity":["missOpportunity","機會","錯過","錯失","失去","刷掉","淘汰","落選","不入取","出局"],
                    "end":["end","丟掉","不見","弄丟","丟失","遺失","偷","找不到","找不回"],
                    "nightmare":["nightmare","惡夢","噩夢","夢到"],
                    "complainToYou":["complainToYou","抱怨","牢騷","問題","東西","埋怨","鬧情緒","怪罪","責備","罵"],
                    "competition":["competition","比賽","競賽","決賽","錦標賽","預賽","循環賽","淘汰賽","海選","大隊接力","趣味競賽","個人賽"],
                    "cheerup":["cheerup"],
                    "notOpen":["notOpen"],
                    "misunderstood":["misunderstood","誤解"],
                    "badTeamMate":["badTeamMate", "分組報告","組員"],
                    "notDone":["notDone","事情","作業寫不完","功課寫不完","寫不完作業", "拖延"],
                    "boringWork":["boringWork","任務"],
                    "stepInPoop":["stepInPoop"],
                    "domestic_violence" :["domestic_violence","家暴","揍","毆打"],
                    "useless":["useless","廢物","廢柴","廢渣","小廢廢","小廢物","小廢柴","小廢渣","笑我笨","沒用","沒路用","懦弱"],
                    "wit":["頭腦","智商","腦袋","腦子","wit"],
                    "progress":["進度","progress","進步","進展","不想寫作業"],
                    "timemanagement":["timemanagement","時間","時間管理","拖延","拖拖拉拉","睡過頭","遲到"],
                    "otherpeople":["otherpeople","其他人"],
                    "friend":["friend","沒朋友","朋友不多","朋友很少","沒什麼朋友"],
                    "forgetYou":["forgetYou","被遺忘","記得"],
                    "perfection":["perfection","做不好"],
                    "lifequality":["lifequality","好累","忙"],
                    "quarrel":["quarrel","吵架","爭吵","吵"],
                    "rough":["rough"],
                    "lowSelfEsteem":["lowSelfEsteem","自卑","沒能力"],
                    "tired":["tired","累","心累"],
                    "insomia":["insomia","睡不好","沒睡好","睡不著","睡不飽","沒睡飽"],
                    "WanttobeAlone":["WanttobeAlone"],
                    "noPartner":["noPartner"],
                    "PartnerLonely":["PartnerLonely"],
                    "Anorexia": ["Anorexia"], 
                    "PressEmotion":["PressEmotion","不知道要向誰說"],
                    "pressure":["pressure","焦慮"],
                    "workWaste":["workWaste"],
                    "friendFight":["friendFight"],
                    "partnerFight":["partnerFight"],
                    "workChange":["workChange"],
                    "futurePathWorry":["futurePathWorry"],
                    "petSick":["petSick"],
                    "homesick":["homesick"],
                    "tummyhurt":["tummyhurt"],
                    "selfSick" : ["selfSick"],
                    "partnerFamilySick":["partnerFamilySick"],
                    "IamAdult":["IamAdult"],
                    "PartnerMoneyFight":["PartnerMoneyFight"],
                    "noPlacetoLive":["noPlacetoLive"],
                    "poor":["poor"]
                    }

sourceReactionDICT = {"appearance":["大家對外表可能會有一定的要求,但是重點還是在你身上,如果你喜歡這樣的自己,那又何嘗不可?"," 外表只是一時的，只要健康就好","美醜其實都是自己定義的！所以抬頭挺胸，做自信的自己！我相信你可以！","比起皮囊，我更喜歡那裡頭的靈魂。", "不論身心靈各方面，多愛自己一點是基本呀!!!", "外在美跟內在美一樣重要唷，給自己多一點自信，只要人活得開心自在，就會由內散發出美麗的光芒。"],
                    "negMood":["現在這個受委屈的心情是真實的，我懂你的不舒服，但現在的繼續努力，未來我相信一定會成為支持你的力量", "遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","我不會叫你加油，因為我知道你已經很努力了。", "找個時間好好休息一下，或是找個有趣的事情來試試看吧！","其實有很糟的一天很正常，往好的方向想，上天不太會給你撐不過的挫折，所以好好的休息一陣子，就重新調整心情重新出發", 
                    "還好嘛? 如果你不介意，可以跟我說說 (抱一個)"],
                    "score":[" 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分", "如果你已經盡力了，那就不愧對自己了。","等到以後，你會明白分數不是一切，那只是數字海中的其中幾個。"],
                    "work":["(抱) 辛苦了，適時地休息一下吧。","世上最遙遠的距離，不是我和你，而是公司到家裡。","努力工作，也要努力花錢，讓這份精神補償金變成喜歡的形狀。"],
                    "schoolwork":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"," 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費。"," 辛苦了，就算是再喜愛的工作都會有累的時候，不和你說加油，因為你已經夠努力了", "要不要試試看換一個新方法呢?", "人生也有許多沒有正確答案的事，正因為每個人答題方式不同，才會有不同的結果。"],
                    "colleagueRelation":["真的辛苦你了！看著同事的情況，一定心裡有點不舒服。","真是辛苦了，不被同事理解感覺一定很不好受。只要你現在做事無愧於心，我覺得未來一定會有欣賞你的人出現。","雖然同為工作上的夥伴，但是並不是事事都可以和同事處得好，先暫時緩緩再看看怎麼樣調適心情吧。"],
                    "colleagueLEI":["啊!這麼早遇到超級大boss的你打怪辛苦了。","辛苦你了，碰到這樣的事情，說出來總會好一點。"],
                    "weather":["♪其實我，不是因為好天氣才這麼說，牽著你走過大雨盛開水花的路口，也是我一樣喜歡的夢♪","因為天氣好，因為天氣不好，因為天氣剛剛好，每一天都很美好。","有時我會聽聽雨的聲音，嘈雜中帶點規律，聽著這規律的節拍，心好像也慢慢平靜下來。"],
                    "family": ["與家人的溝通需要智慧，有時候需要時間來思考下一步，加油加油。","家人和你生活這麼久都不見得很懂你，有話別憋在心裡，試著說出來吧。","和家人的相處其實也會有摩擦，尤其又是和自己最親近的人，遇到這樣的事情真的很不舒服！先休息一下，沉澱一下。","雖然或許家人也有他們的理由，但是其實不管怎麼樣，心裡覺得受傷的事實也不能忽略。謝謝你和我分享這些事情，我們先休息一下，再看看怎麼解決吧~"],
                    "money":["抱歉了酷東西，我需要守住我的錢錢。","好巧，我也覺得錢錢沒有夠用的一天呢！","雖然錢變成了你喜歡的形狀，但是這是不可逆的魔法，購物前還是先分清楚想要和需要吧。","你聽過財務管理的631法則嗎? 將薪水分成60%生活費、30%儲蓄、10%備用或投資，推薦給你試試看!","人和人相處，一定會有摩擦和不愉快的時候! 但重要的是，雙方能不能冷靜下來把話講開，我相信你的家人是非常關心你的!"],
                    "death":["想說什麼我都會聽你說，我也會一直陪著你","相信他會以另一種形式好好地繼續陪伴你。","形體消失了，但精神和回憶會一直一直存在在你的心裡。","和熟悉的人告別真的很不容易，謝謝你和我說，如果你想要更多陪伴我都在這裡。"],
                    "sick":["傾聽身體的聲音，找一天做個健康檢查吧!","有強大的心靈，也要有強壯的身體，沒有什麼比健康更重要了。記得定期做個健康檢查。"],
                    "self":["發現別人的光芒很容易，但記得也要好好沉澱自己，發現自己的光芒。","人一生相處最久的不是別人，是自己。記得善待自己，別忘了要溫柔，別忘了要快樂。"],
                    "stranger":["有時候真的會遇到奇怪的人，這時候就趕快跑遠一點～"],
                    "food":["如果你吐出來了！Good Job! 如果沒有，沒關係，這樣不好吃的東西會用另外一種形式排出體外！","吃到可怕的東西的感覺真的很糟啊！我完全可以理解！","天啊！吃到這樣的東西真的有點難過，快快去吃你喜歡的東西來平衡一下！(我推薦水果，我最喜歡吃了~)","就像有人喜歡芋頭，有人不喜歡。不喜歡的就不要勉強自己去接受。"],
                    "nothing":["生活比海還深，陷溺後便是流沙，你無法徒手拔出流沙裡的人，在拯救溺水者之前，你必須先呼吸。"],
                    "relationship": ["給自己一點時間好好休息吧！","會走的人你留不住，該來的人你擋不了，一切都是緣分。","切勿過度怪罪自己，因為在這之中誰都沒有錯，而誰也都有錯。","理智上可以理解，心情上過不去，也是某種成長痛","要好好長大，會有人愛你。願我們都成為逐漸完整的自己。"],
                    "receipt":[ "換個角度想，你的壞運氣都用在這裡了，接下來都會好運的。","沒關係的，至少你是個監督商家有沒有乖乖繳稅的好公民啊。"],
                    "ticket":[ "有時候運氣也是實力的一種，下次組一支搶票小隊幫忙吧。","可以問問有沒有人想讓票或換票，但切記不要跟黃牛買喔！"],
                    "teacher":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！","他們都曾是學生，理當能理解這時期的困惑與躊躇。"],
                    "boss":["先給你一個擁抱(抱)，真的辛苦你了，現在先好好從工作中休息再看看下一步怎麼做吧！","工作很累吧！先好好休息一下，聽個音樂，再重新出發。","如果是沒來由地指責，那就不要太往心裡去，因為那不是你的錯。"],
                    "thesis":["按照自己的步調來，穩穩地走！","每個人都有自己的路和步調，沒有所謂最正確或最快速，只有最適合自己的那種。","辛苦了，論文真的很需要時間。看看是不是可以和同學、學長姐或是老師討論看看呢？"],
                    "sthbroken":["舊的不去，新的不來，雖然和舊的物品說再見很難過，但是也會迎接新的夥伴啊！", "別難過! 相信你可以找到解決方案的! "],
                    "school":["枯燥乏味之事存在的意義有兩個，一個是凸顯其他有趣的事，另一個是讓你從重複中變成大師。","學校不是唯一可以學習的地方，試著自學一些東西，你會發現其中的樂趣。","學校有時候可能會帶給你一些不開心的心情，辛苦了，先轉換心情，釐清一下自己喜歡什麼吧～～"],
                    "shop":["或許現在不是一個好的時機啊！等時機對了，那所有就對了!"],
                    "toilet":["還好嗎，要不要去一趟廁所?" ],
                    "future":["人對未知都是恐懼的，練習正視自己的恐懼，慢慢來就好。","我記得有人這樣說過: 「未來早已發生，只是在現在這個當下，它們只是尚未集結的片段。」","如果未來很遠的話，那要不要試試看專注做好當下的每一件事情。","很多時候會覺得未來很難捉摸，因為都還沒有發生，也不確定會發生什麼，這個時候不妨好好感受和把握當下，然後遇到喜歡的事情就記錄起來。或許這些喜歡的小東西集結起來就可以成為未來規畫的靈感。"],
                    "suicide":["親愛的，你一點都不孤單!想聊聊天、吐苦水的話，我一直都在!\n或是你可以打這支電話，有專人傾聽你的煩惱。\n衛福部24小時安心專線：1925","你會願意和我聊聊嗎? 那怕是一點點也好，或許我能幫忙。\n或是你可以打這支電話，張老師專線：1980","或許你想逃離的不是世界，而是這一切複雜難解的問題和痛苦。如果你願意的話，說說好嗎? 讓大家陪你一起梳理打結的思緒。\n台北市生命線24小時協談專線：02-2505-9595","老天爺關了你一扇門，一定會幫你開另一扇窗!雖然現在很痛苦，你所失去的，一定會在其他地方得到饋贈。 只要我們保持樂觀的心態，相信有失必有得，一定還是有一線生機的。\n如果你需要找人聊聊，可以打這支專線。\n衛福部24小時安心專線：1925","生老病死是人生中的一大課題，我也還在努力學習中。\n如果有需要，全台各地生命線：1995，提供給你參考。"],
                    "sexualHarassment":["謝謝你願意和我分享，我覺得你非常勇敢，你沒有任何的錯！和你分享這個連結\nhttp://womany.net/read/article/1777"],
                    "hunger":["每天最困難的問題大概就是三餐吃什麼了吧! 我懂！","不要照著時間吃東西，而是覺得餓的時候再吃。想好要吃什麼了嗎? 有的話就去吃吧!","飢餓有兩種，一種是來自生理的渴望，一種是對於意義追尋的渴求。或許你現在需要一點新的東西~","不知道要吃什麼真的是個難題，有時候真的找不到靈感，要不然換個新問題，回想之前吃過覺得不錯吃的東西，來找找看靈感吧！"],
                    "motivation":["遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","感到停滯的時候，不要急著逼自己往前。休息一下充飽電再出發。","很多都會有這種累的時候，其實正是告訴你需要休息一下。先讓自己放鬆一些，再繼續～","失去動力了，不代表要放棄，很多時候只是需要休息。而放棄也沒什麼，如果你確定這不是你想要的。那換一件事情也好。"],
                    "noFriend":["你會練習跟自己相處，聽到自己內心的聲音。","自己是自己最好的朋友，傾聽內心，相信直覺，善待自己。","很多時候和自己相處真的很不容易，這也是需要學習的！不過覺得寂寞的心情其實不用掩藏，一起來想想看你喜歡做什麼事情吧！"],
                    "listen":["你會練習跟自己相處，聽到自己內心的聲音。"],
                    "exchange":["先把結果交給上天吧！我相信你一定為了出國交換付出了很多努力，你真的已經盡力了，相信上天一定會為你預備最好的結果。","準備交換或許不如自己所想，你已經很努力了！","我覺得這樣的結果真的很難過，雖然這次的交換結果不如自己的預期，但或許這次沒有出國反而會有一些新的機會產生也說不定！你很優秀又願意努力，新的機會就會上門。"],
                    "test":[ "如果你已經盡力了，那就不愧對自己了。","考試不是目的而是手段，為的是看看你對某個觀念的熟悉程度，並不是要把你考倒，放寬心~~別太執著。"],
                    "bully":["這樣一定很難受，如果你真的需要幫忙你可以試著打0800-200-885"],
                    "afraid":["辛苦你了，碰到這樣可怕的事情，說出來總會好一點。"],
                    "missOpportunity":["沒關係，如果它是屬於你的，就會是你的，總有一天會得到它的","機會是留給準備好的人，錯過了沒關係，相信努力又有實力的你，絕對可以把握住下一次。","我相信你一定可以把握下一次的機會！所以休息一下，就把這次的經驗當成學習機會！","我覺得我理解你現在的心情，我想應該是不甘心。辛苦了，先好好休息一下，我想信你一定可以把這次的經驗轉化成你的動力！"],
                    "end":["舊的不去，新的不來，會找到更多喜歡的東西的。","要揮別過的事情和東西真的很不容易，因為裡面滿滿都是回憶。","不會有不散的筵席，其實東西也是，不過這樣的感覺是真的很難過。"],
                    "others":["我知道這很難受，加油！我與你同在","辛苦你了！經歷這一切一定讓你很心累...我與你同在"],
                    "nightmare":["還好嗎? 感覺很可怕...別怕，我陪你。","做惡夢的感覺很不好，不過不用擔心，因為我聽說夢境中不好的東西都和現實相反，所以那些可怕的東西都不會發生。","先給你拍拍，別怕，你已經醒了。","別怕！你已經醒了！現在先喝口水，或許可以走一走，然後安心去睡覺吧～"],
                    "complainToYou":["辛苦你了，碰到這樣的事情，說出來總會好一點。","辛苦你了，但真的很不舒服的話，也可以試著跟他們說看看","當一個溫柔的人不容易，當你好好地接住他人的情緒，別忘了也好好照顧你內心的孩子。","當你也覺得負荷不來的時候，可以說給我聽，換我接住你。","辛苦了，遇到這些事情的你真的很不容易，謝謝你和我分享！"],
                    "competition": ["盡力就是最棒的結果","學到更多的人才是最後的贏家。","不可能凡事都是第一名，但只求在這過程中，你享受、你開心。","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。","競賽其實最後都是和以前的自己做比較，每個人狀態不一樣，所以如果你享受這全心全意的準備和付出，你就贏了！我知道你很棒！你也要知道！","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。"],
                    "cheerup":["在哪裡跌倒，就在哪裡躺下，休息一下再出發。","凡事有起有落，到谷底時正是最佳的觸底反彈時機。","謝謝你和我分享你的感覺，雖然知道挫折有時候真的是可以讓自己成長的，但有這樣的感覺真的不好受。先好好休息一下，再出發，相信一定會否極泰來。","不想和你說加油，因為我知道你已經很努力了。我只想和你說你要相信你很棒！所以要相信自己可以度過難關。"],
                    "notOpen":["可能是個可以發掘新東西的機會喔!","雖然喜歡的東西沒有買到，但或許有別的好東西～","我覺得我可以理解這種期待落空的感覺！這樣的感覺真的很不爽！"],
                    "misunderstood":["不用怕! 行得正，坐得端，就什麼都不用怕別人的眼光。","謝謝你把你的心情和我分享，被誤會的感覺真的很討厭，先逃離那個環境，再想想看怎麼解開這些誤會。","我覺得被誤會真的很討厭，真的辛苦了，先喝杯茶，先沉澱一下心情，再出發！","我自己也是最討厭被誤會了，那種不被相信的感覺真的很不好受。","真是辛苦了，不被理解感覺一定很不好受。只要你現在做事無愧於心，我覺得未來一定會有欣賞你的人出現。"],
                    "notDone":["一步一步就可以把手上的事情都做完了！","雖然看似超級多，但一點一點做，一定可以完成的~","我也很討厭事情做不完這種感覺，因為覺得壓力很大啊！但我想和你說，我相信你的能力，按部就班，絕對可以做完的！","手邊事情繁雜的時候真的很不好受，記得要適度休息喔！現在就先喝個水吧！", "先深深吸一口氣，感覺現在時間表亂成一團了，但都還是有先後順序的。好好的再安排看看吧～", "還好嗎? 是不是最近壓力太大了? 人生很長，不妨休息一下，讓身體好好休息一番，再重新出發吧! 加油加油!"],
                    "boringWork":["可以試著把枯燥乏味的事情遊戲化，當作一個個任務來破解或許就會比較有趣了。","其實工作總是會有無聊或是不喜歡的時候，覺得工作起來很無力的時候，或許休息一下轉換一下心情是個好方法！","難免會有這些比較繁瑣、無趣的時刻，但真正厲害的人，即使是無聊的工作也能處理得很好。"],
                    "stepInPoop":["天啊，可以去買張樂透了!"],
                    "domestic_violence" :["家暴只有零次和無數次，提供你發生家暴時可以做的6個步驟：\n(一)、安全第一，儘快離開現場。\n(二)、打110或113報警或救助。\n(三)、到醫院驗傷並開立診斷書。\n(四)、向法院聲請保護令，確保自身安全。\n(五)、對暴力現場或施虐行為進行拍照存證，但應以安全優先考量。\n(六)、尋求法律協助，確保自身應有權益。","不管是你最親的家人或是你最愛的伴侶，只要打人罵人就是不對，千萬別心軟再給對方一次機會，好好保護自己才是最重要的。\n若有需要，請聯繫各直轄市、縣(市)政府家庭暴力及性侵害防治中心:\nhttps://dep.mohw.gov.tw/DOPS/cp-1179-6482-105.html\n他們會很樂意幫忙你。","有些人總會說「我這樣做是為你好」，無止盡的打罵、限制東限制西，長久下來會使我們的心靈越發憂鬱，我們要做的就是盡快脫離這樣假借「以愛之名」不健康的家庭關係。\n若有需要，請尋求各縣市政府駐地方法院家庭暴力事件服務處:\nhttps://dep.mohw.gov.tw/DOPS/cp-1179-6483-105.html\n以取得專業協助。","愛一個人怎麼會捨得讓他受傷?別相信「我是因為愛你才...」這句沒邏輯的話!別讓他再用愛當藉口，將他自己的行為合理化了。\n這裡有衛服部保護司家庭暴力防治法令規章，提供給你參考:\nhttps://dep.mohw.gov.tw/DOPS/lp-1287-105-xCat-item001.html","並不是動手才算家暴，精神上的暴力也算!請盡可能的蒐證，包含人證、錄音、精神門診的診斷書，希望你可以盡快擺脫施暴者的威脅。\n你可以看看這個網頁，以尋求專業且免費的諮詢。\n安心免費法律諮詢家:https://www.vwedding.com.tw/family-law/faq05.php","不知道有沒有我能幫得上忙的地方，這裡有個線上通報平台提供你參考，希望對你有幫助。\n關懷E起來:https://ecare.mohw.gov.tw/#"],
                    "useless":["天生我材必有用，你一定可以找到自己的舞台的。"],
                    "wit":["每個人都有擅長的跟不擅長的事情呀，總有你可以發揮長才的地方!","每次都比過去的自己進步一點點，這樣就很棒了!"],
                    "whattodo":["親愛的，別擔心，靜下心來觀察，你會找到方法的。"],
                    "progress":["別把自己逼得太緊，適時地放鬆，效果會更好喔。","暫時放自己一個假，再回來的時候一定更有餘裕面對!"],
                    "timemanagement":["那可能就需要更有效的時間管理法，建議每天睡前寫下隔天要做的三件任務，將心力放在這三件重要的事即可!","這時候就希望自己像妙麗，有時間管理的魔法!"],
                    "otherpeople":["其實你可以不必和他人比較，只要每次都比過去的自己進步一點點，這樣就很棒了!","你在為你的目標努力，他在為他的理想奮鬥，大家都認真生活著呢!"],
                    "friend":["長大之後會發現，朋友不需要多，擁有幾位知心好友即可。"],
                    "forgetYou":["我懂那種把別人放在心上，但自己卻被遺忘的感覺..."],
                    "perfection":["就算你做得再好，也總有人批評，但你知道自己有努力就好。","沒有人是百分之百完美的，人都有極限，盡力就好。"],
                    "lifequality":["能力範圍之內，對自己好一點吧，沒有人能比你自己更愛你了。"],
                    "quarrel":["有理的爭論是比較激烈的溝通，無理的爭吵是唇槍舌戰。"],
                    "rough":["雖說月有陰情圓缺，不順是很正常的，但是遇到這樣的事情，我相信是是很不開心的，辛苦你了！"],
                    "badTeamMate":["辛苦你了， 相信你一定心很累，謝謝你和我分享，但如果你評估可以，要和這個同伴好好的講。"],
                    "lowSelfEsteem":["要好好相信自己，每個人擅長的地方都不太一樣，所以再適應一下，一定可以找到自己的擅長的地方"],
                    "tired":["還好嗎? 是不是最近壓力太大了? 人生很長，不妨休息一下，讓身體好好休息一番，再重新出發吧! 加油加油!", "現在人人都壓力很大，偶爾心情低落是正常的，只要適度的釋放出來，就不必擔心喔! 這邊也提供一個三分鐘小測驗，可以檢視一下自己的憂鬱指數唷! https://www.ihealth.com.tw/article/%E6%86%82%E9%AC%B1%E7%97%87/"],
                    "insomia":["天啊! 辛苦你了! 一定很難受吧! 建議去看一下醫生，看看能怎麼治療，才能恢復好的睡眠品質。"],
                    "WanttobeAlone":['其實有時候獨處並不是一件壞事，不僅可以讓自己淨空煩惱，還能享受一個人的時光喔。', "我可以懂那種不想面對人的感覺，不想出門就別勉強自己吧! 只要努力地過好每一天，不管出門與否，都會很充實、很有意義的!"],
                    "noPartner":["別難過! 或許最近大家都很忙碌，可以試著多跟另一半溝通，或是讓自己也忙碌起來轉移注意力喔。"],
                    "PartnerLonely":["俗話說: 小別勝新歡，短暫的分離會讓你們在相聚的時候更珍惜對方喔!"],
                    "Anorexia": ["還好嗎? 有時候心情低落也會連帶影響到食慾。試試保持心情愉快，如果症狀沒有改善就需要盡快就醫喔!"], 
                    "PressEmotion":["請試試找個可以信賴的人說心事，長久下來才不會憋出病喔。\n或是有需要的話，可以打這支專線: 衛福部24小時安心專線 1925","請試著和信任的人說說你的狀況，不要害怕麻煩別人，他們一定會很樂意幫你。\n或是有需要的話也可以打這支專線: 衛福部24小時安心專線 1925"],
                    "pressure":["還好嗎? 人生很長，不妨休息一下，讓身體好好休息一番，再重新出發吧! 加油加油!","一點程度的壓力能催出好的表現，過多的壓力會降低人的表現。是不是覺得最近壓力重得讓人喘不過氣呢? 給自己休息一下吧!"],
                    "workWaste":["現在或許覺得是白忙，但是我相信現在的努力未來一定可以幫助你。關於有沒有用不到的經歷，我想推薦給你這篇文章 「【意外之外】訪于美人，與她的書房：「人生沒有用不到的經歷」」https://crossing.cw.com.tw/article/14259"],
                    "friendFight":["和朋友相處不開心真的感覺不太好，謝謝你和我分享，再觀察看看，如果感覺還可以的話要不要再找朋友談談呢？"],
                    "partnerFight":["親密的伴侶難免會有這樣的時候，但我相信好好溝通會有出路的！"],
                    "workChange":["下一站會更好的! 但記得也要好好沉澱自己，機會到來時才能發揮喔!"],
                    "futurePathWorry":["未來的事情人人都說不準，但你煩惱破頭的同時也錯過了讓自己開心的機會耶! 不妨出去，呼吸新鮮空氣吧!"],
                    "petSick":["天啊! 辛苦你了! 一定很難受吧! 在照顧寵物同時，也別忘了要照顧自己喔!"],
                    "homesick":["你一定覺得很寂寞，辛苦你了，一個人在外打拼，真是不容易，看看日程，找找看哪天回家一趟吧～（抱）"],
                    "tummyhurt":['肚子一定很不舒服！如果真的不行，一定要去看醫生啊！'],
                    "selfSick":["辛苦了你了，一定要好好休息，再不舒服，一定要去看醫生啊！"],
                    "partnerFamilySick":["最親的人生病了，你一定覺得很難過，如果可以在適度關心他們的情況之下，自己也要好好休息喔！"],
                    "IamAdult":["遇到難解之事，我都會跟自己說:我是大人了~我是大人了~我是大人了啊~咩噗!","理智上能理解，心情上過不去，也是某種成長痛。"],
                    "PartnerMoneyFight":["會有這種感覺想必是因為覺得對方不珍惜自己，辛苦你，在金錢觀方面觀念不一樣真的很辛苦，如果可以，看看要不要和伴侶再溝通一下啊！"], 
                    "noPlacetoLive":["天啊!這樣一定很徬徨吧！看看是不是可以尋求親朋好友的協助!"],
                    "poor":["我知道這很難受！看看是不是可以尋求親朋好友的協助!"]
                    
                    }