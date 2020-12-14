"""
The following code contains several nested if-else statements. Unfortunately, it
was written without proper alignment and indentation. Rewrite the code and use the
proper conventions of alignment and indentation.

"""
# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
score = float(input('Enter the score value: ')) # User inputs score

# Process and Output, comparing score to constant variables.
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')