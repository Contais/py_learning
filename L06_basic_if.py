"""
案例：
输入三角形的三条边，判定该三角形是等腰三角形、等边三角形、普通三角形、不构成三角形
"""
a = float(input("请输入三角形的第一条边长a = "))
b = float(input("请输入三角形的第二条边长b = "))
c = float(input("请输入三角形的第三条边长c = "))

if a + b > c and a + c > b and b + c > a:
	# pass
	if a == b and a == c:
		print("等边三角形")
	elif a == b or a == c or b == c:
		print("等腰三角形")
	else:
		print("普通三角形")	
else:
	print("不构成三角形")