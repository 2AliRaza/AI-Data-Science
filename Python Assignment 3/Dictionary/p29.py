def split(input_dict):
    odd_dict = {}
    even_dict = {}

    for key, value in input_dict.items():
        if value % 2 == 0:
            even_dict[key] = value
        else:
            odd_dict[key] = value

    return odd_dict, even_dict

input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(split(input_dict))

