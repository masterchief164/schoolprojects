import factorial as fac
import time

inp = input()
inp = int(inp)
start = time.time()
f1 = fac.factorial_rec(inp)
end = time.time()
t1 = (end - start) * 1000
start = time.time()
f2 = fac.factorial_non_rec(inp)
end = time.time()
t2 = (end - start) * 1000
if t1 > t2:
    print("Winner: factorial_rec")
else:
    print("Winner: factorial_non_rec")
print("factorial_rec: ", f1, int(t1))
print("factorial_non_rec: ", f2, int(t2))
