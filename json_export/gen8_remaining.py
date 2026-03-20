import json, os

def w(path, d):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {os.path.basename(path)}")

OUT_S = "/workspace/json_export/students"
OUT_A = "/workspace/json_export/adults"
OUT_T = "/workspace/json_export/teachers"

# ═══ PACS 亲子沟通量表 ═══
pacs_items_open = [
    "我可以与父亲/母亲讨论我对人或事的看法，而不必觉得尴尬或有所顾忌",
    "父亲/母亲总是很认真地听我说话",
    "父亲/母亲尝试理解我的感受",
    "父亲/母亲对我无话不谈",
    "父亲/母亲善于站在我的立场上帮我解决问题",
    "我很容易向父亲/母亲说出心里话",
    "父亲/母亲尝试理解我",
    "我可以向父亲/母亲提出问题，父亲/母亲都能认真回答",
    "父亲/母亲总向我表示他们是爱我的",
    "当我生气时，父亲/母亲尝试理解我",
]
pacs_items_prob = [
    "我向父亲/母亲表达自己的感受时，往往会令我感到委屈",
    "当我和父亲/母亲谈话时，往往感到厌烦或想停止谈话",
    "我不能诚实地告诉父亲/母亲我真正的感受",
    "我有时会避免向父亲/母亲提一些问题",
    "父亲/母亲经常批评我，让我很不舒服",
    "我和父亲/母亲的谈话不如我希望的那么顺畅",
    "父亲/母亲经常打断我",
    "当我们在某件事上意见不同时，父亲/母亲会让我感到恐惧",
    "父亲/母亲贬低我的感受",
    "父亲/母亲抱怨我讲话太多",
]
opts_pacs_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["非常不同意","有些不同意","不确定","有些同意","非常同意"])]
opts_pacs_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["非常不同意","有些不同意","不确定","有些同意","非常同意"])]
questions = []
for i, t in enumerate(pacs_items_open):
    questions.append({"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_pacs_fwd,"reverse_score":False,"subscale_key":"open","is_alert_item":False})
for i, t in enumerate(pacs_items_prob):
    questions.append({"question_no":i+11,"question_text":t,"question_type":"likert","options":opts_pacs_rev,"reverse_score":True,"subscale_key":"problem","is_alert_item":False})
w(os.path.join(OUT_S,"PACS.json"),{
    "name":"亲子沟通量表","short_name":"PACS",
    "description":"评估青少年与父母沟通质量的20题量表，含开放性和问题性沟通两个维度（父亲版/母亲版各一份）。由Barnes HL & Olson DH 1985年编制，安伯欣2004年中文版，α=0.84-0.90。",
    "applicable_levels":[2,3],"question_count":20,"estimated_mins":8,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":list(range(11,21)),
        "subscales":{"open":list(range(1,11)),"problem":list(range(11,21))},
        "subscale_labels":{"open":"开放性沟通","problem":"问题性沟通（反向后高分=良好）"}
    },
    "result_levels":[
        {"range":[20,40],"level":"poor","label":"沟通质量较差","alert":"yellow","note":"总分（含反向处理）"},
        {"range":[41,70],"level":"moderate","label":"沟通质量中等","alert":None,"note":"总分"},
        {"range":[71,100],"level":"good","label":"沟通质量良好","alert":None,"note":"总分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,"questions":questions
})

# ═══ CLS 儿童孤独量表 ═══
cls_texts = [
    "我容易交到朋友","我没有朋友和我一起玩","我喜欢读书（辅助）",
    "在学校里我觉得孤独","我的同学喜欢我","我擅长做游戏（辅助）",
    "我有很多朋友","我感到难过，因为我想有更多的朋友",
    "我喜欢看电视（辅助）","我不知道其他小朋友喜不喜欢我",
    "我喜欢玩体育运动（辅助）","很难让我的同学喜欢我","我喜欢玩游戏（辅助）",
    "在学校里我没有玩伴","我擅长学校里的活动（辅助）","我善于交朋友",
    "我感到孤单","我喜欢做功课（辅助）","我跟别人相处不好",
    "我喜欢画图和绘画（辅助）","我没有可以交谈的人","我和同学玩得很开心",
    "我喜欢科学（辅助）","我有可以一起玩的朋友",
]
is_filler = [False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False]
is_reverse = [True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True]
opts_cls_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["不是这样","很少这样","有时这样","经常这样","总是这样"])]
opts_cls_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["不是这样","很少这样","有时这样","经常这样","总是这样"])]
cls_qs = []
for i,(t,filler,rev) in enumerate(zip(cls_texts,is_filler,is_reverse)):
    cls_qs.append({"question_no":i+1,"question_text":t,"question_type":"likert",
        "options":opts_cls_rev if rev else opts_cls_fwd,"reverse_score":rev,
        "subscale_key":None,"is_alert_item":False,
        "_is_filler_no_score":filler})
