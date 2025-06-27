import turtle  # Used for fractal drawing (Bonus)
import sys

# Step 1: Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Step 2: Recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 3: Recursive fractal drawing (tree example)
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Step 4: Input validator for positive integers
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer. 🚫")
            else:
                return value
        except ValueError:
            print("That’s not a valid number. Try again!")

# Step 5: Menu system
def display_menu():
    print("\nWelcome to the Recursive Artistry Program!")
    print("Choose an option:")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci Number")
    print("3. Draw a Recursive Fractal Tree (Bonus)")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("> ")

        if choice == '1':
            num = get_positive_integer("Enter a number to find its factorial: ")
            print(f"The factorial of {num} is {factorial(num)}.")

        elif choice == '2':
            n = get_positive_integer("Enter the position of the Fibonacci number: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

        elif choice == '3':
            print("Drawing a fractal tree... close the window to return to menu.")
            screen = turtle.Screen()
            screen.bgcolor("white")
            t = turtle.Turtle()
            t.color("green")
            t.left(90)
            t.up()
            t.backward(100)
            t.down()
            t.speed(0)
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == '4':
            print("Thanks for exploring recursion with us. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

# Run the main program
main()
