import json, os
OUT = "/workspace/json_export/adults"
def w(fn, d):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {fn}")

# ═══ ISI 失眠严重程度指数 ═══
w("ISI.json",{
    "name":"失眠严重程度指数量表","short_name":"ISI",
    "description":"评估成人失眠严重程度的7题量表，评估过去两周症状。由Morin CM等1993/2011年编制，α=0.74-0.83。",
    "applicable_levels":[],"question_count":7,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,7],"level":"none","label":"无临床意义失眠","alert":None},
        {"range":[8,14],"level":"subthreshold","label":"轻度失眠","alert":"yellow"},
        {"range":[15,21],"level":"moderate","label":"中度失眠","alert":"orange"},
        {"range":[22,28],"level":"severe","label":"重度失眠","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":1,"question_text":"入睡困难的严重程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["无","轻度","中度","重度","极重度"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":2,"question_text":"维持睡眠困难（夜间醒来）的严重程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["无","轻度","中度","重度","极重度"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":3,"question_text":"早醒问题的严重程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["无","轻度","中度","重度","极重度"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":4,"question_text":"您对目前睡眠模式的满意程度","question_type":"likert","options":[{"value":0,"label":"非常满意","score":0},{"value":1,"label":"满意","score":1},{"value":2,"label":"中等","score":2},{"value":3,"label":"不满意","score":3},{"value":4,"label":"非常不满意","score":4}],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":5,"question_text":"睡眠问题对日常功能（如疲乏、情绪、工作）的影响程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["无","轻微","有些","很多","极大影响"])],"reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":6,"question_text":"您对睡眠问题的担心/苦恼程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["完全没有","轻微","有些","很多","非常"])], "reverse_score":False,"subscale_key":None,"is_alert_item":False},
        {"question_no":7,"question_text":"他人观察到您的睡眠问题影响生活质量的程度","question_type":"likert","options":[{"value":i,"label":l,"score":i} for i,l in enumerate(["完全没有","轻微","有些","很多","非常"])], "reverse_score":False,"subscale_key":None,"is_alert_item":False},
    ]
})

# ═══ ESS 爱普沃斯嗜睡量表 ═══
ess_texts = [
    "坐着阅读书刊时","看电视时","在公共场所安静地坐着（如剧场、会议）",
    "连续乘坐汽车1小时（无间断）","条件允许的情况下，下午躺下休息时",
    "坐着与人谈话时","未饮酒的午餐后安静地坐着","遇到堵车，在停车的几分钟里",
]
opts_ess = [{"value":i,"label":l,"score":i} for i,l in enumerate(["从不打瞌睡","轻度可能打瞌睡","中度可能打瞌睡","很可能打瞌睡"])]
w("ESS.json",{
    "name":"爱普沃斯嗜睡量表","short_name":"ESS",
    "description":"评估白天嗜睡程度的8题量表，由澳大利亚Epworth医院设计。中文版α=0.82。",
    "applicable_levels":[],"question_count":8,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,10],"level":"normal","label":"正常","alert":None},
        {"range":[11,15],"level":"mild","label":"过度嗜睡","alert":"yellow"},
        {"range":[16,24],"level":"severe","label":"严重嗜睡","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_ess,"reverse_score":False,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(ess_texts)]
})

# ═══ BAI 贝克焦虑量表 ═══
bai_texts = [
    "麻木或刺痛感","感到发热","腿部颤抖","无法放松","担心发生最坏的事情",
    "头晕或感到轻飘飘","心跳加速或心悸","坐立不安","被吓到","神经紧张",
    "窒息感","手发抖","颤抖","害怕失控","呼吸困难","害怕快要死去",
    "恐慌","消化不良或腹部不适","昏厥感","脸红","出汗（不因暑热）",
]
opts_bai = [{"value":i,"label":l,"score":i} for i,l in enumerate(["无","轻度，无多大烦扰","中度，不舒适但尚能忍受","重度，只能勉强忍受"])]
w("BAI.json",{
    "name":"贝克焦虑量表","short_name":"BAI",
    "description":"评估过去一周焦虑症状严重程度的21题自评量表。由Beck AT等1988年编制，α=0.91-0.95。",
    "applicable_levels":[],"question_count":21,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,7],"level":"normal","label":"无焦虑","alert":None},
        {"range":[8,15],"level":"mild","label":"轻度焦虑","alert":"yellow"},
        {"range":[16,25],"level":"moderate","label":"中度焦虑","alert":"orange"},
        {"range":[26,63],"level":"severe","label":"重度焦虑","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_bai,"reverse_score":False,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(bai_texts)]
})

