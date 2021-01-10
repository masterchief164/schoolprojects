stri = input().split()


def sor(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def cou(inp1, s):
    c = 0
    for k in inp1:
        if s == k:
            c = c + 1
    return c


def freq(inp1):
    str2 = []
    inp1 = sor(inp1)
    pos = 0
    for k in inp1:

        if k not in str2:
            str2.append(k)
    max1 = 0
    for k in range(0, len(str2)):
        if max1 < cou(inp1, str2[k]):
            max1 = cou(inp1, str2[k])
            pos = k
    print(str2[pos])


freq(stri)
