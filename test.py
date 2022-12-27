import unittest
from sympy import *

from module import solving_differential_equation

class TestSum(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(solving_differential_equation(parse_expr('diff(f(x), x, x) + 9*f(x)'), parse_expr('0'))[1],
                         parse_expr('Eq(f(x), C1*sin(3*x) + C2*cos(3*x))'), "Should be: Eq(f(x), C1*sin(3*x) + C2*cos(3*x))")

    def test_case_2(self):
        self.assertEqual(solving_differential_equation(parse_expr('diff(f(x), x) + 2*x*y + x*y**4'), parse_expr('0'))[1],
                         parse_expr('Eq(f(x), C1 - x**2*y**4/2 - x**2*y)'), "Should be: Eq(f(x), C1 - x**2*y**4/2 - x**2*y)")

    def test_case_3(self):
        self.assertEqual(solving_differential_equation(parse_expr('f(x) * diff(f(x), x)'), parse_expr('2*x*sqrt(9+f(x)**2)'))[1][1],
                         parse_expr('Eq(f(x), sqrt(C1**2 + 2*C1*x**2 + x**4 - 9))'), "Should be: Eq(f(x), sqrt(C1**2 + 2*C1*x**2 + x**4 - 9))")

    def test_case_4(self):
        self.assertEqual(solving_differential_equation(parse_expr('diff(f(x), x)'), parse_expr('-f(x)**2/x**2'), [1, 0.5])[1],
                         parse_expr('Eq(f(x), -x/(1 - 3.0*x))'), "Should be: Eq(f(x), -x/(1 - 3.0*x))")


if __name__ == '__main__':
    unittest.main()