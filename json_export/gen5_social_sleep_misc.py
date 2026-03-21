import json, os
OUT = "/workspace/json_export/students"
def w(fn, d):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {fn}")

# ═══ SASC 儿童社交焦虑量表 ═══
sasc_items = [
    (1,"我害怕在别的孩子面前做没做过的事","fne",False),
    (2,"我担心被人取笑","fne",False),
    (3,"我周围都是我不认识的小朋友时，我觉得害羞","sad",False),
    (4,"我和小伙伴一起时很少说话","sad",False),
    (5,"我担心其他孩子会怎么样看待我","fne",False),
    (6,"我觉得小朋友们取笑我","fne",False),
    (7,"我和陌生的小朋友说话时感到紧张","sad",False),
    (8,"我担心其他孩子会怎样说我","fne",False),
    (9,"我只同我熟悉的小朋友说话","sad",False),
    (10,"我担心别的小朋友会不喜欢我","fne",False),
]
opts_sasc = [{"value":i,"label":l,"score":i} for i,l in enumerate(["从无","有时有","一直有"])]
w("SASC.json",{
    "name":"儿童社交焦虑量表","short_name":"SASC",
    "description":"评估6-13岁儿童社交焦虑的10题量表，含害怕否定评价和社交回避两个因子。由La Greca AM & Stone WL 1993年编制，α=0.76。",
    "applicable_levels":[1,2],"question_count":10,"estimated_mins":5,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":{"fne":[1,2,5,6,8,10],"sad":[3,4,7,9]},
        "subscale_labels":{"fne":"害怕否定评价","sad":"社交回避及苦恼"}
    },
    "result_levels":[
        {"range":[0,6],"level":"normal","label":"无明显社交焦虑","alert":None},
        {"range":[7,12],"level":"mild","label":"中等社交焦虑","alert":"yellow"},
        {"range":[13,20],"level":"severe","label":"明显社交焦虑","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_sasc,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in sasc_items
    ]
})

# ═══ SAS-A 青少年社交焦虑量表 ═══
sasa_items = [
    (1,"我在别人面前做自己不熟悉的事情时会感到焦虑","sad_new",False),
    (2,"我害怕被别人耻笑打趣","fne",False),
    (3,"当我处于陌生人中间时，我会很害羞","sad_new",False),
    (4,"我只和我很熟悉的人交谈","sad_new",False),
    (5,"我感觉同龄人在背后谈论我","fne",False),
    (6,"我担心别人会怎么看我","fne",False),
    (7,"我害怕别人会不喜欢我","fne",False),
    (8,"当和不熟悉的同龄人交谈时我会很紧张","sad_new",False),
    (9,"我总担心别人会怎么评论我","fne",False),
    (10,"当我认识新朋友时总会很紧张","sad_new",False),
    (11,"我担心别人不喜欢我","fne",False),
    (12,"与一群人在一起时我总是保持沉默","sad_general",False),
    (13,"我总觉得别人在取笑我","fne",False),
    (14,"我认为如果我和别人争执的话，别人会不喜欢我","fne",False),
    (15,"我会因为害怕被拒绝而不愿意邀请别人同我一起做事","sad_general",False),
    (16,"同某些人在一起时，我会感到紧张","sad_new",False),
    (17,"即使与很熟悉的人在一起，我也会感到害羞","sad_general",False),
    (18,"对我来说，邀请别人同我一起做事太难了","sad_general",False),
]
opts_5 = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["完全不符合","不太符合","不确定","比较符合","完全符合"])]
w("SAS-A.json",{
    "name":"青少年社交焦虑量表","short_name":"SAS-A",
    "description":"评估11-17岁青少年社交焦虑的18题量表，含害怕否定评价、陌生和一般情境下社交回避三个因子。由La Greca AM & Lopez N 1998年编制，朱海东中文版，α=0.816。",
    "applicable_levels":[2,3],"question_count":18,"estimated_mins":8,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":{
            "fne":[2,5,6,7,9,11,13,14],
            "sad_new":[1,3,4,8,10,16],
            "sad_general":[12,15,17,18]
        },
        "subscale_labels":{"fne":"害怕否定评价","sad_new":"陌生情境社交回避","sad_general":"一般情境社交回避"}
    },
    "result_levels":[
        {"range":[18,45],"level":"normal","label":"无明显社交焦虑","alert":None},
        {"range":[46,60],"level":"mild","label":"中度社交焦虑","alert":"yellow"},
        {"range":[61,90],"level":"severe","label":"明显社交焦虑","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_5,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,_ in sasa_items
    ]
})

