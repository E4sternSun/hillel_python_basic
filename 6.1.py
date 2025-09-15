import string

while True:
    user_input = input("Enter two letters separated by a hyphen : ")
    start, end = user_input.split("-")

    if not user_input.strip():
        print("The string cannot be empty!")
        continue

    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)

    result = letters[start_index:end_index + 1]
    print("Result:", result)

    cont = input("Continue? (yes/y to proceed): ").lower()
    if cont not in ["yes", "y"]:
        print("See you later")
        break
