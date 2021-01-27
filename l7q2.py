def eq(lst):
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            return False
    return True


inp = input().split()
filst = []
if (len(inp) ** 0.5) == int(len(inp) ** 0.5):
    k = int(len(inp) ** 0.5)
    c = 0
    for i in range(k):
        ro = []
        for j in range(k):
            ro.append(int(inp[c]))
            c += 1
        filst.append(ro)
    d1 = 0
    d2 = 0
    for i in range(k):
        d1 += filst[i][i]
        d2 += filst[i][k - 1 - i]
    rs = []
    rc = []
    for i in range(k):
        sr = 0
        sc = 0
        for j in range(k):
            sr += filst[i][j]
            sc += filst[j][i]
        rc.append(sc)
        rs.append(sr)
    if eq(rs) and eq(rc) and d1 == d2:
        print("Truly Awesome List!")
    elif eq(rs) and eq(rc):
        print("Awesome List!")
    else:
        print("Normal List!")
else:
    print("Invalid List!")
