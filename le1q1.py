inp1,inp2=input().split('#')
x1,y1,z1=inp1.split(',')
x2,y2,z2=inp2.split(',')
r=3.44
a1=r*(float(x1)-1.5)/4
b1=r*(float(y1)-3.0)/3
c1=r*(float(z1)-2.5)/2
a2=r*(float(x2)-1.5)/4
b2=r*(float(y2)-3.0)/3
c2=r*(float(z2)-2.5)/2
dist=((a1-a2)**2+(b1-b2)**2+(c1-c2)**2)**0.5
print("%.3f" % dist)
##Shaswat Gupta ECE B2