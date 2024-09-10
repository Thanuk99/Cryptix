import random
import string

def enhance_password(base_password, length, use_special_chars, use_numbers=True, use_uppercase=True):
    """
    Enhance the base password by adding random elements to make it more secure while keeping it user-friendly.
    
    Parameters:
    - base_password (str): User's preferred base password.
    - length (int): Desired length of the final password.
    - use_special_chars (bool): Whether to include special characters.
    - use_numbers (bool): Whether to include numbers.
    - use_uppercase (bool): Whether to include uppercase letters.
    
    Returns:
    - str: Enhanced password.
    """
    # Define characters to use based on user preferences
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Add random characters if necessary to meet the desired length
    remaining_length = length - len(base_password)
    if remaining_length > 0:
        base_password += ''.join(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle the password to ensure randomness
    enhanced_password = ''.join(random.sample(base_password, len(base_password)))
    
    return enhanced_password[:length]

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
    print("Welcome to the Advanced Password Enhancer!")

    # Get user input for the base password
    base_password = input("Enter your preferred base password: ").strip()
    
    # Ask user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the final password (minimum 12 characters): ").strip())
            if length < 12:
                raise ValueError("Length must be at least 12 characters.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Get user preferences for password complexity
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    
    # Enhance the base password
    enhanced_password = enhance_password(base_password, length, use_special_chars, use_numbers, use_uppercase)
    
    # Display the enhanced password and its strength
    print(f"Enhanced Password: {enhanced_password} (Strength: {check_password_strength(enhanced_password)})")

if __name__ == "__main__":
    main()
  