# ═══ GHQ-12 ═══
ghq12_items = [
    (1,"在做什么事情的时候，能集中精神吗？",True),
    (2,"有由于过分担心而失眠的情况吗？",False),
    (3,"觉得自己是有用的人吗？",True),
    (4,"觉得自己有决断力吗？",True),
    (5,"总是处于紧张状态吗？",False),
    (6,"觉得自己不能解决问题吗？",False),
    (7,"能享受日常活动吗？",True),
    (8,"能够面对您所面临的问题吗？",True),
    (9,"感到痛苦、忧虑吗？",False),
    (10,"失去自信了吗？",False),
    (11,"觉得自己是没有价值的人吗？",False),
    (12,"觉得所有的事情都顺利吗？",True),
]
opts_ghq_pos = [{"value":i,"label":l,"score":i} for i,l in enumerate(["比平时好","和平时一样","比平时差","差很多"])]
opts_ghq_neg = [{"value":i,"label":l,"score":3-i} for i,l in enumerate(["根本没有","和平时一样","比以前多","比以前多很多"])]
w("GHQ-12.json",{
    "name":"一般健康问卷","short_name":"GHQ-12",
    "description":"成人心理健康快速筛查的12题量表。由Goldberg DP 1972年编制，α=0.82-0.89。",
    "applicable_levels":[],"question_count":12,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"formula",
        "formula":"GHQ scoring: '比平时好'/'和平时一样'=0, '比平时差'/'差很多'=1; OR Likert 0-1-2-3",
        "reverse_items":[],
        "subscales":{},
        "note":"GHQ二分计分法（0-12分）；或李克特四级计分（0-36分）"
    },
    "result_levels":[
        {"range":[0,2],"level":"normal","label":"无明显心理健康问题","alert":None,"note":"GHQ二分法总分"},
        {"range":[3,12],"level":"positive","label":"可能存在心理健康问题","alert":"yellow","note":"GHQ二分法总分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_ghq_neg if pos else opts_ghq_pos,"reverse_score":pos,"subscale_key":None,"is_alert_item":False}
        for no,t,pos in ghq12_items
    ]
})

# ═══ WHO-5 幸福感指数 ═══
who5_texts = [
    "我感到心情愉快和高兴","我感到平静、放松",
    "我感到积极主动、充满活力","我感到醒来精力充沛，精神焕发",
    "我的日常生活充满了我感兴趣的事物",
]
opts_who5 = [{"value":i,"label":l,"score":i} for i,l in enumerate(
    ["从未","有时","不到一半时间","超过一半时间","大多数时间","所有时间"])]
