import unittest

import calc


class test_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_add_false(self):
        self.assertNotEqual(calc.add(4, 4), 8)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)

    def test_sub_false(self):
        self.assertNotEqual(calc.sub(123123, 123), 0)

    def test_mult(self):
        self.assertEqual(calc.mult(3, 4), 12)

    def test_mult_false(self):
        self.assertNotEqual(calc.mult(4, 4), 16)

    def test_div(self):
        self.assertEqual(calc.div(12, 3), 4)

    def test_div_false(self):
        self.assertNotEqual(calc.div(14, 2), 4)

    def test_div_by_zero(self):
        self.assertEqual(calc.div(14, 0), 7)

    def test_is_integer(self):
        self.assertTrue(calc.is_integer('2342'))

    def test_is_integer_false(self):
        self.assertFalse(calc.is_integer('123f'))
        
    def test_is_integer_float(self):
        self.assertTrue(calc.is_integer('2342.52'))


if __name__ == '__main__':
    unittest.main()
