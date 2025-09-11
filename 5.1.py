import string
import keyword

while True:
    name = input("Enter the variable name : ")

    if name and name[0].isdigit():
        print(False)
    elif any(_.isupper() for _ in name):
        print(False)
    elif any(_ not in string.ascii_lowercase + string.digits + "_" for _ in name):
        print(False)
    elif name in keyword.kwlist:
        print(False)
    elif name.count("_") > 1 and name.strip("_") == "":
        print(False)
    else:
        print(True)

    again = input("Want to check another name? (yes/y to continue): ")
    if again not in ["yes", "YES", "y", "Y"]:
        print("Bye!")
        break
