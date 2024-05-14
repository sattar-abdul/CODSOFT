import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice to select characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator")
    
    try:
        # Prompt user to specify the length of the password
        length = int(input("Enter the length of the password: "))
        
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
        
        # Generate password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
