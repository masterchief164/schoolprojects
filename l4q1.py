# start your code here..
s = input()
ap = 0
bp = 0
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'i' or s[i] == 'u':
        ap += (len(s) - i)
    else:
        bp += (len(s) - i)
if ap == bp:
    print("DRAW")
else:
    print("A", bp)
    print("B", ap)
