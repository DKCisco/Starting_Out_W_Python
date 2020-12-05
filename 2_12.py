"""
12. Stock Transaction Program
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 2,000.
• When Joe purchased the stock, he paid $40.00 per share.
• Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
for the stock.
Two weeks later, Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 2,000.128 Chapter 2 Input, Processing, and Output
• He sold the stock for $42.75 per share.
• He paid his stockbroker another commission that amounted to 3 percent of the amount
he received for the stock.
Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount for which Joe sold the stock.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount is positive, then Joe made a profit. If the amount is
negative, then Joe lost money.

"""

# Assign Constant variables
BROKER_COMMISSION = .03
amount_shares_purchased = 2000
shares_purchased = 2000
price_per_share = 40.00



# Process amounts for stock and commission paid
amount_paid_for_stock = shares_purchased * price_per_share
commission_paid_when_bought = amount_paid_for_stock * BROKER_COMMISSION


# Output amounts for stock and commission paid for
print('\nAmount paid for stock: $', \
      format(amount_paid_for_stock, ',.2f'),sep ='')
print('\nAmount of commission paid at stock purchase: $', \
    format(commission_paid_when_bought, ',.2f'), sep='')

# Define variables for stock sold
shares_sold = 2000.128
price_per_share = 42.75
amount_shares_sold = shares_sold * price_per_share
commission_paid_when_sold = amount_shares_sold * BROKER_COMMISSION
total_commision_paid = commission_paid_when_bought + commission_paid_when_bought
profit = amount_shares_sold - amount_paid_for_stock - total_commision_paid

# Output amounts for stock sold
print('\nPrice per share at sell: $', format(price_per_share, ',.2f'), sep='')

print('\nAmount shares sold for: $', format(amount_shares_sold, ',.2f'), sep='')

print('\nCommission paid when sold: $', format(commission_paid_when_sold, ',.2f'), sep='')

print('\nTotal profit: $', format(profit, ',.2f'), sep='')


