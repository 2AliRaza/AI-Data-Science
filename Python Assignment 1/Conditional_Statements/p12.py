temperature = float(input("Enter the temperature in Celsius: "))

if temperature <= 0:
    print("It's freezing.")
elif 0 < temperature <= 25:
    print("It's moderate.")
else:
    print("It's hot.")