w(os.path.join(OUT_S,"CLS.json"),{
    "name":"儿童孤独量表","short_name":"CLS",
    "description":"评估6-15岁儿童在学校中孤独感的24题量表（16题计分+8题辅助填充）。由Asher SR & Wheeler VA 1985年编制，李晓巍等中文版，α=0.76-0.85。",
    "applicable_levels":[1,2],"question_count":24,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"sum",
        "reverse_items":[i+1 for i,rev in enumerate(is_reverse) if rev],
        "subscales":{},
        "note":"只计16道主题题（非辅助题）的得分，辅助题（is_filler_no_score=true）不计入"
    },
    "result_levels":[
        {"range":[16,32],"level":"low","label":"孤独感低","alert":None,"note":"16道计分题总分"},
        {"range":[33,48],"level":"moderate","label":"中等孤独感","alert":"yellow","note":"16道计分题总分"},
        {"range":[49,64],"level":"high","label":"孤独感较高","alert":"orange","note":"16道计分题总分"},
        {"range":[65,80],"level":"severe","label":"孤独感严重","alert":"red","note":"16道计分题总分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,"questions":cls_qs
})

# ═══ CSES-12 核心自我评价量表 ═══
cses12_items = [
    (1,"我坚信自己能够取得应有的成功",False),
    (2,"有时候我会感到沮丧",True),
    (3,"只要我努力尝试，我总能取得成功",False),
    (4,"有时候，当我失败了，我会觉得自己很没用",True),
    (5,"我总能很出色地完成任务",False),
    (6,"有时候，我感觉自己很难掌控自己的工作",True),
    (7,"总体而言，我对自己很满意",False),
    (8,"我对自己的能力总是充满怀疑",True),
    (9,"我自己能够决定我的生活",False),
    (10,"事业上的成功不由我控制",True),
    (11,"我能够很好地处理好自己绝大部分的问题",False),
    (12,"有些时候，我会觉得事情变得没有希望",True),
]
opts_cses_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["非常不同意","不同意","不确定","同意","非常同意"])]
opts_cses_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["非常不同意","不同意","不确定","同意","非常同意"])]
w(os.path.join(OUT_S,"CSES.json"),{
    "name":"核心自我评价量表","short_name":"CSES",
    "description":"评估个体核心自我评价（自尊、效能、控制点、情绪稳定性综合）的12题量表。由Judge TA等2003年编制，中文版α=0.70-0.78。",
    "applicable_levels":[2,3],"question_count":12,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[2,4,6,8,10,12],"subscales":{}},
    "result_levels":[
        {"range":[12,30],"level":"low","label":"核心自我评价偏低","alert":"yellow"},
        {"range":[31,45],"level":"moderate","label":"核心自我评价中等","alert":None},
        {"range":[46,60],"level":"high","label":"核心自我评价较高","alert":None},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_cses_rev if rev else opts_cses_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in cses12_items
    ]
})

