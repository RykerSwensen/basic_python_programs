# Create a list of friends using user inputs.

# Create a lists for friends
friends = []

# Make a variable for the loop.
name = None

# When the user enters end, the loop will quit.
while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end":

        # Add the name to the list
        friends.append(name)
print()
print("Your friends are:")

# Print the friends in the list.
for friend in friends:
    print(friend)