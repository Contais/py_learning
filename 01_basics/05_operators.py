# 算术运算符
print("====== 算术运算符 start ======")
num1 = float(input("请输入第一个数字num1: "))
num2 = float(input("请输入第二个数字num2: "))
print("num1 + num2 = ", num1 + num2)
print("num1 - num2 = ", num1 - num2)
print("num1 * num2 = ", num1 * num2)
print("num1 / num2 = ", num1 / num2)
print("num1 // num2 = ", num1 // num2)
print("num1 % num2 = ", num1 % num2)
print("num1 ** num2 = ", num1 ** num2)
print("====== 算术运算符 end ======")
print()

# 赋值运算符
print("====== 赋值运算符 start ======")
num1 += 2
print("num1 += 2 = ", num1)
num1 -= 2
print("num1 -= 2 = ", num1)
num1 *= 2
print("num1 *= 2 = ", num1)
num1 /= 2
print("num1 /= 2 = ", num1)
num1 //= 2
print("num1 //= 2 = ", num1)
num1 %= 2
print("num1 %= 2 = ", num1)
num1 **= 2
print("num1 **= 2 = ", num1)
print("====== 赋值运算符 end ======")
print()

# 逻辑运算符
print("====== 比较运算符 start ======")
x = float(input("请输入第一个数字x: "))
y = float(input("请输入第二个数字y: "))
print("x == y ", x == y)
print("x != y ", x != y)
print("x > y ", x > y)
print("x < y ", x < y)
print("x >= y ", x >= y)
print("x <= y ", x <= y)

print("数值比较：666 == 666 ", 666 == 666)
print("字符串比较：\"666\" == \"666\" ", "666" == "666")
print("字符串&数值比较：\"666\" == 666 ", "666" == 666)
print("====== 比较运算符 end ======")
print()

# 逻辑运算符
print("====== 逻辑运算符 start ======")
num = int(input("请输入一个整数："))
print("该整数在10-20之间?", num >= 10 and num <= 20)
print("该整数在10-20之间?", 10 <= num <= 20)
print("该整数不在10-20之间?", num < 10 or num > 20)
print("not的使用: not True = ", not True)
print("====== 逻辑运算符 end ======")