import sys

for _ in range(int(input())):
    n = int(input())
    s = input()
    inf = sys.maxsize
    rt = [inf] * n
    lt = [inf] * n
    r = inf
    l = inf
    for i in range(n):
        if s[i] == '1':
            lt[i] = 0
            l = 0
        else:
            if l == inf:
                lt[i] = inf
            else:
                l += 1
                lt[i] = l
        if s[n - i - 1] == '1':
            rt[n - i - 1] = 0
            r = 0
        else:
            if r == inf:
                rt[n - i - 1] = inf
            else:
                r += 1
                rt[n - i - 1] = r
    ans = 0
    for i in range(n):
        ans += min(lt[i], rt[i])
    print("Case #" + str(_ + 1) + ": " + str(ans))
