def second_index(text: str, some_str: str) -> int | None:
    """
    Returns the index of the second occurrence of a substring in a given string.

    :param: The string to search in.
    :return: The index of the second occurrence of the substring, or None if it doesn't occur twice.
    """
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + len(some_str))
    return second if second != -1 else None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
