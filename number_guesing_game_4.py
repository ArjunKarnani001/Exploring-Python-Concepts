import random

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Step 2: Initialize variables
attempts = 0
max_attempts = 10

print("🎉 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Step 3: Loop until the correct guess or max attempts
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again. ⬇️")
    elif guess > number_to_guess:
        print("Too high! Try again. ⬆️")
    else:
        print(f"🎊 Congratulations! You guessed it in {attempts} attempt(s)!")
        break
else:
    print("😢 Game over! Better luck next time!")
    print(f"The number was: {number_to_guess}")
