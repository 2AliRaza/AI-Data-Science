original_dict = {'a': 1, 'b': 2, 'c': 3}

reversed_dict = {value: keys for keys, value in original_dict.items()}

print(reversed_dict)