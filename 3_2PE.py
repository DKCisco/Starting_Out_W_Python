"""
2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user
which rectangle has the greater area, or if the areas are the same.

"""

# Establsih length and width variables
length_1 = int(input('Enter the length of rectangle 1: '))
width_1 = int(input('Enter the width of rectangle 1: '))
length_2 = int(input('Enter the length of rectangle 2: '))
width_2 = int(input('Enter the width of rectangle 2: '))

# Process and output
if length_1 * width_1 >= length_2 * width_2:
    print('Rectangle 1 has the larger area.')
else:
    print('Rectangle 2 has the larger area.')