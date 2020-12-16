# Start your code here..
s = input()
s1 = ""
for x in range(len(s)):
    if (s[x].isupper()):
        s1 += s[x].lower()
    else:
        s1 += s[x].upper()
print(s1)
##Shaswat Gupta ECE B2
