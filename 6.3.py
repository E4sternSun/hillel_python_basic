while True:
    try:
        user_input = int(input("Enter a positive integer: "))
    except ValueError:
        print("Error: please enter a number.")
        continue

    while user_input >= 9:
        digits = str(user_input)
        result = int(digits[0])
        for _ in range(1, len(digits)):
            result *= int(digits[_])
        user_input = result

    print(f"Result: {user_input}")

    cont = input("Continue? (yes/y to proceed): ").strip().lower()
    if cont not in ["yes", "y"]:
        print("See you later")
        break
