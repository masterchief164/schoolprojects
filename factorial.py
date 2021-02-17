def factorial_rec(a):
    if a == 1:
        return 1
    else:
        return a * factorial_rec(a - 1)


def factorial_non_rec(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact
