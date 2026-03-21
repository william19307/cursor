import json, os
OUT = "/workspace/json_export/students"
def w(fn, d):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {fn}")

# ═══════════════════════════════════════════════
# SCARED (41题)
# ═══════════════════════════════════════════════
scared_items = [
    (1,"当我感到害怕时，呼吸困难","somatic_panic"),
    (2,"我在学校里头疼","school_phobia"),
    (3,"我不喜欢和不太熟悉的人在一起","social_phobia"),
    (4,"如果我离开家，我就害怕","separation_anxiety"),
    (5,"我担心很多事情","generalized_anxiety"),
    (6,"当我害怕时，我感到恶心","somatic_panic"),
    (7,"我总是担心将会发生什么事情","generalized_anxiety"),
    (8,"当我离开家时，我思念家人","separation_anxiety"),
    (9,"我不知为何总感到害怕","somatic_panic"),
    (10,"见到不太熟悉的人，我就会感到紧张","social_phobia"),
    (11,"我不想去上学","school_phobia"),
    (12,"当我害怕时，我感到自己好像要疯了","somatic_panic"),
    (13,"我担心独自在家睡觉","separation_anxiety"),
    (14,"我担心是否能与别的小朋友一样好","generalized_anxiety"),
    (15,"当我害怕时，我感到好像什么事情都不真实","somatic_panic"),
    (16,"我做梦梦见有关与家人分离的事情","separation_anxiety"),
    (17,"我担心上学","school_phobia"),
    (18,"当我害怕时，我感到心跳加快","somatic_panic"),
    (19,"我会颤抖","somatic_panic"),
    (20,"我做梦梦见有坏事发生在我的父母身上","separation_anxiety"),
    (21,"我担心事情不能很好地实现","generalized_anxiety"),
    (22,"当我害怕时，我感到出汗","somatic_panic"),
    (23,"我是一个担忧者","generalized_anxiety"),
    (24,"我不知道什么原因就会产生很强的害怕感","somatic_panic"),
    (25,"我害怕单独在家","separation_anxiety"),
    (26,"我很难与不熟悉的人交谈","social_phobia"),
    (27,"当我害怕时，我感到胸闷","somatic_panic"),
    (28,"我担心我去上学有什么不好的事情发生在我父母身上","generalized_anxiety"),
    (29,"我不想离开家","separation_anxiety"),
    (30,"当我害怕时，我感到头昏眼花","somatic_panic"),
    (31,"我担心有什么坏事情发生在我的父母身上","separation_anxiety"),
    (32,"我感到羞于见人","social_phobia"),
    (33,"我担心将来会发生的事情","generalized_anxiety"),
    (34,"当我害怕时，我感到恶心或肚子痛","somatic_panic"),
    (35,"我担心自己把事情没有做好","generalized_anxiety"),
    (36,"上学前，我害怕上学","school_phobia"),
    (37,"我担心已经发生的事情","generalized_anxiety"),
    (38,"当我害怕时，我感到头昏","somatic_panic"),
    (39,"当其他孩子在一起笑的时候，如果我认为他们在笑我，我感到很不舒服","social_phobia"),
    (40,"我是一个羞怯的孩子","social_phobia"),
    (41,"在学校或聚会场合逃跑","social_phobia"),
]
opts_scared = [
    {"value":0,"label":"没有此问题","score":0},
    {"value":1,"label":"有时有此问题","score":1},
    {"value":2,"label":"经常有此问题","score":2},
]
subscale_thresholds = {
    "somatic_panic": 7,
    "generalized_anxiety": 9,
    "separation_anxiety": 5,
    "social_phobia": 8,
    "school_phobia": 3,
}
w("SCARED.json",{
    "name":"儿童焦虑情绪障碍筛查表","short_name":"SCARED",
    "description":"筛查6-18岁儿童青少年焦虑相关情绪障碍，含5类焦虑亚型。由Birmaher等1997年编制，苏林雁等2008年中文修订版。",
    "applicable_levels":[1,2,3],"question_count":41,"estimated_mins":10,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum",
        "reverse_items":[],
        "subscales":{
            "somatic_panic":[1,6,9,12,15,18,19,22,24,27,30,34,38],
            "generalized_anxiety":[5,7,14,21,23,28,33,35,37],
            "separation_anxiety":[4,8,13,16,20,25,29,31],
            "social_phobia":[3,10,26,32,39,40,41],
            "school_phobia":[2,11,17,36]
        },
        "subscale_labels":{
            "somatic_panic":"躯体化/惊恐","generalized_anxiety":"广泛性焦虑",
            "separation_anxiety":"分离焦虑","social_phobia":"社交恐怖","school_phobia":"学校恐怖"
        },
        "subscale_thresholds":subscale_thresholds
    },
    "result_levels":[
        {"range":[0,22],"level":"normal","label":"无明显焦虑","alert":None,"note":"8-11岁总分阈值23，12-18岁男22/女24"},
        {"range":[23,82],"level":"positive","label":"焦虑阳性","alert":"orange","note":"需进一步评估"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_scared,"reverse_score":False,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub in scared_items
    ]
})

