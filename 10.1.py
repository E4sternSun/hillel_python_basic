def pow(x: int) -> int:
    """
    Returns the square of the input value.

    :param x: The input number to be squared.
    return: The square of the input value.
    """
    return x ** 2

def some_gen(begin: int, end: int, func):
    """
    A generator function that yields elements of a numeric sequence.

    :param begin: The first element to be yielded.
    :param end: The last element to be yielded.
    :param func: A function that takes an integer and returns
    :yield: The next element to be yielded.
    """
    yield begin
    current = begin
    for _ in range(1, end):
        current = func(current)
        yield current

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
