n = 0
while True:
    n = input("Enter the operation(+,-,*,/, sqrt) or EXIT to close the app: ")
    if n == "EXIT":
        break
    if n == "sqrt":
        a = int(input("Enter the number: "))
        print(a ** 2)
    else:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if n == '+':
            print(a + b)
        elif n == '-':
            print(a - b)
        elif n == '*':
            print(a * b)
        elif n == '/':
            print(a / b)

