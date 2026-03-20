import json, os
OUT = "/workspace/json_export/students"
def w(fn, d):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {fn}")

def opts5(labels): # 5-point with custom labels
    return [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(labels)]

def opts7():
    return [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
        ["完全不同意","不同意","有些不同意","不确定","有些同意","同意","完全同意"])]

def opts4agree():
    return [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
        ["完全不正确","有点正确","多数正确","完全正确"])]

# ═══ GSES 一般自我效能感量表 ═══
gses_texts = [
    "如果我尽力去做的话，我总是能够解决问题的",
    "即使别人反对我，我仍有办法取得我所要的",
    "对我来说，坚持理想和达成目标是轻而易举的",
    "我自信能有效地应付任何突如其来的事情",
    "以我的才智，我定能应付意料之外的情况",
    "如果我付出必要的努力，我一定能解决大多数的难题",
    "我能冷静地面对困难，因为我信赖自己处理问题的能力",
    "面对一个难题时，我通常能找到几个解决方法",
    "有麻烦的时候，我通常能想到一些应付的方法",
    "无论什么事在我身上发生，我都能够应付自如",
]
w("GSES.json",{
    "name":"一般自我效能感量表","short_name":"GSES",
    "description":"评估个体应对困境和挑战的整体自我效能感，10题单维度。由Schwarzer R & Jerusalem M 1993年编制，王才康等2001年中文版，α=0.87。",
    "applicable_levels":[2,3],"question_count":10,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[10,20],"level":"low","label":"低自我效能感","alert":"yellow"},
        {"range":[21,30],"level":"medium","label":"中等自我效能感","alert":None},
        {"range":[31,40],"level":"high","label":"高自我效能感","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts4agree(),"reverse_score":False,"subscale_key":None,"is_alert_item":False}
        for i,t in enumerate(gses_texts)
    ]
})

# ═══ Grit-S 坚毅量表 ═══
grit_items = [
    (1,"新思想和新项目有时会干扰我之前的项目",True),
    (2,"挫折不会让我气馁。我不轻易放弃",False),
    (3,"我经常给自己设定一个目标，但后来又追求不同的目标",True),
    (4,"我是一个非常勤奋努力的人",False),
    (5,"对于需要几个月才能完成的项目，我很难集中注意力",True),
    (6,"只要我开始了一件事情，我就会去完成",False),
    (7,"我的兴趣每年都在变化",True),
    (8,"我很努力，绝不放弃",False),
]
opts_grit_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["完全不像我","不太像我","有点像我","基本像我","非常像我"])]
opts_grit_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["完全不像我","不太像我","有点像我","基本像我","非常像我"])]
w("Grit-S.json",{
    "name":"坚毅量表简版","short_name":"Grit-S",
    "description":"评估长期目标坚持力（努力坚持）和兴趣一致性的8题量表。由Duckworth AL等2007年编制，中文版已在中小学生中验证。得分越高坚毅性越强。",
    "applicable_levels":[1,2,3],"question_count":8,"estimated_mins":3,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"formula",
        "formula":"perseverance = mean(items 2,4,6,8); consistency = mean(items 1,3,5,7 reversed); total = mean(all 8)",
        "reverse_items":[1,3,5,7],
        "subscales":{"perseverance":[2,4,6,8],"consistency":[1,3,5,7]}
    },
    "result_levels":[
        {"range":[1.0,2.5],"level":"low","label":"低坚毅性（约P10以下）","alert":None,"note":"均分"},
        {"range":[2.5,3.8],"level":"medium","label":"中等坚毅性","alert":None,"note":"均分"},
        {"range":[3.8,5.0],"level":"high","label":"高坚毅性（约P50以上）","alert":None,"note":"均分"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_grit_rev if rev else opts_grit_fwd,"reverse_score":rev,
         "subscale_key":"consistency" if no in [1,3,5,7] else "perseverance","is_alert_item":False}
        for no,t,rev in grit_items
    ]
})

