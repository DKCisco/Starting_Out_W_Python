"""

9. Circle Measurements
Write a program that asks the user to enter the radius of a circle. The program should calculate and display the area and circumference of the circle using πr2 for the area and 2πr
for the circumference.
Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in
the program.

"""

import math

# Input from user
radius = float(input('\nRadius of a circle: '))

# Process
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

# Output
print('Area', format(area, ',.4f'))
print('Radius', format(radius, ',.4f'))
print('Circumference', format(circumference, ',.4f'))
