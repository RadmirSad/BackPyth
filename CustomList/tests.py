from MyList import CalcList
import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.my_list = CalcList([5, 10, 4, -8, 2.0])
        self.dop_list = [12, 0, -7, 1, -6, 7.0]
        self.dop_list2 = [3, 2, 1]
        self.dop_err_list = (15, 6, 8)
        self.dop_err_list2 = [12, "4", 9, 1]

    def __check_elem_eq(self, fir, sec):
        self.assertIsInstance(fir, CalcList)
        for i in range(len(fir)):
            self.assertEqual(fir[i], CalcList(sec)[i])

    def test_add_valid(self):
        one = self.my_list + self.dop_list
        self.__check_elem_eq(one, [17, 10, -3, -7, -4.0, 7.0])
        two = self.dop_list + self.my_list
        self.__check_elem_eq(two, [17, 10, -3, -7, -4.0, 7.0])
        three = one + two
        self.__check_elem_eq(three, [34, 20, -6, -14, -8.0, 14.0])

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.my_list + self.dop_err_list
        with self.assertRaises(ArithmeticError):
            self.my_list + self.dop_err_list2

    def test_eq_valid(self):
        one = [5, 10, 4, -8, 2.0]   # 13
        self.assertEqual(one, self.my_list)
        two = [10, 4, -1]           # 13
        self.assertEqual(two, self.my_list)
        three = [15, 0]
        self.assertNotEqual(three, self.my_list)

    def test_eq_invalid(self):
        with self.assertRaises(TypeError):
            flag = self.my_list == self.dop_err_list
        with self.assertRaises(TypeError):
            flag = self.my_list == self.dop_err_list2

    def test_neg(self):
        one = -self.my_list
        self.assertIsInstance(one, CalcList)
        for i in range(len(one)):
            self.assertEqual(one[i], [-5, -10, -4, 8, -2.0][i])
            self.assertEqual(self.my_list[i], [5, 10, 4, -8, 2.0][i])

    def test_sub_valid(self):
        one = self.my_list - self.dop_list
        self.assertIsInstance(one, CalcList)
        self.__check_elem_eq(one, [-7, 10, 11, -9, 8.0, -7.0])
        self.__check_elem_eq(self.my_list, [5, 10, 4, -8, 2.0])
        two = self.dop_list - self.my_list
        self.assertIsInstance(two, CalcList)
        self.__check_elem_eq(two, [7, -10, -11, 9, -8.0, 7.0])
        three = self.dop_list2 - self.my_list
        self.assertIsInstance(three, CalcList)
        self.__check_elem_eq(three, [-2, -8, -3, 8, -2.0])

    def test_sub_invalid(self):
        with self.assertRaises(TypeError):
            self.my_list - self.dop_err_list
        with self.assertRaises(TypeError):
            self.my_list - self.dop_err_list2
        with self.assertRaises(TypeError):
            self.dop_err_list - self.my_list
        with self.assertRaises(ArithmeticError):
            self.dop_err_list2 - self.my_list

    def test_ne(self):
        self.assertNotEqual(self.my_list, self.dop_list)
        self.assertNotEqual(self.dop_list, self.dop_list2)
        self.assertNotEqual(self.my_list, self.dop_list2)

    def test_lt(self):
        self.assertLess(self.dop_list2, self.my_list)
        self.assertLess(self.dop_list2, self.dop_list)
        dop1 = CalcList([11, 2])
        self.assertFalse(self.my_list < dop1)

    def test_le(self):
        dop1 = CalcList([12, 3, -2])
        self.assertLessEqual(self.my_list, dop1)
        self.assertFalse(self.my_list <= self.dop_list2)

    def test_gt(self):
        self.assertGreater(self.my_list, self.dop_list2)
        self.assertGreater(self.dop_list, self.dop_list2)
        dop1 = CalcList([11, 2])
        self.assertFalse(dop1 > self.my_list)

    def test_ge(self):
        dop1 = CalcList([12, 3, -2])
        self.assertGreaterEqual(self.my_list, dop1)
        self.assertGreaterEqual(self.my_list, self.my_list)
        self.assertFalse(self.dop_list2 >= self.dop_list)
