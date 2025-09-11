value = []

if value:
    selected_indices = list(range(0, len(value), 2))
    selected_values = [value[x] for x in selected_indices if x < len(value)]
    result = sum(selected_values) * value[-1]
else:
    result = 0

print(result)
