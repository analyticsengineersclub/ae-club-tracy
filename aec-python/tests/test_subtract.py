import unittest
from calc import aec_subtract, aec_divide

class TestSubtract(unittest.TestCase):
    
    def test_subtract(self):
        arg_ints = [20,5]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 15)

    def test_postive(self):
        arg_ints = [5, 20]
        sub_results = aec_subtract(arg_ints)
        self.assertEqual(sub_results, 0)

class TestDivide(unittest.TestCase):
    
    def test_divide(self):
        arg_ints = [50, 2]
        divide_result = aec_divide(arg_ints)
        self.assertEqual(divide_result, 25)
    
    def test_zero_denom(self):
        arg_ints = [50, 0]
        divide_result = aec_divide(arg_ints)
        self.assertEqual(divide_result, 0)


if __name__ == "__main__":
    unittest.main()