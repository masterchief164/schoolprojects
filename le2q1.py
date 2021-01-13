size = input()
size = int(size)
m = (2 * size) - 2

for i in range(size):

    for j in range(m):
        print(end=" ")

    m = m - 1

    for j in range(0, i + 1):
        print('*', end=" ")

    print(" ")

m=m+2
for i in reversed( range(size-1)):

    for j in range(m):
        print(end=" ")

    m = m + 1

    for j in range(0, i + 1):
        print('*', end=" ")

    print(" ")
