# 定义
t1 = (2, 3, 5, 66, 33, 66, 12)
print(f"t1 = {t1}; type = {type(t1)}")
# get: 索引访问
print(f"t1[0] = {t1[0]}")
print(f"t1[-1] = {t1[-1]}")

# update: 元组不允许修改操作

# 切片
print(t1[0:5:1])
print(t1[:5:1])
print(t1[:5:])
print(t1[:5])
print(t1[5:6:1])
print(t1[5::1])
print(t1[5::])
print(t1[::2])

# count(): 统计元素在元组出现的个数
print(f"t1.count(66) = {t1.count(66)}")

# index(): 统计元素在元组出现的第一个索引
print(f"t1.index(66) = {t1.index(66)}")

# 定义空元组
# 方式一: t = tuple()
t2 = tuple()
print(f"t2 = {t2}; type = {type(t2)}")
# 方式二: t = ()
t3 = ()
print(f"t3 = {t3}; type = {type(t3)}")

# 定义单元素元组
# 格式: t = (100,)
# 注意如果t = (100), 那么t回事int类型
t4 = (100,)
print(f"t4 = {t4}; type = {type(t4)}")
t5 = (100,)
print(f"t4 = {t5}; type = {type(t5)}")

# 组包(Packing): 将多个值合并到一个容器(元组、列表)中
t6 = (2, 3, 5, 6, 66, 33, 12)
t7 = 2, 3, 5, 6, 66, 33, 12
print(f"t6 = {t6}; type = {type(t6)}")
print(f"t7 = {t7}; type = {type(t7)}")

# 解包(Unpacking): 将容器(元组、列表)解开成独立的元素，分别赋值给多个元素
# 数量要对应
a, b, c, d, e, f, g = t6
print(a, b, c, d, e, f, g)
# 扩展解包(*): 在元组解包时，*表示收集剩余的所有元素->生成列表，以便于进行进一步的处理
first, second, *other, last = t6
print("first, second, *other, last = t6")
print(f"first = {first}")
print(f"second = {second}")
print(f"other = {other}; type = {type(other)}")
print(f"last = {last}")


# 案例一
# 交换元素: x=100,y=200,z=300;将x、y、z的值分别赋值给z、x、y
x = 100
y = 200
z = 300
print("====== exchange start ======")
print(f"before: x = {x}; y = {y}; z = {z}")
z, x, y = x, y, z
print("====== exchange end ======")
print(f"after: x = {x}; y = {y}; z = {z}")


# 案例二
# 统计学生成绩单，并统计相关指标
students = (
	("S001", "王林", 85, 92, 78),
	("S002", "李慕婉", 92, 88, 95),
	("S003", "十三", 78, 85, 82),
	("S004", "曾牛", 88, 79, 91),
	("S005", "周轶", 95, 96, 89),
	("S006", "王卓", 76, 82, 77),
	("S007", "红蝶", 89, 91, 94),
	("S008", "徐立国", 75, 69, 82),
	("S009", "许木", 86, 89, 98),
	("S010", "遁天", 66, 59, 72),
)
print(f"\n学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分\t\t优秀(平均分>90)")
for num, name, chinese, math, english in students:
	total = chinese + math + english
	avg = total / 3
	level = "优" if avg > 90 else ""
	print(f"{num}\t\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}\t\t{level}")
	# {avg:.1f}: 这里表示保留一位小数

# 为了练习元组的使用 这里冗余了一些操作(正确的做法应该是在上面的循环里内统计)
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print("\n科目\t\t最高分\t\t最低分\t\t平均分")
print(f"语文\t\t{max(chinese_scores)}\t\t{min(chinese_scores)}\t\t{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学\t\t{max(math_scores)}\t\t{min(math_scores)}\t\t{sum(math_scores)/len(math_scores)}")
print(f"英语\t\t{max(english_scores)}\t\t{min(english_scores)}\t\t{sum(english_scores)/len(english_scores)}")