# ═══ MSPSS 多维感知社会支持量表 ═══
mspss_items = [
    (1,"有一个特殊的人在我需要时出现在我身边","significant_other"),
    (2,"有一个特殊的人可以和我分享快乐和悲伤","significant_other"),
    (3,"我的家人真的尽力帮助我","family"),
    (4,"我从家人那里获得所需的情感帮助和支持","family"),
    (5,"有一个特殊的人对我是真正的安慰来源","significant_other"),
    (6,"我的朋友真的尽力帮助我","friends"),
    (7,"当事情出错时，我可以依靠我的朋友","friends"),
    (8,"我可以和我的家人谈论我的问题","family"),
    (9,"我有朋友可以和他们分享快乐和悲伤","friends"),
    (10,"我生命中有一个特殊的人关心我的感受","significant_other"),
    (11,"我的家人愿意帮我做决定","family"),
    (12,"我可以和我的朋友谈论我的问题","friends"),
]
opts_7 = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(
    ["非常强烈不同意","强烈不同意","轻度不同意","中立","轻度同意","强烈同意","非常强烈同意"])]
w("MSPSS.json",{
    "name":"多维感知社会支持量表","short_name":"MSPSS",
    "description":"评估来自重要他人、家庭和朋友三方面社会支持的12题量表。由Zimet GD等1988年编制，已在8-14岁儿童中验证适用。",
    "applicable_levels":[1,2,3],"question_count":12,"estimated_mins":5,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula","formula":"subscale_mean = subscale_sum / 4; total_mean = all_sum / 12",
        "reverse_items":[],
        "subscales":{
            "significant_other":[1,2,5,10],"family":[3,4,8,11],"friends":[6,7,9,12]
        },
        "subscale_labels":{"significant_other":"重要他人支持","family":"家庭支持","friends":"朋友支持"}
    },
    "result_levels":[
        {"range":[1.0,2.99],"level":"low","label":"社会支持不足","alert":"yellow","note":"各维度均分"},
        {"range":[3.0,4.99],"level":"medium","label":"社会支持一般","alert":None,"note":"各维度均分"},
        {"range":[5.0,7.0],"level":"high","label":"社会支持充足","alert":None,"note":"各维度均分"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_7,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub in mspss_items
    ]
})

