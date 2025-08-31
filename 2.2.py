number = int(input("\033[92m🧑‍🎓Terentiev Oleksii\nEnter a 5-digit number: "))

a, ones = divmod(number, 10)
b, tens = divmod(a, 10)
c, hundreds = divmod(b, 10)
d, thousands = divmod(c, 10)
tens_of_thousands = d

#тут так само, як і в першому завданні, тільки цифр 5 і print всіх змінних в 1 строці.
print(ones, tens, hundreds, thousands, tens_of_thousands)
print("\nWith love to divmod <3\033[0m")
