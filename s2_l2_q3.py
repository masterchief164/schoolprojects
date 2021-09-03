# question 3
def Check(order, arr1, arr2):
    f = 1
    for i in range(order):
        for j in range(order):
            if arr1[i][j] != arr2[i][j]:
                f = 0

    if f == 1:
        return 0
    else:
        return 1


arr1 = []
arr2 = []
order = int(input())
for i in range(order):
    row = input("Enter row 1 \n").strip(" ").split(" ")
    arr1.append(row)

for i in range(order):
    row = input("Enter row 1 \n").strip(" ").split(" ")
    arr2.append(row)
if Check(order, arr1, arr2) == 0:
    print("Identical")
else:
    print("Not Identical")
