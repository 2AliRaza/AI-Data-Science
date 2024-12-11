dict1 = {'a': 5, 'b': 10} 
dict2 = {'a': 3, 'b': 7}

for key1, Value1 in dict1.items():
    for key2, Value2 in dict2.items():
        if key1==key2:
            dict1[key1]=Value1+Value2


print(dict1)
