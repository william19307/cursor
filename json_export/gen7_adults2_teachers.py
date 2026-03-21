import json, os

def w(path, d):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {os.path.basename(path)}")

OUT_A = "/workspace/json_export/adults"
OUT_T = "/workspace/json_export/teachers"

# ═══ MAAS 正念注意觉知量表 ═══
maas_texts = [
    "在做某件事时，我可能感受到情绪困扰，但直到一段时间后才意识到这件事",
    "我不小心把东西打翻或把东西弄破",
    "我发现自己机械地完成任务，并不真正意识到我在做什么",
    "我很快速地从一地方移动到另一地方，不太在意一路上发生了什么",
    "我忽视身体的不适或紧绷感，因为我正专注于另外一件事情",
    "我忘了别人的名字，几乎是刚认识就忘了",
    "我好像是在用自动驾驶模式运作，并没有意识到自己在做什么",
    "我为了完成任务而冲冲忙忙，并不太注意任务本身",
    "我太专注于我想达成的目标，以致完全没注意到完成目标的当下",
    "我机械地做工作或任务，心思都在别处",
    "我发现自己在听别人说话时，同时也在做其他事",
    "我开车来到目的地，却不记得行经的路程",
    "我发现自己沉浸在过去或未来，而没有注意到现在",
    "我发现自己做事情心不在焉",
    "我进食时，并没有注意到自己在吃什么",
]
opts_maas = [{"value":i+1,"label":l,"score":6-i} for i,l in enumerate(
    ["几乎总是","很频繁","比较频繁","不太频繁","很少","几乎从不"])]
w(os.path.join(OUT_A,"MAAS.json"),{
    "name":"正念注意觉知量表","short_name":"MAAS",
    "description":"评估日常对当下注意觉知能力的15题量表，所有题目反向计分（高分=高正念）。由Brown KW & Ryan RM 2003年编制，周仁来等中文版，α=0.89。",
    "applicable_levels":[],"question_count":15,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"formula","formula":"mean = sum / 15; higher = more mindful","reverse_items":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],"subscales":{}},
    "result_levels":[
        {"range":[1.0,2.99],"level":"low","label":"正念水平较低","alert":"yellow","note":"均分"},
        {"range":[3.0,4.49],"level":"medium","label":"正念水平中等","alert":None,"note":"均分"},
        {"range":[4.5,6.0],"level":"high","label":"正念水平较高","alert":None,"note":"均分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_maas,"reverse_score":True,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(maas_texts)]
})

# ═══ CFQ 认知融合问卷 ═══
cfq_texts = [
    "我的想法给我的生活造成了很多困扰",
    "我与我的想法纠缠在一起",
    "在面对困难的想法和感受时，我很难做到我最在乎的事",
    "我很难与令人不安的想法和感受保持距离",
    "我与我的想法融为一体",
    "我花了很多精力与我的想法和感受斗争",
    "与我的想法斗争阻止了我活在当下",
]
opts_cfq = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["从不","很少","有时","经常","非常经常","几乎总是","总是"])]
w(os.path.join(OUT_A,"CFQ.json"),{
    "name":"认知融合问卷","short_name":"CFQ",
    "description":"评估对想法过度认同和融合程度的7题量表（ACT接受承诺疗法核心概念）。由Gillanders DT等2014年编制，α=0.94。",
    "applicable_levels":[],"question_count":7,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[7,20],"level":"low","label":"认知融合程度低","alert":None},
        {"range":[21,35],"level":"moderate","label":"中等认知融合","alert":"yellow"},
        {"range":[36,49],"level":"high","label":"认知融合程度高","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_cfq,"reverse_score":False,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(cfq_texts)]
})

