while True:
    op = input("Select operation (+, -, /, *) or 'exit' for exit: ")
    if op == "exit":
        print("Bye!")
        break

    a = int(input("Enter the first number for calculation: "))
    b = int(input("Enter the second number for calculation: "))

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b == 0:
            print("\n\033[91mYou can't divide by zero!\033[0m")
        else:
            print(a / b)
    else:
        print("\n\033[91mThe arithmetic operator was chosen incorrectly!\033[0m")
