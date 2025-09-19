while True:
    user_input = input("Введіть кількість секунд (від 0 до 8640000): ")

    if not user_input.isdigit():
        print("Помилка: потрібно внести ціле число.")
        continue

    total_seconds = int(user_input)

    if not (0 <= total_seconds <= 8640000):
        print("Помилка: число має бути від 0 до 8640000.")
        continue

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    s = str(days)
    if s.endswith("11") or s.endswith("12") or s.endswith("13") or s.endswith("14"):
        day_word = "днів"
    elif s.endswith("1"):
        day_word = "день"
    elif s.endswith(("2", "3", "4")):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{days} {day_word}, {hours:02d}:{minutes:02d}:{seconds:02d}")

    cont = input("Бажаєте продовжити? (так/т для продовження): ").strip().lower()
    if cont not in ["так", "т"]:
        print("Допобачення!")
        break