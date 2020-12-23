s=input()
l=len(s)
mid=int (l/2)
a=s[:mid-1]
a=a[::-1]
b=s[mid-1:mid+2]
c=s[mid+2:]
c=c[::-1]
s=a+b+c
print(s)
##Shaswat Gupta ECE B2