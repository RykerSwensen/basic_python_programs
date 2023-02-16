# Lets start by understanding how to convert fahrenheit to celcsius. 
# The conversion is (temperature in fahrenheit - 32) * (5/9)

# To start we need to get the temperature in Fahrenheit
temperature_in_fahrenheit = float(input('What is the temperature in Fahrenheit? '))

# Using the conversion above, lets convert the users temperature to celsius
temperature_in_celsius = (temperature_in_fahrenheit - 32) * (5/9)

# Print out the conversion!
print(f'The temperature in Celsius is {temperature_in_celsius}')
print()