# Create a basic gradebook program to print the users letter grade.

# Prompt for their grade percentage.
grade = int(input('What is your grade percentage? '))

# 90+ = A, 80+ = B, 70+ = C, 60+ = D, Else = F
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
sign = ''

# There are no A-, F+, or F-
last_digit = grade % 10
if last_digit >= 7:
    sign = '+'
elif last_digit <= 3:
    sign = '-'
else:
    sign = ''
if grade >= 90:
    sign = ''
if grade <= 59:
    sign = ''

print(f'Your letter grade is {letter}{sign}.')

if grade >= 90:
    print('Good job!')
else:
    print('Better luck next time!')