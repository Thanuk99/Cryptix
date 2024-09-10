import random
import string

def generate_password(name, birth_date, length=12, use_special_chars=True, num_passwords=1):
    """
    Generate short, strong, and easy-to-remember passwords using user-specific information.

    Parameters:
    - name (str): User's name.
    - birth_date (str): User's birth date (format: YYYYMMDD).
    - length (int): Length of each password.
    - use_special_chars (bool): Whether to include special characters.
    - num_passwords (int): Number of passwords to generate.
    
    Returns:
    - list of str: Generated passwords.
    """
    # Prepare base parts of the password
    base_parts = [name.replace(" ", ""), birth_date]  # Remove spaces from name and add birth date
    base_password = ''.join(base_parts)
    
    # Define characters to use
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    passwords = []
    for _ in range(num_passwords):
        # Generate additional random characters
        remaining_length = length - len(base_password)
        if remaining_length > 0:
            base_password += ''.join(random.choice(characters) for _ in range(remaining_length))
        
        # Shuffle the password to ensure randomness
        password = ''.join(random.sample(base_password, len(base_password)))
        passwords.append(password[:length])
    
    return passwords

def check_password_strength(password):
    """Check the strength of the generated password."""
    strength = "Weak"
    if len(password) >= 8:
        if (any(c.islower() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in string.punctuation for c in password)):
            strength = "Strong"
        elif (any(c.islower() for c in password) and 
              any(c.isupper() for c in password) and 
              any(c.isdigit() for c in password)):
            strength = "Moderate"
    return strength

def main():
    print("Welcome to the Personalized Password Generator!")

    # Get user input for name
    name = input("Enter your name (first and last): ").strip()
    
    # Get user input for birth date
    while True:
        birth_date = input("Enter your birth date (format: YYYYMMDD): ").strip()
        if len(birth_date) == 8 and birth_date.isdigit():
            break
        print("Invalid birth date format. Please enter in YYYYMMDD format.")
    
    # Get user input for number of passwords
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords < 1:
                raise ValueError("Number must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (default is 12): ") or 12)
            if length < 8:
                raise ValueError("Length must be at least 8 characters.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Get user input for including special characters
    special_chars_input = input("Include special characters? (y/n): ").strip().lower()
    use_special_chars = special_chars_input == 'y'

    # Generate passwords
    passwords = generate_password(name=name, birth_date=birth_date, length=length, 
                                   use_special_chars=use_special_chars, num_passwords=num_passwords)
    
    # Display passwords and their strengths
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password} (Strength: {check_password_strength(password)})")

if __name__ == "__main__":
    main()
