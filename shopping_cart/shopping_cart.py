# This project is to create a shopping cart program to get store users input into a list, 
# we want the name and total of each item, we want to be able to add multiple items, 
# be able to remove an item, compute a total, and quit the program.

# Welcome the users to the program.S
print("Welcome to the Shopping Cart Program! I hope you're able to find all the things you want and don't need!")
print()

# Make a list for items and a list for prices.
item_lists = []
prices = []

# declare a variable for a loop, we want it to be set to nothing.
action = ""

# Create a while loop, we know how many options there are. 
# As long as the input is quit/5 the program will run.
while action != "quit":

    # Display all of the options for the user.
    print("Please select one of the following:\n" "1. Add item\n" "2. View cart\n" "3. Remove item\n" "4. Compute total\n" "5. Quit\n")

    # Get the users input, we want to set that input to the variable we created.
    action = input("Please enter an action: ")
    print()

    # Add item
    if action == "1":

        # Get the item the user wants to add.
        item = input("What item would you like to add?: ")

        # Add the input to the item list.
        item_lists.append(item)

        # Get the price the item the user entered?
        # .capitalize will capitalize the name of the item.
        price = float(input(f"What is the price of '{item.capitalize()}'?: "))

        # Add the price to the price list. 
        prices.append(price)
        print(f"'{item.capitalize()}' has been added to the cart.\n")

    # View cart
    elif action == "2":
        print("The items in your shopping cart are: \n")

        # Find all items and prices in the lists.
        for i in range(len(item_lists)) and range(len(prices)):

            # Contents in item list.
            item = item_lists[i]

            # Contents in price list.
            price = prices[i]

            # Print both lists content.
            combo = (f"{i + 1}. {item.capitalize()} - ${float(prices[i]):.2f}")
            print(combo)
            print()
    
    # Remove Item 
    elif action == "3":
        index = int(input("What item would you like to remove? "))

        # pop will remove the items in the list. 
        item_lists.pop(index - 1)
        prices.pop(index - 1)
        print()

    # Compute Total
    elif action == "4":
        total = 0

        # Find all of the prices in the list.
        for i in range(len (item_lists)): 

            # Add all of the prices together.
            total += float(prices [i])
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    # Quit Program
    elif action == "5":
        
        # Set action to quit, then the loop breaks and program ends.
        action = "quit"
        end = ("Maybe you should reconsider and spend some money here!")
        print(end)
