import basic_ops as bo
import adv_ops as ao


def isprime(a):
    for i in range(2, bo.add(int(ao.pow(a, .5))), 1):
        if ao.isdivisible(a, i):
            return False
    return True


def all_primes(a):
    lst = []
    for i in range(2, bo.add(a, 1)):
        if isprime(i):
            lst.append(i)
    return lst


def prime_factors(a):
    lst = []
    while ao.isdivisible(a, 2):
        lst.append(2)
        a, b = ao.divide(a, 2)

    for i in range(3, bo.add(int(ao.pow(a, 0.5)), 1), 2):
        while ao.isdivisible(a, i):
            lst.append(i)
            a, b = ao.divide(a, i)
    if a > 2:
        lst.append(a)
    return lst
