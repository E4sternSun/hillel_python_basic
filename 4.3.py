import random

list_random = [random.randint(0, 9) for _ in range(random.randint(3, 10))]
print("Random list:", list_random)

new_list = [list_random[0], list_random[2], list_random[-2]]
print("New list:", new_list)
