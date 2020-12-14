"""
Write an if-else statement that determines whether the points variable is outside
the range of 9 to 51. If the variable’s value is outside this range it should display
“Invalid points.” Otherwise, it should display “Valid points.”

"""
# Input & variable assignment
points = int(input('Number of points:'))

# Process & Output
if points < 51 and points > 9:
    print('Valid points')
else:
    print('Invalid points')

