class Student:
    # 类属性
    school = 'Python School'

    def __init__(self, id, name, age):
        # 实例属性
        self.name = name
        self.age = age
        # 私有属性（约定俗成：单下划线 _ 保护，双下划线 __ 私有）
        self.__id = id

    # 实例方法：第一个参数必须是self
    # self的用法类似java中的this
    def get_id(self):
        return self.__id


if __name__ == '__main__':
    stu1 = Student("s001", "时光", 18)
    stu2 = Student("s002", "俞亮", 18)
    print(stu1)
    print(stu2)

    # 访问类属性
    print("Student.school: ", Student.school)
    print("stu1.school: ", stu1.school)
    # 访问对象的属性
    print(f"stu1: {stu1.name}_{stu1.age}")
    print(f"stu2: {stu2.name}_{stu2.age}")
    # 访问对象的私有属性
    print(f"stu1: {stu1.get_id()}")
    # 一些方法测试
    print(f"stu2: {stu2.__dict__}")
    print(type(stu1))
    print(dir(Student))
