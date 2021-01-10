def fib():
    out = ""
    a = 0
    b = 1

    def pri():
        nonlocal a, b
        c = a + b
        a = b
        b = c

    for i in range(s):
        pri()
        out = out + str(b) + " "

    return out


s = int(input())
#    fib()
print(fib())
