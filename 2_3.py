"""
3. Pounds to Kilograms
One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
the mass of an object in pounds and then calculates and displays the mass of the object in
kilograms.

"""

# Prompt for input of object mass in pounds, that input is converted to float
mass_lbs = float(input('Please input the mass of the object in pounds: '))

# Calculate and store conversion
mass_kg = mass_lbs * 0.454

# Display the mass in kilograms
print('The mass, ', mass_lbs, 'lbs is ', mass_kg, 'kg.')