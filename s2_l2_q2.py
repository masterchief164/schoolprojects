# question 2
def mean(a):
    sumOfElements = 0
    for i in a:
        sumOfElements += i
    return round(sumOfElements / 3)


arr = [[], [], []]
for i in range(3):
    for j in range(3):
        inp = input()
        arr[j].append(inp)

f = 1
for i in range(3):
    for j in range(3):
        if not (arr[i][j].isnumeric() and 0 < int(arr[i][j]) < 101):
            f = 0
if f == 1:
    for i in range(3):
        for j in range(3):
            arr[i][j] = int(arr[i][j])
    participants = [mean(i) for i in arr]
    maxi = -1
    for i in participants:
        if maxi < i:
            maxi = i
    if maxi < 70:
        print("All candidates are unfit")
    else:
        for i in range(3):
            if participants[i] == maxi:
                print("Candidate Number: ", (i + 1), ", Mean Oxygen Level:", maxi)
else:
    print("INVALID INPUT!")
