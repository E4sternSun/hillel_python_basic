while True:
    op = input("Select operation (+, -, /, *): ")
    a = int(input("Enter the first number for calculation: "))
    b = int(input("Enter the second number for calculation: "))

    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        if b == 0:
            print("\n\033[91mYou can't divide by zero!\033[0m")
        else:
            print(a / b)
    else:
        print("\n\033[91mThe arithmetic operator was chosen incorrectly!\033[0m")
    again = input("Do you want to calculate again? (yes/y to continue): ")
    if again not in ["yes", "YES", "y", "Y"]:
        print("Bye!")
        break
