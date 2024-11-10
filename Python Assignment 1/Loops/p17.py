correct_number = 42  # You can change this to any number you want
guessed_number = None

while guessed_number != correct_number:
    guessed_number = int(input("Guess the number: "))

print("Congratulations! You've guessed the correct number.")