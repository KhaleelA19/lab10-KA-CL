# https://github.com/KhaleelA19/lab10-KA-CL.git
# Partner 1: Khaleel Abiru
# Partner 2: Camila Lipson

import math

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return b/a
def logarithm(a,b):
    if b <= 0 or a <= 1:
            raise ValueError("Base must be greater than 1 and Argument must be greater than 0")
    return math.log(b,a)
def exp(a,b):
    return a**b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot calculate square root of negative numbers.")

def hypotenuse(a, b):
    return math.hypot(a, b)