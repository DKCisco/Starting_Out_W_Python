"""

10. Ingredient Adjuster
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, then displays the number of cups
of each ingredient needed for the specified number of cookies.

"""

# Input from user for cookie amount being baked
number_of_cookies = float(input('Amount of cookies needed: '))

# Constant variables for recipe for 48 cookies
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
COOKIES = 48

# Calculate the recipe based on user input of number of cookies
toal_sugar = float(SUGAR * number_of_cookies) / COOKIES
toal_butter = float(BUTTER * number_of_cookies) / COOKIES
total_flour = float(FLOUR * number_of_cookies) / COOKIES

# Output the calculated recipe based on user input of number of cookies
print('\nNumber of cookies: ', number_of_cookies, end='\n\n')
print('Total sugar: ', format(toal_sugar, ',.2f'), end='\n\n')
print('Total flour: ', format(total_flour, ',.2f'), end='\n\n')
print('Total butter: ', format(toal_butter, ',.2f'), end='\n\n')



