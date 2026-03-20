import json, os
OUT = "/workspace/json_export/students"
def w(fn, d):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Written: {fn}")

# ═══════════════════════════════════════════════
# MHT (100题)
# ═══════════════════════════════════════════════
mht_subscales = {
    "validity":[82,84,86,88,90,92,94,96,98,100],
    "learning_anxiety":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "social_anxiety":[16,17,18,19,20,21,22,23,24,25],
    "loneliness":[26,27,28,29,30,31,32,33,34,35],
    "self_blame":[36,37,38,39,40,41,42,43,44,45],
    "over_sensitivity":[46,47,48,49,50,51,52,53,54,55],
    "physical_symptoms":[56,57,58,59,60,61,62,63,64,65,66,67,68,69,70],
    "phobia":[71,72,73,74,75,76,77,78,79,80],
    "impulsivity":[81,83,85,87,89,91,93,95,97,99],
}
item_sub = {}
for sub, items in mht_subscales.items():
    for i in items:
        item_sub[i] = sub

mht_texts = {
    1:"你夜里睡觉时，是否总想着明天的功课？",2:"老师在向全班提问时，你是否会觉得是在提问自己而感到不安？",
    3:"你是否一听说要考试心里就紧张？",4:"你考试成绩不好时，心里是否感到不快？",
    5:"你学习成绩不好时，是否总是提心吊胆？",6:"考试时，当你想不起来原先掌握的知识时，你是否会感到焦虑？",
    7:"你考试后，在没有知道成绩之前，是否总是放心不下？",8:"你是否一遇到考试，就担心会考坏？",
    9:"你是否希望考试能顺利通过？",10:"你在没有完成任务之前，是否总担心完不成任务？",
    11:"你当着大家的面朗读课文时，是否总是怕读错？",12:"你是否认为学校里得到的学习成绩总是不大可靠的？",
    13:"你是否认为你比别人更担心学习？",14:"你是否做过考试考坏了的梦？",
    15:"你是否做过学习成绩不好时，受到爸爸妈妈或老师训斥的梦？",
    16:"你是否经常觉得有同学在背后说你的坏话？",17:"你受到父母批评后，是否总是想不开，放在心上？",
    18:"你在游戏或与别人的竞争中输给了对方，是否就不想再干了？",19:"人家在背后议论你，你是否感到讨厌？",
    20:"你在大家面前或被老师提问时，是否会脸红？",21:"你是否很担心叫你担任班干部？",
    22:"你是否总是觉得好像有人在注意你？",23:"在工作或学习时，如果有人注意你，你心里是否紧张？",
    24:"你受到批评时，心情是否不愉快？",25:"你受到老师批评时，心里是否总是不安？",
    26:"同学们在笑时，你是否也不会笑？",27:"你是否觉得到同学家里去玩不如在自己家里玩？",
    28:"你和大家在一起时，是否也觉得自己是孤单的一个人？",29:"你是否觉得和同学一起玩，不如自己一个人玩？",
    30:"同学们在交谈时，你是否不想加入？",31:"当你和大家在一起时，是否觉得自己是多余的人？",
    32:"你是否讨厌参加运动会和文艺演出会？",33:"你的朋友是否很少？",
    34:"你是否不喜欢同别人谈话？",35:"在人多的地方，你是否觉得很怕？",
    36:"你在体育比赛输了时，心里是否一直认为自己不好？",37:"你受到批评后，是否总认为是自己不好？",
    38:"别人笑你的时候，你是否会认为是自己做错了什么事？",39:"你学习成绩不好时，是否总是认为是自己不用功的缘故？",
    40:"你失败时候，是否总是认为是自己的责任？",41:"大家受到责备时，你是否认为主要是自己的过错？",
    42:"你在体育比赛时，是否一出错就特别留神？",43:"碰到为难的事情时，你是否认为自己难以应付？",
    44:"你是否有时会后悔，那件事不做就好了？",45:"你和同学吵架以后，是否总是认为是自己的错？",
    46:"你心里是否总想为班级做点好事？",47:"你学习的时候，思想是否经常开小差？",
    48:"你把东西借给别人时，是否担心别人会把东西弄坏？",49:"碰到不顺利的事情时，你心里是否很烦躁？",
    50:"你是否非常担心家里有人生病或死去？",51:"你是否在梦里见到过死去的人？",
    52:"你对收音机和汽车的声音是否特别敏感？",53:"你心里是否总觉得好像有什么事没有做好？",
    54:"你是否担心会发生什么意外的事？",55:"你在决定要做什么事时，是否总是犹豫不决？",
    56:"你手上是否经常出汗？",57:"你害羞时是否会脸红？",58:"你是否经常头痛？",
    59:"你被老师提问时，心里是否总是很紧张？",60:"你没有参加运动，心脏是否经常噗通噗通地跳？",
    61:"你是否很容易疲劳？",62:"你是否很不愿吃药？",63:"夜里你是否很难入睡？",
    64:"你是否总觉得身体好像有什么毛病？",65:"你是否经常认为自己的体型和面孔比别人难看？",
    66:"你是否经常觉得肠胃不好？",67:"你是否经常咬指甲？",68:"你是否舔手指头？",
    69:"你是否经常感到呼吸困难？",70:"你去厕所的次数是否比别人多？",
    71:"你是否很怕到高的地方去？",72:"你是否害怕很多东西？",73:"你是否经常做噩梦？",
    74:"你胆子是否很小？",75:"夜里，你是否很怕一个人在房间里睡觉？",
    76:"你乘车穿过隧道或路过高桥时，是否很怕？",77:"你是否喜欢整夜开着灯睡觉？",
    78:"你听到打雷声是否非常害怕？",79:"你是否非常害怕黑暗？",80:"你是否经常感到后面有人跟着你？",
    81:"你是否经常生气？",82:"你是否不想得到好的成绩？",83:"你是否经常会突然想哭？",
    84:"你以前是否说过谎话？",85:"你有时是否会觉得，还是死了好？",
    86:"你是否一次也没有失约过？",87:"你是否经常想大声喊叫？",88:"你是否不愿说出别人不让说的事？",
    89:"你有时是否想过自己一个人到遥远的地方去？",90:"你是否总是很有礼貌？",
    91:"你被人说了坏话，是否想立即采取报复行动？",92:"老师或父母说的话，你是否都照办？",
    93:"你心里不开心，是否会乱丢、乱砸东西？",94:"你是否发过怒？",
    95:"你想要的东西，是否就一定要拿到手？",96:"你不喜欢的课，老师提前下课，你是否会感到特别高兴？",
    97:"你是否经常想从高的地方跳下来？",98:"你是否无论对谁都很亲热？",
    99:"你是否会经常急躁得坐立不安？",100:"对不认识的人，你是否会都喜欢？",
}
opts_mht = [
    {"value":0,"label":"否（不是）","score":0},
    {"value":1,"label":"是","score":1},
]
w("MHT.json",{
    "name":"心理健康诊断测验","short_name":"MHT",
    "description":"综合评估中小学生8类焦虑倾向的100题筛查量表，含效度量表。由华东师范大学周步成教授根据日本铃木清等人测验修订，适用于小学四年级至高中。",
    "applicable_levels":[1,2,3],"question_count":100,"estimated_mins":25,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[],
        "validity_scale":mht_subscales["validity"],
        "validity_rule":"如效度量表得分>7，答卷无效",
        "subscales":{k:v for k,v in mht_subscales.items() if k!="validity"},
        "subscale_labels":{
            "learning_anxiety":"学习焦虑","social_anxiety":"对人焦虑","loneliness":"孤独倾向",
            "self_blame":"自责倾向","over_sensitivity":"过敏倾向","physical_symptoms":"身体症状",
            "phobia":"恐怖倾向","impulsivity":"冲动倾向"
        }
    },
    "result_levels":[
        {"range":[0,44],"level":"normal","label":"心理健康良好","alert":None,"note":"总分"},
        {"range":[45,64],"level":"mild","label":"有一定问题倾向","alert":"yellow","note":"总分"},
        {"range":[65,100],"level":"severe","label":"存在明显心理障碍","alert":"red","note":"总分"},
    ],
    "alert_rules":{
        "item_rules":[
            {"question_no":85,"condition":"value == 1","alert":"red","reason":"感到还是死了好"},
            {"question_no":97,"condition":"value == 1","alert":"red","reason":"有从高处跳下的想法"},
        ],
        "subscale_rules":[
            {"subscale_key":"learning_anxiety","condition":"score >= 8","alert":"orange","reason":"学习焦虑偏高"},
            {"subscale_key":"impulsivity","condition":"score >= 8","alert":"orange","reason":"冲动倾向偏高"},
        ],
        "validity_rule":{"validity_key":"validity","condition":"score > 7","alert":"gray","reason":"答卷可能无效"}
    },
    "is_active":True,
    "questions":[
        {"question_no":i,"question_text":mht_texts[i],"question_type":"single",
         "options":opts_mht,"reverse_score":False,"subscale_key":item_sub.get(i),"is_alert_item":(i in [85,97])}
        for i in range(1,101)
    ]
})

