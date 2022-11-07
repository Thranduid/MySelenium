class Calculator:
    """ 
    用于完成两个数的加减乘除计算的类
    """
    # 类的初始化函数

    def __init__(self, a, b) -> None:
        self.a = int(a)
        self.b = int(b)

    # 加
    def add(self):
        return self.a + self.b

    # 减
    def sub(self):
        return self.a - self.b

    # 乘
    def multiply(self):
        return self.a * self.b

    # 除
    def devision(self):
        return self.a / self.b