# ═══ MLQ 生命意义感量表 ═══
mlq_items = [
    (1,"我明白自己生活的意义","presence",False),
    (2,"我正在寻觅我人生的一个目的或使命","search",False),
    (3,"我的生活没有明确的目的","presence",True),
    (4,"我正在寻找自己生活的意义","search",False),
    (5,"我的生活有一个清晰的方向","presence",False),
    (6,"我正在寻觅让我感觉自己生活饶有意义的东西","search",False),
    (7,"我知道什么东西能使自己的生活有意义","presence",False),
    (8,"我总在尝试寻找自己生活的目的","search",False),
    (9,"我已经发现一个让自己满意的生活目的","presence",False),
    (10,"我一直在寻找某样能使我的生活感觉起来是重要的东西","search",False),
]
opts_mlq_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["完全不符合","很不符合","稍不符合","不确定","稍符合","很符合","完全符合"])]
opts_mlq_rev = [{"value":i+1,"label":l,"score":7-i} for i,l in enumerate(["完全不符合","很不符合","稍不符合","不确定","稍符合","很符合","完全符合"])]
w("MLQ.json",{
    "name":"生命意义感量表","short_name":"MLQ",
    "description":"评估生命意义的「拥有」与「寻求」两个维度，10题七级评分。由Steger MF等2006年编制，王鑫强等中文版，α=0.81-0.91。",
    "applicable_levels":[2,3],"question_count":10,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"sum","reverse_items":[3],
        "subscales":{"presence":[1,3,5,7,9],"search":[2,4,6,8,10]},
        "subscale_labels":{"presence":"拥有意义感（MLQ-P）","search":"寻求意义感（MLQ-S）"}
    },
    "result_levels":[
        {"subscale":"presence","range":[5,19],"level":"low","label":"意义感较低","alert":"yellow"},
        {"subscale":"presence","range":[20,28],"level":"medium","label":"意义感中等","alert":None},
        {"subscale":"presence","range":[29,35],"level":"high","label":"意义感较高","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_mlq_rev if rev else opts_mlq_fwd,"reverse_score":rev,
         "subscale_key":sub,"is_alert_item":False}
        for no,t,sub,rev in mlq_items
    ]
})

# ═══ GQ-6 感恩问卷 ═══
gq6_items = [
    (1,"我生命中有太多我觉得要感谢的",False),
    (2,"如果我列出我觉得要感谢的，那将会是很长一串",False),
    (3,"当我环顾这个世界时，我看不出有多少值得我感谢",True),
    (4,"我要感谢各种各样的人",False),
    (5,"随着年龄的增长，我发现自己越来越能够欣赏那些构成我人生经历的人、事和情景",False),
    (6,"要我说出要感谢什么人或什么事，通常要花很长的时间才能想出来",True),
]
opts_gq_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["完全不同意","不同意","轻度不同意","不确定","轻度同意","同意","完全同意"])]
opts_gq_rev = [{"value":i+1,"label":l,"score":7-i} for i,l in enumerate(["完全不同意","不同意","轻度不同意","不确定","轻度同意","同意","完全同意"])]
w("GQ-6.json",{
    "name":"感恩问卷","short_name":"GQ-6",
    "description":"评估个体感恩倾向的6题量表，七级评分。由McCullough ME等2002年编制，刘建榕等中文版，α=0.82。",
    "applicable_levels":[1,2,3],"question_count":6,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[3,6],"subscales":{}},
    "result_levels":[
        {"range":[6,24],"level":"low","label":"感恩倾向较低","alert":None},
        {"range":[25,36],"level":"medium","label":"感恩倾向中等","alert":None},
        {"range":[37,42],"level":"high","label":"感恩倾向较高","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_gq_rev if rev else opts_gq_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in gq6_items
    ]
})

