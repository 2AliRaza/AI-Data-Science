def search(input_dict, key):
    if key in input_dict:
        return input_dict[key]
    else:
        return "Key not found"

my_dict = {'a': 10, 'b': 15, 'c': 20}

print(search(my_dict, 'b')) 

print(search(my_dict, 'd'))  