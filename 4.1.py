list_example = [0]

list_calc = list_example[:] = [x for x in list_example if x != 0] + [0] * list_example.count(0)

print(list_calc)
