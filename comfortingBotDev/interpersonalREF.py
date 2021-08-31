#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# INTERPERSONAL

'''
"familyLIST":["爸媽","父母","父母親","我爸","爸爸","父親","我媽","媽媽","母親",
              "兄弟姐妹","兄弟姊妹","我哥","哥哥","我姐","我姊","姊姊","姐姐","我弟","弟弟","我妹","妹妹",
              "祖父母","阿公","阿嬤","爺爺","奶奶","外公","外婆","祖父","祖母","長輩","老人家","阿祖",
              "親戚","叔叔","叔","舅舅","舅","伯","姨丈","姑丈","阿姨","姨","姑姑","姑","嬸嬸","嬸","舅媽",
              "表兄弟姊妹","表兄弟姐妹","表哥","表弟","表姊","表姐","表妹",
              "堂兄弟姐妹","堂兄弟姊妹","堂哥","堂弟","堂姊","堂姐","堂妹","外甥","外甥女","姪子","姪女",
              "家裡的人","親人","家人","同居人","老公","老婆","夜間部同學","先生","太太","公婆","公公","婆婆","岳父","岳母",
              "兒子","女兒","孫子","孫女","曾孫","曾孫女","大嫂","嫂子","嫂","姊夫","姐夫","弟媳","妹婿","女婿","媳婦","妹夫"],
"petLIST":["寵物","狗","狗狗","拉不拉多","黃金獵犬","鬥牛犬","巴哥","貴賓","馬爾濟斯","土狗","博美","柴犬","哈士奇","約克夏",
           "吉娃娃","牧羊犬","獵犬","秋田犬","米格魯","比熊犬","沙皮","鬆獅","臘腸狗","大麥町","雪納瑞","蝴蝶犬","聖伯納","藏獒",
           "貓","貓貓","摺耳貓","短毛貓","反耳貓","波絲貓","黑貓","橘貓","花貓",
           "鼠","寵物鼠","黃金鼠","天竺鼠","三線鼠",
           "魚","犬","鳥","龜","鼬","蛇"],
"friendLIST":["朋友","朋朋","麻吉","閨密","兄弟","同學","姊妹","姐妹"],
"partnerLIST":["男友","男朋友","女友","女朋友","閃光","閃","伴侶","另一半"],
"colleagueLIST":["同事","組員","工作夥伴","前輩","後輩","新人","助理","同組同學"]
'''

handleSoruceDICT = {
# About family, pet, friend, partner
                    "family":["family"],
                    "pet":["pet"],
                    "friend":["friend"],
                    "partner":["partner"],
                    "colleague":["colleague"],
# Sick / death                  
                    "familySick":["familySick"],
                    "petSick":["petSick"],
                    "death":["death","死掉","過世","逝世","辭世","與世長辭","離世","駕鶴西歸","圓寂","當天使","死了","死亡","死翹翹","喪禮","告別式"],
# Team
                    "badTeamMate":["badTeamMate","雷同事","雷組員","雷夥伴","雷同學","不做事","偷懶","講壞話","豬隊友","小人","雙面人","馬屁精","分組報告"],
# Relationship
                    "loveBetrayal":["loveBetrayal","出軌","劈腿","在外面亂來","在外面亂搞","背著我亂來","背著我亂搞","渣","渣男","渣女","花心","不專一","腳踏兩條船"],
                    "breakup":["breakup","分手","提分手","說要分手","說要跟我分手","被甩了","甩了我","被男友甩了","被女友甩了","被男朋友甩了","被女朋友甩了","失戀"],
                    "crush":["crush","暗戀的人","喜歡的人","迷戀的人","單戀","暗戀"],
                    "relationship":["relationship","遠距離","跨國戀","偽單身","老夫老妻","沒感覺"],
# Fight                   
                    "moneyFight":["moneyFight","好摳","AA","AA制","為錢吵架","價錢談不攏","為錢起爭執","欠錢不還","欠我錢","欠一堆錢","一屁股債"],
                    "familyFight":["familyFight"],
                    "partnerFight":["partnerFight"],
                    "otherFight":["otherFight"],
# Competition
                    "competition":["competition","比賽","競賽","決賽","錦標賽","預賽","循環賽","淘汰賽","海選","大隊接力","趣味競賽","個人賽","團體賽"],
# Lonely / no friend / no partner / forgotten
                    "feelLonely":["feelLonely","寂寞","孤單","孤獨","想有人陪","很少陪我","沒人陪","相處時間少","相處時間變少"],
                    "noFriend":["noFriend","沒朋友","邊緣","邊緣人","人緣不好","沒人跟我一組","交不到朋友","朋友很少","朋友不多","沒什麼朋友","沒甚麼朋友"],
                    "noPartner":["noPartner","想脫魯","想交男友","想交女友","想談戀愛"],
                    "forgetYou":["forgetYou"],
# Teacher / boss / supervisor / authority
                    "teacher":["teacher","老師","導師","教師","教授","指導老師","口試委員","口委"],
                    "boss":["boss","老闆","主管","上司","經理","副理","慣老闆","董事長","理事","理事長","組長","課長"],
# Listen / complain / misunderstood
                    "listen":["listen","心事","傾聽","傾訴"],
                    "complainToYou":["complainToYou","抱怨","牢騷","發牢騷","埋怨","罵","鬧情緒"],
                    "misunderstood":["misunderstood","誤解","誤會"],
# Other people / stranger
                    "otherPeople":["otherPeople","其他人","別人","周圍的人","身邊的人"],
                    "stranger":["stranger","陌生人","怪人","噁男","噁女","奇怪的人","莫名其妙的人","隔壁的人"]

}


