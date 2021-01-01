n = int(input())
for i in range(n):
    s = ""
    for j in range(2 * n - 2):
        if j % 2 == 0 and (j / 2 + i >= n - 1):
            s = chr(97 + n - i - 1 + int((2 * n - 2 - j) / 2)) + s
        else:
            s = "-" + s
    s = s[::-1] + chr(97 + n - 1 - i) + s
    print(s)
for i in reversed(range(n-1)):
    s = ""
    for j in range(2 * n - 2):
        if j % 2 == 0 and (j / 2 + i >= n - 1):
            s = chr(97 + n - i - 1 + int((2 * n - 2 - j) / 2)) + s
        else:
            s = "-" + s
    s = s[::-1] + chr(97 + n - 1 - i) + s
    print(s)
