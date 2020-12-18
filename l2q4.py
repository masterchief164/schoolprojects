# start your code here..
s, i, c = input().split("\\t")
i = int(i)
if (i <= (len(s) - 1)) and i >= (0 - len(s)):
    if (i != -1) and (i != len(s) - 1):
        s1 = s[:i] + c + s[i + 1:]
    else:
        s1 = s[:i] + c
print(s1)
