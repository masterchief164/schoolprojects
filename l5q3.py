def fib():
    s = int(input())
    out = ""
    a = 0
    b = 1

    def pri():
        print(out)
        return

    for i in range(s):
        c = a + b
        a = b
        b = c
        out = out + str(b) + " "
    pri()


fib()