# ═══════════════════════════════════════════════
# MSSMHS / MMHI-60 (60题)
# ═══════════════════════════════════════════════
mmhi_subscales = {
    "obsessive":    [3,10,12,22,23,31],
    "paranoid":     [11,20,24,26,47,49],
    "hostile":      [19,21,25,52,54,58],
    "interpersonal":[4,17,18,33,45,51],
    "depression":   [5,13,14,16,44,57],
    "anxiety":      [6,15,34,36,43,46],
    "study_stress": [1,7,27,38,40,55],
    "maladjustment":[8,29,30,39,41,42],
    "emotional":    [2,9,32,35,50,53],
    "imbalance":    [28,37,54,56,60],
}
mmhi_texts = [
    "我不喜欢参加学校的课外活动","我心情时好时坏","做作业必须反复检查","感到人们对我不友好，不喜欢我",
    "我感到苦闷","我感到紧张或容易紧张","我学习劲头时高时低","我对现在的学校生活感到不适应",
    "我看不惯现在的社会风气","为保证正确，做事必须做得很慢","我的想法总与别人不一样","总担心自己的衣服是否整齐",
    "容易哭泣","我感到前途没有希望","我感到坐立不安，心神不定","经常责怪自己",
    "当别人看我或议论我时感到不自在","感到别人不理解我，不同情我","我常发脾气，想控制但控制不住","觉得别人想占我的便宜",
    "大叫或摔东西","总在想一些不必要的事情","必须反复洗手或反复数数","总感到有人在背后议论我",
    "时常与人争论、抬杠","我觉得大多数人都不可信任","我对做作业的热情忽高忽低","同学考试成绩比我高，我感到难过",
    "我不适应老师的教学方法","老师对我不公平","我感到学习负担很重","我对同学忽冷忽热",
    "上课时总担心老师会提问自己","我无缘无故地突然感到害怕","我对老师时而亲近，时而疏远","一听说要考试，心里就感到紧张",
    "别的同学穿戴比我好、有钱，感到不舒服","我讨厌做作业","家里的环境干扰我的学习","我讨厌上学",
    "我不喜欢班里的风气","父母对我不公平","感到心里烦躁","我常常无精打采，提不起劲来",
    "我的感情容易受到别人的伤害","觉得心里不踏实","别人对我的表现评价不当","明知担心没有用，但总害怕考不好",
    "总觉得别人在跟我作对","我容易激动和烦恼","同异性在一起时，感到害羞不自在","有想伤害他人或打人的冲动",
    "我对父母时而亲热时而冷淡","我对比我强的同学并不服气","我讨厌考试","心里总觉得有事",
    "经常有自杀的念头","有想摔东西的冲动","要求别人十全十美","同学考试成绩比我高，但能力并不比我强",
]

