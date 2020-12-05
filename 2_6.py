"""
6. Payment Instalments
Write a program that asks the user to enter the amount of a purchase and the desired
number of payment instalments. The program should add 5 percent to the amount to get
the total purchase amount, and then divide it by the desired number of instalments, then
The Sales
Prediction ProblemProgramming Exercises 127
display messages telling the user the total amount of the purchase and how much each
instalment will cost.

"""

# Prompt user to input amount of purchase
amount_of_purchase = float(input('Enter the amount of purchase: $'))

# Prompt user for desired number of payment instalments
number_of_installments = int(input('Enter the desired number of payments: '))

# Assign PERCENTAGE variable
PERCENTAGE = .05

# Calculate
total_purchase_amount = (PERCENTAGE * amount_of_purchase) + amount_of_purchase
installment_amount = total_purchase_amount / number_of_installments

# Display
print('Amount of purchase: $', format(amount_of_purchase, ',.2f'), sep = '')
print('Number of installments = ', number_of_installments)
print('Installment amount: $', format(installment_amount, ',.2f'), sep = '',)




