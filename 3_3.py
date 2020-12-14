"""
Write an if-else statement that assigns 0 to the variable b if the variable
a is less than 10. Otherwise, it should assign 99 to the variable b.

"""
# Assign variables
a = int(input('Enter the value of a: '))

# Process
if a < 10:
    b = 0
else:
    b = 99

# Output
print('The value of b =', b)