def is_palindrome(text: str) -> bool:
    """
    Checks whether a given string is a palindrome, ignoring punctuation and case.

    :param: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("OK")
