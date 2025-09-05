my_list = []

if len(my_list) > 1:
    last = my_list.pop()
    my_list.insert(0, last)

print(my_list)
