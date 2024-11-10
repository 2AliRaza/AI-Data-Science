import time

start_number = int(input("Enter a number to start the countdown: "))
for number in range(start_number, -1, -1):
    print(number)
    time.sleep(1)