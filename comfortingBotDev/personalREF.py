#!/usr/bin/env python3
# -*- coding:utf-8 -*-


handleSoruceDICT = {
                    # 生理相關
                    "appearance":["appearance","身體","顏值","身高","體重","額頭","髮質","髮際","髮際線","臉","眼袋","眉毛","鼻子","嘴唇","下巴","雙下巴","耳朵","脖子","手","手臂","手肘","胸部","皮膚","皺紋","斑","痣","肚子大","肚子凸","小腹","腰","肚臍","腿","大腿","小腿","膚色","屁股", "醜", "短", "肚子", "很胖", "痘痘"],
                    "period":["period", "月經", "生理期", "生理"],
                    "sick":["sick","生病","痠痛","痠","痛","身體不舒服"],
                    "toilet":["toilet","拉屎", "廁所", "想大便","肚子痛","脹氣","緊張","想吐","吃壞肚子","胃痛","絞痛","肚子悶","消化不良"],
                    "hunger":["hunger","吃啥","食物","食慾","餓","飽","美食沙漠","嘴饞","小鳥胃","午餐吃什麼","晚餐吃什麼","早餐吃什麼","午餐要吃什麼","晚餐要吃什麼","早餐要吃什麼","午餐吃甚麼","晚餐吃甚麼","早餐吃甚麼"],
                    "nightmare":["nightmare","惡夢","噩夢","夢到", "做惡夢", "夢到可怕"],
                    "Anorexia": ["Anorexia"],
                    "WanttobeAlone":["WanttobeAlone", "不想跟別人social", "躲在宿舍"], 
                    "insomia":["insomia","睡不好","沒睡好","睡不著","睡不飽","沒睡飽", "睡"],
                    "tired":["tired", "身體變好差", "身體"],
                    
                    #心情相關
                    "negMood":["mood","心","心情","內心","身心","感覺","感受","情緒","厭世","悲觀","累","懶","疲憊","疲乏","疲倦","負能量","憂慮","憂鬱","擔憂","抑鬱","陰鬱","鬱悶","哀傷","悶悶不樂","害怕","恐懼","生氣","易怒","怒氣沖沖","惱羞成怒","惱羞","惱怒","抓狂","發狂","煩躁","緊張","壓迫","擔心","受傷","悲傷","挫折","挫敗","討厭","噁心","心情低落","氣餒","喪氣","落魄","可悲","尷尬","罪惡感","卑微","受辱","嘲弄","懊悔","懊惱","感到抱歉","愚蠢","無力","笨","無能","無用","墮落","自甘墮落","疏遠","空虛","痛苦","哭","想哭","大哭","偷哭","嫉妒","忌妒","不安","不在乎","不高興","不開心","不愉快","不滿意","不耐煩","不爽","心情不好","心情不優","不夠格","不受歡迎","不被愛","不被喜歡","不被重視","不被看重","不知所措","不信任","沒面子","被忽略","被騙","責備","責罵","辱罵","誤解","誤會‘","羞辱","操弄","壓榨","威脅","欺負","忍受","好痛苦", "很糟","沒有", "偏心", "難過", "被看見", "沒人懂", "糟糕", "很差","被說", "孤單", "傷心", "失望"],
                    "selfHate":["selfHate", "自己","個人","一個人"],
                    "nothing":["nothing","價值","不知道","無助","迷惘","困惑","廢","弱","沒用","渾渾噩噩","無所事事","原地踏步","沈淪","後退","退步","沒事", "沒什麼", "沒"],
                    "bully":["bully","霸凌","排擠","嘲笑","嘲諷","污辱","汙衊","抹黑","辱罵","毆打","圍毆","勒索", "排擠",],
                    "afraid":["afraid","可怕","害怕","恐怖","危險","尾隨","跟蹤","變態","色狼","神經病","車禍","生死一瞬間","人生跑馬燈","好害怕","受夠","不想再忍", "預防針"],
                    "cheerup":["cheerup", "不起勁", "才可以成功", "失敗"],
                    "envy":["envy", "厲害","頭腦","智商","腦袋","腦子", "憑什麼", "做到"],
                    "annoyed":["annoyed","煩躁", "很煩"],
                    "homeSick":["homeSick", "想家", "想回家"],
                    "pressure":["pressure","焦慮", "壓力", "爆炸", "困難"],
                    "PressEmotion":["PressEmotion","不知道要向誰說", "壓抑"],
                    "lowSelfEsteem":["lowSelfEsteem","自卑","沒有貢獻", "討厭", "很廢", "沒能力", "廢物","廢柴","廢渣","小廢廢","小廢物","小廢柴","小廢渣","笑我笨","沒用","沒路用","懦弱", "自己", "微不足道"],
                    "rough":["rough", "很雖", "事情都不順", "不順"], 
                    
                    #工作/學業相關 
                    "work":["work", "上班", "下班","工作","工作量","work","會議","業務","專案","廠商","加班","報表","開會","簡報","考績","年終","職場","業界"],
                    "schoolwork":["schoolwork","作業", "分數", "方向","作品","homework","分組","報告","分工","呈現","期中","期末"],
                    "score":["score","分數","成績","表現","考","考試","評量","模擬考","學測","指考","會考","托福","雅思","多益","學科","證照","低分","差","不及格","不理想","差強人意","失望","失足", "考上", "低空飛過"],
                    "test":["test","考試","測驗","小考","隨堂考","期中","期末","升學考","學測","統測","指考","口試","筆試","甄試","乙級","甲級","多益","英檢"],
                    "motivation":["motivation","力氣","動力","心力","狀態差","低潮","無力","心累","懶","不想動","瓶頸","動機", "不想做", "提不起勁", "做事"],
                    "noAbility":["noAbility",  "很難做"],
                    "futurePathWorry":["futurePathWorry",  "找得到工作","未來","將來","以後","之後","生涯","職涯","理想","夢想","目標","前途","前景","願景", "考"],
                    "workChange":["workChange", "換工作", "換不了工作" ],
                    "workWaste":["workWaste", "白忙", "沒有成效", "白工"],                    
                    
                    #生活相關
                    "noPlacetoLive":["noPlacetoLive", "住在哪裡", "租屋處"], 
                    "quarrel":["quarrel","起了口角","吵架","爭吵","吵", "起了衝突"],
                    "lifeQuality":["lifeQuality","沒生活品質","好累","忙", "生活品質"],
                    "perfection":["perfection","做不好", "標準"],
                    "TimeManagement":["TimeManagement","時間","時間管理","拖延","拖拖拉拉","睡過頭","遲到"]
                    }

