# 方式1：导入包，通过包访问子模块
import my_package

print("包版本：", my_package.__version__)
print("字符串反转：", my_package.str_reverse("Hello World"))
print("判断质数：", my_package.is_prime(7))

# 方式2：导入包并起别名
import my_package as mytools
print("字符串大写：", mytools.str_upper("Hello Python"))
print("数字求和：", mytools.num_sum([1, 2, 3, 4, 5, 6]))

# 方式3：从包中导入指定子模块
from my_package import sub_mod1, sub_mod2
print("子模块调用：", sub_mod1.str_upper("Hello Python"))

# 方式4：直接导入包内的函数（推荐，简化代码）
from my_package import str_reverse
print("直接导入函数：", str_reverse("Hello Python"))