# ═══════════════════════════════════════════════
# CDI 儿童抑郁量表 (27题，每题三选一)
# ═══════════════════════════════════════════════
cdi_items = [
    (1,"悲伤情绪",[("偶尔感到难过",0),("经常感到难过",1),("总是感到难过",2)],False),
    (2,"对未来的看法",[("对未来不悲观",0),("对未来感到悲观",1),("未来没有希望，只会变得更糟",2)],False),
    (3,"自我评价失败感",[("大多数事情做得很好",0),("许多事情做得不对",1),("做的每件事情都不对",2)],False),
    (4,"失去乐趣",[("有很多乐趣",0),("有一些乐趣",1),("没有任何乐趣",2)],False),
    (5,"自责感",[("大多数时候不坏",0),("有时候很坏",1),("总是很坏",2)],False),
    (6,"对未来担忧",[("有时想到坏事会发生",0),("担忧坏事会发生",1),("确信可怕的事情会发生",2)],False),
    (7,"自我否定",[("喜欢自己",0),("不喜欢自己",1),("讨厌自己",2)],True),
    (8,"自责",[("不觉得自己对任何不好的事情负责",0),("许多不好的事情是自己的错",1),("所有不好的事情都是自己的错",2)],False),
    (9,"自杀意念",[("不想杀死自己",0),("想杀死自己但不会这样做",1),("想杀死自己",2)],False),
    (10,"哭泣",[("偶尔感到哭泣",0),("许多天感到哭泣",1),("每天都感到哭泣",2)],False),
    (11,"烦恼",[("很少令我烦恼",0),("有时令我烦恼",1),("总是令我烦恼",2)],False),
    (12,"社交回避",[("喜欢与他人在一起",0),("经常不喜欢与他人在一起",1),("根本不喜欢与他人在一起",2)],False),
    (13,"对学校的态度",[("喜欢上学",0),("不确定是否喜欢上学",1),("不喜欢上学",2)],True),
    (14,"睡眠",[("睡得很好",0),("有时难以入睡",1),("经常难以入睡",2)],False),
    (15,"疲劳",[("有时感到疲倦",0),("经常感到疲倦",1),("总是感到疲倦",2)],False),
    (16,"孤独",[("大多数时候不感到孤独",0),("有时感到孤独",1),("经常感到孤独",2)],False),
    (17,"郁闷",[("有时不开心",0),("经常不开心",1),("从来没有开心过",2)],False),
    (18,"无聊",[("不感到烦闷",0),("有时感到烦闷",1),("经常感到烦闷",2)],False),
    (19,"食欲",[("胃口很好",0),("胃口有时不好",1),("胃口总是不好",2)],False),
    (20,"身体疼痛",[("身体没有疼痛",0),("有时感到身体疼痛",1),("经常感到身体疼痛",2)],False),
    (21,"孤立无援",[("不感到孤立无援",0),("经常感到孤立无援",1),("总是感到孤立无援",2)],False),
    (22,"自伤想法",[("从来没有想过伤害自己",0),("有时想伤害自己但不会这样做",1),("想伤害自己",2)],False),
    (23,"完成作业",[("照常做作业",0),("做作业比以前难",1),("完全不能做作业",2)],False),
    (24,"学业成绩",[("成绩和以前一样好",0),("成绩没有以前好",1),("在学业上表现很差",2)],False),
    (25,"听话",[("和以前一样听话",0),("不如以前听话",1),("一点都不听话",2)],False),
    (26,"与同伴相处",[("和别的孩子相处融洽",0),("有时相处不好",1),("根本相处不好",2)],False),
    (27,"被照顾感",[("觉得有人照顾我",0),("不确定是否有人照顾我",1),("觉得没有人照顾我",2)],False),
]

