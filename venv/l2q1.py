# start your code here..
a,b=input().split()
a=a[:len(a)-3]
b=b[:len(b)-3]
if a.isalpha():
    a=a+b
    a=a.lower()
    b=a[::-1]
    if a==b:
        print(True)
    else:
        print(False)
else:
    print("Invalid")