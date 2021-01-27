lst = input().split()


def ass(s):
    asum = 0
    for i in range(len(s)):
        asum += ord(s[i])
    return asum


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


super_list = []
for i in lst:
    k = i
    if k.isdigit() or k.replace('-', '', 1).isdigit():
        if int(k) not in super_list:
            super_list.append(int(k))
    elif k.replace('.', '', 1).replace('-', '', 1).isdigit() and k.count('.') < 2:
        if (int(float(k)) + 1) not in super_list:
            super_list.append(int(float(k)) + 1)
    else:
        c = ass(k)
        if c not in super_list:
            super_list.append(c)
finlst = []
for i in super_list:
    if i % 3 != 0:
        if i > 30:
            if not isPrime(i + 5):
                finlst.append(i + 5)
        else:
            if not isPrime(i - 5):
                finlst.append(i - 5)

if len(finlst) == 0:
    print("Empty")
else:
    st = ""
    for i in finlst:
        st += (str(i) + " ")
    print(st.rstrip(" "))
