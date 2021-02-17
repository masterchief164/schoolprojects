import math_ops as mo

inp = input()
if len(inp) == 0:
    print('Empty list')
else:
    inp = int(inp)
    print(mo.isprime(inp))
    lst = mo.all_primes(inp)
    for i in lst:
        print(i, end=" ")
    print()
    lst = mo.prime_factors(inp)
    for i in lst:
        print(i, end=" ")
