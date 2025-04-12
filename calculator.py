import math


def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot calculate square root of negative numbers.")

def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return b/a
def log(a,b):
    if b <= 0 or a <= 1:
            raise ValueError("Base must be greater than 1 and Argument must be greater than 0")
    return math.log(b,a)
def exp(a,b):
    return a**b
