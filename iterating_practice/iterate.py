# This program is used to demonstrate iterating through a list of items.

# Let's make a list of colors.
colors = ["red", "blue", "green", "yellow"]

# Print the colors inside of the list of colors.
for color in colors:
    print(color)

# Print a blank line to seperate the iterating examples.
print() 

# Now, let's iterate through a list of numbers.
for i in range(1, 9):
    print(i)
print()


# Iterate by even numbers.
# Start at 2, go up through, but not including 21, and count by 2.
for i in range(2, 21, 2):
    print(i)