# ═══ PSQI - 匹兹堡睡眠质量（混合题型，复杂评分）═══
w("PSQI.json",{
    "name":"匹兹堡睡眠质量指数","short_name":"PSQI",
    "description":"评估最近一个月睡眠质量的量表，含填写时间、频率选择等混合题型，需计算7个成分得分。由Buysse DJ等1989年编制，刘贤臣等1996年中文版。",
    "applicable_levels":[3],"question_count":19,"estimated_mins":10,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"formula",
        "formula":"component scores A-G calculated per PSQI manual; total = sum of 7 components",
        "note":"7个成分：A主观睡眠质量、B入睡时间、C睡眠时长、D睡眠效率、E睡眠障碍、F催眠药物、G日间功能。各成分0-3分，总分0-21分。",
        "reverse_items":[],
        "subscales":{
            "A_quality":["q6"],"B_latency":["q2","q5a"],"C_duration":["q4"],
            "D_efficiency":["q1","q3","q4"],"E_disturbance":["q5b_j"],
            "F_medication":["q7"],"G_daytime":["q8","q9"]
        }
    },
    "result_levels":[
        {"range":[0,5],"level":"good","label":"睡眠质量很好","alert":None,"note":"总分"},
        {"range":[6,10],"level":"fair","label":"睡眠质量较好","alert":None,"note":"总分"},
        {"range":[11,15],"level":"poor","label":"睡眠质量较差","alert":"yellow","note":"总分"},
        {"range":[16,21],"level":"very_poor","label":"睡眠质量很差","alert":"orange","note":"总分"},
    ],
    "alert_rules":{"item_rules":[]},"_incomplete":False,
    "is_active":True,
    "questions":[
        {"question_no":1,"question_text":"过去一个月，您通常上床睡觉的时间是？","question_type":"text","options":[],"reverse_score":False,"subscale_key":"D_efficiency","is_alert_item":False},
        {"question_no":2,"question_text":"过去一个月，每晚通常要多长时间（分钟）才能入睡？","question_type":"number","options":[],"reverse_score":False,"subscale_key":"B_latency","is_alert_item":False},
        {"question_no":3,"question_text":"过去一个月，每天早上通常什么时候起床？","question_type":"text","options":[],"reverse_score":False,"subscale_key":"D_efficiency","is_alert_item":False},
        {"question_no":4,"question_text":"过去一个月，每晚实际睡眠时间有多少小时？","question_type":"number","options":[],"reverse_score":False,"subscale_key":"C_duration","is_alert_item":False},
        {"question_no":5,"question_text":"过去一个月，因不能在30分钟内入睡而影响睡眠的频率？","question_type":"likert","options":[{"value":0,"label":"无","score":0},{"value":1,"label":"<1次/周","score":1},{"value":2,"label":"1-2次/周","score":2},{"value":3,"label":"≥3次/周","score":3}],"reverse_score":False,"subscale_key":"B_latency","is_alert_item":False},
        {"question_no":6,"question_text":"过去一个月，您对总体睡眠质量的评价？","question_type":"likert","options":[{"value":0,"label":"很好","score":0},{"value":1,"label":"较好","score":1},{"value":2,"label":"较差","score":2},{"value":3,"label":"很差","score":3}],"reverse_score":False,"subscale_key":"A_quality","is_alert_item":False},
        {"question_no":7,"question_text":"过去一个月，使用催眠药物（处方药或非处方药）的频率？","question_type":"likert","options":[{"value":0,"label":"无","score":0},{"value":1,"label":"<1次/周","score":1},{"value":2,"label":"1-2次/周","score":2},{"value":3,"label":"≥3次/周","score":3}],"reverse_score":False,"subscale_key":"F_medication","is_alert_item":False},
        {"question_no":8,"question_text":"过去一个月，开车、吃饭等时难以保持清醒的频率？","question_type":"likert","options":[{"value":0,"label":"无","score":0},{"value":1,"label":"<1次/周","score":1},{"value":2,"label":"1-2次/周","score":2},{"value":3,"label":"≥3次/周","score":3}],"reverse_score":False,"subscale_key":"G_daytime","is_alert_item":False},
        {"question_no":9,"question_text":"过去一个月，做事时精力不足的困扰程度？","question_type":"likert","options":[{"value":0,"label":"无","score":0},{"value":1,"label":"有时","score":1},{"value":2,"label":"经常","score":2},{"value":3,"label":"非常明显","score":3}],"reverse_score":False,"subscale_key":"G_daytime","is_alert_item":False},
    ]
})

# ═══ RRS 反刍思维量表 ═══
rrs_texts = [
    "我常常想我是多么孤独","我常常想：如果我不能停止想这些，那我就不能总是继续做手头的事",
    "我常常想我疲劳、痛苦的感觉","我常常想：集中注意力是多么困难",
    "我常常想我究竟做了什么会导致这样","我常常想自己是多么消极被动、毫无动力",
    "我常常分析最近发生的事以便理解为什么感到郁闷","我常常想我对其他事情感到麻木",
    "我常常想我为什么如此不顺心","我常常想我为什么总是这样",
    "我常常独自思考为什么会这样","我常常写下自己正在想的事情并加以分析",
    "我常常思考现状，希望它有所好转","我常常想如果这种感觉持续的话，就无法集中注意",
    "我常常想为什么我有这些问题，而别人却没有","我常常想我为什么不能把事情处理得更好",
    "我常常想我为什么感到如此伤心","我常常想我的缺点、失败、错误和过失",
    "我常常想：我对做任何事都提不起劲来","我常常分析自己的性格以便理解为何感到压抑",
    "我会常常单独到某个地方去想我的感受","我常常想我是多么地生自己的气",
]
rrs_subscales = {
    "brooding":[5,10,13,15,16],
    "reflection":[7,11,12,20,21],
    "symptom":[1,2,3,4,6,8,9,14,17,18,19,22],
}
item_sub_rrs = {}
for sub, items in rrs_subscales.items():
    for i in items:
        item_sub_rrs[i] = sub

