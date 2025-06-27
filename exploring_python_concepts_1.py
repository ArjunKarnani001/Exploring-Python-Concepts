# Task 1: Describe yourself using variables

name = "Arjun"
age = 20
height = 5.10

# Print a friendly introduction
print(f"Hey there, my name is {name}! I’m {age} years old and {height} feet tall.")

# Task 2: Basic math with two numbers

num1 = 8
num2 = 3

# Addition
print("The sum of", num1, "and", num2, "is", num1 + num2)

# Subtraction
print("The difference when we subtract", num2, "from", num1, "is", num1 - num2)

# Multiplication
print("Multiplying", num1, "and", num2, "gives us", num1 * num2)

# Division
print("Dividing", num1, "by", num2, "gives us", num1 / num2)

# Bonus: show off a little!
print("See? Math can be fun when Python does it for you!")


# Task 3: Positive, Negative, or Zero?

# Ask the user for a number
user_input = input("Enter a number, any number: ")

# Convert input to a number (we'll use float to allow decimals too!)
number = float(user_input)

# Check if the number is positive, negative, or zero
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
