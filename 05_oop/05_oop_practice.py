# 练习
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"商品名称：{self.name}；商品价格：{self.price}；库存：{self.stock}"


class ShoppingCart:
    def __init__(self, username):
        self.__items = dict()
        # 冗余字段
        self.__username = username

    def add_product(self, product, quantity=1):
        """添加购物车"""
        # todo 库存校验 后续对库存校验并抛出相关异常
        if product in self.__items:
            self.__items[product] += quantity
        else:
            self.__items[product] = quantity
        print(f"✅ 成功添加 {quantity} 件【{product.name}】到{self.__username}的购物车")

    def remove_product(self, product, quantity=None):
        """删除购物车中的商品：quantity=None 则删除全部，否则删除指定数量"""
        if quantity is None:
            # 删除所有商品
            del self.__items[product]
            print(f"❌ 已从{self.__username}的购物车移除全部【{product.name}】")
        else:
            if self.__items[product] <= quantity:
                quantity = self.__items[product]
                self.__items[product] -= quantity
                print(f"❌ 已从{self.__username}的购物车移除全部【{product.name}】")
            else:
                self.__items[product] -= quantity
                print(f"❌ 已从{self.__username}的购物车移除 {quantity} 件【{product.name}】")

    def view_cart(self):
        """查看购物车列表"""
        if not self.__items:
            print(f"🛒 {self.__username}的购物车为空")
            return

        print(f"\n🛒 {self.__username}的购物车详情：")
        total_price = 0
        for idx, (product, quantity) in enumerate(self.__items.items(), 1):
            item_price = round(product.price * quantity, 2)
            total_price += item_price
            print(f"{idx}.{product.name} - 单价：{product.price} - 数量：{quantity} | 小计：{item_price}")
        print(f"👉 购物车总价：{total_price}元\n")


class User:
    def __init__(self, username):
        self.username = username
        self.cart = ShoppingCart(self.username)


if __name__ == '__main__':
    # 商品列表
    product_apple = Product("Apple", 9.9, 200)
    product_banana = Product("Banana", 2.8, 89)
    product_milk = Product("Milk", 4, 35)
    product_pen = Product("Pen", 4.5, 3)
    print(product_apple)
    print(product_banana)
    print(product_milk)
    print(product_pen)
    print()

    # 用户列表
    u_eason = User("eason")
    u_constance = User("constance")

    # 添加购物车
    u_eason.cart.add_product(product_apple, 5)
    u_eason.cart.add_product(product_banana, 6)
    u_eason.cart.add_product(product_milk)
    u_constance.cart.add_product(product_pen)

    # 查看购物车
    u_eason.cart.view_cart()

    # 删除购物车
    u_eason.cart.remove_product(product_apple, 10)
    u_eason.cart.remove_product(product_banana, 2)
    u_eason.cart.remove_product(product_milk)
    u_eason.cart.view_cart()

    # 用户2的购物车列表
    u_constance.cart.view_cart()
