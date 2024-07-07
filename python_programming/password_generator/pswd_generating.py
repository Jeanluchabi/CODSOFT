import string
import random

def generate_password(length, use_special_chars=True):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user input for including special characters
    use_special_chars = input("Include special characters? (yes/no): ").lower() in ['yes', 'y']

    # Generate and display the password
    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

