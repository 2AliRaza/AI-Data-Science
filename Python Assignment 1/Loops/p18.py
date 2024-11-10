start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for number in range(end, start - 1, -1):
    print(number)