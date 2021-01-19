def is_prime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f = f + 1
    if f == 2:
        return 1
    else:
        return 0


n = input()
n = int(n)
a = 1
b = 1
c = 0
while c < n:
    c = a + b
    a = b
    b = c
if n - a < b - n:
    l = a
elif n - a >= n - b:
    l = b
elif n - a == 0 or b - n == 0:
    l = n
for i in range(1, l + 1):
    if is_prime(i) == 1 and l % i == 0:
        print(i, end=' ')