w("WHO-5.json",{
    "name":"WHO-5幸福感指数","short_name":"WHO-5",
    "description":"WHO官方免费提供的5题心理健康筛查量表，评估过去两周。积极心理健康指标，也可用于抑郁筛查（≤13分建议PHQ-9进一步评估）。",
    "applicable_levels":[],"question_count":5,"estimated_mins":2,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"formula","formula":"raw_score = sum; percentage_score = raw_score * 4",
        "reverse_items":[],"subscales":{}
    },
    "result_levels":[
        {"range":[0,13],"level":"poor","label":"心理健康状态较差","alert":"yellow","note":"原始总分（0-25），建议PHQ-9进一步筛查"},
        {"range":[14,20],"level":"moderate","label":"心理健康状态一般","alert":None,"note":"原始总分"},
        {"range":[21,25],"level":"good","label":"心理健康状态良好","alert":None,"note":"原始总分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[{"question_no":i+1,"question_text":t,"question_type":"likert","options":opts_who5,"reverse_score":False,"subscale_key":None,"is_alert_item":False} for i,t in enumerate(who5_texts)]
})

# ═══ UCLA 孤独感量表 ═══
ucla_items = [
    (1,"您常感到与周围人的关系和谐吗？",True),
    (2,"您常感到缺少伙伴吗？",False),
    (3,"您常感到没人可以信赖吗？",False),
    (4,"您常感到寂寞吗？",False),
    (5,"您常感到属于朋友们中的一员吗？",True),
    (6,"您常感到与周围的人有许多共同点吗？",True),
    (7,"您常感到与任何人都不亲密了吗？",False),
    (8,"您常感到您的兴趣与想法与周围的人不一样吗？",False),
    (9,"您常感到想要与人来往、结交朋友吗？",True),
    (10,"您常感到与人亲近吗？",True),
    (11,"您常感到被人冷落吗？",False),
    (12,"您常感到您与别人来往毫无意义吗？",False),
    (13,"您常感到没有人很了解您吗？",False),
    (14,"您常感到与别人隔开了吗？",False),
    (15,"您常感到当您愿意时就能找到伙伴吗？",True),
    (16,"您常感到有人真正了解您吗？",True),
    (17,"您常感到羞怯吗？",False),
    (18,"您常感到有人围着您但并不关心您吗？",False),
    (19,"您常感到有人愿意与您交谈吗？",True),
    (20,"您常感到有人值得您信赖吗？",True),
]
opts_ucla_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["从不","很少","有时","总是"])]
opts_ucla_rev = [{"value":i+1,"label":l,"score":4-i} for i,l in enumerate(["从不","很少","有时","总是"])]
w("UCLA-LS.json",{
    "name":"UCLA孤独感量表第三版","short_name":"UCLA-LS",
    "description":"评估成人孤独感水平的20题量表（第三版）。由Russell DW 1996年编制，α=0.90。",
    "applicable_levels":[],"question_count":20,"estimated_mins":7,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[1,5,6,9,10,15,16,19,20],"subscales":{}},
    "result_levels":[
        {"range":[20,28],"level":"low","label":"低度孤独","alert":None},
        {"range":[29,38],"level":"moderate","label":"中等孤独","alert":"yellow"},
        {"range":[39,43],"level":"high","label":"较高孤独","alert":"orange"},
        {"range":[44,80],"level":"very_high","label":"高度孤独","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_ucla_rev if rev else opts_ucla_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in ucla_items
    ]
})

# ═══ AUDIT 酒精筛查 ═══
audit_items_opts = [
    ("您的饮酒频率如何？",[("从不",0),("每月≤1次",1),("每月2-4次",2),("每周2-3次",3),("每周≥4次",4)]),
    ("饮酒时，您通常会喝几杯？（1杯=含10g纯酒精）",[("1-2杯",0),("3-4杯",1),("5-6杯",2),("7-9杯",3),("≥10杯",4)]),
    ("每次喝6杯以上的情况有多频繁？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("过去一年，您是否发现一旦开始喝酒就很难停下来？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("过去一年，您是否因为饮酒而不能完成日常工作？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("过去一年，大量饮酒后，您是否需要在早上喝酒才能正常生活？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("过去一年，您是否在饮酒后感到内疚或后悔？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("过去一年，您是否因为饮酒而不能记起前一晚发生的事情？",[("从不",0),("不到每月",1),("每月",2),("每周",3),("几乎每天",4)]),
    ("您或他人是否因为您的饮酒而受到伤害？",[("没有",0),("有，但不是过去一年",2),("是，在过去一年",4)]),
    ("家人、朋友、医生是否对您饮酒表示担忧或建议您戒酒？",[("没有",0),("有，但不是过去一年",2),("是，在过去一年",4)]),
]
w("AUDIT.json",{
    "name":"酒精使用障碍识别测验","short_name":"AUDIT",
    "description":"WHO开发的10题酒精筛查工具，识别危险饮酒、有害饮酒和酒精依赖。中文版灵敏度0.96，特异度0.85。",
    "applicable_levels":[],"question_count":10,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,7],"level":"low","label":"低风险","alert":None},
        {"range":[8,15],"level":"risky","label":"危险饮酒","alert":"yellow"},
        {"range":[16,19],"level":"harmful","label":"有害饮酒","alert":"orange"},
        {"range":[20,40],"level":"dependent","label":"可能酒精依赖","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":9,"condition":"value >= 2","alert":"orange","reason":"饮酒已造成伤害"},
        {"question_no":10,"condition":"value >= 2","alert":"orange","reason":"他人已对饮酒表示担忧"},
    ]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":text,"question_type":"single",
         "options":[{"value":j,"label":l,"score":s} for j,(l,s) in enumerate(opts)],
         "reverse_score":False,"subscale_key":None,"is_alert_item":(i>=8)}
        for i,(text,opts) in enumerate(audit_items_opts)
    ]
})

