value = []

if value:
    selected_indices = [0, 2, 4]
    selected_values = [value[x] for x in selected_indices if x < len(value)]
    result = sum(selected_values) * value[-1]
else:
    result = 0

print(result)
