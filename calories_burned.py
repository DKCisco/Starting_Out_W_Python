"""
2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

"""
# Define the variable
CALS_BURNED_PER_MIN = 4.2

for minutes in range(10, 31, 5):
    CALORIES = int(minutes * CALS_BURNED_PER_MIN)
    print('You burned', CALORIES, 'Calories in', minutes, 'minutes.')