# ═══ PCL-5 PTSD检查表 ═══
pcl5_subscales = {
    "re_experiencing":[1,2,3,4,5],
    "avoidance":[6,7],
    "negative_cognition":[8,9,10,11,12,13,14],
    "hyperarousal":[15,16,17,18,19,20],
}
pcl5_texts = [
    "对创伤性经历反复出现、不受控的痛苦记忆",
    "关于创伤性经历的反复痛苦梦境",
    "突然感到或表现得好像创伤性经历又在发生（闪回）",
    "当有事物提醒您时，感到非常难过",
    "当有事物提醒您时，有强烈的生理反应（如心跳加速）",
    "回避关于创伤性经历的记忆、想法或感受",
    "回避可能提醒您创伤性经历的外部线索",
    "无法记住创伤性经历的重要方面",
    "对自己、他人或世界持有强烈的负性信念",
    "因创伤性经历而自责或责备他人",
    "强烈的负性情绪（如恐惧、恐怖、愤怒、内疚或羞耻）",
    "对以前喜欢的活动不再感兴趣",
    "感到与他人疏远或脱节",
    "无法体验积极情绪（无法感到快乐、爱或满足）",
    "易激惹的行为和愤怒爆发",
    "做危险或自我毁灭的事情",
    "过度警觉或保持警惕",
    "容易受到惊吓",
    "注意力集中困难",
    "睡眠困难",
]
item_sub_pcl = {}
for sub, items in pcl5_subscales.items():
    for i in items:
        item_sub_pcl[i] = sub
opts_pcl = [{"value":i,"label":l,"score":i} for i,l in enumerate(
    ["完全没有","有一点","中等程度","很多","极其严重"])]
w("PCL-5.json",{
    "name":"PTSD检查表（DSM-5版）","short_name":"PCL-5",
    "description":"评估PTSD症状严重程度的20题量表，评估过去一个月。由美国退伍军人事务部2013年编制，α=0.90+。",
    "applicable_levels":[],"question_count":20,"estimated_mins":8,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":pcl5_subscales,
        "subscale_labels":{
            "re_experiencing":"再体验","avoidance":"回避",
            "negative_cognition":"认知与情绪负性改变","hyperarousal":"过度警觉"
        }
    },
    "result_levels":[
        {"range":[0,32],"level":"normal","label":"PTSD可能性较低","alert":None},
        {"range":[33,49],"level":"possible","label":"可能存在PTSD","alert":"orange"},
        {"range":[50,80],"level":"likely","label":"高度可能PTSD","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":16,"condition":"value >= 2","alert":"red","reason":"危险或自我毁灭行为"},
    ]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":pcl5_texts[i],"question_type":"likert",
         "options":opts_pcl,"reverse_score":False,"subscale_key":item_sub_pcl.get(i+1),"is_alert_item":(i+1==16)}
        for i in range(20)
    ]
})

