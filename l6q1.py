def add(a, b):
    sums = a + b
    return sums


def sub(a, b):
    subs = a - b
    return subs


def multiply(a, b):
    pro = 0
    for i in range(b):
        pro = add(pro, a)

    return pro


def divide(a, b):
    rem = sub(a, b)
    c = 0
    while rem >= 0:
        rem = sub(rem, b)
        c = c + 1
    if rem < 0:
        rem = add(rem, b)
    return c, rem


cho, a, b = input().split()
if cho == '1' or cho == '2' or cho == '3' or cho == '4':
    if a.isnumeric() and b.isnumeric() and int(a) >= 0 and int(b) >= 0:
        a = int(a)
        b = int(b)
        if cho == '1':
            print(add(a, b))
        elif cho == '2':
            print(sub(a, b))
        elif cho == '3':
            print(multiply(a, b))
        elif cho == '4':
            if b == 0:
                print('Cannot divide by Zero')
            else:
                q, r = (divide(a, b))
                print(q, r)
    else:
        print('Invalid Inputs')
else:
    print('Wrong Choice!')
