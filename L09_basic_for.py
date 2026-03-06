# range()
for i in range(10):
	print(i)
else: 
	print()

for i in range(20, 30):
	print(i)
else: 
	print()

for i in range(0, 10 ,3):
	print(i)
else: 
	print()

# 九九乘法表
for i in range(1, 10):
	for j in range (1, i + 1):
		print(f"{j} x {i} = {i * j}", end = "\t")
	print()


# 猜数字游戏
import random
print("====== 猜数字游戏 ======")
random_num = random.randint(1, 100)
while True:
	num = int(input("请输入一个数字(1-100)："))
	if random_num > num :
		print("猜小了~")
		continue
	elif random_num < num:
		print("猜大了~")
		continue
	else:
		print("恭喜猜对了~")
		break