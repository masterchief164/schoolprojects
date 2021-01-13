# write your code here..
inp = input()
if len(inp) > 2:
    sig = inp[0]
    msg = inp[2:]
    comp = ""
    fin = ""
    k = 0
    i = 0
    f = 0
    while k != len(msg) - 1:
        c = 1
        f = 0
        for i in range(k, len(msg) - 1):
            if msg[i] == msg[i + 1]:
                c = c + 1
                f = 1
            else:
                break

        fin = fin + str(c) + msg[k]
        k = i + 1
    if f == 0:
        fin = fin + str(1) + msg[len(msg) - 1]
    if len(fin) < len(msg):
        fin = fin + sig
        print(fin)
    else:
        inp = msg + sig
        print(inp)
else:
    print(inp)
