# start your code here..
s,i,c=input().split("\\t")
i=int(i)
s1=s[i+1:]
s=s[:i]
s=s+c+s1
print(s)
