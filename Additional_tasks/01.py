days = int(input("\033[92m🧑‍🎓Terentiev Oleksii\033[0m\n\n🕓 Enter the number of days: "))
hours = int(input("🕒 Enter the number of hours: "))
minutes = int(input("🕑 Enter the number of minutes: "))
seconds = int(input("🕐 Enter the number of seconds: "))

total_seconds = (
    days * 86400 +
    hours * 3600 +
    minutes * 60 +
    seconds
)

print("\n🔢\033[94mTotal number of seconds:", total_seconds, "\033[0m")
