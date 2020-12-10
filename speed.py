# Assign variable from Input
speed = int(input('What is your speed: '))

# Process & Output
if speed >= 0 and speed <= 200:
    print('The number is valid')
else:
    print('The number is invalid.')