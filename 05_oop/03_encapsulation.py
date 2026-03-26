# 封装与访问控制
# 私有成员变量和私有方法：通过封装，隐藏实现细节，提供接口
class Phone:
    # 私有成员变量：变量名以__开头；访问控制（无法直接被类对象使用）
    __is_5g_enabled = False

    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price

    def get_brand(self):
        return self.__brand

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # 私有方法：方法名以__开头；访问控制（无法直接被类对象使用）
    def __check_5g(self):
        return self.__is_5g_enabled

    def enable_5g(self):
        self.__is_5g_enabled = True
        print("5G已启用")

    def disable_5g(self):
        self.__is_5g_enabled = False
        print("5G已关闭")

    def call(self):
        if self.__check_5g():
            print("5G通话中...")
        else:
            print("普通通话中...")


if __name__ == '__main__':
    phone = Phone("华为", 5999)
    print(phone.get_brand())
    print(phone.get_price())
    phone.set_price(6999)
    # 私有成员变量 无法被类对象使用
    # print(phone.__is_5g_enabled)
    phone.call()
    phone.enable_5g()
    phone.call()
    phone.disable_5g()
    phone.call()