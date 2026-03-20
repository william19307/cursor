import json, os

OUT = "/workspace/json_export/students"

def w(filename, data):
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written: {filename}")

# ── 通用选项模板 ──────────────────────────────
def opts_phq():  # PHQ-9/GAD-7 四级
    return [
        {"value":0,"label":"完全不会","score":0},
        {"value":1,"label":"几天","score":1},
        {"value":2,"label":"超过一半天数","score":2},
        {"value":3,"label":"几乎每天","score":3},
    ]

def opts_4freq():  # 0-3 频率：从不/有时/经常/总是
    return [
        {"value":0,"label":"从不","score":0},
        {"value":1,"label":"有时","score":1},
        {"value":2,"label":"经常","score":2},
        {"value":3,"label":"总是","score":3},
    ]

def opts_5scale():  # 1-5 Likert
    return [
        {"value":1,"label":"完全不符合","score":1},
        {"value":2,"label":"不太符合","score":2},
        {"value":3,"label":"不确定","score":3},
        {"value":4,"label":"比较符合","score":4},
        {"value":5,"label":"完全符合","score":5},
    ]

def opts_7scale():
    return [
        {"value":1,"label":"完全不同意","score":1},
        {"value":2,"label":"不同意","score":2},
        {"value":3,"label":"有些不同意","score":3},
        {"value":4,"label":"不确定","score":4},
        {"value":5,"label":"有些同意","score":5},
        {"value":6,"label":"同意","score":6},
        {"value":7,"label":"完全同意","score":7},
    ]

def opts_yesno():
    return [
        {"value":0,"label":"否","score":0},
        {"value":1,"label":"是","score":1},
    ]

def opts_4agree():
    return [
        {"value":1,"label":"完全不正确","score":1},
        {"value":2,"label":"有点正确","score":2},
        {"value":3,"label":"多数正确","score":3},
        {"value":4,"label":"完全正确","score":4},
    ]

def opts_grit():
    return [
        {"value":1,"label":"完全不像我","score":1},
        {"value":2,"label":"不太像我","score":2},
        {"value":3,"label":"有点像我","score":3},
        {"value":4,"label":"基本像我","score":4},
        {"value":5,"label":"非常像我","score":5},
    ]

def opts_grit_rev():
    return [
        {"value":1,"label":"完全不像我","score":5},
        {"value":2,"label":"不太像我","score":4},
        {"value":3,"label":"有点像我","score":3},
        {"value":4,"label":"基本像我","score":2},
        {"value":5,"label":"非常像我","score":1},
    ]

def opts_camm():
    return [
        {"value":0,"label":"从不","score":4},
        {"value":1,"label":"很少","score":3},
        {"value":2,"label":"有时","score":2},
        {"value":3,"label":"经常","score":1},
        {"value":4,"label":"总是","score":0},
    ]

# ═══════════════════════════════════════════════
# 1. PHQ-9
# ═══════════════════════════════════════════════
phq9_questions = [
    "做事时提不起劲或没有兴趣",
    "感到心情低落、沮丧或绝望",
    "入睡困难、睡不安稳或睡眠过多",
    "感觉疲倦或没有活力",
    "食欲不振或吃太多",
    "觉得自己很糟糕，或觉得自己很失败，或让自己或家人失望",
    "对事物专注有困难，例如阅读报纸或看电视时不能集中注意力",
    "动作或说话速度缓慢到别人已经觉察，或正好相反——烦躁或坐立不安，动来动去的情况比平时更多",
    "有不如死掉或用某种方式伤害自己的念头",
]

