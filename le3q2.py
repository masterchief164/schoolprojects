def first(a):
    p, q = a.split(",")
    return int(p)


def remred(a):
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(a) - 1, -1, -1):

            s1, e1 = a[i][0], a[i][1]
            s2, e2 = a[j][0], a[j][1]
            if ((s1 == s2 and e1 == e2 and i != j) or (s1 == s2 and e2 < e1) or (e1 == e2 and s1 < s2) or (
                    s1 < s2 and e1 > e2)):
                a.remove(a[j])
                break
    return a


def over(a, b):
    return a[0] < b[0] < a[1]


def resover(lot):
    i = 0
    j = 1
    while j < len(lot):
        if over(lot[i], lot[j]):
            s1 = lot[i][0]
            s2 = lot[j][0]
            e2 = lot[j][1]
            lot[i] = (s1, s2)
            lot[j] = (s2, e2)
        i += 1
        j += 1
    return lot


inp = input().split("__")
inptup = []
for i in inp:
    inptup.append(tuple(map(int, i.split(','))))
inp = remred(inptup)
inp.sort()
inp = resover(inp)
print(inp)
