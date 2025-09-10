import random

lst = [random.randint(0, 9) for _ in range(random.randint(3, 10))]
print("random list:", lst)

new_lst = [lst[0], lst[2], lst[-2]]
print("new list:", new_lst)
