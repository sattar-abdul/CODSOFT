# function to perform addition
def add(x, y):
    return x + y

# function to perform subtraction
def subtract(x, y):
    return x - y

# function to perform multiplication
def multiply(x, y):
    return x * y

# function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by 0"
    return x / y

def calculator():
    while True:

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = int(input("Choose an operation:"))

        if choice in (1,2,3,4):

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue

            print("--------------")
            if choice == 1:
                print("Result: ",add(num1, num2))
            elif choice == 2:
                print("Result: ",subtract(num1, num2))
            elif choice == 3:
                print("Result: ",multiply(num1, num2))
            elif choice == 4:
                print("Result: ",divide(num1, num2))
            print("--------------")

        elif choice == 5:
            print("Closing the Calculator")
            break
        else:
            print("Invalid input. Please try again.")

# run the calculator
calculator()