# ═══ PANAS 正负性情绪量表 ═══
panas_items = [
    (1,"感兴趣的","positive"),(2,"心烦的","negative"),(3,"精神活力高的","positive"),
    (4,"心神不宁的","negative"),(5,"劲头足的","positive"),(6,"内疚的","negative"),
    (7,"恐惧的","negative"),(8,"充满敌意的","negative"),(9,"充满热情的","positive"),
    (10,"自豪的","positive"),(11,"易怒的","negative"),(12,"警觉性高的","positive"),
    (13,"羞愧的","negative"),(14,"备受鼓舞的","positive"),(15,"紧张的","negative"),
    (16,"意志坚定的","positive"),(17,"注意力集中的","positive"),(18,"坐立不安的","negative"),
    (19,"有活力的","positive"),(20,"害怕的","negative"),
]
opts_panas = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["几乎没有","比较少","中等程度","比较多","极其多"])]
w("PANAS.json",{
    "name":"正性负性情绪量表","short_name":"PANAS",
    "description":"评估积极和消极情感状态的20题量表，描述近1-2周内的情绪。由Watson D等1988年编制，黄丽等2003年中文版。",
    "applicable_levels":[2,3],"question_count":20,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":{
            "positive":[1,3,5,9,10,12,14,16,17,19],
            "negative":[2,4,6,7,8,11,13,15,18,20]
        },
        "subscale_labels":{"positive":"正性情绪（PA）","negative":"负性情绪（NA）"}
    },
    "result_levels":[
        {"subscale":"positive","range":[10,24],"level":"low","label":"正性情绪偏低","alert":"yellow"},
        {"subscale":"positive","range":[25,35],"level":"medium","label":"正性情绪中等","alert":None},
        {"subscale":"positive","range":[36,50],"level":"high","label":"正性情绪较高","alert":None},
        {"subscale":"negative","range":[10,19],"level":"low","label":"负性情绪较少","alert":None},
        {"subscale":"negative","range":[20,30],"level":"medium","label":"负性情绪中等","alert":"yellow"},
        {"subscale":"negative","range":[31,50],"level":"high","label":"负性情绪较多","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_panas,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub in panas_items
    ]
})

# ═══ CAMM 儿童青少年正念量表 ═══
camm_texts = [
    "我为自己产生没有意义的情绪而感到不悦",
    "在学校，我在教室之间走动时没有注意到自己在做什么",
    "我让自己保持忙碌状态，这样就不会注意到自己的想法或感受",
    "我告诉自己不应该有自己正在经历的那种感受",
    "我推开自己不喜欢的想法",
    "我很难同时只专注于一件事",
    "我为自己产生的某些想法而感到不悦",
    "我想着过去发生的事情，而不是想着现在正在发生的事情",
    "我认为我的某些感受是不好的，我不应该有这些感受",
    "我阻止自己产生自己不喜欢的感受",
]
# All CAMM items are reverse-coded
opts_camm = [{"value":i,"label":l,"score":4-i} for i,l in enumerate(["从不","很少","有时","经常","总是"])]
w("CAMM.json",{
    "name":"儿童青少年正念量表","short_name":"CAMM",
    "description":"评估儿童青少年正念觉察能力的10题量表，所有题目均反向计分（高分=高正念）。由Greco LA等2011年编制，Chen等中文版，α=0.826。",
    "applicable_levels":[1,2,3],"question_count":10,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"sum","reverse_items":[1,2,3,4,5,6,7,8,9,10],
        "subscales":{},
        "note":"所有题目反向计分后求和；≥22分提示良好正念水平"
    },
    "result_levels":[
        {"range":[0,21],"level":"low","label":"正念水平偏低","alert":"yellow"},
        {"range":[22,40],"level":"adequate","label":"正念水平良好","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts_camm,"reverse_score":True,"subscale_key":None,"is_alert_item":False}
        for i,t in enumerate(camm_texts)
    ]
})

