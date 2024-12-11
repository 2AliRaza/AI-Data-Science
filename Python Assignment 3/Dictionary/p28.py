nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

flattened_dict = {}

for key, value in nested_dict.items():
     for inner_key, inner_value in value.items():
         flattened_dict[f"{key}_{inner_key}"] = inner_value

print(flattened_dict)