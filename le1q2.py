a,b=input().split("---")
a=a.casefold()
b=b.casefold()
i=a.rfind(b)
a=a[:i]
print(a.rfind(b))
##Shaswat Gupta B2 ECE