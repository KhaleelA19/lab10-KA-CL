import math

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot calculate square root of negative numbers.")
try:
    def hypotenuse(a, b):
        return math.hypot(a, b)
except ValueError as e:
    print(f"ValueError: {e}")

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a > 0:
        return b/a
    else:
        raise ValueError("Cannot divide by zero")

def logarithm(a,b):
    if b <= 0 or a <= 1:
            raise ValueError("Base must be greater than 1 and Argument must be greater than 0")
    return math.log(b,a)

def exponent(a,b):
    return a**b