# ═══ ERQ 情绪调节问卷 ═══
erq_items = [
    (1,"当我想感受一些积极的情绪时，我会改变自己思考问题的角度","reappraisal",False),
    (2,"我不会表露自己的情绪","suppression",False),
    (3,"当我想少感受一些消极的情绪时，我会改变自己思考问题的角度","reappraisal",False),
    (4,"当感受到积极情绪时，我会很小心地不让它们表露出来","suppression",False),
    (5,"在面对压力情境时，我会使自己以有助于保持平静的方式来考虑它","reappraisal",False),
    (6,"我控制自己情绪的方式是不表达它们","suppression",False),
    (7,"当我想多感受一些积极的情绪时，我会改变自己对情境的考虑方式","reappraisal",False),
    (8,"我会通过改变对情境的考虑方式来控制自己的情绪","reappraisal",False),
    (9,"当感受到消极的情绪时，我确保不会表露它们","suppression",False),
    (10,"当我想少感受一些消极的情绪时，我会改变自己对情境的考虑方式","reappraisal",False),
]
opts_erq = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["非常不同意","不同意","有些不同意","不确定","有些同意","同意","非常同意"])]
w("ERQ.json",{
    "name":"情绪调节问卷","short_name":"ERQ",
    "description":"评估认知重评和表达抑制两种情绪调节策略的10题量表。由Gross JJ & John OP 2003年编制，中文版α=0.85（认知重评）/0.77（表达抑制）。",
    "applicable_levels":[2,3],"question_count":10,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula",
        "formula":"reappraisal_mean = mean(items 1,3,5,7,8,10); suppression_mean = mean(items 2,4,6,9)",
        "reverse_items":[],
        "subscales":{"reappraisal":[1,3,5,7,8,10],"suppression":[2,4,6,9]},
        "subscale_labels":{"reappraisal":"认知重评","suppression":"表达抑制"}
    },
    "result_levels":[],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_erq,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in erq_items
    ]
})

# ═══ SWLS 生活满意度量表 ═══
swls_texts = [
    "我生活中的大多数方面接近我的理想",
    "我的生活条件很好",
    "我对自己的生活感到满意",
    "迄今为止我在生活中得到了想得到的重要东西",
    "如果我能回头重走人生之路，我几乎不想改变任何东西",
]
opts_swls = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["完全不同意","不同意","有些不同意","不确定","有些同意","同意","完全同意"])]
w("SWLS.json",{
    "name":"生活满意度量表","short_name":"SWLS",
    "description":"评估整体主观生活满意度的5题量表，七级评分。由Diener E等1985年编制，公共领域免费使用，α=0.78-0.87。",
    "applicable_levels":[2,3],"question_count":5,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[5,9],"level":"very_dissatisfied","label":"非常不满意","alert":"orange"},
        {"range":[10,14],"level":"dissatisfied","label":"不满意","alert":"yellow"},
        {"range":[15,19],"level":"slightly_dissatisfied","label":"有些不满意","alert":None},
        {"range":[20,20],"level":"neutral","label":"中性","alert":None},
        {"range":[21,25],"level":"slightly_satisfied","label":"较为满意","alert":None},
        {"range":[26,30],"level":"satisfied","label":"满意","alert":None},
        {"range":[31,35],"level":"very_satisfied","label":"非常满意","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts_swls,"reverse_score":False,"subscale_key":None,"is_alert_item":False}
        for i,t in enumerate(swls_texts)
    ]
})

# ═══ BSCS 简式自我控制量表 ═══
bscs_items = [
    (1,"我能很好地抵制诱惑",False),
    (2,"我会做一些能给自己带来快乐但对自己有害的事",True),
    (3,"大家说我有钢铁般的自制力",False),
    (4,"有时我会被有乐趣的事情干扰而不能按时完成任务",True),
    (5,"我能为了一个长远目标高效地工作",False),
    (6,"有时我会忍不住去做一些明明知道不对的事情",True),
    (7,"我常常考虑不周就付诸行动",True),
]
opts_bscs_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["完全不符合","不太符合","一般","比较符合","完全符合"])]
opts_bscs_rev = [{"value":i+1,"label":l,"score":5-i} for i,l in enumerate(["完全不符合","不太符合","一般","比较符合","完全符合"])]
w("BSCS.json",{
    "name":"简式自我控制量表","short_name":"BSCS",
    "description":"评估自律性和冲动控制的7题量表。由Morean等2014年编制，中文版α=0.83，重测信度=0.81。",
    "applicable_levels":[2,3],"question_count":7,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[2,4,6,7],"subscales":{}},
    "result_levels":[
        {"range":[7,17],"level":"low","label":"自我控制能力较弱","alert":"yellow"},
        {"range":[18,25],"level":"medium","label":"自我控制能力中等","alert":None},
        {"range":[26,35],"level":"high","label":"自我控制能力较强","alert":None},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_bscs_rev if rev else opts_bscs_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in bscs_items
    ]
})

