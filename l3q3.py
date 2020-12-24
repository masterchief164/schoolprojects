x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])

if a > b:
    tmp = a
    a = b
    b = tmp
if c > d:
    tmp = c
    c = d
    d = tmp
if a > c:
    tmp = a
    a = c
    c = tmp
if b > d:
    tmp = b
    b = d
    d = tmp
if b > c:
    tmp = b
    b = c
    c = tmp
if a==b:
    if a==c:
        if a==d:
            print(a)
        else:
            print(d)
    else:
        print(c)
else:
    print(b)