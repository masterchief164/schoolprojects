import basic_ops as bo
import math
import numpy


def multiply(a, b):
    pro = 0
    for i in range(b):
        pro = bo.add(pro, a)

    return pro


def divide(a, b):
    rem = bo.sub(a, b)
    c = 0
    while rem >= 0:
        rem = bo.sub(rem, b)
        c = c + 1
    if rem < 0:
        rem = bo.add(rem, b)
    return c, rem


def isdivisible(a, b):
    q, r = divide(a, b)
    if r == 0:
        return True
    else:
        return False


def pow(a, b):
    return math.pow(a, b)


def factorial(a):
    return math.factorial(a)


def reciprocal(a):
    return numpy.reciprocal(a)


def log(a):
    return math.log(a)