# ═══ AGQ-R 成就目标问卷 ═══
agq_items = [
    (1,"本学期，我力争尽可能彻底地理解课程内容","mastery_approach",False),
    (2,"本学期，我的目标是尽可能多地学习","mastery_approach",False),
    (3,"本学期，我的目的是完全掌握本学期课程中呈现的材料","mastery_approach",False),
    (4,"本学期，我努力避免对课程材料理解不完整","mastery_avoidance",False),
    (5,"本学期，我努力避免学习少于我可能学到的","mastery_avoidance",False),
    (6,"本学期，我的目标是避免学习少于可能学到的内容","mastery_avoidance",False),
    (7,"本学期，我的目标是表现得比其他学生更好","performance_approach",False),
    (8,"本学期，我的目的是在课程中相对于其他学生表现良好","performance_approach",False),
    (9,"我努力比其他学生表现得更好","performance_approach",False),
    (10,"本学期，我的目标是避免表现不好","performance_avoidance",False),
    (11,"本学期，我的目的是避免表现得比其他学生差","performance_avoidance",False),
    (12,"本学期，我努力避免表现得不好","performance_avoidance",False),
]
opts_agq = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["非常不同意","不同意","有些不同意","不确定","有些同意","同意","非常同意"])]
w("AGQ-R.json",{
    "name":"成就目标问卷修订版","short_name":"AGQ-R",
    "description":"评估学业成就目标四维度（掌握趋近/回避、成绩趋近/回避）的12题量表。由Elliot AJ & Murayama K 2008年编制，中文版α=0.83-0.92。",
    "applicable_levels":[2,3],"question_count":12,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula","formula":"subscale_mean = subscale_sum / 3","reverse_items":[],
        "subscales":{
            "mastery_approach":[1,2,3],"mastery_avoidance":[4,5,6],
            "performance_approach":[7,8,9],"performance_avoidance":[10,11,12]
        },
        "subscale_labels":{
            "mastery_approach":"掌握趋近目标","mastery_avoidance":"掌握回避目标",
            "performance_approach":"成绩趋近目标","performance_avoidance":"成绩回避目标"
        }
    },
    "result_levels":[],"alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_agq,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in agq_items
    ]
})

# ═══ PSS-10 压力知觉量表 ═══
pss_items = [
    (1,"因为发生意外的事情而感到心烦意乱",False),
    (2,"感到无法控制生活中重要的事情",False),
    (3,"感到紧张和压力",False),
    (4,"成功地处理了生活中令人烦恼的问题",True),
    (5,"感到能有效地应付生活中的重要变化",True),
    (6,"对自己处理个人问题的能力缺乏信心",False),
    (7,"能够按自己的方式处理事情",True),
    (8,"感到有能力应对困难",True),
    (9,"因为发生在控制范围之外的事情而感到愤怒",False),
    (10,"感到困难积累了太多无法克服",False),
]
opts_pss_fwd = [{"value":i,"label":l,"score":i} for i,l in enumerate(["从不","偶尔","有时","经常","总是"])]
opts_pss_rev = [{"value":i,"label":l,"score":4-i} for i,l in enumerate(["从不","偶尔","有时","经常","总是"])]
w("PSS-10.json",{
    "name":"压力知觉量表（10题）","short_name":"PSS-10",
    "description":"评估近一个月内感知压力水平的10题量表。由Cohen S等1983年编制，中文版α=0.78-0.86。",
    "applicable_levels":[2,3],"question_count":10,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[4,5,7,8],"subscales":{}},
    "result_levels":[
        {"range":[0,13],"level":"low","label":"低压力","alert":None},
        {"range":[14,26],"level":"moderate","label":"中等压力","alert":"yellow"},
        {"range":[27,40],"level":"high","label":"高压力","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_pss_rev if rev else opts_pss_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in pss_items
    ]
})

print("Batch 4 (GSES, Grit-S, MLQ, GQ-6, PANAS, CAMM, ERQ, SWLS, BSCS, AGQ-R, PSS-10) done")