# ═══ SCS-SF 自我同情量表简版 ═══
scs_items = [
    (1,"当我经历某些痛苦时，我试着以平衡的方式来对待这些感受","mindfulness",False),
    (2,"当我感到自己不足时，我提醒自己大多数人也会有这种感受","common_humanity",False),
    (3,"在感到困境时，我倾向于责备自己","self_judgment",True),
    (4,"当我面对生活中的困难时，我对自己是友善和体谅的","self_kindness",False),
    (5,"如果失败了，我沉浸在失败的感受中","over_identification",True),
    (6,"感觉不安时，我试着以较为平衡的方式看待事情","mindfulness",False),
    (7,"当我感到自己不足时，我会提醒自己这是共同的人类体验","common_humanity",False),
    (8,"感到低落时，我不接纳且批判自己的缺失","self_judgment",True),
    (9,"心情低落时，我倾向于觉得大多数人比我快乐","isolation",True),
    (10,"在重要的事上失败时，我会感到孤单","isolation",True),
    (11,"在重要的事上受挫时，我沉溺在自己不够好的感受中","over_identification",True),
    (12,"感到低落时，我给予自己关爱和温暖","self_kindness",False),
]
opts_scs_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["几乎从不","很少","有时","经常","几乎总是"])]
opts_scs_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["几乎从不","很少","有时","经常","几乎总是"])]
w(os.path.join(OUT_S,"SCS-SF.json"),{
    "name":"自我同情量表简版","short_name":"SCS-SF",
    "description":"评估自我同情程度的12题量表（6个维度各2题）。由Raes F等2011年编制，α=0.80+。中文版青少年版（SCS-Y）已在中国青少年中验证。",
    "applicable_levels":[2,3],"question_count":12,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula",
        "formula":"total_mean = mean of all 6 subscale means (after reverse scoring)",
        "reverse_items":[3,5,8,9,10,11],
        "subscales":{
            "self_kindness":[4,12],"self_judgment":[3,8],
            "common_humanity":[2,7],"isolation":[9,10],
            "mindfulness":[1,6],"over_identification":[5,11]
        },
        "subscale_labels":{
            "self_kindness":"自我友善","self_judgment":"自我评判（反向）",
            "common_humanity":"共通人性","isolation":"孤立感（反向）",
            "mindfulness":"正念","over_identification":"过度认同（反向）"
        }
    },
    "result_levels":[
        {"range":[1.0,2.49],"level":"low","label":"自我同情程度低","alert":"yellow","note":"总均分（1-5）"},
        {"range":[2.5,3.5],"level":"moderate","label":"自我同情程度中等","alert":None,"note":"总均分"},
        {"range":[3.5,5.0],"level":"high","label":"自我同情程度高","alert":None,"note":"总均分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_scs_rev if rev else opts_scs_fwd,"reverse_score":rev,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,rev in scs_items
    ]
})

# ═══ UWES 工作投入量表（教师版）═══
uwes_items = [
    (1,"在工作中，我感到自己精力充沛","vigor",False),
    (2,"我认为我的工作很有意义和价值","dedication",False),
    (3,"时间在工作中飞速流逝","absorption",False),
    (4,"在工作中，我感到自己强健而充满活力","vigor",False),
    (5,"我对自己所从事的工作充满热情","dedication",False),
    (6,"当我工作时，我会忘记周围的一切","absorption",False),
    (7,"我的工作给我带来鼓舞和激励","dedication",False),
    (8,"早晨起来，我感到很想去工作","vigor",False),
    (9,"当我工作非常投入时，我感到很愉悦","absorption",False),
    (10,"我为从事这份工作而感到自豪","dedication",False),
    (11,"我完全投入到工作中","absorption",False),
    (12,"在工作中，我能坚持，即使事情进展不顺利","vigor",False),
    (13,"我的工作是富于挑战性的","dedication",False),
    (14,"在工作时，我很难使自己分心","absorption",False),
    (15,"在工作中，我的意志很坚强","vigor",False),
    (16,"很难从工作中分离出来","absorption",False),
    (17,"在工作中，我总是坚持不懈，即使事情不顺利","vigor",False),
]
opts_uwes = [{"value":i,"label":l,"score":i} for i,l in enumerate(
    ["从不（0）","几乎没有，一年几次（1）","有时，一月几次（2）","经常，每月几次（3）",
     "很经常，每周几次（4）","几乎总是，每天（5）","总是，每天数次（6）"])]
w(os.path.join(OUT_T,"UWES.json"),{
    "name":"Utrecht工作投入量表","short_name":"UWES",
    "description":"评估工作投入的活力、奉献和专注三维度，17题七级评分。由Schaufeli WB等2002年编制，中文版学术发表。",
    "applicable_levels":[],"question_count":17,"estimated_mins":8,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula","formula":"subscale_mean = subscale_sum / n_items","reverse_items":[],
        "subscales":{
            "vigor":[1,4,8,12,15,17],
            "dedication":[2,5,7,10,13],
            "absorption":[3,6,9,11,14,16]
        },
        "subscale_labels":{"vigor":"活力","dedication":"奉献","absorption":"专注"}
    },
    "result_levels":[
        {"range":[0,2.99],"level":"low","label":"工作投入度低","alert":"yellow","note":"各维度均分"},
        {"range":[3.0,4.49],"level":"moderate","label":"工作投入度中等","alert":None,"note":"各维度均分"},
        {"range":[4.5,6.0],"level":"high","label":"工作投入度高","alert":None,"note":"各维度均分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_uwes,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in uwes_items
    ]
})