item_sub2 = {}
for sub, items in mmhi_subscales.items():
    for i in items:
        item_sub2[i] = sub

opts_5 = [
    {"value":1,"label":"无（从无此感觉）","score":1},
    {"value":2,"label":"轻度（偶尔有此感觉）","score":2},
    {"value":3,"label":"中度（有时有此感觉）","score":3},
    {"value":4,"label":"偏重（经常有此感觉）","score":4},
    {"value":5,"label":"严重（几乎总是有此感觉）","score":5},
]
w("MSSMHS.json",{
    "name":"中国中学生心理健康量表","short_name":"MSSMHS",
    "description":"评估中学生10个心理健康维度的60题量表，每维度6题，取均分。由中科院王极盛教授编制，1997年发表。",
    "applicable_levels":[2,3],"question_count":60,"estimated_mins":15,
    "scoring_type":"subscale",
    "scoring_rule":{
        "method":"formula",
        "formula":"subscale_mean = subscale_sum / 6; total_mean = all_sum / 60",
        "reverse_items":[],
        "subscales":mmhi_subscales,
        "subscale_labels":{
            "obsessive":"强迫症状","paranoid":"偏执","hostile":"敌对","interpersonal":"人际关系敏感",
            "depression":"抑郁","anxiety":"焦虑","study_stress":"学习压力感","maladjustment":"适应不良",
            "emotional":"情绪不稳定","imbalance":"心理不平衡"
        }
    },
    "result_levels":[
        {"range":[1.0,1.99],"level":"normal","label":"正常","alert":None,"note":"分量表均分"},
        {"range":[2.0,2.99],"level":"mild","label":"轻度问题","alert":"yellow","note":"分量表均分"},
        {"range":[3.0,3.99],"level":"moderate","label":"中度问题","alert":"orange","note":"分量表均分"},
        {"range":[4.0,4.99],"level":"severe","label":"较重问题","alert":"red","note":"分量表均分"},
        {"range":[5.0,5.0],"level":"extremely_severe","label":"严重问题","alert":"red","note":"分量表均分"},
    ],
    "alert_rules":{
        "item_rules":[
            {"question_no":57,"condition":"value >= 2","alert":"red","reason":"经常有自杀的念头"},
            {"question_no":52,"condition":"value >= 4","alert":"orange","reason":"有想伤害他人或打人的冲动"},
        ]
    },
    "is_active":True,
    "questions":[
        {"question_no":i+1,"question_text":mmhi_texts[i],"question_type":"likert",
         "options":opts_5,"reverse_score":False,"subscale_key":item_sub2.get(i+1),"is_alert_item":(i+1 in [57,52])}
        for i in range(60)
    ]
})

