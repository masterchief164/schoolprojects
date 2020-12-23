# write your code here..
x = input().split()
for (i) in range(4):
    x[i] = int(x[i])
for (i) in range(4):
    mininx = i
    for (j) in range(i + 1, 4):
        if x[mininx] > x[j]:
            mininx = j

    x[i], x[mininx] = x[mininx], x[i]
for (i) in range(3):
    if x[i] != x[i + 1]:
        break;
print(x[i + 1])