# Task 1: Fruit List 

# Creating a list of favorite fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# Appending a new fruit
fruits.append('fig')
print("After adding a fruit:", fruits)

# Removing a fruit (let’s remove 'apple')
fruits.remove('apple')
print("After removing a fruit:", fruits)

# Printing the list in reverse order using slicing
reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)


# Task 2: Dictionary of Me

# Creating a dictionary with some basic info
my_info = {
    "name": "Arjun",
    "age": 20,
    "city": "Houston"
}

# Adding a new key-value pair
my_info["favorite color"] = "Blue"

# Updating the city
my_info["city"] = "Austin"

# Printing all keys and values
print("Keys:", ", ".join(my_info.keys()))
print("Values:", ", ".join(str(value) for value in my_info.values()))


# Task 3: Tuple Time 

# A tuple of favorite things
favorites = ("Inception", "Bohemian Rhapsody", "1984")
print("Favorite things:", favorites)

# Try to change one element (uncomment to see the error)
# favorites[0] = "Interstellar"  # ❌ This will raise a TypeError

print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(favorites))
