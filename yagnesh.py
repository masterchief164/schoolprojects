t = int(input())
vowels = set("aeiou")
VOWELS = set("AEIOU")
s = set({})
S = set({})
print(VOWELS)
for i in range(t):
    string = input()
    for char in string:
        if char in vowels:
            s.add(char)
        elif char in VOWELS:
            S.add(char)
    if len(s) == len(vowels) or len(S) == len(VOWELS):
        print("lovely string")
    else:
        print("ugly string")
