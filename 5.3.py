import string

while True:
    text = input("Enter a string for the hashtag: ").lower()

    if not text.strip():
        print("The string cannot be empty!")
        continue

    cleaned = text.translate(str.maketrans("", "", string.punctuation))
    words = cleaned.split()
    capitalized = [word.capitalize() for word in words]
    hashtag = "#" + "".join(capitalized)
    print("Your hashtag:", hashtag[:140])

    cont = input("Continue? (yes/y to proceed): ").lower()
    if cont not in ['yes', 'y']:
        print("See you later")
        break
