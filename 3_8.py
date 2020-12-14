"""
Write an if statement that uses the turtle graphics library to determine whether the
turtle’s heading is in the range of 0 degrees to 45 degrees (including 0 and 45 in the
range). If so, raise the turtle’s pen.

"""

# Input
import turtle

# Variable assignment.
turtle.setheading(41)
angle = turtle.heading()

# Output
turtle.setheading(angle)
if angle > 0 and angle < 45:
    turtle.penup()
    turtle.done