# ═══ DBAS-16 睡眠功能失调信念量表（成人）═══
dbas_texts = [
    "我需要睡满8小时才能在白天感觉神清气爽，表现良好",
    "当我有一两晚睡不好的时候，我知道这会影响接下来一周的日程安排",
    "当我睡眠不好时，我担心我可能会精神崩溃",
    "我觉得我对睡眠没有任何掌控力",
    "我担心，如果两三天不睡觉，我可能会患上神经疾病",
    "当我感到沮丧或忧虑时，我的睡眠必然会受到影响",
    "我相信失眠是由于一种化学失衡造成的",
    "我认为当我失眠时我可能会感觉很糟糕，因为我什么事都做不了",
    "我永远无法预测我能否好好睡一觉",
    "没有服用安眠药我就无法睡个好觉",
    "当我晚上睡得不好时，我知道这会影响到我第二天做事",
    "为了保持白天的功能并保持健康，我相信一定需要睡一整夜",
    "我认为失眠是一种医学疾病",
    "当我很难入睡时，就继续躺在床上，努力继续尝试",
    "我担心长期缺乏睡眠会对健康产生严重影响",
    "我很难在夜里醒来后重新入睡",
]
opts_dbas = [{"value":i,"label":str(i),"score":i} for i in range(11)]
w(os.path.join(OUT_A,"DBAS-16.json"),{
    "name":"睡眠功能失调信念量表（16题）","short_name":"DBAS-16",
    "description":"评估对睡眠的不合理信念，16题，0-10分十一级评分（0=完全不同意，10=完全同意）。由Morin CM等2007年编制，α=0.80。",
    "applicable_levels":[],"question_count":16,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{"method":"formula","formula":"mean = sum / 16","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,40],"level":"low","label":"睡眠信念合理","alert":None,"note":"总分（0-160）"},
        {"range":[41,80],"level":"moderate","label":"存在一定功能失调信念","alert":"yellow","note":"总分"},
        {"range":[81,160],"level":"high","label":"功能失调信念较多","alert":"orange","note":"总分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_dbas,"reverse_score":False,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(dbas_texts)]
})

# ═══ ACEs 儿童期逆境问卷 ═══
aces_texts = [
    "父母或家中其他成年人经常辱骂、贬低您或让您感到害怕（情感虐待）",
    "父母或家中其他成年人经常推打、抓打、扇打或投掷物品（躯体虐待）",
    "成年人或比您大至少5岁的人以性的方式触摸或骚扰您（性虐待）",
    "您常常感到家庭成员不关爱您，觉得自己不重要（情感忽视）",
    "您常常感到没有足够的食物、要穿脏衣服或没有人保护您（躯体忽视）",
    "您的父母是否离婚或分居（父母分离）",
    "您的家庭成员是否曾经被关进监狱（家庭成员被监禁）",
    "家里是否有人患有抑郁、精神疾病，或曾经尝试自杀（家庭精神健康问题）",
    "您的母亲或继母是否经常被推、打或刀枪威胁（目睹家暴）",
    "您是否与酗酒或使用毒品的家庭成员一起生活（家庭物质滥用）",
]
w(os.path.join(OUT_A,"ACEs.json"),{
    "name":"儿童期逆境问卷","short_name":"ACEs",
    "description":"评估18岁前不良童年经历暴露情况的10题量表，回顾性自报。由Felitti VJ等1998年编制（ACE Study），WHO中文版。",
    "applicable_levels":[],"question_count":10,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,0],"level":"none","label":"无已知逆境","alert":None},
        {"range":[1,3],"level":"moderate","label":"中等逆境暴露","alert":"yellow"},
        {"range":[4,10],"level":"high","label":"高逆境暴露","alert":"orange","note":"≥4分成年后各类健康问题风险明显升高"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":1,"condition":"value == 1","alert":"orange","reason":"情感虐待经历"},
        {"question_no":2,"condition":"value == 1","alert":"orange","reason":"躯体虐待经历"},
        {"question_no":3,"condition":"value == 1","alert":"red","reason":"性虐待经历"},
    ]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"single",
         "options":[{"value":0,"label":"否","score":0},{"value":1,"label":"是","score":1}],
         "reverse_score":False,"subscale_key":None,"is_alert_item":(i<3)}
        for i,t in enumerate(aces_texts)
    ]
})

print("Batch 8 done: PACS, CLS, CSES, SCS-SF, UWES, DBAS-16, ACEs")
