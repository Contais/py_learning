print("====== 字符串定义 start ======")
str_01 = 'I\'ve been to Shenzhen.'
print(str_01)

str_02 = "I'm staying at home now."
print(str_02)

str_03 = """
    line_01
    line_02
"""
print(str_03)
print("====== 字符串定义 end ======")
print()

print("====== 字符串拼接 start ======")
sw_slogen_01 = "投资汕尾 " "顺风顺水"
print(sw_slogen_01)
sw_slogen_02 = "好海水 " + "在汕尾"
print(sw_slogen_02)
print("====== 字符串拼接 end ======")
print()

print("====== 字符串格式化 start ======")
name = "yike"
age = 2
# %格式化1: "%s" % 变量
print("my name is %s" % name)
# %格式化2: "%s..%s" % (变量1, 变量2)
print("my name is %s, my age is %s" % (name, age))
# f格式化: f"内容{变量/表达式}"
print(f"my name is {name}, my age is {age}")
print("====== 字符串格式化 end ======")
print()