# ═══════════════════════════════════════════════
# SDQ 长处和困难问卷（学生自评版，11岁以上）
# ═══════════════════════════════════════════════
sdq_items = [
    (1,"体贴别人的感受","prosocial",False),
    (2,"坐立不安，多动，不能长时间安静","hyperactivity",False),
    (3,"经常头疼、肚子疼或不舒服","emotional",False),
    (4,"愿意和他人分享（食物、游戏等）","prosocial",False),
    (5,"常常发脾气","conduct",False),
    (6,"比较孤僻，倾向于独处","peer",False),
    (7,"总体上乖顺听话，大人让做的事基本能照做","conduct",True),
    (8,"担心很多，经常担忧","emotional",False),
    (9,"如果有人受伤、沮丧或者感到不适，愿意帮助","prosocial",False),
    (10,"不断动来动去，坐立不安","hyperactivity",False),
    (11,"有一个或几个好朋友","peer",True),
    (12,"经常与其他小孩打架，或者欺负他们","conduct",False),
    (13,"经常不开心，情绪低落，或者哭泣","emotional",False),
    (14,"总体上被其他小孩所喜欢","peer",True),
    (15,"容易分心，不能集中注意力","hyperactivity",False),
    (16,"在新环境中感到紧张，容易失去自信","emotional",False),
    (17,"善待年纪比自己小的孩子","prosocial",False),
    (18,"常说谎或者欺骗他人","conduct",False),
    (19,"被其他小孩欺负或虐待","peer",False),
    (20,"经常主动帮助别人","prosocial",False),
    (21,"做事之前先想想","hyperactivity",True),
    (22,"从家里、学校或其他地方偷东西","conduct",False),
    (23,"和大人相处比和小孩相处好","peer",False),
    (24,"有很多害怕的事情，容易感到害怕","emotional",False),
    (25,"能把任务坚持完成，注意力持久","hyperactivity",True),
]
opts_sdq_fwd = [
    {"value":0,"label":"不符合","score":0},
    {"value":1,"label":"有些符合","score":1},
    {"value":2,"label":"完全符合","score":2},
]
opts_sdq_rev = [
    {"value":0,"label":"不符合","score":2},
    {"value":1,"label":"有些符合","score":1},
    {"value":2,"label":"完全符合","score":0},
]
w("SDQ.json",{
    "name":"长处和困难问卷（学生自评版）","short_name":"SDQ",
    "description":"评估11-16岁儿童青少年行为情绪特点的25题量表，兼顾问题与优势。由Goodman R 1997年编制，sdqinfo.org提供简体中文版。",
    "applicable_levels":[2,3],"question_count":25,"estimated_mins":7,
    "scoring_type":"both",
    "scoring_rule":{
        "method":"sum","reverse_items":[7,11,14,21,25],
        "subscales":{
            "emotional":[3,8,13,16,24],
            "conduct":[5,7,12,18,22],
            "hyperactivity":[2,10,15,21,25],
            "peer":[6,11,14,19,23],
            "prosocial":[1,4,9,17,20],
        },
        "note":"困难总分=情绪+品行+多动+同伴（不含亲社会）"
    },
    "result_levels":[
        {"range":[0,13],"level":"normal","label":"正常","alert":None,"note":"困难总分"},
        {"range":[14,16],"level":"borderline","label":"临界状态","alert":"yellow","note":"困难总分"},
        {"range":[17,40],"level":"abnormal","label":"异常","alert":"orange","note":"困难总分"},
    ],
    "alert_rules":{"item_rules":[]},
    "is_active":True,
    "questions":[
        {"question_no":no,"question_text":t,"question_type":"likert",
         "options":opts_sdq_rev if rev else opts_sdq_fwd,"reverse_score":rev,"subscale_key":sub,"is_alert_item":False}
        for no,t,sub,rev in sdq_items
    ]
})

print("Batch 3 (MHT, MSSMHS, SDQ) done")
