def fun():
    s = int(input())
    while s % 10 != s:
        temp = s
        s = 0
        while temp / 10 > 0:
            s = s + (temp % 10)
            temp = int(temp / 10)
    return s


print(fun())