sourceReactionDICT = {
# About family, pet, friend, partner
                    "family":["越是親近的人，越容易用為你好當作藉口，希望你能照做，但有時候這句為你好，只是為了他們自己好。","有些事情不該因為是家人而讓步，如果你覺得不妥，就應該說出來大家好好檢視、討論。"],
                    "pet":["寵物也是有靈性的，或許有耐心地多講幾次，牠就會懂噢。","人家說寵物跟主人生活久了會變得相像，難道你家寵物也是嗎?"],
                    "friend":["難以捉摸的人際距離，有時太疏離有時太靠近，如何和新朋友舊朋友好好相處，是我仍然在學習的事情。"],
                    "partner":["兩個人的相處需要磨合，合則來不合則去。"],
                    "colleague":["除了做好自己的份內工作，經營團隊關係也是個重要的課題呢。"],
# Sick / death                  
                    "familySick":["絕對沒有人願意生病，所以在他們不舒服且徬徨無助的時刻，適當的照顧和心理支持是最好的後援!","你也要好好照顧自己，才有力氣照顧他人。"],
                    "petSick":["照顧寵物的同時，也別忘了好好照顧自己喔!","你待牠就像對待家人一樣，相信在你細心的照顧之下，牠會好起來的。"],
                    "death":["想說什麼我都會聽你說，我也會一直陪著你。","相信他會以另一種形式好好地繼續陪伴你。","形體消失了，但精神和回憶會一直一直存在在你的心裡。","和熟悉的人告別真的很不容易，如果你想要更多陪伴我都在這裡。"],
# Team
                    "badTeamMate":["辛苦你了，遇到這樣的人這樣的事你一定心很累，如果可以的話，要不要和他好好溝通一下呢~","啊!這麼早遇到超級大boss的你打怪辛苦了。"],
# Relationship
                    "loveBetrayal":["哎呀不小心踢到一個東西，請問是你遺失的嗎? 但我想應該不是，因為他看起來像個垃圾。","相信你已經把一切壞運氣都用在這裡了，接下來只會遇見更好的人!"],
                    "breakup":["給自己一點時間好好休息吧！","會走的人你留不住，該來的人你擋不了，一切都是緣分。","切勿過度怪罪自己，因為在這之中誰都沒有錯，而誰也都有錯。","理智上可以理解，心情上過不去，也是某種成長痛","要好好長大，會有人愛你。願我們都成為逐漸完整的自己。"],
                    "crush":["如果有緣份，那個人絕對會來到你身邊的。","有些關係說了就會變質，但有些關係不說不會開始呀~","會走的人你留不住，該來的人你擋不了，一切都是緣分。"],
                    "relationship":["維持一段關係不容易，要讓產生裂痕卻是輕而易舉，要好好珍惜喔。"],
# Fight                   
                    "moneyFight":["所有事情只要牽扯到金錢，就會變成複雜的問題，即使再親近的人也是如此。","該是自己的權利就去爭取，不是屬於自己的就不要貪心。","不是要你成為一個斤斤計較的人，但有時候人與人之間還是算得清楚一點，對雙方都比較好。"],
                    "familyFight":["我們常對外人客客氣氣很有耐心，卻對親近的人不耐煩、大小聲。溝通時不要急著反駁對方，要先傾聽再表達。","家人朝夕相處難免有磨擦，但不愉快過後，你們終究還是要一起生活的啊。找個時間好好聊聊和解吧。"],
                    "partnerFight":["兩個獨立個體不可能事事都有完全相同的想法，不過相信靜下心來討論，一定可以找到讓兩個人都滿意的解方。","吵架的時候不要翻舊帳，也不要吵隔夜架，更不要因為一時在氣頭上而做出人身攻擊或是說出傷人的話。"],
                    "otherFight":["每個人都有他的立場，若能稍稍同理他人，或許雙方都能找到和平共處的平衡點。","人與人之間的溝通需要智慧，不管是誰，都不要急著出一張嘴。"],
# Competition
                    "competition":["盡力就是最棒的結果。","從那之中學到更多的人才是最後的贏家。","不可能凡事都是第一名，但只求在這過程中，你享受、你開心。","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。","競賽其實最後都是和以前的自己做比較，我知道你很棒！你也要知道！","和別人比較是永遠比不完的，只要比以前的自己進步一點點，你就很棒了。"],
# Lonely / no friend / no partner / forgotten
                    "feelLonely":["不論身邊有多少人，都會感到孤獨。","需要被理解而不被理解，正是我們感到孤獨的原因。","能陪你最久的人就是你自己，所以無論如何都要學會和自己相處。","孤獨並不全然是件壞事，換個角度想，此時此刻的時間&空間、生理&心理，全屬於你自己。"],
                    "noFriend":["朋友不用多，有幾個真心待人又懂你的知心好友即可。","根據研究，一個人最多能經營的關係是150人，也就是說真正有在交流互動的大約只有150人而已。","羨慕他人擁有龐大人脈的同時，也別忘了過多過複雜的人際網絡會帶來虛耗，經營這些都是很費力的。"],
                    "noPartner":["看著別人都出雙入對的很是羨慕，但單身又何嘗不好呢? 超級自由的啊!!!","我懂你!有時候不是自己太挑，是看來看去都沒有適合的人。","可以試著把理想型的條件都寫下來，越詳細越好，這樣月老就可以很精準地幫你找人喔!"],
                    "forgetYou":["我懂那種把別人放在心上，但自己卻被遺忘的感覺...","老師點名漏掉你、朋友邀請少了你、家庭出遊忘了你，我也有相同的經驗，非常感同身受QAQ"],
# Teacher / boss / supervisor / authority
                    "teacher":["他們都曾是學生，理當能理解這時期的困惑與躊躇。"],
                    "boss":["工作很累吧！先好好休息一下，再重新出發。","有些事情有些話，不要太往心裡去，因為那不是你的錯也不是你的責任。"],
# Listen / complain / misunderstood
                    "listen":["你可以說給我聽呀~~我來接住你。","讓我來當你的樹洞，承接你所有的負面情緒。"],
                    "complainToYou":["辛苦你們了，不論是聽的一方還是說的一方。","當一個溫柔的人不容易，當你好好地接住他人的情緒，別忘了也好好照顧你內心的孩子。","當你也覺得負荷不來的時候，可以說給我聽，換我接住你。"],
                    "misunderstood":["我自己也是最討厭被誤會了，那種不被信任的感覺真的很不好受。","真理會越辯越明，時間會證明你是對的。"],
# Other people / stranger
                    "otherPeople":["要怎麼處理外界看你或是你看外界的眼光，這是你的自由，但更多時候它是一種選擇。"],
                    "stranger":["遇到怪怪的人還是先跑為妙!","裝作若無其事快快離開現場吧。"]

}