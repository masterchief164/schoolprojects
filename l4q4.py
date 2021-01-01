# write your code here..
inp = input()
f = 0
if len(inp) == 16 and (inp[0] == '4' or inp[0] == '5' or inp[0] == '6') and inp.isnumeric():
    for i in range(len(inp) - 3):
        if inp[i] == inp[i + 1] == inp[i + 2] == inp[i + 3]:
            f = 1

else:
    f = 1
if f:
    print("Invalid")
else:
    print("Valid")