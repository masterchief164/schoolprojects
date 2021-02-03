lst = input().split()
nlst = []
for i in lst:
    if i[::-1] not in lst:
        nlst.append(i)
for i in nlst:
    print(i, end=" ")
