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


