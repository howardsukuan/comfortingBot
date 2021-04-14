#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for domestic_violence

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_domestic_violence = True
userDefinedDICT = {}

familyLIST = ["爸","媽","家裡的人","弟","哥","姊","姐","妹","女友","男友","我","家人","阿公","阿嬤","叔","阿姨","舅","舅媽","伯","姑","先生","太太","老公","老婆","同居人"]
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_domestic_violence:
        print("[domestic_violence] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[媽媽]因為我成績退步[一直]打[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"         
        pass

    if utterance == "[弟弟]把[我]壓在[地][上]說要打死[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"         
        pass

    if utterance == "[我]被[家人]揍到流血":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass

    if utterance == "[我]被[爸爸]打":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass

    if utterance == "[爸爸][一直]揍[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence" 
        pass

    if utterance == "[爸爸][喝醉酒]回來就打[媽]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"         
        pass

    if utterance == "[爸爸]打[我]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass

    if utterance == "[爸爸]毆打[媽媽]":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"         
        pass

    if utterance == "[男友]對[我]動手":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[爸爸]拿[藤條]抽[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[我]被[爸爸]揍":
        # write your code here
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[爸爸]向[我]揮拳":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[爸爸]痛毆[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass     
    
    if utterance == "[爸爸]對[我]施暴":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass  
    
    if utterance == "[爸爸]家暴[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass 
    
    if utterance == "[爸爸]對[我]使用暴力":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass 
    
    if utterance == "[我]被[爸爸]虐待":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass 
    
    if utterance == "[爸爸]把[我]抓起來摔":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass 
    
    if utterance == "[爸爸]對[我]動粗":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[爸爸]拿熱水潑[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass
    
    if utterance == "[爸爸]把[我]打到瘀青":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass        
         
    if utterance == "[爸爸]把[我]打到流血":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass  
    
    if utterance == "[爸爸][常常]賞[我]巴掌":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"        
        pass  
    
    if utterance == "[爸爸]對[我]拳打腳踢":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass      
    
    if utterance == "[爸爸]拿菸燙[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass    
    
    if utterance == "[爸爸][一直]抓[我]的頭去撞牆":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"        
        pass  
    
    if utterance == "[爸爸]用言語辱罵[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass    
    
    if utterance == "[爸爸]用[拳頭]打[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"        
        pass   
    
    if utterance == "[爸爸]心情不好就打[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"        
        pass    
    
    if utterance == "[爸爸]心情不好就揍[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass 
    
    if utterance == "[爸爸]限制[我]出門的自由":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass
    
    if utterance == "[爸爸]要殺掉[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass 
    
    if utterance == "[爸爸]說要殺掉[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass 
    
    if utterance == "[爸爸]說要打死[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass   
    
    if utterance == "[爸爸]要打死[我]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass 
    
    if utterance == "[我]被[家人]打得半死":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"            
        pass     
    
    if utterance == "[我]被[家人]打個半死":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"                
        pass
    
    if utterance == "[爸爸]常對[我]使用言語暴力":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"                
        pass
    
    if utterance == "[爸爸][常常]對[我]罵髒話":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"                
        pass        
    
    if utterance == "[爸爸][常常]罵[我]髒話":
        if any(e in args[0] for e in familyLIST) and any(e in args[2] for e in familyLIST) and (args[0] != args[2]):
            resultDICT["source"] = "domestic_violence"                
        pass   
    
    if utterance == "[爸爸]把[我]鎖在家[裡]":
        if any(e in args[0] for e in familyLIST) and any(e in args[1] for e in familyLIST) and (args[0] != args[1]):
            resultDICT["source"] = "domestic_violence"                
        pass           
    
    return resultDICT