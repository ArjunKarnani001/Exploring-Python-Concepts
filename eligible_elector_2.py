# Voter Eligibility Checker

# Step 1: Ask the user's age
age = int(input("How old are you? "))

# Step 2: Decide the eligibility
if age >= 18:
    # User is old enough to vote
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    # User is not eligible yet – calculate how many years to wait
    years_left = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more year(s) to go!")

# Step 3: Add a finishing touch
print("Thank you for checking your voter eligibility. Stay informed!")
