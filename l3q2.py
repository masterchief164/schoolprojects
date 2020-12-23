# write your code here..
x=int(input())
if(x%100==0):
    if(x%400==0):
        print(True)
    else:
        print(False)
else:
    if(x%4==0):
        print(True)
    else:
        print(False)