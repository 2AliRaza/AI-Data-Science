num1=int(input("Enter a First Number : "))
num2=int(input("Enter a Second Number : "))
num3=int(input("Enter a Third Number : "))

if num1>num2:
    if num1>num3:
        print(f"Number {num1} is Larger")
elif num2>num3:
    print(f"Number {num2} is Larger")
else:
    print(f"Number {num3} is Larger")

