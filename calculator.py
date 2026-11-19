#https://github.com/AtalayAydogar/lab11-AA-JC
# Partner 1: Atalay Aydogar
# Partner 2: Jonathan Cunningham

import math
def square_root(a):
    if a<0:
        raise ValueError("Square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b/a

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    elif a ==1 or a<=0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