opts_rrs = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["从不","有时","经常","总是"])]
w("RRS.json",{
    "name":"反刍思维量表","short_name":"RRS",
    "description":"评估对消极情绪的反复思考倾向，22题，含症状反刍、忧思和反省三维度。由Nolen-Hoeksema S 1991年编制，α=0.90，重测信度=0.82。",
    "applicable_levels":[2,3],"question_count":22,"estimated_mins":8,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":rrs_subscales,
        "subscale_labels":{"brooding":"强迫思考/忧思","reflection":"反省深思","symptom":"症状反刍"}
    },
    "result_levels":[
        {"range":[22,44],"level":"low","label":"反刍倾向较低","alert":None},
        {"range":[45,66],"level":"moderate","label":"中等反刍倾向","alert":"yellow"},
        {"range":[67,88],"level":"high","label":"反刍倾向较强","alert":"orange"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":rrs_texts[i],"question_type":"likert",
         "options":opts_rrs,"reverse_score":False,"subscale_key":item_sub_rrs.get(i+1),"is_alert_item":False}
        for i in range(22)
    ]
})

# ═══ TAI 考试焦虑测验 ═══
tai_texts = [
    "在重要的考试前几天，我就坐立不安了","临近考试时，我就泻肚子了",
    "一想到考试即将来临，身体就会发僵","在考试前，我总感到苦恼",
    "在考试前，我感到烦躁，脾气变坏","在紧张的复习期间，常会想到：这次考试要是得到个坏分数怎么办？",
    "越临近考试，我的注意力越难集中","一想到马上就要考试了，参加任何文娱活动都感到没劲",
    "在考试前，我总预感到这次考试将要考坏","在考试前，我常做关于考试的梦",
    "到了考试那天，我就不安起来","当听到开始考试的铃声响了，我的心马上紧张地急跳起来",
    "遇到重要的考试，我的脑子就变得比平时迟钝","看到考试题目越多、越难，我就越感到不安",
    "在考试中，我的手会变得冰凉","在考试时，我感到十分紧张",
    "一遇到很难的考试，我就担心自己会不及格","在紧张的考试中，我却会想些与考试无关的事情，注意力集中不起来",
    "在考试时，我会紧张得连平时记得滚瓜烂熟的知识也回忆不起来","在考试时，我会沉浸在空想之中，一时忘了自己是在考试",
    "考试时，我想上厕所的次数比平时多","考试时，即使不热，我也会浑身出汗",
    "在考试时，我紧张得手发僵，写字不流畅","考试时，我经常会看错题目",
    "在进行重要的考试时，我的头就会痛起来","发现剩下的时间来不及做完全部考题，我就急得手足无措、浑身大汗",
    "如果我考了个坏分数，家长或老师会严厉地指责我","在考试后，发现自己会做的题目没有答对时，就十分生自己的气",
    "有几次在重要的考试之后，我腹泻了","我对考试十分厌烦",
    "只要考试不计成绩，我就会喜欢考试","考试不应当像现在这样的紧张状态下进行",
    "不考试，我能学到更多的知识",
]
opts_tai = [
    {"value":0,"label":"D（很不符合）","score":0},
    {"value":1,"label":"C（不太符合）","score":1},
    {"value":2,"label":"B（比较符合）","score":2},
    {"value":3,"label":"A（很符合）","score":3},
]
w("TAI.json",{
    "name":"考试焦虑测验","short_name":"TAI",
    "description":"评估中学生考试焦虑程度的33题量表，含忧虑和情绪两维度。原版由Spielberger CD 1980年编制，中文33题版广泛使用。",
    "applicable_levels":[2,3],"question_count":33,"estimated_mins":10,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,24],"level":"normal","label":"镇定自若","alert":None},
        {"range":[25,49],"level":"mild","label":"轻度焦虑","alert":"yellow"},
        {"range":[50,74],"level":"moderate","label":"中度焦虑","alert":"orange"},
        {"range":[75,99],"level":"severe","label":"重度焦虑","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":tai_texts[i],"question_type":"likert",
         "options":opts_tai,"reverse_score":False,"subscale_key":None,"is_alert_item":False}
        for i in range(33)
    ]
})

