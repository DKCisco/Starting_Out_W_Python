"""
 Write an if statement that assigns 10 to the variable b,
 and 50 to the variable c if the variable a is equal to 100.

"""
# Input
print('The value of A, B, and C is dependent of the value of A .')
a = int(input('Input the value of A: '))

# Process & Output
if a >= 100:
    b = 10
    c = 50
    print('The value of A',a,'B',b,'And C',c)
else:
    b = 0
    c = 0
    print('The value of A',a,'B',b,'And C',c)