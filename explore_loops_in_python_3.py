# Task 1: Countdown Timer

# Ask the user for a starting number
start = int(input("Enter the starting number for countdown: "))

# Count down using a while loop
while start > 0:
    print(start, end=" ")
    start -= 1

# After countdown ends
print("Blast off!")


# Task 2: Multiplication Table

# Ask the user for a number
num = int(input("Enter a number to generate its multiplication table: "))

# Print the table from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    

# Task 3: Factorial Calculator

# Ask the user for a number
n = int(input("Enter a number to find its factorial: "))

# Start with 1 (since factorial of 0 is 1 too!)
factorial = 1

# Multiply from 1 up to the number
for i in range(1, n + 1):
    factorial *= i

# Show the result
print(f"The factorial of {n} is {factorial}.")

