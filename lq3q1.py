def binaryToDecimal(n):
    num = n
    dec_value = 0

    base = 1

    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)

        dec_value += last_digit * base
        base = base * 2
    return dec_value


inp = input().split("_")
c = 0
s = ""
s1 = 0
for i in inp:
    flag = 1
    c = 0
    if 16 >= len(i) >= 8:
        for j in range(len(i) - 2):
            if i[j].casefold() == i[j + 2].casefold():
                c += 1
        if c >= 2:
            flag = 0
    else:
        flag = 0
    s = s + str(flag)
    s1 = binaryToDecimal(int(s))
print(s1)
