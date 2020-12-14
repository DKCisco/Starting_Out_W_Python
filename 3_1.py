"""
 Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z
 if the variable x is greater than 100.

"""
# Input
print('The value of Y and Z is dependent of the size of x.')
x = int(input('What is the value of x: '))

# Process & Output
if x >= 100:
    y = 20
    z = 40
    print('The value of X',x,'Y',y,'And z',z)
else:
    y = 0
    z = 0
    print('The value of X',x,'Y',y,'And z',z)