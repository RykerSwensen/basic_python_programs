# This is a program to demonstrate addition, multiplication, and division operators
# in Python.

# Prompt for users age
age = int(input('What is your age? '))

# There age next year is just +1
next_year_age = age + 1
print(f'On your next birthday you will be {next_year_age}.')
print()

# Prompt for cartons of eggs.
cartons = int(input('How many cartons of eggs do you have? '))

# 12 Eggs per carton. Cartons * 12
eggs = cartons * 12
print(f'You have {eggs} eggs.')
print()

# Prompt for cookies and people.
cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))

# Cookies per person = cookies / people
cookies_per_person = cookies / people
print(f'Each person can have {cookies_per_person} cookies.')
print()