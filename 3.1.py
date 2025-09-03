number_1 = int(input("\033[92m🧑‍🎓Terentiev Oleksii\033[0m\n\nEnter the first number for calculation: "))
term = input("Select operation (+, -, / or *): ")
number_2 = int(input("Enter the second number for calculation: "))
number_3 = None

if term == "+":
    number_3 = number_1 + number_2
elif term == "-":
    number_3 = number_1 - number_2
elif term == "/":
    if number_2 == 0:
        print("\n\033[91mYou can't divide by zero!\033[0m")
    else:
        number_3 = number_1 / number_2
elif term == "*":
    number_3 = number_1 * number_2
else:
    print("\n\033[91mThe arithmetic operator was chosen incorrectly!\033[0m")

if number_3 is not None:
    print("\n\033[94mThe result of your calculation =", number_3, "\033[0m")
