import random
import string

def generate_random_password(length):

    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


password_length = 12
print(generate_random_password(password_length))