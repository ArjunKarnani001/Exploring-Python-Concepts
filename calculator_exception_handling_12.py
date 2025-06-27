import logging

# Step 4: Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def get_number(prompt):
    """Get a number from the user with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error("ValueError occurred: %s", e)

def calculator():
    print("Welcome to the Error-Free Calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                if choice == '1':
                    result = num1 + num2
                    operation = "Addition"
                elif choice == '2':
                    result = num1 - num2
                    operation = "Subtraction"
                elif choice == '3':
                    result = num1 * num2
                    operation = "Multiplication"
                elif choice == '4':
                    result = num1 / num2
                    operation = "Division"
                print(f"{operation} result: {result}")
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error("ZeroDivisionError occurred: %s", e)
            except Exception as e:
                print("An unexpected error occurred.")
                logging.error("Unexpected error: %s", e)
            finally:
                print("Operation attempted.\n")
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
calculator()
