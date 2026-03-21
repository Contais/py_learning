# 定义
# key不能重复 必须是不可变类型（str、int、float、tuple）
dict1 = {"Lebron": 23, "Curry": 30, "Kobe": 24, "Harden": 13, "Rose": 1, "Kobe": 8}
print(f"dict1= {dict1}; type: {type(dict1)}")
dict2 = dict()
dict3 = {}
print(f"dict1= {dict2}; type: {type(dict2)}")
print(f"dict2= {dict3}; type: {type(dict3)}")

# 操作
# add
dict1["Wade"] = 3
print(f"dict1= {dict1}")
# delete
dict1.pop("Harden")
print(f"delete: dict1.pop('Harden') dict1= {dict1}")
del dict1["Kobe"]
print(f"delete: del dict1['Kobe'] dict1= {dict1}")
# get
num_lebron = dict1["Lebron"]
print(f"get: dict1[\"Lebron\"] = {num_lebron}")
print(f"get: dict1.get('Rose') = {dict1.get('Rose')}")
print(f"get: dict1.keys()) = {dict1.keys()}")
print(f"get: dict1.values()) = {dict1.values()}")
print(f"get: dict1.items() = {dict1.items()}; type: {type(dict1.items())}")
# update
num_lebron = 6
print(f"update: dict1[\"Lebron\"] = {num_lebron}")

# 遍历
print("====== for start ======")
for k in dict1:
    print(f"{k}: {dict1[k]}")
print("====== for end ======")
print("====== for start ======")
for item in dict1.items():
    print(f"{item[0]} = {item[1]}")
print("====== for end ======")
print("====== for start ======")
for k, v in dict1.items():
    print(f"{k}: {v}")
print("====== for end ======")

# 练习
print("\n\n\n\n\n\n")
print("欢迎使用教务管理系统～")
menu = """########## 教务管理系统 ##########
#         1.添加学生信息         #
#         2.修改学生信息         #
#         3.删除学生信息         #
#         4.查询学生信息         #
#         5.查询所有学生         #
#         6.统计成绩            #
#         7.退出系统            #
################################"""
students = dict()
while True:
    print(menu)
    choice = input("请选择要执行的操作(1-7):")
    match choice:
        case "1":  # 添加学生信息
            num = input("请输入学生学号:")
            if num in students:
                print(f"请勿重复录入(该学生{num}信息已存在教务系统中.)")
                continue
            name = input("请输入学生姓名:")
            score_chinese = float(input("请输入语文成绩:"))
            score_math = float(input("请输入数学成绩:"))
            score_english = float(input("请输入英语成绩:"))
            students[num] = {"name": name, "score_chinese": score_chinese, "score_math": score_math,
                             "score_english": score_english}
            print("添加成功～")
        case "2":  # 修改学生信息
            num = input("请输入需要修改的学生学号:")
            if num not in students:
                print(f"该学生{num}信息暂未录入系统.")
                continue
            name = input("请输入学生姓名:")
            score_chinese = float(input("请输入语文成绩:"))
            score_math = float(input("请输入数学成绩:"))
            score_english = float(input("请输入英语成绩:"))
            students[num] = {"name": name, "score_chinese": score_chinese, "score_math": score_math,
                             "score_english": score_english}
            print("修改成功～")
        case "3":  # 删除学生信息
            num = input("请输入需要删除的学生学号:")
            if num not in students:
                print(f"该学生{num}信息暂未录入系统.")
                continue
            del students[num]
        case "4":  # 查询学生信息
            num = input("请输入需要查询的学生学号:")
            if num not in students:
                print(f"该学生{num}信息暂未录入系统.")
                continue
            student = students[num]
            print(
                f"学号:{num}\t姓名:{student['name']}\t语文:{student['score_chinese']}\t数学:{student['score_math']}\t英语:{student[score_english]}")
        case "5":  # 查询所有学生
            print("学号\t\t姓名\t\t\t语文\t\t\t数学\t\t\t英语")
            for num, info in students.items():
                print(
                    f"{num}\t\t{info['name']}\t\t{info['score_chinese']}\t\t{info['score_math']}\t\t{info['score_english']}")
            pass
        case "6":  # 统计成绩
            student_count = len(students)
            if student_count == 0:
                print("暂无学生信息.")
                continue
            scores_chinese = []
            scores_math = []
            scores_english = []
            for num, info in students.items():
                scores_chinese.append(info['score_chinese'])
                scores_math.append(info['score_math'])
                scores_english.append(info['score_english'])
            # 语文成绩统计
            chinese_max = max(scores_chinese)
            chinese_min = min(scores_chinese)
            chinese_avg = sum(scores_chinese) / student_count
            chinese_max_names = []
            chinese_min_names = []
            for num, info in students.items():
                if chinese_max == info['score_chinese']:
                    chinese_max_names.append(f"{info['name']}({num})")
                if chinese_min == info['score_chinese']:
                    chinese_min_names.append(f"{info['name']}({num})")
            # 数学成绩统计
            math_max = max(scores_math)
            math_min = min(scores_math)
            math_avg = sum(scores_math) / student_count
            math_max_names = []
            math_min_names = []
            for num, info in students.items():
                if math_max == info['score_math']:
                    math_max_names.append(f"{info['name']}({num})")
                if math_min == info['score_math']:
                    math_min_names.append(f"{info['name']}({num})")
            # 英语成绩统计
            english_max = max(scores_english)
            english_min = min(scores_english)
            english_avg = sum(scores_english) / student_count
            english_max_names = []
            english_min_names = []
            for num, info in students.items():
                if english_max == info['score_english']:
                    english_max_names.append(f"{info['name']}({num})")
                if english_min == info['score_english']:
                    english_min_names.append(f"{info['name']}({num})")
            # ---------------------- 输出结果 ----------------------
            print("📊 班级成绩统计：")
            print("语文：")
            print(f"  最高分：{chinese_max} 分（学生：{'、'.join(chinese_max_names)}）")
            print(f"  最低分：{chinese_min} 分（学生：{'、'.join(chinese_min_names)}）")
            print(f"  平均分：{round(chinese_avg, 2)} 分")
            print("数学：")
            print(f"  最高分：{math_max} 分（学生：{'、'.join(math_max_names)}）")
            print(f"  最低分：{math_min} 分（学生：{'、'.join(math_min_names)}）")
            print(f"  平均分：{round(math_avg, 2)} 分")
            print("英语：")
            print(f"  最高分：{english_max} 分（学生：{'、'.join(english_max_names)}）")
            print(f"  最低分：{english_min} 分（学生：{'、'.join(english_min_names)}）")
            print(f"  平均分：{round(english_avg, 2)} 分")
        case "7":
            print("退出系统.")
            break
        case _:
            print("非法操作,请重试～")
    print("返回菜单.\n")
