lst0 = input().split()
lst1 = input().split()
maxdif = 0
for i in range(len(lst0)):
    if int(lst0[i]) - int(lst1[i]) > maxdif:
        maxdif = int(lst0[i]) - int(lst1[i])
    elif int(lst1[i]) - int(lst0[i]) > maxdif:
        maxdif = int(lst1[i]) - int(lst0[i])
print(maxdif)
