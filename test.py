import unittest
from sympy import *

from module import solving_differential_equation

class TestSum(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(solving_differential_equation(parse_expr('Derivative(f(x), x, x) + 9*f(x)'), parse_expr('0'))[1], parse_expr('Eq(f(x), C1*sin(3*x) + C2*cos(3*x))'), "Should be: Eq(f(x), C1*sin(3*x) + C2*cos(3*x))")

if __name__ == '__main__':
    unittest.main()