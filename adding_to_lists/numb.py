# Create a list of numbers from user inputs.

# Create a list.
numbers = []

# Create a variable for the loop.
numero = None

# When the user enters 0 the loop will end.
while numero != 0:
    numero = int(input("Enter number: "))
    if numero != 0:

        # Add number to the list.
        numbers.append(numero)
print()

# Print numbers in the list.
for number in numbers:
    print(number)
