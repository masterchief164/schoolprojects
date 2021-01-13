#def primeFactors(n):
 #   while n % 2 == 0:
  #      print(2, end=" ")
   #     n = n / 2

   # for i in range(3, int(n ** 0.5) + 1, 2):

    #    while n % i == 0:
     #       print(int(i), end=" ")
      #      n = n / i

#    if n > 2:
 #       print(int(n), end=" ")


#def fib(n):
 #   a = 1
  #  b = 1
   # c = a + b
    #while n >= c:
     #   a = b
      #  b = c
       # c = a + b
#    return c, b


#inp = int(input())
#b,a = fib(inp)
#if inp - a < b - inp:
 #   l = a
#elif inp - a >= inp - b:
 #   l = b
#elif inp - a == 0 or b - inp == 0:
 #   l = inp
#primeFactors(l)


# write your code here..
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
