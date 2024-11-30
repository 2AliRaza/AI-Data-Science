def count(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency


input_str = "hello world"
print(count(input_str))
 