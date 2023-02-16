# Ask the user to enter the temperature.
temperature = float(input('What is the temperature? Hopefully its nice and warm!!!:'))

# Ask if it is Farenheit or Celcius.
degrees = input('Farenheit or Celcius (F/C)? ')


# Celcius conversion to Farenheit
def get_celcius(temp):
    celsius = temp * 9.0/5.0 + 32.0
    return celsius

# Now we want to return windchill temperatures between speeds of 5-60 mph.
def find_wind(wind):

    # Wind chill conversion = 35.74 + .6215 * temperature - 35.75 * (wind ** .16) + .4275 * temperature * (wind ** .16)
    wind_chill = float(35.74 + .6215 * temperature - 35.75 * (wind ** .16) + .4275 * temperature * (wind ** .16))
    print(f'At temperature {temperature}F, and wind speed {v}mph, the wind chill is: {wind_chill:.2f}F')
    return wind_chill

# If the user enters the temperature in Farenheit, iterate through the range of find_wind.
if degrees.upper().strip() == 'F':
    for v in range(5,65,5):
        find_wind(v)

# If the user enters the temperature by Celcius, we need to first convert 
# the temperature to Farenheit, then return the iterated temperatures.
elif degrees.upper().strip() == 'C':
    temperature = get_celcius(temperature)
    for v in range(5,65,5):
        find_wind(v)

else:
    print('Input Error, please try to not enter a radical input next time!!!')