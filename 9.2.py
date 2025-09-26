def difference(*args: float) -> float:
    """
    Calculates the difference between the maximum and minimum values from a variable number of numeric arguments.

    :param args: A variable number of numeric values (int or float).
    :return: The difference between the largest and smallest value, rounded to 2 decimal places if needed.
    """
    if not args:
        return 0
    return round(max(args) - min(args), 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
