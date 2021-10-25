import unittest
from MetaCust import CustomMeta, CustomClass


class ForTest1(metaclass=CustomMeta):
    a = 15

    def __init__(self):
        self.b = 'bbbb'
        self.c = [0, 1, '15']

    def test_func1(self, text):
        return 'good'+text

    def test_func2(self):
        return 'good2'


class ForTest2(ForTest1):
    static = 105

    def __init__(self):
        self.custom_d = 'dddd'
        self.e = {'key': 'value'}

    def test_func3(self):
        return 'good3'


class TestList(unittest.TestCase):
    def setUp(self):
        self.first = ForTest1()
        self.second = ForTest2()
        self.third = CustomClass()

    def test_names_first_valid(self):
        self.assertEqual(self.first.custom_a, 15)
        self.assertEqual(self.first.custom_b, 'bbbb')
        self.assertEqual(self.first.custom_c, [0, 1, '15'])
        self.assertEqual(self.first.custom_test_func1('11'), 'good11')
        self.assertEqual(self.first.custom_test_func2(), 'good2')

    def test_names_first_invalid(self):
        with self.assertRaises(AttributeError):
            print(self.first.a)
        with self.assertRaises(AttributeError):
            print(self.first.b)
        with self.assertRaises(AttributeError):
            print(self.first.c)
        with self.assertRaises(AttributeError):
            print(self.first.test_func1('11'))
        with self.assertRaises(AttributeError):
            print(self.first.test_func2())

    def test_names_second_valid(self):
        self.assertEqual(self.second.custom_a, 15)
        self.assertEqual(self.second.custom_b, 'bbbb')
        self.assertEqual(self.second.custom_c, [0, 1, '15'])
        self.assertEqual(self.second.custom_test_func1('11'), 'good11')
        self.assertEqual(self.second.custom_test_func2(), 'good2')
        self.assertEqual(self.second.custom_custom_d, 'dddd')
        self.assertEqual(self.second.custom_e, {'key': 'value'})
        self.assertEqual(self.second.custom_test_func3(), 'good3')

    def test_names_second_invalid(self):
        with self.assertRaises(AttributeError):
            print(self.second.a)
        with self.assertRaises(AttributeError):
            print(self.second.b)
        with self.assertRaises(AttributeError):
            print(self.second.c)
        with self.assertRaises(AttributeError):
            print(self.second.test_func1('11'))
        with self.assertRaises(AttributeError):
            print(self.second.test_func2())

    def test_names_third_valid(self):
        self.assertEqual(self.third.custom_x, 50)
        self.assertEqual(self.third.custom_val, 99)
        self.assertEqual(self.third.custom_line(), 100)

    def test_names_third_invalid(self):
        with self.assertRaises(AttributeError):
            print(self.third.x)
        with self.assertRaises(AttributeError):
            print(self.third.val)
        with self.assertRaises(AttributeError):
            print(self.third.line())