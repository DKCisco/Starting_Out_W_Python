"""

Chris owns an auto repair business and has several employees. If any employee works over 40 hours in a week,
he pays them 1.5 times their regular hourly pay rate for all hours over 40. He has asked
you to design a simple payroll program that calculates an employee’s gross pay, including any overtime wages.

"""
# Define Constant Variables
work_week = 40
ot_rate = 1.5

# Input
hours_worked = float(input('Enter the number of hours worked: '))
hourly_rate = float(input('Enter your hourly pay rate: '))

# Process
if hours_worked > work_week:
    # Calculate the pay with OT
    overtime_hours = hours_worked - work_week

    # Calculate the overtime pay
    overtime_pay = overtime_hours * hourly_rate * ot_rate

    # Calculate the total pay
    total_pay = work_week * hourly_rate + overtime_pay
else:
    # Calculate the total pay without overtime
    total_pay = hours_worked * hourly_rate

# Output
print('The total pay for the week is: $', format(total_pay, ',.2f'), sep='')






