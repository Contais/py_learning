# 导入模块(as 别名) import module (as name) -> 调用语法: 模块名(或别名).方法()
import math
import random as rnd
# 导入模块中的方法 from module import function -> 调用语法: 方法()
from time import localtime, strftime
from random import randint as rdint
from cmath import *

print(math.cos(0))
print(math.sin(pi / 2))
print(rnd.randint(0, 1000))
print(rdint(0, 1000))
print(localtime())
print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

# 针对起别名导致重名的测试
import_rdint = rdint


def rdint(a: int, b: int) -> int:
    return -1


print("自定义rdint的结果：", rdint(0, 10))
print("原random.randint的结果：", import_rdint(0, 10))
