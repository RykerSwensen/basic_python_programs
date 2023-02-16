# This program is designed to get the area of a square, 
# volume of a cube, 
# area of a rectangle, 
# area of a circle, 
# and volume of a sphere.

# Get the length of one side, that is all we need as all sides of a square are the same.
length_of_side_of_square = int(input('What is the length of one side of the square in centimeters? '))

# area of a square is to multiply 2 sides. To convert centimeters to meters you / 10000
area_of_square = (length_of_side_of_square * length_of_side_of_square) / 10000

# Volume of a cube = length of side ^ 3  /  10000
volume_of_cube = (length_of_side_of_square ** 3) / 10000
print(f'The area of the square is {area_of_square} square meters.')
print(f'The volume of the cube {volume_of_cube} square meters.')
print()


# To get the dimensions of a rectangle we need length and width. 
length_of_rectangle = int(input('What is the length of the rectangle in centimeters? '))
width_of_rectangle = int(input('what is the width of the rectangle in centimeters? '))

# Area of rectangle = length * width / 10000
area_of_rectangle = (length_of_rectangle * width_of_rectangle) / 10000
print(f'The area of the rectangle is {area_of_rectangle} square meters.')
print()

# Get the radius of the circle
radius_of_circle = int(input('What is the radius of the circle in centimeters? '))
sign = 1
pie = 0
for i in range(1, 1_000_000, 2):
    pie += sign * 1/i
    sign *= -1
pi = 4 * pie
area_of_circle = (pi * (radius_of_circle ** 2)) / 10000
volume_of_sphere = ((4/3) * pi * (radius_of_circle ** 3)) / 10000
print(f'The area of the circle is {area_of_circle} square meters.')
print(f'The volume of the sphere is {volume_of_sphere} square meters.')
print()
#\n inside the string to leave spaces before and after! use this to practice for. 
# round(whatever, 2) round to 2 decimal places in code. 