w("PHQ-9.json", {
    "name":"患者健康问卷抑郁量表","short_name":"PHQ-9",
    "description":"用于筛查和评估抑郁症状严重程度的9题自评量表，评估过去两周的症状频率。由Kroenke K等2001年编制，Pfizer官方免费授权使用。",
    "applicable_levels":[2,3],"question_count":9,"estimated_mins":5,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,4],"level":"normal","label":"无抑郁","alert":None},
        {"range":[5,9],"level":"mild","label":"轻微抑郁","alert":"yellow"},
        {"range":[10,14],"level":"moderate","label":"中度抑郁","alert":"orange"},
        {"range":[15,19],"level":"moderately_severe","label":"中重度抑郁","alert":"red"},
        {"range":[20,27],"level":"severe","label":"重度抑郁","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":9,"condition":"value >= 1","alert":"red","reason":"自杀/自伤念头，须立即评估安全性"}
    ]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts_phq(),"reverse_score":False,"subscale_key":None,"is_alert_item":(i==8)}
        for i,t in enumerate(phq9_questions)
    ]
})

# ═══════════════════════════════════════════════
# 2. GAD-7
# ═══════════════════════════════════════════════
gad7_questions = [
    "感觉紧张、焦虑或急切",
    "不能够停止或控制担忧",
    "对各种各样的事情担忧过多",
    "很难放松下来",
    "由于不安而无法静坐",
    "变得容易烦恼或急躁",
    "感到似乎将有可怕的事情发生而害怕",
]
w("GAD-7.json",{
    "name":"广泛性焦虑障碍量表","short_name":"GAD-7",
    "description":"评估广泛性焦虑症状的7题自评量表，评估过去两周的症状频率。由Spitzer RL等2006年编制，Pfizer官方免费授权使用。",
    "applicable_levels":[2,3],"question_count":7,"estimated_mins":3,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[],"subscales":{}},
    "result_levels":[
        {"range":[0,4],"level":"normal","label":"无焦虑","alert":None},
        {"range":[5,9],"level":"mild","label":"轻微焦虑","alert":"yellow"},
        {"range":[10,14],"level":"moderate","label":"中度焦虑","alert":"orange"},
        {"range":[15,21],"level":"severe","label":"重度焦虑","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":t,"question_type":"likert",
         "options":opts_phq(),"reverse_score":False,"subscale_key":None,"is_alert_item":False}
        for i,t in enumerate(gad7_questions)
    ]
})

