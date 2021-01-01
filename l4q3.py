n = int(input())
s = ""
while n != 0:

    temp = n % 16

    if temp < 10:
        s = s + chr(temp + 48)
    else:
        s = s + chr(temp + 55)
    n = int(n / 16)
s = s[::-1]
print(s)
