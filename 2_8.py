"""

8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, then calculate the amounts
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

"""

# Input from user amount of meal
meal_amount = float(input('\nEnter the amount of the meal: $'))

# Assign * calculate tip
TIP_PERCENTAGE = .18
tip = meal_amount * TIP_PERCENTAGE

# Assign tax
SALES_TAX = .07
tax = meal_amount * SALES_TAX

# Calculate grand total
grand_total = tip + meal_amount + tax

# Display each amount and the total
print('Meal amount = $', format(meal_amount, ',.2f'), sep='')
print('Tip percentage = %', format(TIP_PERCENTAGE, ',.2%'))
print('Tip amount = $', format(tip, ',.2f'), sep='')
print('Grand Total = $', format(grand_total, ',.2f'), sep='')