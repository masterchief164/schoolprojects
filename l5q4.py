def floor(inp):
    return int(inp)


def split_txt():
    s = input()
    k = float(input())
    a = s[:floor(k * len(s) / 100)]
    b = ''
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
            b += '$'
        else:
            b += a[i]
    b += "###"
    s = s[floor(k * len(s) / 100):]
    s += "###"
    print(b)
    print(s)


split_txt()
