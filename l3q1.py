# write your code here..
g=float(input())
if(g>10):
    print("Invalid GPA")
elif (g==10):
    print("O")
elif (g>=9):
    print('A')
elif (g>=8):
    print('B')
elif (g>=7):
    print('C')
elif (g>=6):
    print('D')
elif (g>=5.5):
    print("Pass")
elif (g<5.5 and g>=0) :
    print("Fail")
else :
    print("Invalid GPA")