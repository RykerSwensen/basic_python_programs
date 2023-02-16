# Import math library. We can use the squareroot 
import math

print('Welcome to the velocity calculator. Please enter the following:\n')

# Prompt for inputs
# Use the conversion methods
m = float(input('What is the mass in kilograms?: '))
g = float(input('What is the gravity in m/s^2? (9.8 for earth, 24 for jupiter): '))
t = float(input('What is the time in seconds?: '))
p = float(input('What is the density of the fluid in kg/m^3? (1.3 for air, 1000 for water): '))
A = float(input('What is the cross sectional area in m^2?: '))
C = float(input('What is the drag constant? (0.5 for sphere, 1.1 for cylinder): '))
c = (1/2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Return the velovity.
print(f'The inner value of c is: {c:.3f}.')
print(f'The velocity after {t} seconds is: {v:.3f} m/s.')
print()
