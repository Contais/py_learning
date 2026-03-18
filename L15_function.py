def circle_area(radius):
    """
    Returns the area of a circle.
    :param radius: 半径
    :return: 面积
    """
    pi = 3.14159
    return round(pi * radius ** 2, 2)


def rectangle_area(length, width):
    """
    Returns the area of a rectangle.
    :param length: 长
    :param width: 宽
    :return: 面积
    """
    return length * width


def triangle_area(bottom, height):
    """
    Returns the area of a triangle.
    :param bottom: 底
    :param height: 高
    :return: 面积
    """
    area = bottom * height / 2
    return area


def rectangle_calculator(length, width):
    """
    Return the area and the perimeter of the rectangle.
    :param length: 长
    :param width: 宽
    :return: 面积,周长
    """
    area = rectangle_area(length, width)
    perimeter = 2 * length + 2 * width
    return area, perimeter


def print_circle_area(radius):
    print(circle_area(radius))


# 没有返回值的函数 如果用参数接收 最终会是None
test = print_circle_area(10)
# 测试方法注释 help()
print(help(rectangle_area))
# 单个返回值的函数调用
print(f"计算圆的面积: {circle_area(10)}")
# 多个返回值的函数调用
area, perimeter = rectangle_calculator(10, 5)
print(f"长方形面积:{area},周长:{perimeter}")


# 嵌套
def function_a():
    print("====== function_a start ======")
    print("====== function_a end ======")


def function_b():
    print("====== function_b start ======")
    function_a()
    print("====== function_b end ======")


def function_c():
    print("====== function_c start ======")
    function_b()
    print("====== function_c end ======")


function_c()

# 变量作用域
print("\n====== 变量作用域 ======")
var_a = 100
var_b = 100
print(f"start: var_a = {var_a}, var_b = {var_b}")


def variable_scope():
    var_a = 200
    global var_b
    var_b = 200
    print(f"function end: var_a = {var_a}, var_b = {var_b}")


variable_scope()
print(f"end: var_a = {var_a}, var_b = {var_b}")

# 传参方式
print("\n====== 传参方式 ======")


def register_user(username, password, mobile, region='china', sex=1):
    print(
        f"[register_user success] username = {username}, password ={password}, mobile = {mobile}, region = {region}, sex = {sex}")


register_user("zhang_san", "123456", "13700000001", "china", 1)
register_user(username="li_si", password="123456", mobile="13700000002", region="hongkong", sex=2)
register_user(mobile="13700000003", username="wang_wu", password="123456", region="hongkong", sex=1)
register_user("zhao_liu", "123456", "13700000004", "macau")
register_user("li_bai", "666666", "13700000005", region="macau")


def calculator_add(x, y):
    return x + y


def calculator_sub(x, y):
    return x - y


def calculator_mul(x, y):
    return x * y


def calculator_div(x, y):
    return x / y


def calculator(x, y, operator):
    return operator(x, y)


print(calculator_add(10, 20))
print(calculator(10, 20, calculator_add))
print(calculator(10, 20, calculator_sub))
print(calculator(10, 20, calculator_mul))
print(calculator(10, 20, calculator_div))


def statistics(*args, **kwargs):
    """

    :param args: 不定长位置参数；需要汇总统计的数值
    :param kwargs: 不定长关键字参数；（setRound = 保留的小数位，isPrint：是否打印）
    :return: （最大值，最小值，平均值)
    """
    max_num = max(*args)
    min_num = min(*args)
    avg_num = sum(args) / len(args)
    if kwargs.get("setRound") is not None:
        avg_num = round(avg_num, kwargs["setRound"])
    if kwargs["isPrint"]:
        print(f"最大值 = {max_num}, 最小值 = {min_num}, 平均值 = {avg_num}")
    return max_num, min_num, avg_num


print(statistics(1, 2, 3, 4, 5, 6, 77, 8, 90, setRound=2, isPrint=1))

print("\n====== 匿名函数 ======")
f_print = lambda: print("这是没带参数的匿名函数.")
f_add = lambda x, y: x + y
f_print()
print(f_add(1, 2))

print("\n====== 递归案例：阶乘 ======")


def factorial(number):
    """
    return number!
    :param number: 正整数
    :return: number的阶乘
    """
    return 1 if number <= 1 else number * factorial(number - 1)


print(f"5! = {factorial(5)}")
print(f"8! = {factorial(8)}")
print(f"10! = {factorial(10)}")
