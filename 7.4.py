common_elements = lambda: {x for x in range(100) if divmod(x, 15)[1] == 0}
"""
Returns numbers from 0 to 99 divisible by both 3 and 5.
"""

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, 'Test1'
print('ОК')
