import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Please select at least one character type.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                raise ValueError("Password length must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    if not (include_uppercase or include_lowercase or include_digits or include_special):
        print("No character types selected. Please select at least one character type.")
        return get_user_input()

    return length, include_uppercase, include_lowercase, include_digits, include_special

def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_lowercase, include_digits, include_special = get_user_input()
    
    try:
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
