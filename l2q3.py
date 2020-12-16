# start your code here..
s= input()
k=s.find('\\')
ss=s[k+2:]
ss=ss.lower()
s=s[:k]
s=s.lower()
res = len(s.split(ss))-1
print(res)
##Shaswat Gupta ECE B2