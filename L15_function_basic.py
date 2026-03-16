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

def triangle_area(bottom,height):
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







