user_input = input("Enter a string: ")

if user_input.isupper():
    print("The string is uppercase.")
elif user_input.islower():
    print("The string is lowercase.")
elif any(c.isupper() for c in user_input) and any(c.islower() for c in user_input):
    print("The string is a mix of uppercase and lowercase.")
else:
    print("The string does not contain any letters.")