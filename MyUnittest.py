# Study the frame of the Unittest.

# 第一步导入unittest
import unittest

# 导入要测试的计算类
from Calculator import Calculator

# 第二步创建一个类，继承unittest的TestCase类


class TestCalcultor(unittest.TestCase):

    def test_add(self):
        c = Calculator(6, 2)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(6, 2)
        result = c.sub()
        self.assertEqual(result, 4)

    def test_multiply(self):
        c = Calculator(6, 2)
        result = c.multiply()
        self.assertEqual(result, 12)

    def test_division(self):
        c = Calculator(6, 2)
        result = c.devision()
        self.assertEqual(result, 3)

    def test_yu(self):
        c = Calculator(6, 2)
        result = c.yu()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