def cdi_opts(choices, is_rev):
    opts = []
    for i,(label,score) in enumerate(choices):
        opts.append({"value":i,"label":label,"score":score})
    return opts

w("CDI.json",{
    "name":"儿童抑郁量表","short_name":"CDI",
    "description":"评估7-17岁儿童青少年抑郁症状的27题自评量表，每题从三个陈述中选最符合的。由Kovacs M 1992年编制，中文版学术发表。",
    "applicable_levels":[1,2,3],"question_count":27,"estimated_mins":15,
    "scoring_type":"total",
    "scoring_rule":{"method":"sum","reverse_items":[7,13],"subscales":{}},
    "result_levels":[
        {"range":[0,12],"level":"normal","label":"无抑郁症状","alert":None,"note":"6-8岁阈值13，9-12岁阈值17，12+阈值19"},
        {"range":[13,19],"level":"mild","label":"轻度抑郁倾向","alert":"yellow"},
        {"range":[20,29],"level":"moderate","label":"中度抑郁倾向","alert":"orange"},
        {"range":[30,54],"level":"severe","label":"重度抑郁倾向","alert":"red"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":9,"condition":"value >= 1","alert":"red","reason":"自杀意念题"},
        {"question_no":22,"condition":"value >= 1","alert":"red","reason":"自伤想法题"},
    ]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":text,"question_type":"single",
         "options":cdi_opts(choices,rev),"reverse_score":rev,"subscale_key":None,
         "is_alert_item":(no in [9,22])}
        for no,text,choices,rev in cdi_items
    ]
})

# ═══════════════════════════════════════════════
# SCL-90 症状自评量表
# ═══════════════════════════════════════════════
scl90_subscales = {
    "somatization":[1,4,12,27,40,42,48,49,52,53,56,58],
    "obsessive_compulsive":[3,9,10,28,38,45,46,51,55,65],
    "interpersonal_sensitivity":[6,21,34,36,37,41,61,69,73],
    "depression":[5,14,15,20,22,26,29,30,31,32,54,71,79],
    "anxiety":[2,17,23,33,39,57,72,78,80,86],
    "hostility":[11,24,63,67,74,81],
    "phobic_anxiety":[13,25,47,50,70,75,82],
    "paranoid_ideation":[8,18,43,68,76,83],
    "psychoticism":[7,16,35,62,77,84,85,87,88,90],
    "additional":[19,44,59,60,64,66,89],
}
scl90_texts = [
    "头痛","神经过敏，心中不踏实","头脑中有不必要的想法或字句盘旋","头昏或昏倒",
    "对异性的兴趣减退","对旁人责备求全","感到别人能控制您的思想","责怪别人制造麻烦",
    "忘性大","担心自己的衣饰整齐及仪态的端正","容易烦恼和激动","胸痛",
    "害怕空旷的场所或街道","感到自己的精力下降，活动减慢","想结束自己的生命","听到旁人听不到的声音",
    "发抖","感到大多数人都不可信任","胃口差","容易哭泣",
    "同异性相处时感到害羞不自在","感到受骗、中了圈套或有人想抓您","无缘无故地突然感到害怕","自己不能控制地大发脾气",
    "怕单独出门","经常责怪自己","腰痛","感到难以完成任务",
    "感到孤独","感到苦闷","过分担忧","对事物不感兴趣",
    "感到害怕","您的感情容易受到伤害","旁人能知道您的私下想法","感到别人不理解您、不同情您",
    "感到人们对您不友好，不喜欢您","做事必须做得很慢以保证做得正确","心跳得很厉害","恶心或胃部不舒服",
    "感到比不上他人","肌肉酸痛","感到有人在监视您、谈论您","难以入睡",
    "做事必须反复检查","难以做出决定","怕乘电车、公共汽车、地铁或火车","呼吸有困难",
    "一阵阵发冷或发热","因为感到害怕而避开某些东西、场合或活动","脑子变空了","身体发麻或刺痛",
    "喉咙有梗塞感","感到没有前途，没有希望","不能集中注意力","感到身体的某一部分软弱无力",
    "感到紧张或容易紧张","感到手或脚发重","想到死亡的事","吃得太多",
    "当别人看着您或谈论您时感到不自在","有一些不属于您自己的想法","有想打人或伤害他人的冲动","醒得太早",
    "必须反复洗手、点数目或触摸某些东西","睡得不稳不深","有想摔坏或破坏东西的冲动","有一些别人没有的想法或念头",
    "感到对别人神经过敏","在商店或电影院等人多的地方感到不自在","感到任何事情都很困难","一阵阵恐惧或惊恐",
    "感到在公共场合吃东西很不舒服","经常与人争论","单独一人时神经很紧张","别人没有适当地肯定您的成绩时感到烦恼",
    "即使和别人在一起也感到孤单","感到坐立不安心神不定","感到自己没有什么价值","感到熟悉的东西变得陌生或不像是真的",
    "大叫或摔东西","害怕会在公共场合昏倒","感到别人想占您的便宜","为一些有关性的想法而很苦恼",
    "您认为应该因为自己的过错而受到惩罚","感到要赶快把事情做完","感到自己的身体有严重问题","从未感到和其他人很亲近",
    "感到自己有罪","感到自己的脑子有毛病",
]

