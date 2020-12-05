"""
4. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent.
"""

# Price of the first item input by user
item_1 = float(input("Please enter the price of the first item: "))

# Price of the second item input by user
item_2 = float(input("Please enter the price of the second item: "))

# Price of the third item input by user
item_3 = float(input("Please enter the price of the third item: "))

# Price of the fourth item input by user
item_4 = float(input("Please enter the price of the fourth item: "))

# Price of the fifth item input by user
item_5 = float(input("Please enter the price of the fifth item: "))

# Calculate the subtotal by adding all items together
subtotal = item_1 + item_2 + item_3 + item_4 + item_5

# Calculate tax rate
tax = 0.07 * subtotal

# Calculate Total and assign the variable
total = subtotal + tax

# Display Results formatted in dollars with commas
print("Subtotal: $" + format(subtotal, ",.2f"),"Tax Amount: $" + \
      format(tax , ",.2f"), "Total: $" + format(total, ",.2f"), \
      sep = "\n")

