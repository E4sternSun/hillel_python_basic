def is_even(number: int) -> bool:
    """
    Перевірка чи є число парним, через перевірку останнього біта.
    (якщо парне - останній біт = 0, непарне = 1)

    :param int number: Ціле число, яке потрібно перевірити.
    :return bool: True, якщо число парне - False, якщо непарне.
    """

    return bin(number)[-1] == '0'

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