sourceReactionDICT = {
                    #生理相關
                    "appearance":["大家對外表可能會有一定的要求,但是重點還是在你身上,如果你喜歡這樣的自己,那又何嘗不可?"," 外表只是一時的，只要健康就好","美醜其實都是自己定義的！所以抬頭挺胸，做自信的自己！我相信你可以！","比起皮囊，我更喜歡那裡頭的靈魂。", "不論身心靈各方面，多愛自己一點是基本呀!!!", "外在美跟內在美一樣重要唷，給自己多一點自信，只要人活得開心自在，就會由內散發出美麗的光芒。"],
                    "period":["生理期來一定很不舒服吧！記得好好休息一下喔！", "這種身體疲憊心情很不好、肚子痛的感覺一定讓你心情很不好，要好好休息一下喔！", "好好喝個熱熱的紅豆湯，讓肚子暖起來，也讓新暖起來！"],
                    "sick":["傾聽身體的聲音，找一天做個健康檢查吧!","有強大的心靈，也要有強壯的身體，沒有什麼比健康更重要了。記得定期做個健康檢查。", "身體一定很不舒服！如果真的不行，一定要去看醫生啊！"],
                    "toilet":["還好嗎，要不要去一趟廁所?" ],
                    "hunger":["每天最困難的問題大概就是三餐吃什麼了吧! 我懂！","不要照著時間吃東西，而是覺得餓的時候再吃。想好要吃什麼了嗎? 有的話就去吃吧!","飢餓有兩種，一種是來自生理的渴望，一種是對於意義追尋的渴求。或許你現在需要一點新的東西~","不知道要吃什麼真的是個難題，有時候真的找不到靈感，要不然換個新問題，回想之前吃過覺得不錯吃的東西，來找找看靈感吧！"],
                    "nightmare":["還好嗎? 感覺很可怕...別怕，我陪你。","做惡夢的感覺很不好，不過不用擔心，因為我聽說夢境中不好的東西都和現實相反，所以那些可怕的東西都不會發生。","先給你拍拍，別怕，你已經醒了。","別怕！你已經醒了！現在先喝口水，或許可以走一走，然後安心去睡覺吧～"],
                    "Anorexia": ["還好嗎? 有時候心情低落也會連帶影響到食慾。試試保持心情愉快，如果症狀沒有改善就需要盡快就醫喔!"], 
                    "WanttobeAlone":['其實有時候獨處並不是一件壞事，不僅可以讓自己淨空煩惱，還能享受一個人的時光喔。', "我可以懂那種不想面對人的感覺，不想出門就別勉強自己吧! 只要努力地過好每一天，不管出門與否，都會很充實、很有意義的!"],
                    "insomia":["天啊! 辛苦你了! 一定很難受吧! 建議去看一下醫生，看看能怎麼治療，才能恢復好的睡眠品質。"],
                    "tired":["還好嗎? 是不是最近壓力太大了? 人生很長，不妨休息一下，讓身體好好休息一番，再重新出發吧! 加油加油!", "現在人人都壓力很大，偶爾心情低落是正常的，只要適度的釋放出來，就不必擔心喔! 這邊也提供一個三分鐘小測驗，可以檢視一下自己的憂鬱指數唷! https://www.ihealth.com.tw/article/%E6%86%82%E9%AC%B1%E7%97%87/"],
                    
                    #心情相關
                     "negMood":["現在這個受委屈的心情是真實的，我懂你的不舒服，但現在的繼續努力，未來我相信一定會成為支持你的力量", "遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","我不會叫你加油，因為我知道你已經很努力了。", "找個時間好好休息一下，或是找個有趣的事情來試試看吧！","其實有很糟的一天很正常，往好的方向想，上天不太會給你撐不過的挫折，所以好好的休息一陣子，就重新調整心情重新出發", "還好嘛? 如果你不介意，可以跟我說說 (抱一個)"],
                    "selfHate":["發現別人的光芒很容易，但記得也要好好沉澱自己，發現自己的光芒。","人一生相處最久的不是別人，是自己。記得善待自己，別忘了要溫柔，別忘了要快樂。"],
                    "nothing":["生活比海還深，陷溺後便是流沙，你無法徒手拔出流沙裡的人，在拯救溺水者之前，你必須先呼吸。"],
                    "afraid":["辛苦你了，碰到這樣可怕的事情，說出來總會好一點。"],
                    "cheerup":["在哪裡跌倒，就在哪裡躺下，休息一下再出發。","凡事有起有落，到谷底時正是最佳的觸底反彈時機。","謝謝你和我分享你的感覺，雖然知道挫折有時候真的是可以讓自己成長的，但有這樣的感覺真的不好受。先好好休息一下，再出發，相信一定會否極泰來。","不想和你說加油，因為我知道你已經很努力了。我只想和你說你要相信你很棒！所以要相信自己可以度過難關。"],
                    "envy":["每個人都有擅長的跟不擅長的事情呀，總有你可以發揮長才的地方!","每次都比過去的自己進步一點點，這樣就很棒了!"],
                    "annoyed":["覺得很煩躁嗎？相信面對手頭上的事情你一定覺得心很累，暫時先脫離目前手上的事情，做一點你想要的東西！"],
                    "homeSick":["你一定覺得很寂寞，辛苦你了，一個人在外打拼，真是不容易，看看日程，找找看哪天回家一趟吧～（抱）"],
                    "pressure":["還好嗎? 人生很長，不妨休息一下，讓身體好好休息一番，再重新出發吧! 加油加油!","一點程度的壓力能催出好的表現，過多的壓力會降低人的表現。是不是覺得最近壓力重得讓人喘不過氣呢? 給自己休息一下吧!"],
                    "PressEmotion":["請試試找個可以信賴的人說心事，長久下來才不會憋出病喔。\n或是有需要的話，可以打這支專線: 衛福部24小時安心專線 1925","請試著和信任的人說說你的狀況，不要害怕麻煩別人，他們一定會很樂意幫你。\n或是有需要的話也可以打這支專線: 衛福部24小時安心專線 1925"],
                    "lowSelfEsteem":["要好好相信自己，每個人擅長的地方都不太一樣，所以再適應一下，一定可以找到自己的擅長的地方", "天生我材必有用，你一定可以找到自己的舞台的。"],
                    "rough":["雖說月有陰情圓缺，不順是很正常的，但是遇到這樣的事情，我相信是是很不開心的，辛苦你了！"],
                    
                    #課業工作相關
                    "work":["(抱) 辛苦了，適時地休息一下吧。","世上最遙遠的距離，不是我和你，而是公司到家裡。","努力工作，也要努力花錢，讓這份精神補償金變成喜歡的形狀。"],
                    "schoolwork":["按照自己的步調走，對得起自己就好，其他就隨他們講吧！"," 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費。"," 辛苦了，就算是再喜愛的工作都會有累的時候，不和你說加油，因為你已經夠努力了", "要不要試試看換一個新方法呢?", "人生也有許多沒有正確答案的事，正因為每個人答題方式不同，才會有不同的結果。"],
                    "score":[" 我相信你一定做了很多的努力，辛苦你了，但我相信你這邊做的努力不會白費，一定可以成為未來很好的養分", "如果你已經盡力了，那就不愧對自己了。","等到以後，你會明白分數不是一切，那只是數字海中的其中幾個。"],
                    "test":[ "如果你已經盡力了，那就不愧對自己了。","考試不是目的而是手段，為的是看看你對某個觀念的熟悉程度，並不是要把你考倒，放寬心~~別太執著。"],
                    "motivation":["遇到難解之事，都會在心裡跟自己說: 我是大人 我是大人 我是大人了啊 咩噗!!!","感到停滯的時候，不要急著逼自己往前。休息一下充飽電再出發。","很多都會有這種累的時候，其實正是告訴你需要休息一下。先讓自己放鬆一些，再繼續～","失去動力了，不代表要放棄，很多時候只是需要休息。而放棄也沒什麼，如果你確定這不是你想要的。那換一件事情也好。"],
                    "noAbility":["看到自己能力不足是一個進步的開始，所以認清現在需要再進步什麼！再接再勵！"],
                    "futurePathWorry":["未來的事情人人都說不準，但你煩惱破頭的同時也錯過了讓自己開心的機會耶! 不妨出去，呼吸新鮮空氣吧!", "人對未知都是恐懼的，練習正視自己的恐懼，慢慢來就好。","我記得有人這樣說過: 「未來早已發生，只是在現在這個當下，它們只是尚未集結的片段。」","如果未來很遠的話，那要不要試試看專注做好當下的每一件事情。","很多時候會覺得未來很難捉摸，因為都還沒有發生，也不確定會發生什麼，這個時候不妨好好感受和把握當下，然後遇到喜歡的事情就記錄起來。或許這些喜歡的小東西集結起來就可以成為未來規畫的靈感。"],
                    "workChange":["下一站會更好的! 但記得也要好好沉澱自己，機會到來時才能發揮喔!"],
                    "workWaste":["現在或許覺得是白忙，但是我相信現在的努力未來一定可以幫助你。關於有沒有用不到的經歷，我想推薦給你這篇文章 「【意外之外】訪于美人，與她的書房：「人生沒有用不到的經歷」」https://crossing.cw.com.tw/article/14259"],
                    
                    #生活相關
                     "noPlacetoLive":["天啊!這樣一定很徬徨吧！看看是不是可以尋求親朋好友的協助!"],
                     "quarrel":["有理的爭論是比較激烈的溝通，無理的爭吵是唇槍舌戰。"],
                     "lifequality":["能力範圍之內，對自己好一點吧，沒有人能比你自己更愛你了。"],
                     "perfection":["就算你做得再好，也總有人批評，但你知道自己有努力就好。","沒有人是百分之百完美的，人都有極限，盡力就好。"]                    
                    }