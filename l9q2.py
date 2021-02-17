import basic_ops as bo
import adv_ops as ao

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
        a, b = input().split(",")
        a = int(a)
        b = int(b)
