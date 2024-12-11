def flatten(nested_list):
    flattened = []
    
    for item in nested_list:
        if isinstance(item, list):
             flattened.extend(item)
        else:
            # If the item is not a list, append it directly
            flattened.append(item)
    
    return flattened

nested_list = [1, [2, 3], [4, 8], [5, 6], 7]
flattened_list = flatten(nested_list)
print(flattened_list) 