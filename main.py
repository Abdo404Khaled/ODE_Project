from sympy import *
from sympy.abc import x
from module import solving_differential_equation

init_printing(use_latex=True)

print('Welcome to differential equation app')
while True:
    print('Enter the differential equation ( dy/dx -> diff(f(x), x), d^2y/dx^2 -> diff(f(x), x, x), x^4 -> x**4, squareroot of x^2 -> sqrt(x**2)')
    left = input('leftHandSide: ')
    right = input('rightHandSide: ')
    print('Enter Intial Conditions if not applicable enter both -1')
    initial_y = float(input('y: '))
    initial_x = float(input('x: '))
    left = parse_expr(left)
    right = parse_expr(right)
    print(f'Your function: {left} = {right}')
    solution = solving_differential_equation(left, right) if initial_x == -1 and initial_y == -1\
        else solving_differential_equation(left, right, [initial_x, initial_y])
    print(f'Applicable Solving Techniques: {solution[0]}')
    print(f'The solution: {solution[1]}')
    print(100*'*')