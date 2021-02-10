import sys


def containsAny(stri, chaset):
    return 1 in [c in stri for c in chaset]


try:
    inp = input()
    if not inp:
        raise ValueError("User hasn't provided any input")
except ValueError as e:
    print(e)
else:
    charset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', '+', ' ']
    try:
        if not (containsAny(inp, charset)):
            raise Exception("The input is in wrong format")
    except Exception as e:
        print(e)
    else:
        inp = inp.split()
        try:
            for i in range(len(inp)):
                inp[i] = float(inp[i])
        except ValueError:
            print("The entered values are not integers or float")
        else:
            for i in inp:
                try:
                    k = 1 / i
                except ZeroDivisionError:
                    print("The reciprocal of zero doesn't exist")
                    sys.exit(0)
                else:
                    print(k, end=" ")
            print()
finally:
    print('Execution completed!')
