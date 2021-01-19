def asc():
    inp = input()
    s = 0
    for i in range(len(inp)):
        if inp[i] != " ":
            print(inp[i], "ASCII value :", ord(inp[i]))
            s = s + ord(inp[i])

    print(s)
    sod(s)


def sod(a):
    while a > 10:
        n = a
        s = 0
        while n > 0:
            d = n % 10
            s = s + d
            n = int(n / 10)
        a = s
    print(a)
    fact(a)


def fact(k):
    f = 1
    for i in range(1, k + 1):
        f = f * i
    print(f)


asc()
