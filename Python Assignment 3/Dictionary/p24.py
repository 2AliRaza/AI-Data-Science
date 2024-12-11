dict = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

unique = {}
seen_values = set()

for key, value in dict.items():
    if value not in seen_values:
        unique[key] = value
        seen_values.add(value)

print(unique)