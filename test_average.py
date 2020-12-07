"""

This program calculates the average of 3 test scores using decision structure.

"""
# Assign varibale to score above 95% average.
HIGH_AVERAGE = 95

# Get the test scores from user.
test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))

# Calculate the average test score
average = (test1 + test2 + test3) / 3

# Print the average.
print("The average score is: %s %%\n" % average)

# Congratulate the user based on if the score is above or equal to 95.
if average >= HIGH_AVERAGE:
    print('Congratulations on scoring 95% or better, Einstein would be proud')
    print('That is a great average!')
