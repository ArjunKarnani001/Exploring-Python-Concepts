# Task 1: Slicing & Indexing

text = "Python is amazing!"

# First 6 characters
first_word = text[:6]

# Extract the word "amazing"
amazing_part = text[10:17]

# Reverse the entire string
reversed_text = text[::-1]

# Print results with labels
print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_text)

# Task 2: String Methods 

message = " hello, python world! "

# Remove leading/trailing spaces
stripped = message.strip()

# Capitalize first character
capitalized = stripped.capitalize()

# Replace "world" with "universe"
replaced = stripped.replace("world", "universe")

# Convert to uppercase
uppercased = stripped.upper()

# Print results
print("Stripped:", stripped)
print("Capitalized:", capitalized)
print("Replaced:", replaced)
print("Uppercased:", uppercased)


# Task 3: Palindrome Checker 

# Ask user for input
word = input("Enter a word: ")

# Check if word is the same backward
if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Nope, '{word}' is not a palindrome.")
