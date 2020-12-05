"""

11. Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered in a class.
The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

"""

# Input
male_number = int(input('Enter the number of males: '))
female_number = int(input('Enter the number of females: '))

# Process
class_size = int(male_number + female_number)
percentage_males = (male_number / class_size)
percentage_females = (female_number / class_size)

# Output calculated percentages
print('The class size is: ', class_size)
print('Percentage of males: ', format(percentage_males, '.0%'))
print('Percentage of females: ', format(percentage_females, '.0%'))
