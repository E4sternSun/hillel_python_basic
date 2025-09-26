def common_elements() -> set[int]:
    """
    Returns numbers from 0 to 99 divisible by both 3 and 5,
    using two lists converted to sets and set intersection.
    """
    list_3 = [x for x in range(100) if x % 3 == 0]
    list_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(list_3)
    set_5 = set(list_5)

    return set_3 & set_5


assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, 'Test1'
print('ОК')
