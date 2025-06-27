# Inventory Manager

# Step 1: Start with an inventory dictionary
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Function to display the inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    print()

# Function to calculate total inventory value
def calculate_total_value():
    total = sum(quantity * price for quantity, price in inventory.values())
    print(f"Total value of inventory: ${total:.2f}\n")

# Step 2: Add, Remove, and Update Items
def add_item():
    item = input("Enter item name to add: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    inventory[item] = (quantity, price)
    print(f"Added {item} to inventory.")

def remove_item():
    item = input("Enter item name to remove: ")
    if item in inventory:
        del inventory[item]
        print(f"Removed {item} from inventory.")
    else:
        print("Item not found.")

def update_item():
    item = input("Enter item name to update: ")
    if item in inventory:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[item] = (quantity, price)
        print(f"Updated {item}.")
    else:
        print("Item not found.")

# Step 3: Main loop
def inventory_manager():
    print("Welcome to the Inventory Manager!")

    while True:
        print("\nChoose an option:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Calculate Total Value")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            calculate_total_value()
        elif choice == '6':
            print("Thanks for using the Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the inventory manager
inventory_manager()
