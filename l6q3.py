s = input()
l = len(s) - 1
sta = 0

ans = ""


def isPalindrome(st):
    global l
    global sta

    if l == sta:
        return True

    if st[l] != st[sta]:
        return False

    if sta < l + 1:
        l = l - 1
        sta = sta + 1
        return isPalindrome(st)

    return True


def generate_substrings(s):
    lst = [s]
    if len(s) > 0:
        lst.extend(generate_substrings(s[1:]))
        lst.extend(generate_substrings(s[:-1]))
    return list(lst)


def reverse(st):
    if len(st) == 0:
        return st
    else:
        return reverse(st[1:]) + st[0]


if isPalindrome(s.lower()):
    subst = generate_substrings(s)
    printed = []
    subst.sort(key=lambda v: s.index(v))
    subst.sort(key=len)

    for p in range(len(subst)):
        if subst[p] not in printed:
            print(subst[p], end=" ")
        printed.append(subst[p])
else:
    print(reverse(s))
