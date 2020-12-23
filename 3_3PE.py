"""
3. Quarter of the Year
Write a program that asks the user for a month as a number between 1 and 12. The
program should display a message indicating whether the month is in the first quarter,
the second quarter, the third quarter, or the fourth quarter of the year. Following are the
guidelines:
•	 If the user enters either 1, 2, or 3, the month is in the first quarter.
•	 If the user enters a number between 4 and 6, the month is in the second quarter.
•	 If the number is either 7, 8, or 9, the month is in the third quarter.
•	 If the month is between 10 and 12, the month is in the fourth quarter.
•	 If the number is not between 1 and 12, the program should display an error.

"""

#Input
month_number = int(input('Input a month as a number between 1 and 12:  '))
display_text = ""

if month_number < 1 or month_number > 12:
    display_text = "\nError. 12 months in a year. Please enter a 1 - 12 whole digit.\n"
else:
    display_text = "\nMonth " + format(month_number) + " is in the"

    if month_number >= 1 and month_number <= 3:
        display_text += " first"

    elif month_number >= 4 and month_number <= 6:
        display_text += " second"

    elif month_number >= 7 and month_number <= 9:
        display_text += " third"

    elif month_number >= 10 and month_number <= 12:
        display_text += " fourth"

    display_text += " quarter.\n"

print(display_text)