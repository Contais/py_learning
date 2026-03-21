class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        """打印对象时的友好展示（面向用户）：¥价格 《书名》"""
        # __str__方法是Python中的“魔法”方法之一，它允许开发者定义对象的字符串表示。
        # 当使用print输出对象时，如果类中定义了__str__方法，那么就会打印这个方法中return的数据。
        return f"¥{self.price}\t《{self.title}》"

    def __repr__(self):
        return f"Book(title='{self.title}', price='{self.price}')"

    def __lt__(self, other):
        # 重载 运算符< : 比较两本书的价格
        return self.price < other.price

    def __eq__(self, other):
        # 重载equal方法：用于判断实例是否一致（默认是对比实例的内存指向)
        return self.price == other.price and self.title == other.title


if __name__ == "__main__":
    book1 = Book("Python 编程从入门到精通", 89.9)
    book2 = Book("面向对象编程实战", 69.9)
    book3 = Book("面向对象编程实战", 69.9)
    # __str__
    print(book1)
    print(book2)
    # __repr__
    print(repr(book1))
    print(repr(book2))
    # 运算符
    print(book1 < book2)
    print(book1 > book2)
    # __eq__
    print(book1 == book2)
    print(book3 == book2)

