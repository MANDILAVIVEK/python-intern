import random
import string

def generate_password(length):
    """
    Generate a strong, secure password of a given length.

    The password will contain a mix of:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (!, @, #, $, etc.)

    :param length: The length of the password to generate
    :return: A strong, secure password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("-------------------------------")

    # Ask the user for the length and number of passwords to generate
    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate the passwords
    passwords = [generate_password(length) for _ in range(num_passwords)]

    # Print the generated passwords
    print("Generated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()