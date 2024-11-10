number = int(input("Enter an integer: "))

divisible_by_2 = (number % 2 == 0)
divisible_by_3 = (number % 3 == 0)

if divisible_by_2 and divisible_by_3:
    print(f"{number} is divisible by both 2 and 3.")
elif divisible_by_2:
    print(f"{number} is divisible by 2.")
elif divisible_by_3:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 2 or 3.")