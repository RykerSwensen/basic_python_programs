# This is a basic python program that is developed to decide
# if the rider can or cannot ride the ride.

# Get the age of the rider
first_rider_age = int(input('What is the age of the first rider? '))

# Get the height of the rider
first_rider_height = int(input('What is the height of the first rider in inches? '))

# Ask if they are with another rider, supervised riders have 
# different requirements.
second_rider_question = input('Is there a second rider? YES or NO ')

# If there is a second rider, 
if second_rider_question.lower == ('yes'):

    # Ask for the second riders age.
    second_rider_age = int(input('What is the age of the second rider?'))

    # Ask for the second riders height.
    second_rider_height = int(input('What is the height of the second rider?'))
else:
    print()

# If there is not a second rider,
if second_rider_question.lower() == ('no'):

    # if they are 18 or older and they are 62 inches or taller, 
    # then they are allowed to ride the ride.
    if first_rider_age >= 18 and first_rider_height >= 62:
        print('Congratulations! You are allowed to ride this ride!')

    # If not they cannot ride the ride.
    else:
        print('Sorry, you are not allowed to ride this ride!')

# If there is a second rider, 
elif second_rider_question.lower() == ('yes'):

    # if the first rider is 18 or older and has a height of 36 or taller, 
    if first_rider_age >= 18 and first_rider_height >= 36:

        # and if the second rider is 36 inches or taller, then they can both ride the ride.
        if second_rider_height >= 36:
            print('Congatulations! You both are allowed to ride this ride!')

        # Else they cannot ride the ride.
        else:
            print('Sorry, only the first rider can ride this ride!')

    # Else if the second rider is 18 or older and taller than 36 inches,
    elif second_rider_age>=18 and second_rider_height>= 36:

        # and if the first rider is 36 inches or taller, then they can ride the ride. 
        if first_rider_height >= 36:
            print('Congatulations! You both are allowed to ride this ride!')

        # Else they cannot ride the ride.
        else:
            print('Sorry, only the second rider is allowed to ride this ride!')

# Else they cannot ride the ride.
else:
    print('Sorry, we could not let you on today, please try another ride!')