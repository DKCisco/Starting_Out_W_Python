"""
A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, then displays the
profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
"""

# Ask user to enter projected income
projected_total_sales = float(input("Enter the projected" + \
                                    "amount of total sales: "))

# Percentage
profit = 0.23 * projected_total_sales

# Print profit
print("$" + format(profit, ",.2f"))

