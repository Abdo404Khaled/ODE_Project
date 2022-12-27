from sympy import *
from sympy.abc import x

def solving_differential_equation(leftHand, rightHand, intialConditions = []) -> []:
    f = Function('f')
    equation = dsolve(Eq(leftHand, rightHand), f(x)) if not intialConditions \
        else dsolve(Eq(leftHand, rightHand), f(x), ics={f(intialConditions[0]): intialConditions[1]})
    equationType = classify_ode(Eq(leftHand, rightHand), f(x))
    return [equationType, equation]