# ═══════════════════════════════════════════════
# 3. DASS-21
# ═══════════════════════════════════════════════
dass21 = [
    (1,"我发现自己很难安抚下来","stress"),
    (2,"我感到嘴巴干燥","anxiety"),
    (3,"我完全无法感受到积极的感受","depression"),
    (4,"我感到呼吸困难（如呼吸过快、气短）","anxiety"),
    (5,"我发现自己很难开始做事情","depression"),
    (6,"我有过度反应的趋势","stress"),
    (7,"我感到四肢颤抖","anxiety"),
    (8,"我感到很难放松","stress"),
    (9,"我发现自己处于令人担忧的情况中却无法感受到任何情绪","depression"),
    (10,"我觉得我对什么都没有期待","depression"),
    (11,"我发现自己很容易烦躁不安","stress"),
    (12,"我感到需要大量精力才能完成任务","stress"),
    (13,"我感到悲伤和沮丧","depression"),
    (14,"我发现对不得不等待的情况越来越没有耐心","stress"),
    (15,"我感到头晕目眩","anxiety"),
    (16,"我感到失去了做任何事情的热情","depression"),
    (17,"我感到自己一点价值都没有","depression"),
    (18,"我发现自己很容易烦恼","stress"),
    (19,"我感到心跳加速（非体力活动引起）","anxiety"),
    (20,"我无缘无故地感到害怕","anxiety"),
    (21,"我感到生活没有任何意义","depression"),
]
opts_dass = [
    {"value":0,"label":"根本不符合我的情况","score":0},
    {"value":1,"label":"偶尔有","score":1},
    {"value":2,"label":"相当符合，有相当一段时间有","score":2},
    {"value":3,"label":"非常符合，大多数时间都有","score":3},
]
w("DASS-21.json",{
    "name":"抑郁-焦虑-压力量表21项","short_name":"DASS-21",
    "description":"评估抑郁、焦虑、压力三维度的21题自评量表，评估过去一周的状态。由Lovibond & Lovibond 1995年编制，澳大利亚新南威尔士大学官方免费提供。",
    "applicable_levels":[2,3],"question_count":21,"estimated_mins":8,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"sum",
        "reverse_items":[],
        "note":"各分量表原始分×2换算为等量分后对照临界值",
        "subscales":{
            "depression":[3,5,10,13,16,17,21],
            "anxiety":[2,4,7,9,15,19,20],
            "stress":[1,6,8,11,12,14,18]
        }
    },
    "result_levels":[
        {"subscale":"depression","range":[0,9],"level":"normal","label":"正常","alert":None},
        {"subscale":"depression","range":[10,13],"level":"mild","label":"轻度抑郁","alert":"yellow"},
        {"subscale":"depression","range":[14,20],"level":"moderate","label":"中度抑郁","alert":"orange"},
        {"subscale":"depression","range":[21,27],"level":"severe","label":"重度抑郁","alert":"red"},
        {"subscale":"depression","range":[28,42],"level":"extremely_severe","label":"极重度抑郁","alert":"red"},
        {"subscale":"anxiety","range":[0,7],"level":"normal","label":"正常","alert":None},
        {"subscale":"anxiety","range":[8,9],"level":"mild","label":"轻度焦虑","alert":"yellow"},
        {"subscale":"anxiety","range":[10,14],"level":"moderate","label":"中度焦虑","alert":"orange"},
        {"subscale":"anxiety","range":[15,19],"level":"severe","label":"重度焦虑","alert":"red"},
        {"subscale":"anxiety","range":[20,42],"level":"extremely_severe","label":"极重度焦虑","alert":"red"},
        {"subscale":"stress","range":[0,14],"level":"normal","label":"正常","alert":None},
        {"subscale":"stress","range":[15,18],"level":"mild","label":"轻度压力","alert":"yellow"},
        {"subscale":"stress","range":[19,25],"level":"moderate","label":"中度压力","alert":"orange"},
        {"subscale":"stress","range":[26,33],"level":"severe","label":"重度压力","alert":"red"},
        {"subscale":"stress","range":[34,42],"level":"extremely_severe","label":"极重度压力","alert":"red"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_dass,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub in dass21
    ]
})

# ═══════════════════════════════════════════════
# 4. SAS 焦虑自评量表
# ═══════════════════════════════════════════════
sas_items = [
    (1,"我觉得比平时容易紧张和着急（焦虑）",False),
    (2,"我无缘无故地感到害怕",False),
    (3,"我容易心里烦乱或觉得惊恐",False),
    (4,"我觉得我可能将要发疯",False),
    (5,"我觉得一切都很好，也不会发生什么不幸",True),
    (6,"我手脚发抖打颤",False),
    (7,"我因为头痛、颈痛和背痛而苦恼",False),
    (8,"我感到容易衰弱和疲乏",False),
    (9,"我觉得心平气和，并且容易安静坐着",True),
    (10,"我觉得心跳得很快",False),
    (11,"我因一阵阵头晕而苦恼",False),
    (12,"我有过晕倒发作或觉得要晕倒似的",False),
    (13,"我呼气吸气都感到很容易",True),
    (14,"我手脚麻木和刺痛",False),
    (15,"我因胃痛和消化不良而苦恼",False),
    (16,"我常常要小便",False),
    (17,"我的手常常是干燥温暖的",True),
    (18,"我脸红发热",False),
    (19,"我容易入睡并且一夜睡得很好",True),
    (20,"我做恶梦",False),
]
opts_sas_fwd = [
    {"value":1,"label":"没有或很少时间","score":1},
    {"value":2,"label":"有时","score":2},
    {"value":3,"label":"大部分时间","score":3},
    {"value":4,"label":"绝大部分或全部时间","score":4},
]
opts_sas_rev = [
    {"value":1,"label":"没有或很少时间","score":4},
    {"value":2,"label":"有时","score":3},
    {"value":3,"label":"大部分时间","score":2},
    {"value":4,"label":"绝大部分或全部时间","score":1},
]
w("SAS.json",{
    "name":"焦虑自评量表","short_name":"SAS",
    "description":"评估最近一周焦虑症状严重程度的20题自评量表。由Zung WK 1971年编制，吴文源中文版。粗分×1.25取整得标准分。",
    "applicable_levels":[3],"question_count":20,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"formula",
        "formula":"standard_score = round(raw_sum * 1.25)",
        "reverse_items":[5,9,13,17,19],
        "subscales":{},
        "note":"粗分为20题得分之和（20-80），标准分=粗分×1.25取整（25-100）"
    },
    "result_levels":[
        {"range":[0,49],"level":"normal","label":"无显著焦虑","alert":None,"note":"标准分"},
        {"range":[50,59],"level":"mild","label":"轻度焦虑","alert":"yellow","note":"标准分"},
        {"range":[60,69],"level":"moderate","label":"中度焦虑","alert":"orange","note":"标准分"},
        {"range":[70,100],"level":"severe","label":"重度焦虑","alert":"red","note":"标准分"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_sas_rev if rev else opts_sas_fwd,"reverse_score":rev,"subscale_key":None,"is_alert_item":False}
        for no,t,rev in sas_items
    ]
})

