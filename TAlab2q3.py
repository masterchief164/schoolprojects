c = 0
m1 = []
m2 = []
inp = input().split()
inp2 = input().split()
for i in range(3):
    ro = []
    for j in range(3):
        ro.append(int(inp[c]))
        c += 1
    m1.append(ro)
c = 0
for i in range(3):
    ro = []
    for j in range(3):
        ro.append(int(inp[c]))
        c += 1
    m2.append(ro)
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += m1[i][k] * m2[k][j]
for i in range(3):
    for j in range(3):
        print(result[i][j], end=" ")
    print()
