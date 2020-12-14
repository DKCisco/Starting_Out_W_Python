"""
Write an if-else statement that assigns True to the again variable
if the score variable is within the range of 40 to 49.
If the score variable’s value is outside this range,
assign False to the again variable.

"""
# Input & Assign
score = int(input('Enter the value for score: '))

# Process
if score < 49 and score > 40:
    again = False
else:
    again = True


# Output
print('The value of again = ', again)