# ═══════════════════════════════════════════════
# 5. SDS 抑郁自评量表
# ═══════════════════════════════════════════════
sds_items = [
    (1,"我觉得闷闷不乐，情绪低沉",False),
    (2,"我觉得一天之中早晨最好",True),
    (3,"我一阵阵哭出来或觉得想哭",False),
    (4,"我晚上睡眠不好",False),
    (5,"我吃得跟平常一样多",True),
    (6,"我与异性密切接触时和以往一样感到愉快",True),
    (7,"我发觉我的体重在下降",False),
    (8,"我有便秘的苦恼",False),
    (9,"我心跳比平常快",False),
    (10,"我无缘无故地感到疲乏",False),
    (11,"我的头脑跟平常一样清楚",True),
    (12,"我觉得经常做的事情并没有困难",True),
    (13,"我觉得不安而平静不下来",False),
    (14,"我对将来抱有希望",True),
    (15,"我比平常容易生气激动",False),
    (16,"我觉得做出决定是容易的",True),
    (17,"我觉得自己是个有用的人，有人需要我",True),
    (18,"我的生活过得很有意思",True),
    (19,"我认为如果我死了别人会生活得更好",False),
    (20,"平常感兴趣的事我仍然照样感兴趣",True),
]
w("SDS.json",{
    "name":"抑郁自评量表","short_name":"SDS",
    "description":"评估最近一周抑郁症状严重程度的20题自评量表。由Zung WK 1965年编制，吴文源中文版。粗分×1.25取整得标准分。",
    "applicable_levels":[3],"question_count":20,"estimated_mins":8,
    "scoring_type":"total",
    "scoring_rule":{
        "method":"formula",
        "formula":"standard_score = round(raw_sum * 1.25)",
        "reverse_items":[2,5,6,11,12,14,16,17,18,20],
        "subscales":{},
        "note":"粗分为20题得分之和（20-80），标准分=粗分×1.25取整（25-100）"
    },
    "result_levels":[
        {"range":[0,49],"level":"normal","label":"无抑郁","alert":None,"note":"标准分"},
        {"range":[50,60],"level":"mild","label":"轻度抑郁","alert":"yellow","note":"标准分"},
        {"range":[61,70],"level":"moderate","label":"中度抑郁","alert":"orange","note":"标准分"},
        {"range":[71,100],"level":"severe","label":"重度抑郁","alert":"red","note":"标准分"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":19,"condition":"value >= 3","alert":"red","reason":"死亡/自杀想法，须立即评估安全性"}
    ]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_sas_rev if rev else opts_sas_fwd,"reverse_score":rev,
         "subscale_key":None,"is_alert_item":(no==19)}
        for no,t,rev in sds_items
    ]
})

print("Batch 1 (PHQ-9, GAD-7, DASS-21, SAS, SDS) done")
