# Task 1: Functions to greet and add

def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

# Example usage
greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")


# Task 2: Function with default parameter

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage
describe_pet("Buddy")          # Uses default: dog
describe_pet("Whiskers", "cat")


# Task 3: Function with variable number of arguments

def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

# Example usage
make_sandwich("Lettuce", "Tomato", "Cheese")


# Task 4.1: Recursive factorial function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Task 4.2: Recursive fibonacci function

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")
