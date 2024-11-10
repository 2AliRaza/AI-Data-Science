lower_r = float(input("Enter the lower num of the range: "))
upper_r = float(input("Enter the upper num of the range: "))
number = float(input("Enter a number to check: "))

if lower_r <= number <= upper_r:
    print(f"{number} is within the range of {lower_r} and {upper_r}.")
else:
    print(f"{number} is not within the range of {lower_r} and {upper_r}.")