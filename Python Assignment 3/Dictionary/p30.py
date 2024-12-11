dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new={}

for key, value in dict.items():
    if dict[key]<=3:
        new[key]=value


print(new)