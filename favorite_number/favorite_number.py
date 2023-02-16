# Ask the user for two numbers, find which one is greater. 
# Ask the user for their favorite animal, compare it to your
# favorite animal.

# Prompt for numbers
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

# Compare the numbers
if first_number > second_number:
    print('The first number is greater!')
elif first_number == second_number:
    print('The numbers are equal!')
else:
    print('The second number is greater!')
print()


# Prompt for favorite animal.
user_favorite_animal = input('What is your favorite animal? ')

# My favorite animal is dog, so the right answer is dog! ;)
if user_favorite_animal.lower() == 'dog':
    print('Thats my favorite animal too!')
else:
    print('That is a unique choice... However, it is the wrong choice, that is not my favorite animal.')