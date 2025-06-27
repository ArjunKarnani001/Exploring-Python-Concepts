# Task 1: Handle division errors and invalid input

while True:
    try:
        num = int(input("Enter a number: "))  # Ask user for input
        result = 100 / num                   # Try dividing 100 by the number
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero. 🚫")
    except ValueError:
        print("Invalid input! Please enter a valid number. ❌")
    else:
        print(f"100 divided by {num} is {result}. ✅")
        break  # Exit loop if everything is successful


# Task 2: Trigger and handle common exceptions

# IndexError: accessing an invalid index
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 does not exist
except IndexError:
    print("IndexError occurred! List index out of range. ⚠️")

# KeyError: accessing a missing key in a dictionary
try:
    my_dict = {"name": "Arjun"}
    print(my_dict["age"])  # 'age' key is not in the dictionary
except KeyError:
    print("KeyError occurred! Key not found in the dictionary. ⚠️")

# TypeError: adding incompatible types
try:
    result = "5" + 10  # Cannot add string and integer
except TypeError:
    print("TypeError occurred! Unsupported operand types. ⚠️")


# Task 3: Safe division with full exception handling

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed. 🚫")
except ValueError:
    print("Invalid input! Please enter numbers only. ❌")
else:
    print(f"The result is {result}. ✅")
finally:
    print("This block always executes. 🔚")
