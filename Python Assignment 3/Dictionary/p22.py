data = {'a': 10, 'b': 15, 'c': 7}

max_key = max(data, key=data.get)

print(f"The key with the maximum value is: '{max_key}' with a value of {data[max_key]}")