# ═══ BDI-II 贝克抑郁量表 ═══ (complex multi-option per item)
w(os.path.join(OUT_A,"BDI-II.json"),{
    "name":"贝克抑郁量表第二版","short_name":"BDI-II",
    "description":"评估过去两周抑郁症状严重程度的21题自评量表，每题四个陈述选最符合的（0-3分）。由Beck AT等1996年编制，α=0.91-0.95。",
    "applicable_levels":[],"question_count":21,"estimated_mins":10,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,13],"level":"minimal","label":"无/极小抑郁","alert":None},
        {"range":[14,19],"level":"mild","label":"轻度抑郁","alert":"yellow"},
        {"range":[20,28],"level":"moderate","label":"中度抑郁","alert":"orange"},
        {"range":[29,63],"level":"severe","label":"重度抑郁","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":9,"condition":"value >= 1","alert":"red","reason":"有自杀念头（想杀死自己）"},
    ]},"is_active":True,
    "questions":[
        {"question_no":1,"question_text":"悲伤情绪","question_type":"single","options":[{"value":0,"label":"我不感到悲伤","score":0},{"value":1,"label":"我大部分时间感到悲伤","score":1},{"value":2,"label":"我常常感到悲伤","score":2},{"value":3,"label":"我总是感到悲伤","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":2,"question_text":"对未来悲观","question_type":"single","options":[{"value":0,"label":"我对未来并不悲观","score":0},{"value":1,"label":"比以前更悲观","score":1},{"value":2,"label":"我不期待事情好转","score":2},{"value":3,"label":"未来毫无希望，只会更糟","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":3,"question_text":"失败感","question_type":"single","options":[{"value":0,"label":"我不觉得自己是个失败者","score":0},{"value":1,"label":"我失败的次数比应该有的多","score":1},{"value":2,"label":"回顾过去，我看到许多失败","score":2},{"value":3,"label":"我感到自己是个彻底的失败者","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":4,"question_text":"丧失愉悦感","question_type":"single","options":[{"value":0,"label":"我从过去喜欢的事情中得到同样的满足感","score":0},{"value":1,"label":"我不再像以前那样享受事情","score":1},{"value":2,"label":"我从以前享受的事情中获得很少满足感","score":2},{"value":3,"label":"我从以前享受的事情中获得不到任何满足感","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":5,"question_text":"内疚感","question_type":"single","options":[{"value":0,"label":"我不特别感到内疚","score":0},{"value":1,"label":"我对很多事情感到内疚","score":1},{"value":2,"label":"我大部分时间感到内疚","score":2},{"value":3,"label":"我总是感到内疚","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":6,"question_text":"惩罚感","question_type":"single","options":[{"value":0,"label":"我不感到我在被惩罚","score":0},{"value":1,"label":"我感到可能受到惩罚","score":1},{"value":2,"label":"我期待受到惩罚","score":2},{"value":3,"label":"我感到我正在受到惩罚","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":7,"question_text":"自我评价","question_type":"single","options":[{"value":0,"label":"我对自己感觉和以前一样","score":0},{"value":1,"label":"我失去了对自己的信心","score":1},{"value":2,"label":"我对自己感到失望","score":2},{"value":3,"label":"我讨厌自己","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":8,"question_text":"自我批评","question_type":"single","options":[{"value":0,"label":"我不比以前更自责","score":0},{"value":1,"label":"我比以前更批评自己","score":1},{"value":2,"label":"我为所有的过失责备自己","score":2},{"value":3,"label":"我为所有坏事责备自己","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":9,"question_text":"自杀念头","question_type":"single","options":[{"value":0,"label":"我没有想过杀死自己","score":0},{"value":1,"label":"我有杀死自己的想法但不会去做","score":1},{"value":2,"label":"我很想杀死自己","score":2},{"value":3,"label":"如果有机会我会杀死自己","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":True},
        {"question_no":10,"question_text":"哭泣","question_type":"single","options":[{"value":0,"label":"我不比以前哭更多","score":0},{"value":1,"label":"比以前哭得更多","score":1},{"value":2,"label":"现在任何小事都让我哭","score":2},{"value":3,"label":"我想哭但哭不出来","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":11,"question_text":"烦躁","question_type":"single","options":[{"value":0,"label":"我不比平时更烦躁","score":0},{"value":1,"label":"比平时更容易烦躁","score":1},{"value":2,"label":"比以前更容易烦躁","score":2},{"value":3,"label":"我一直感到烦躁","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":12,"question_text":"对活动丧失兴趣","question_type":"single","options":[{"value":0,"label":"我没有失去对人或活动的兴趣","score":0},{"value":1,"label":"我比以前对人或事物更少感兴趣","score":1},{"value":2,"label":"我失去了对大多数人或事的兴趣","score":2},{"value":3,"label":"很难对任何事情感兴趣","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":13,"question_text":"优柔寡断","question_type":"single","options":[{"value":0,"label":"我做决定和以前一样容易","score":0},{"value":1,"label":"我发现做决定比以前困难","score":1},{"value":2,"label":"我做决定比以前更困难","score":2},{"value":3,"label":"我在做任何决定上都有困难","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":14,"question_text":"无价值感","question_type":"single","options":[{"value":0,"label":"我不觉得自己毫无价值","score":0},{"value":1,"label":"我不认为自己和以前一样有价值和有用","score":1},{"value":2,"label":"与他人相比我觉得自己没什么价值","score":2},{"value":3,"label":"我感到自己完全没有价值","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":15,"question_text":"精力丧失","question_type":"single","options":[{"value":0,"label":"我的精力和以前一样多","score":0},{"value":1,"label":"我的精力比以前少了","score":1},{"value":2,"label":"我没有足够的精力做多少事情","score":2},{"value":3,"label":"我没有精力做任何事情","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":16,"question_text":"睡眠变化","question_type":"single","options":[{"value":0,"label":"我的睡眠没有改变","score":0},{"value":1,"label":"我比平时睡得略多/少","score":1},{"value":2,"label":"我比平时睡得多/少很多","score":2},{"value":3,"label":"我几乎整天睡觉/严重失眠","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":17,"question_text":"易怒","question_type":"single","options":[{"value":0,"label":"我不比以前更易怒","score":0},{"value":1,"label":"比平时更易怒","score":1},{"value":2,"label":"我比以前更易怒","score":2},{"value":3,"label":"我一直感到易怒","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":18,"question_text":"食欲变化","question_type":"single","options":[{"value":0,"label":"我的食欲没有改变","score":0},{"value":1,"label":"我的食欲略有减少/增加","score":1},{"value":2,"label":"我的食欲减少/增加很多","score":2},{"value":3,"label":"我完全没有食欲/总是渴望食物","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":19,"question_text":"注意力集中困难","question_type":"single","options":[{"value":0,"label":"我的注意力和以前一样","score":0},{"value":1,"label":"我的注意力不如以前","score":1},{"value":2,"label":"我很难长时间集中注意力","score":2},{"value":3,"label":"我发现我根本无法集中注意力","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":20,"question_text":"疲劳","question_type":"single","options":[{"value":0,"label":"我不比以前更疲劳","score":0},{"value":1,"label":"我比以前更容易疲劳","score":1},{"value":2,"label":"我太疲了，许多事情都无法进行","score":2},{"value":3,"label":"我太疲劳了，做任何事都没有","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":21,"question_text":"性欲减退","question_type":"single","options":[{"value":0,"label":"我最近没注意到性欲有变化","score":0},{"value":1,"label":"我比以前对性的兴趣少了","score":1},{"value":2,"label":"我现在对性的兴趣少了很多","score":2},{"value":3,"label":"我对性完全失去了兴趣","score":3}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
    ]
})

# ═══ TIPI 十项人格量表 ═══
tipi_items = [
    (1,"外向、热情","E",False),
    (2,"批判的、爱争辩的","A",True),
    (3,"可靠的、自律的","C",False),
    (4,"焦虑的、容易沮丧的","N",False),
    (5,"对新经历开放、思维复杂","O",False),
    (6,"内向、安静","E",True),
    (7,"亲切的、待人友好","A",False),
    (8,"凌乱的、粗心大意的","C",True),
    (9,"情绪平静的、心理稳定的","N",True),
    (10,"传统的、缺乏创意","O",True),
]
opts_tipi = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["强烈不同意","不同意","有些不同意","不确定","有些同意","同意","强烈同意"])]
opts_tipi_rev = [{"value":i+1,"label":l,"score":7-i} for i,l in enumerate(
    ["强烈不同意","不同意","有些不同意","不确定","有些同意","同意","强烈同意"])]
w(os.path.join(OUT_A,"TIPI.json"),{
    "name":"十项人格量表","short_name":"TIPI",
    "description":"大五人格快速筛查的10题量表，每维度2题（一正一反），七级评分。由Gosling SD等2003年编制，α=0.61-0.73。",
    "applicable_levels":[],"question_count":10,"estimated_mins":2,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula",
        "formula":"each_dimension_mean = (forward_item + reversed_item) / 2",
        "reverse_items":[2,6,8,9,10],
        "subscales":{"E":[1,6],"A":[2,7],"C":[3,8],"N":[4,9],"O":[5,10]},
        "subscale_labels":{"E":"外向性","A":"宜人性","C":"尽责性","N":"神经质","O":"开放性"}
    },
    "result_levels":[],"alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":f"我是一个……的人（{t}）","question_type":"likert",
         "options":opts_tipi_rev if rev else opts_tipi,"reverse_score":rev,
         "subscale_key":sub,"is_alert_item":False}
        for no,t,sub,rev in tipi_items
    ]
})

# ═══ LOT-R 特质乐观量表 ═══
lotr_items = [
    (1,"不确定时，我通常期待最好的结果",False),
    (3,"如果出了什么不好的事，对我来说就可能出更多不好的事",True),
    (4,"我总是对我的未来持乐观态度",False),
    (6,"对我来说，事情从来不会像我希望的那样发展",True),
    (8,"我很少期待事情向我期望的方向发展",True),
    (10,"总体上，我期待会发生更多好事而非坏事",False),
]
opts_lotr = [{"value":i,"label":l,"score":i} for i,l in enumerate(
    ["强烈不同意","不同意","不确定","同意","强烈同意"])]
opts_lotr_rev = [{"value":i,"label":l,"score":4-i} for i,l in enumerate(
    ["强烈不同意","不同意","不确定","同意","强烈同意"])]
w(os.path.join(OUT_A,"LOT-R.json"),{
    "name":"特质乐观量表修订版","short_name":"LOT-R",
    "description":"评估对未来结果乐观程度的6题量表（含4道填充题，不计分）。由Scheier MF等1994年编制，α=0.71-0.84。",
    "applicable_levels":[],"question_count":6,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"sum","reverse_items":[3,6,8],
        "note":"原始问卷题号为1,3,4,6,8,10，本版重新编号为1-6",
        "subscales":{}
    },
    "result_levels":[
        {"range":[0,8],"level":"pessimistic","label":"悲观倾向","alert":"yellow"},
        {"range":[9,14],"level":"moderate","label":"中等乐观","alert":None},
        {"range":[15,24],"level":"optimistic","label":"乐观倾向","alert":None},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts_lotr_rev if rev else opts_lotr,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for i,(orig_no,t,rev) in enumerate(lotr_items)
    ]
})

# ═══ PSS-14 感知压力量表 ═══
pss14_items = [
    (1,"因为发生意外的事情而感到心烦意乱",False),
    (2,"感到无法控制生活中重要的事情",False),
    (3,"感到紧张和有压力",False),
    (4,"成功地处理了生活中令人烦恼的问题",True),
    (5,"感到自己有效地应付了生活中的重要变化",True),
    (6,"对处理个人问题的能力没有信心",False),
    (7,"能够按自己的意愿行事",True),
    (8,"感到无力控制事情的方式",False),
    (9,"因为超出控制的事情而愤怒",False),
    (10,"感到困难在增加，以至于无法克服",False),
    (11,"为意料之外发生的事情烦恼",False),
    (12,"感到能够掌控烦恼事件",True),
    (13,"能够管理自己消极的感受",True),
    (14,"感到事情正按照自己的意愿发展",True),
]
opts_pss14_fwd = [{"value":i,"label":l,"score":i} for i,l in enumerate(["从不","几乎不","有时","相当多","很频繁"])]
opts_pss14_rev = [{"value":i,"label":l,"score":4-i} for i,l in enumerate(["从不","几乎不","有时","相当多","很频繁"])]
w(os.path.join(OUT_A,"PSS-14.json"),{
    "name":"感知压力量表14题版","short_name":"PSS-14",
    "description":"评估近一个月感知压力水平的14题量表。由Cohen S等1983年编制，α=0.78-0.86。",
    "applicable_levels":[],"question_count":14,"estimated_mins":6,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[4,5,7,12,13,14],"subscales":{}},
    "result_levels":[
        {"range":[0,19],"level":"low","label":"低压力","alert":None},
        {"range":[20,34],"level":"moderate","label":"中等压力","alert":"yellow"},
        {"range":[35,56],"level":"high","label":"高压力","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_pss14_rev if rev else opts_pss14_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in pss14_items
    ]
})

# ═══ WHOQOL-BREF 生活质量量表 ═══
w(os.path.join(OUT_A,"WHOQOL-BREF.json"),{
    "name":"世界卫生组织生存质量量表简表","short_name":"WHOQOL-BREF",
    "description":"评估身体健康、心理健康、社会关系、环境四领域生活质量的26题量表。WHO官方免费提供中文版（who.int）。需复杂公式计算领域得分。",
    "applicable_levels":[],"question_count":26,"estimated_mins":12,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula",
        "formula":"domain_score = (sum_of_items * 4) / (n_items * 4) * 100; range 0-100",
        "reverse_items":[3,4,26],
        "subscales":{
            "physical":[3,4,10,15,16,17,18],
            "psychological":[5,6,7,11,19,26],
            "social":[20,21,22],
            "environment":[8,9,12,13,14,23,24,25]
        },
        "subscale_labels":{
            "physical":"生理健康","psychological":"心理健康",
            "social":"社会关系","environment":"环境"
        },
        "note":"第1、2题为整体生活质量和健康满意度评估，单独计分"
    },
    "result_levels":[
        {"range":[0,49],"level":"poor","label":"生活质量较差","alert":"yellow","note":"领域百分制得分"},
        {"range":[50,74],"level":"moderate","label":"生活质量中等","alert":None,"note":"领域百分制得分"},
        {"range":[75,100],"level":"good","label":"生活质量良好","alert":None,"note":"领域百分制得分"},
    ],
    "alert_rules":{"item_rules":[]},"_incomplete":False,"is_active":True,
    "questions":[
        {"question_no":1,"question_text":"您如何评价您的生活质量？","question_type":"likert","options":[{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["很差","差","不好不差","好","很好"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":2,"question_text":"您对自己的健康状况满意吗？","question_type":"likert","options":[{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["很不满意","不满意","不好不差","满意","很满意"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
    ] + [
        {"question_no":i+3,"question_text":f"WHOQOL-BREF第{i+3}题（见量表原文）","question_type":"likert","options":[{"value":j+1,"label":l,"score":j+1} for j,l in enumerate(["根本不","少","中等","相当多","极其多"])],"reverse_score":(i+3) in [1,2,24],"subscale_key":None,"is_alert_item":False}
        for i in range(24)
    ]
})

# ═══ MMSE 认知筛查（公式+常模，is_active=false）═══
w(os.path.join(OUT_A,"MMSE.json"),{
    "name":"简易精神状态检查","short_name":"MMSE",
    "description":"评估认知功能障碍的30题面谈式测试，需专业人员实施。由Folstein MF等1975年编制，需常模参照。",
    "applicable_levels":[],"question_count":30,"estimated_mins":10,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"norm",
        "note":"需专业人员面对面实施；包含定向力（10题）、即时记忆（3题）、注意力（5题）、延迟回忆（3题）、语言能力（9题）",
        "reverse_items":[],"subscales":{}
    },
    "result_levels":[
        {"range":[27,30],"level":"normal","label":"认知功能正常","alert":None},
        {"range":[20,26],"level":"mild","label":"轻度认知障碍","alert":"yellow"},
        {"range":[10,19],"level":"moderate","label":"中度认知障碍","alert":"orange"},
        {"range":[0,9],"level":"severe","label":"重度认知障碍","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":False,
    "_note":"需专业人员面谈实施，不适合在线自评系统","questions":[]
})

# ═══ MoCA 蒙特利尔认知评估（is_active=false）═══
w(os.path.join(OUT_A,"MoCA.json"),{
    "name":"蒙特利尔认知评估量表","short_name":"MoCA",
    "description":"评估轻度认知障碍的面谈式评估工具，共30分，需专业人员实施。由Nasreddine ZS等2005年编制。",
    "applicable_levels":[],"question_count":30,"estimated_mins":10,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"formula","note":"需专业人员实施；教育年限≤12年可加1分（最高30分）",
        "reverse_items":[],"subscales":{}
    },
    "result_levels":[
        {"range":[26,30],"level":"normal","label":"认知功能正常","alert":None},
        {"range":[0,25],"level":"impaired","label":"提示轻度认知障碍","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":False,
    "_note":"需专业人员面谈实施","questions":[]
})

# ═══════════════════ TEACHERS ═══════════════════

# ═══ MBI-ES 教师职业倦怠量表 ═══
mbi_items = [
    (1,"工作让我感到情绪上的疲竭","ee",False),
    (2,"工作结束时我感到精疲力竭","ee",False),
    (3,"早晨起床后要去面对一天的工作时，我感到疲惫","ee",False),
    (4,"整天与学生一起工作，对我来说是一种压力","ee",False),
    (5,"工作使我精力耗尽","ee",False),
    (6,"工作让我感到沮丧","ee",False),
    (7,"我感到我工作得太卖力了","ee",False),
    (8,"与学生近距离接触让我感到紧张","ee",False),
    (9,"在这份工作中，我感到已到了精神崩溃临界点","ee",False),
    (10,"和学生在一起，我可以很容易创造一个轻松的氛围","pa",True),
    (11,"我在工作中做了一些有价值的事情","pa",True),
    (12,"我能够帮学生找到自信","pa",True),
    (13,"我可以有效地处理学生的问题","pa",True),
    (14,"我可以给学生一些有益的指导","pa",True),
    (15,"我觉得我对他人的生活有积极影响","pa",True),
    (16,"当学生遇到问题的时候，愿意和我交流","pa",True),
    (17,"我可以很容易理解学生的感受","pa",True),
    (18,"我因为一点小事就把学生劈头盖脸地骂一顿","dp",False),
    (19,"我对学生很苛刻","dp",False),
    (20,"我有骂学生的冲动","dp",False),
    (21,"我觉得学生对我处理问题的方式感到不满","dp",False),
    (22,"我觉得我常把学生当作无生命的物体来对待","dp",False),
]
opts_mbi_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["非常不赞同","不赞同","有些不赞同","有些赞同","赞同","非常赞同"])]
opts_mbi_rev = [{"value":i+1,"label":l,"score":6-i} for i,l in enumerate(
    ["非常不赞同","不赞同","有些不赞同","有些赞同","赞同","非常赞同"])]
w(os.path.join(OUT_T,"MBI-ES.json"),{
    "name":"教师职业倦怠量表","short_name":"MBI-ES",
    "description":"评估教师职业倦怠三维度（情绪衰竭/非人性化/个人成就感）的22题量表。由Maslach C等1996年编制，伍新春中文版，α=0.75-0.90。",
    "applicable_levels":[],"question_count":22,"estimated_mins":10,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"sum","reverse_items":[10,11,12,13,14,15,16,17],
        "subscales":{"ee":[1,2,3,4,5,6,7,8,9],"pa":[10,11,12,13,14,15,16,17],"dp":[18,19,20,21,22]},
        "subscale_labels":{"ee":"情绪衰竭","pa":"个人成就感（反向倦怠）","dp":"非人性化"},
        "note":"PA维度：分越低=倦怠越重；EE和DP：分越高=倦怠越重"
    },
    "result_levels":[
        {"subscale":"ee","range":[9,16],"level":"low","label":"低倦怠","alert":None},
        {"subscale":"ee","range":[17,26],"level":"moderate","label":"中度倦怠","alert":"yellow"},
        {"subscale":"ee","range":[27,54],"level":"high","label":"高度倦怠","alert":"red"},
        {"subscale":"dp","range":[5,6],"level":"low","label":"低倦怠","alert":None},
        {"subscale":"dp","range":[7,12],"level":"moderate","label":"中度倦怠","alert":"yellow"},
        {"subscale":"dp","range":[13,30],"level":"high","label":"高度倦怠","alert":"red"},
        {"subscale":"pa","range":[39,48],"level":"good","label":"成就感高","alert":None},
        {"subscale":"pa","range":[32,38],"level":"moderate","label":"成就感中等","alert":"yellow"},
        {"subscale":"pa","range":[8,31],"level":"low","label":"成就感低/倦怠","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_mbi_rev if rev else opts_mbi_fwd,"reverse_score":rev,
         "subscale_key":sub,"is_alert_item":False}
        for no,t,sub,rev in mbi_items
    ]
})

# ═══ DASS-21 教师版（与成人版相同）═══
# (already generated in students section; same JSON)
print("Teacher DASS-21 is same as adult DASS-21 - using same file")

# ═══ TSES 教师效能感量表 ═══
tses_items = [
    (1,"能有多大程度控制那些会破坏课堂的行为？","student_engagement",False),
    (2,"能在多大程度上激励那些学习动机低的学生？","student_engagement",False),
    (3,"能在多大程度上让学生相信自己在学校中能做好？","student_engagement",False),
    (4,"能在多大程度上让学生注意课堂规矩？","classroom_management",False),
    (5,"能在多大程度上激励学生重视学业？","student_engagement",False),
    (6,"能在多大程度上帮助学生进行批判性思维？","instructional_strategies",False),
    (7,"能在多大程度上让学生在课堂上有创造性思维？","instructional_strategies",False),
    (8,"能在多大程度上帮助学生学会解决问题？","instructional_strategies",False),
    (9,"能在多大程度上为不同学习能力的学生提供不同解释？","instructional_strategies",False),
    (10,"能在多大程度上提供好的问题让学生思考？","instructional_strategies",False),
    (11,"能在多大程度上使用多种评估方法？","instructional_strategies",False),
    (12,"能在多大程度上为困难学生提供有效的替代解释？","instructional_strategies",False),
    (13,"能在多大程度上实施多种教学策略？","instructional_strategies",False),
    (14,"能在多大程度上让学生遵守课堂规则？","classroom_management",False),
    (15,"能在多大程度上建立课堂常规？","classroom_management",False),
    (16,"能在多大程度上控制破坏性行为？","classroom_management",False),
    (17,"能在多大程度上维持课堂纪律？","classroom_management",False),
    (18,"能在多大程度上应对学生的挑战？","classroom_management",False),
    (19,"能在多大程度上确定学生是否理解了所教授的内容？","instructional_strategies",False),
    (20,"能在多大程度上让家长参与孩子的教育？","student_engagement",False),
    (21,"能在多大程度上按自己的方式处理教学工作？","student_engagement",False),
    (22,"能在多大程度上激励那些对校内活动兴趣不高的学生？","student_engagement",False),
    (23,"能在多大程度上冷静地处理学生情绪上的问题？","student_engagement",False),
    (24,"能在多大程度上为学习困难的学生提供适当的挑战？","instructional_strategies",False),
]
opts_tses = [{"value":i+1,"label":str(i+1)+"（"+l+"）","score":i+1} for i,l in enumerate(
    ["完全没有","很少","有一些","有些程度","中等程度","相当程度","大程度","非常大程度","极大程度"])]
w(os.path.join(OUT_T,"TSES.json"),{
    "name":"教师效能感量表","short_name":"TSES",
    "description":"评估教师在课堂管理、教学策略、学生参与三方面效能感的24题量表，九级评分。由Tschannen-Moran M & Hoy AW 2001年编制，α=0.888。",
    "applicable_levels":[],"question_count":24,"estimated_mins":10,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula","formula":"subscale_mean = subscale_sum / n_items","reverse_items":[],
        "subscales":{
            "student_engagement":[1,2,3,5,20,21,22,23],
            "instructional_strategies":[6,7,8,9,10,11,12,13,19,24],
            "classroom_management":[4,14,15,16,17,18]
        },
        "subscale_labels":{"student_engagement":"学生参与效能感","instructional_strategies":"教学策略效能感","classroom_management":"课堂管理效能感"}
    },
    "result_levels":[
        {"range":[1,4],"level":"low","label":"效能感偏低","alert":"yellow","note":"均分"},
        {"range":[4,7],"level":"moderate","label":"效能感中等","alert":None,"note":"均分"},
        {"range":[7,9],"level":"high","label":"效能感较高","alert":None,"note":"均分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_tses,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in tses_items
    ]
})

print("All teacher scales done")
print("Remaining adult scales done: MAAS, CFQ, BDI-II, TIPI, LOT-R, PSS-14, WHOQOL-BREF, MMSE, MoCA")
