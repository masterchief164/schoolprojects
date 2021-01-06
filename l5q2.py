inp = input().split()
inp.sort()
freq = 0
pos = 0
count = 1
for i in range(1,len(inp)):
    if inp[i] == inp[i - 1]:
        count = count + 1
    else:
        if freq < count:
            freq = count
            pos = i-1
        count = 1
print(inp[pos])
