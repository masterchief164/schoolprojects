size = input()
size = int(size)
m = size - 1

for i in range(size):

    for j in range(m):
        print(end=" ")

    m = m - 1

    for j in range(i + 1):
        print('*', end=" ")

    print(" ")

m = m + 2
for i in range(size - 2, -1, -1):

    for j in range(m):
        print(end=" ")

    m = m + 1

    for j in range(0, i + 1):
        print('*', end=" ")

    print(" ")