# ═══ OCI-R 强迫症状量表 ═══
ocir_subscales = {
    "hoarding":[1,7,13],"neutralizing":[2,8,14],"ordering":[3,9,15],
    "obsessing":[4,10,16],"washing":[5,11,17],"checking":[6,12,18],
}
ocir_texts = [
    "我在家里积累了大量的物品，以至于这些物品开始妨碍到我",
    "当有不好的念头时，我需要通过另外一些好的念头来抵消它",
    "我害怕我不把东西按特定方式排列就会遭到某种不幸",
    "我常常有闯入性的淫秽想法，让我感到不安",
    "我洗手的次数比大多数人多",
    "我觉得有必要反复检查门是否关好、电器是否关闭等",
    "扔掉一些东西让我感到很不舒服",
    "我有时候感到我必须反复做一件事，直到觉得刚刚好了为止",
    "因为我对对称性和整洁性感到很不舒服，所以我对此想了很多",
    "我脑子里经常出现闯入性的想法，让我很烦恼",
    "我在用手接触过东西后，觉得手感染了细菌",
    "我经常要花很多时间检查我的东西",
    "我收集了很多我不会用到的东西",
    "我有时候觉得必须反复执行某个特定动作",
    "我感到心烦，因为我的想法对我来说不是一个好兆头",
    "我对某些令我憎恶的念头感到很烦恼",
    "我喜欢自己保持整洁，经常洗手",
    "我觉得我反复检查事情有些过分了",
]
item_sub_oci = {}
for sub, items in ocir_subscales.items():
    for i in items:
        item_sub_oci[i] = sub
opts_ocir = [{"value":i,"label":l,"score":i} for i,l in enumerate(["完全没有","轻度","中度","重度","极度严重"])]
w("OCI-R.json",{
    "name":"强迫症状量表修订版","short_name":"OCI-R",
    "description":"评估强迫症状严重程度的18题量表，含6个症状维度。由Foa EB等2002年编制，α=0.87-0.90。阳性阈值：总分≥21分。",
    "applicable_levels":[],"question_count":18,"estimated_mins":5,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":ocir_subscales,
        "subscale_labels":{
            "hoarding":"囤积","neutralizing":"心理中和","ordering":"排序",
            "obsessing":"强迫思维","washing":"洗涤","checking":"强迫检查"
        }
    },
    "result_levels":[
        {"range":[0,20],"level":"normal","label":"低于强迫症阈值","alert":None},
        {"range":[21,72],"level":"positive","label":"高于阳性阈值","alert":"orange","note":"建议进一步专业评估"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":ocir_texts[i],"question_type":"likert",
         "options":opts_ocir,"reverse_score":False,"subscale_key":item_sub_oci.get(i+1),"is_alert_item":False}
        for i in range(18)
    ]
})