# ═══ Rosenberg SES 自尊量表 ═══
ses_items = [
    (1,"我觉得我是一个有价值的人，至少与其他人不相上下",False),
    (2,"我觉得我有很多优点",False),
    (3,"总体来说，我倾向于认为自己是失败者",True),
    (4,"我有能力和别人一样做好大多数事情",False),
    (5,"我觉得我没有什么值得自豪的地方",True),
    (6,"我对自己有良好的态度",False),
    (7,"总体上我对自己满意",False),
    (8,"我希望我能有更多的自尊",True),
    (9,"我有时觉得自己无用",True),
    (10,"我有时认为自己一点都不好",True),
]
opts_ses_fwd = [{"value":i+1,"label":l,"score":i+1} for i,l in enumerate(["非常不符合","不符合","符合","非常符合"])]
opts_ses_rev = [{"value":i+1,"label":l,"score":4-i} for i,l in enumerate(["非常不符合","不符合","符合","非常符合"])]
w("SES.json",{
    "name":"罗森伯格自尊量表","short_name":"SES",
    "description":"评估整体自尊水平的10题量表，公共领域免费使用。由Rosenberg M 1965年编制，α良好。",
    "applicable_levels":[1,2,3],"question_count":10,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[3,5,8,9,10],"subscales":{}},
    "result_levels":[
        {"range":[10,19],"level":"low","label":"低自尊","alert":"yellow"},
        {"range":[20,29],"level":"medium","label":"中等自尊","alert":None},
        {"range":[30,40],"level":"high","label":"高自尊","alert":None},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_ses_rev if rev else opts_ses_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in ses_items
    ]
})

# ═══ PTGI 创伤后成长量表 ═══
ptgi_texts = [
    "我培养/发展了新的兴趣","我改变了生命中重要事物的先后顺序",
    "我对自己的生命价值有了更多的欣赏/认识","我有更多依靠自己的感觉",
    "我对精神事物有了更好的理解","我明白当我遇到困难时可以依靠他人",
    "我确立了新的生命之路","我有与他人更亲近的感觉",
    "我更愿意表达我的情感","我知道我能更好地处理困难",
    "我能以我的生命做更好的事情","我更能接受任何事情的最后结果",
    "我能更好地珍惜每一天","这次事件给我带来了新的机会",
    "我对他人有了更多的同情","我花更多精力在人际关系上",
    "对需要改变的事物，我更倾向于去改变它","我发现自己比想象中的更强",
    "我对人世间如此美好的体会更深了","我更接受自己需要他人",
]
ptgi_subscales = {
    "life_appreciation":[2,3,7,11,13,17,19],
    "personal_strength":[4,10,12,16],
    "new_possibilities":[1,5,14,15,18],
    "relating_others":[6,8,9,20],
}
item_sub_ptgi = {}
for sub, items in ptgi_subscales.items():
    for i in items:
        item_sub_ptgi[i] = sub
opts_ptgi = [{"value":i,"label":l,"score":i} for i,l in enumerate(
    ["完全没有","极少","有一些","中等程度","相当多","非常多"])]
w("PTGI.json",{
    "name":"创伤后成长量表","short_name":"PTGI",
    "description":"评估经历创伤性事件后积极心理变化的20题量表，总分0-100分。由Tedeschi RG & Calhoun LG 1996年编制，汪际等中文版，α=0.90。",
    "applicable_levels":[2,3],"question_count":20,"estimated_mins":8,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "subscales":ptgi_subscales,
        "subscale_labels":{
            "life_appreciation":"人生感悟","personal_strength":"个人力量",
            "new_possibilities":"新的可能性","relating_others":"与他人关系"
        }
    },
    "result_levels":[
        {"range":[0,20],"level":"low","label":"创伤后成长较少","alert":None},
        {"range":[21,50],"level":"moderate","label":"有一定创伤后成长","alert":None},
        {"range":[51,100],"level":"high","label":"明显创伤后成长","alert":None},
    ],
    "alert_rules":{"item_rules":[]},"is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":ptgi_texts[i],"question_type":"likert",
         "options":opts_ptgi,"reverse_score":False,"subscale_key":item_sub_ptgi.get(i+1),"is_alert_item":False}
        for i in range(20)
    ]
})

print("Batch 5 done: SASC, SAS-A, MSPSS, PSQI, RRS, TAI, SES, PTGI")
