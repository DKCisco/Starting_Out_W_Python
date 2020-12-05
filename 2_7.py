"""
7. Miles-per-Gallon
A car's miles-per-gallon (MPG) can be calculated with the following formula:
MPG 5 Miles driven 4 Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car's MPG and display the result.

"""

# Receive input
miles_driven = float(input('\nEnter number of miles driven: '))
gallons_of_gas_used = float(input('Enter gallons of gas used: '))

# Calculate MPG
mpg = miles_driven / gallons_of_gas_used

# Output info
print('Miles per gallon = ', format(mpg, ',.2f'))