# ═══ BHS 贝克绝望感量表 ═══
bhs_items = [
    (1,"我对未来充满希望与热情","F",True),
    (2,"我不如自己努力摆脱困境，因为根本没有什么可做的","T",False),
    (3,"当事情进展不顺利时，我总是知道会好转的","F",True),
    (4,"我无法想象10年后的生活会是什么样的","T",False),
    (5,"我有足够的时间来完成我最渴望做的事情","F",True),
    (6,"在未来，我预计自己会成功地达到我最重要的目标","F",True),
    (7,"我的未来对我来说看起来很暗淡","T",False),
    (8,"我碰巧比其他人更好运，从好事中获得良好利益","F",True),
    (9,"我无法获得良好的生活","T",False),
    (10,"我过去的经历很好地为我的未来做了准备","F",True),
    (11,"我看到的未来除了不愉快之外什么都没有","T",False),
    (12,"我不指望得到我真正想要的东西","T",False),
    (13,"当我展望未来时，我期待比现在更幸福","F",True),
    (14,"事情从来不会如我所愿","T",False),
    (15,"我对未来充满信心","F",True),
    (16,"我永远得不到我想要的，所以想要任何东西都是愚蠢的","T",False),
    (17,"我几乎不可能在未来获得真正的满足","T",False),
    (18,"未来对我来说看起来很模糊和不确定","T",False),
    (19,"我可以期待比坏事更多的好事","F",True),
    (20,"为了未来努力是毫无意义的","T",False),
]
opts_bhs = [{"value":0,"label":"否","score":0},{"value":1,"label":"是","score":1}]
w("BHS.json",{
    "name":"贝克绝望感量表","short_name":"BHS",
    "description":"评估对未来消极预期的20题量表，是自杀风险的重要预测指标。由Beck AT等1974年编制，α=0.93。高分（≥9分）与自杀风险相关。",
    "applicable_levels":[],"question_count":20,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"sum",
        "reverse_items":[1,3,5,6,8,10,13,15,19],
        "note":"答'是'且对应无望方向得1分，答'否'且对应有望方向得1分（具体见原量表）",
        "subscales":{}
    },
    "result_levels":[
        {"range":[0,3],"level":"minimal","label":"无/轻微绝望","alert":None},
        {"range":[4,8],"level":"mild","label":"轻度绝望","alert":"yellow"},
        {"range":[9,14],"level":"moderate","label":"中度绝望","alert":"orange"},
        {"range":[15,20],"level":"severe","label":"重度绝望","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":None,"condition":"total >= 9","alert":"red","reason":"绝望感评分≥9分，与自杀风险显著相关，须进行安全评估"}
    ]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"single",
         "options":opts_bhs,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,_,rev in bhs_items
    ]
})

# ═══ GDS-15 老年抑郁量表 ═══
gds_items = [
    (1,"总的来说，您对自己的生活感到满意吗？","否"),
    (2,"您是否减少了许多以往的兴趣和爱好？","是"),
    (3,"您是否感到生活空虚？","是"),
    (4,"您是否经常感到厌倦？","是"),
    (5,"您对未来充满希望吗？","否"),
    (6,"您是否有一些无法摆脱的令人烦恼的想法？","是"),
    (7,"您大多数时候精神状态良好吗？","否"),
    (8,"您是否害怕会有坏事降临到您身上？","是"),
    (9,"您大多数时间是否感到幸福？","否"),
    (10,"您是否经常感到无助？","是"),
    (11,"您是否经常感到不安或坐立不安？","是"),
    (12,"您是否宁愿待在家里，而不是去做一些新的事情？","是"),
    (13,"您是否经常担忧将来的事情？","是"),
    (14,"您觉得您的记忆力比大多数人差吗？","是"),
    (15,"您觉得活着是美好的吗？","否"),
]
w("GDS-15.json",{
    "name":"老年抑郁量表简版","short_name":"GDS-15",
    "description":"用于老年人（≥60岁）抑郁筛查的15题是/否量表。由Yesavage JA等1983年编制，α=0.85。",
    "applicable_levels":[],"question_count":15,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"sum",
        "reverse_items":[1,5,7,9,15],
        "note":"答'是'且对应抑郁的答案得1分，答'否'且对应抑郁答案（反向题）得1分",
        "subscales":{}
    },
    "result_levels":[
        {"range":[0,4],"level":"normal","label":"正常，无抑郁","alert":None},
        {"range":[5,8],"level":"mild","label":"轻度抑郁","alert":"yellow"},
        {"range":[9,11],"level":"moderate","label":"中度抑郁","alert":"orange"},
        {"range":[12,15],"level":"severe","label":"重度抑郁","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"single",
         "options":[{"value":0,"label":"否","score":1 if pos_ans=="否" else 0},{"value":1,"label":"是","score":1 if pos_ans=="是" else 0}],
         "reverse_score":pos_ans=="否","subscale_key":None,"is_alert_item":False}
        for no,t,pos_ans in gds_items
    ]
})

print("Batch 6 (adults): ISI, ESS, BAI, GHQ-12, WHO-5, UCLA-LS, AUDIT, PCL-5, OCI-R, BHS, GDS-15 done")
