# This program calculates the sum of a series
# of numbers entered by the user.

MAX = 5 # The maximum number

# Initialize an accumulator variable.
total = 0.0

# Explain what we are doing.
print('This program calculates the sum of')
print(MAX,'numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

# Displays the total of the numbers.
print('The total is', total)