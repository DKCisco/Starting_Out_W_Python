"""
Write an if statement that uses the turtle graphics library to determine whether the
turtle’s pen size is greater than 1 or the pen color is red. If so, set the pen size to 1 and
the pen color to blue.

"""
# Define variables
import turtle
import time

# Process and output
if turtle.pencolor() == 'red' and turtle.pensize() > 1:
    turtle.pencolor()
else:
    turtle.pencolor('red'), turtle.pensize(1)

print(turtle.pencolor(), turtle.pensize())