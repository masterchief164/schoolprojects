def fibo():
    a = 1
    b = 1

    def fib():
        nonlocal a, b
        n = a + b
        b = a
        a = n
        return b

    return fib


f = fibo()
inp = int(input())
for i in range(inp):
    print(f(), end=" ")
