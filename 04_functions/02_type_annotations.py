# 定义变量
a: int = 100
b: float = 66.6
c: bool = True
d: str = "test"
e: None = None
f: list[int] = [-1, 2, 3, 4]
g: list[int | float] = [1, 2, 3, 4, 5.66, 6.71]
h: tuple[str, int, int] = ("勒布朗", 23, 2003)
i: set[str] = {"Java", "Python", "Go", "JavaScript", "C", "C++"}
j: dict[str, str] = {"13700000001": "zhang_san", "13700000002": "li_si", "13700000003": "wang_wu"}


# 方法参数类型、返回值类型定义
def statistics(*args: float, **kwargs: dict[str, int]) -> tuple[float, float, float]:
    """
    通过数值列表计算最大值、最小值、平均值并返回
    :param args: 不定长位置参数；需要汇总统计的数值
    :param kwargs: 不定长关键字参数；（setRound = 保留的小数位，isPrint：是否打印）
    :return: （最大值，最小值，平均值)
    """
    max_num = max(*args)
    min_num = min(*args)
    avg_num = sum(args) / len(args)
    if kwargs.get("setRound") is not None:
        avg_num = round(avg_num, kwargs["setRound"])
    isPrint = kwargs.get("isPrint")
    if isPrint is not None and isPrint:
        print(f"最大值 = {max_num}, 最小值 = {min_num}, 平均值 = {avg_num}")
    return max_num, min_num, avg_num


print(statistics(a, b, c, *f, *g))
