# start your code here..
a,b=input().split()
a=a[:len(a)-3]
b=b[:len(b)-3]
a=a+b
if a.isalpha():
    a=a.lower()
    b=a[::-1]
    if a==b:
        print(True)
    else:
        print(False)
else:
    print("Invalid")

#Shaswat Gupta ECE B2