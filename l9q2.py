import basic_ops as bo
import adv_ops as ao
import re

while True:
    print("Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Factorial")
    print("7. Reciprocal")
    print("8. Log")
    print("9. Quit")
    print("Enter your choice: ", end="")
    ch = input()
    if ch == "1":
        print("Enter two numbers to perform addition:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                k[1] = float(k[1])
                print(bo.add(k[0], k[1]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                k[5] = float(k[5])
                k[6] = float(k[6])
                print(bo.add(k[1] / k[2], k[5] / k[6]))
        except Exception as e:
            print('Invalid input')
    elif ch == '2':
        print("Enter two numbers to perform subtract:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                k[1] = float(k[1])
                print(bo.sub(k[0], k[1]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                k[5] = float(k[5])
                k[6] = float(k[6])
                print(bo.sub(k[1] / k[2], k[5] / k[6]))
        except Exception:
            print('Invalid input')
    elif ch == '3':
        print("Enter two numbers to perform multiply:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                k[1] = float(k[1])
                print(ao.multiply(k[0], k[1]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                k[5] = float(k[5])
                k[6] = float(k[6])
                print(ao.multiply(k[1] / k[2], k[5] / k[6]))
        except Exception:
            print('Invalid input')
    elif ch == '4':
        print("Enter two numbers to perform divide:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                k[1] = float(k[1])
                print(ao.divide(k[0], k[1]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                k[5] = float(k[5])
                k[6] = float(k[6])
                print(ao.divide(k[1] / k[2], k[5] / k[6]))
        except Exception:
            print('Invalid input')
    elif ch == '5':
        print("Enter two numbers to perform power:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                k[1] = float(k[1])
                print(ao.pow(k[0], k[1]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                k[5] = float(k[5])
                k[6] = float(k[6])
                print(ao.pow(k[1] / k[2], k[5] / k[6]))
        except Exception:
            print('Invalid input')
    elif ch == '6':
        print("Enter the numbers to find factorial of:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k[0] = float(k[0])
                print(ao.factorial(k[0]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                print(ao.factorial(k[1] / k[2]))
        except Exception:
            print('Invalid input')
    elif ch == '7':
        print("Enter the numbers to find reciprocal of:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                print(ao.reciprocal(k[0]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                print(ao.reciprocal(k[1] / k[2]))
        except Exception:
            print('Invalid input')
    elif ch == '8':
        print("Enter the number to find log of:", end=" ")
        k = input()
        try:
            if k.find("(") == -1:
                k = k.split(",")
                k[0] = float(k[0])
                print(ao.log(k[0]))
            else:
                k = re.split("\(|\)|,", k)
                k[1] = float(k[1])
                k[2] = float(k[2])
                print(ao.log(k[1] / k[2]))
        except Exception:
            print('Invalid input')
    elif ch == '9':
        break
    else:
        print('wrong input')
