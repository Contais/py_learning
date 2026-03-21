"""异常处理核心练习
知识点：try-except/else/finally、异常类型、主动抛异常、自定义异常
"""

# ===================== 1. 基础异常处理（try-except） =====================
def basic_exception_demo():
    """基础：捕获指定异常，避免程序崩溃"""
    print("===== 基础异常处理演示 =====")
    try:
        dividend = float(input("请输入一个数字作为[被除数]："))
        divisor = float(input("请输入一个数字作为[除数]："))
        quotient = round(dividend / divisor, 2)
    except ValueError as e:
        print("【异常】请输入有效的数字！",e)
    except ZeroDivisionError as e:
        print("【异常】除数不能为0！", e)
    except Exception as e:
        print("【异常】未知错误！",e)
    else:
        # 只有try块无异常时才执行
        print(f"{dividend} / {divisor} = {quotient}")
    finally:
        print("计算流程结束\n")


# ===================== 2. 主动抛出异常（raise） =====================
def raise_exception_demo():
    """主动抛异常：校验参数合法性"""
    print("===== 主动抛异常演示 =====")
    def check_age(age):
        if not isinstance(age, int):
            # 主动抛出类型错误，可自定义提示信息
            raise TypeError("年龄必须是整数类型！")
        if age < 0 or age > 150:
            # 主动抛出值错误
            raise ValueError("年龄必须在0-150之间！")
        print(f"年龄校验通过：{age}岁")

    # 测试主动抛异常
    try:
        check_age("18")  # 触发TypeError
        # check_age(200)  # 取消注释触发ValueError
    except (TypeError, ValueError) as e:
        print(f"年龄校验失败：{e}\n")

# ===================== 3. 自定义异常（面向对象） =====================
class CustomException(Exception):
    """自定义异常：继承自基础Exception类，可添加自定义逻辑"""
    def __init__(self, msg, code):
        self.msg = msg  # 异常提示信息
        self.code = code  # 自定义错误码
        super().__init__(self.msg)  # 调用父类构造方法

    # 自定义异常的字符串展示
    def __str__(self):
        return f"错误码{self.code}：{self.msg}"

def custom_exception_demo():
    """自定义异常演示"""
    print("===== 自定义异常演示 =====")
    try:
        # 模拟业务场景：用户登录密码长度不足
        password = input("请设置密码（至少6位）：")
        if len(password) < 6:
            # 抛出自定义异常
            raise CustomException("密码长度不足6位", 1001)
        print("密码设置成功！")
    except CustomException as e:
        print(f"自定义异常捕获：{e}\n")

# ===================== 4. 异常处理最佳实践（综合示例） =====================
def best_practice_demo():
    """异常处理最佳实践：精准捕获、释放资源、记录错误"""
    print("===== 异常处理最佳实践 =====")
    file_path = "../.gitignore"
    file = None
    try:
        # 尝试读取文件（文件可能不存在/无权限）
        file = open(file_path, "r", encoding="utf-8")
        content = file.read()
        print(f"文件内容：{content}")
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在！")
    except PermissionError:
        print(f"错误：无权限读取文件 {file_path}！")
    except Exception as e:
        print(f"文件读取失败：{e}")
    finally:
        # 无论是否异常，都关闭文件（释放资源）
        if file:
            file.close()
            print("文件已关闭")
    print()

# 执行所有演示函数
if __name__ == "__main__":
    basic_exception_demo()
    raise_exception_demo()
    custom_exception_demo()
    best_practice_demo()