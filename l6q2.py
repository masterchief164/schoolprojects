def sup(k):
    if k < 10:
        return k
    else:
        k1 = k
        s = 0
        while k1 > 0:
            d = k1 % 10
            s = s + d
            k1 = int(k1 / 10)
        return sup(s)


print(sup(int(input())))
