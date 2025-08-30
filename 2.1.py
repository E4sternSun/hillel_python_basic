number = int(input("\033[92m🧑‍🎓Terentiev Oleksii\nEnter a 4-digit number: "))

# divmod (x, y), тому я задав перемінні a, b, c як "x"; ones, tens, hundreds, thousands як "y"
a, ones = divmod(number, 10)
b, tens = divmod(a, 10)
c, hundreds = divmod(b, 10)
thousands = c # тут нам divmod не потрібен, бо ми взяли цілу частину від ділення в строці вище

print(thousands)
print(hundreds)
print(tens)
print(ones)
print("\nWith love to divmod <3\033[0m")
# тут має бути пуста строка, але в git репозиторію вона чомусь не відображається.
