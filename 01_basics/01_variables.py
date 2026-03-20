print(100)
print(0.633)
print(True)
# print(true) 错误的写法 bool类型: True或False首字母大写
print(False)
print("Hello Python.")
print(None)

year = 2026
print("年份: " + str(year))

# 练习：a=100,b=200,c=300;将a、b、c的值分别赋值给c、a、b
a = 100
b = 200
c = 300
print("====== exchange start ======")
print("before: a = " + str(a))
print("before: b = " + str(b))
print("before: c = " + str(c))
d = a
a = c
c = b
b = d
print("====== exchange end ======")
print("after: a = " + str(a))
print("after: b = " + str(b))
print("after: c = " + str(c))