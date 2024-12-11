def cube(n):
    cubes_dict = {i: i**3 for i in range(1, n + 1)}
    return cubes_dict

n = int(input("Enter a positive integer: "))
if n > 0:
     print(cube(n))
else:
    print("Please enter a positive integer.")
