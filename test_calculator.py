import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        #     fill in code
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 100), 100)

    def test_subtract(self):  # 3 assertions
        #     fill in code
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(0, 100), -100)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(-3, -7), 21)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)
        self.assertEqual(div(20, 10), 0.5)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        #     # call division function inside, example:
        #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        #     fill in code
        self.assertEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self):  # 1 assertion
        #     # use same technique from test_divide_by_zero
        #     fill in code
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    #     fill in code

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):  # 3 assertions
        #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-3)
        #     # Test basic function
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()