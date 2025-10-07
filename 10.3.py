def is_even(digit: int) -> bool:
    """
    Перевірка чи є число парним.

    :param int digit: Ціле число, яке потрібно перевірити.
    :return bool: True, якщо число парне - False, якщо непарне.
    """
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
