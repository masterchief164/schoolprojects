stri = input().split()


def freq(inp1):
    str2 = []
    inp1.sort()
    for k in inp1:

        if k not in str2:
            str2.append(k)
    max1 = 0
    for k in range(0, len(str2)):
        if max1 < inp1.count(str2[k]):
            max1 = inp1.count(str2[k])
            pos = k
    print(str2[pos])


freq(stri)