# build subscale map
item_sub = {}
for sub, items in scl90_subscales.items():
    for i in items:
        item_sub[i] = sub

opts_scl = [
    {"value":1,"label":"没有（从无此感觉）","score":1},
    {"value":2,"label":"轻度","score":2},
    {"value":3,"label":"中度","score":3},
    {"value":4,"label":"相当重","score":4},
    {"value":5,"label":"严重","score":5},
]
w("SCL-90.json",{
    "name":"症状自评量表","short_name":"SCL-90",
    "description":"综合评估9大心理症状维度的90题自评量表，评估最近一周内的心理健康状况。由Derogatis LR 1975年编制，吴文源中文版。",
    "applicable_levels":[3],"question_count":90,"estimated_mins":25,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"formula",
        "formula":"factor_score = subscale_sum / subscale_item_count; total_score = all_items_sum; mean_score = total_score / 90",
        "reverse_items":[],
        "subscales":{k:v for k,v in scl90_subscales.items()},
        "subscale_labels":{
            "somatization":"躯体化","obsessive_compulsive":"强迫症状","interpersonal_sensitivity":"人际关系敏感",
            "depression":"抑郁","anxiety":"焦虑","hostility":"敌对","phobic_anxiety":"恐怖",
            "paranoid_ideation":"偏执","psychoticism":"精神病性","additional":"附加项目"
        }
    },
    "result_levels":[
        {"range":[90,160],"level":"normal","label":"正常","alert":None,"note":"总分"},
        {"range":[160,200],"level":"mild","label":"有一定心理问题","alert":"yellow","note":"总分"},
        {"range":[200,450],"level":"severe","label":"较明显心理障碍","alert":"red","note":"总分"},
    ],
    "alert_rules":{"item_rules":[
        {"question_no":15,"condition":"value >= 3","alert":"red","reason":"结束生命的想法"},
        {"question_no":59,"condition":"value >= 3","alert":"orange","reason":"死亡相关想法"},
    ]},
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":scl90_texts[i],"question_type":"likert",
         "options":opts_scl,"reverse_score":False,"subscale_key":item_sub.get(i+1),"is_alert_item":(i+1 in [15,59])}
        for i in range(90)
    ]
})

print("Batch 2 (SCARED, CDI, SCL-90) done")
