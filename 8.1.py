def add_one(digits):
    """
    Adds 1 to the number represented by a list of digits.

    :param: A list of integers (0–9) representing a whole number.
    :return: A list of digits representing the result after adding 1.
    """
    number = int("".join(map(str, digits))) + 1
    return [int(d) for d in str(number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("OK")
