from sympy import *
from sympy.abc import x

init_printing(use_latex=True)

def solving_differential_equation(leftHand, rightHand, intialConditions = []) -> []:
    f = Function('f')
    equation = dsolve(Eq(leftHand, rightHand), f(x)) if not intialConditions \
        else dsolve(Eq(leftHand, rightHand), f(x), ics={f(intialConditions[0]): intialConditions[1]})
    equationType = classify_ode(Eq(leftHand, rightHand), f(x))
    return [equationType, equation]


print('Welcome to differential equation app')
while True:
    print('Enter the differential equation ( dy/dx -> diff(f(x), x), d^2y/dx^2 -> diff(f(x), x, x), x^4 -> x**4, squareroot of x^2 -> sqrt(x**2)')
    left = input('leftHandSide: ')
    right = input('rightHandSide: ')
    print('Enter Intial Conditions if not applicable enter both -1')
    intial_y = int(input('y: '))
    intial_x = int(input('x: '))
    left = parse_expr(left)
    right = parse_expr(right)
    print(f'Your function: {left} = {right}')
    solution = solving_differential_equation(left, right) if intial_x == -1 and intial_y == -1\
        else solving_differential_equation(left, right, [intial_x, intial_y])
    print(f'Applicable Solving Techniques: {solution[0]}')
    print(f'The solution: {solution[1]}')
    print(100*'*')