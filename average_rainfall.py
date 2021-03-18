"""

5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.

"""

# Get number of years from the user
years_total = int(input('Enter the number of years to track: '))

# Assign the number of months in a year
months = 12

# Accumulator
total = 0.0

for years_rain in range(years_total):
    print('\nYear Number', years_rain + 1 )
    print('------------------------------')
for month in range(months):
        print('How many inches for month ', month + 1, end='')
        rain = int(input(' Enter rain amount: '))
        total += rain

number_months = years_total * months
average = total / number_months

print('The total inches of rain was ', format(total,'.2f'))
print('The number of months measured was', number_months)
print('The average rainfall was', format(average, '.2f'), 'inches')