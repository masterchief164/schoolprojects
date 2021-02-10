# Start your code here..
# converting in binary
def binaryconversion(a, b):
    return a * (2 ** b)


l = input().split("_")
list = []
for i in l:
    length = len(i)
    i = i.casefold()
    if length >= 8 and length <= 16:
        c = 0
        for j in range(len(i) - 2):
            if i[j] == i[j + 2]:
                c += 1
        if c <= 1:
            list.append(1)
        else:
            list.append(0)
    else:
        list.append(0)
p = 0
s = 0
while p < len(list):
    q = len(list) - p - 1
    s += binaryconversion(list[q], p)
    p += 1
print(s)
