# 定义
s1 = {"C", "D", "E", "F", "G", "H", "I", "J"}
s2 = set()
print(f"s1 = {s1}, type(s1) = {type(s1)}")
print(f"s2 = {s2}, type(s2) = {type(s2)}")

# 常见方法
# add(): 添加元素
s2.add("C")
print(f"s2 = {s2}")
# remove(): 删除元素
s1.remove("D")
print(f"s1 = {s1}")
# pop(): 随机删除元素并返回
p = s1.pop()
print(f"【s1.pop()】s1 = {s1}; p = {p}")
# clear(): 清空集合
s2.clear()
print(f"【s2.clear()】s2 = {s2}")
s3 = {"A", "D", "E", "W", "G", "Q", "V", "C"}
# difference(): 求两集合的差集
print(f"s1.difference(s3) = {s1.difference(s3)}")
print(f"s1 - s3 = {s1 - s3}")
# union(): 求两集合的并集
print(f"s1.union(s3) = {s1.union(s3)}")
print(f"s1 | s3 = {s1 | s3}")
# intersecting(): 求两集合的交集
print(f"s1.intersection(s3) = {s1.intersection(s3)}")
print(f"s1 & s3 = {s1 & s3}")
# 推导式
s4 = {i for i in s1 if i not in s3}
print(f"{s4}")

# 案例
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# 题目
# 1. 同时选修了法语和艺术的学生
common_french_art = french_set & art_set
print(f"同时选修了法语和艺术的学生: {common_french_art}")
# 2. 同时选修了所有四门课程的学生
common_all = football_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生: {common_all}")
# 3. 选修了足球但没有选修篮球的学生
football_not_basketball = football_set - basketball_set
print(f"选修了足球但没有选修篮球的学生: {football_not_basketball}")
# 4. 统计每一个学生选修的课程数量
all_students = football_set | basketball_set | french_set | art_set
all_lessons = [*football_set, *basketball_set, *french_set, *art_set]
print("统计学生选修课程数量")
for student in all_students:
    print(f"{student}: {all_lessons.count(student)}")
