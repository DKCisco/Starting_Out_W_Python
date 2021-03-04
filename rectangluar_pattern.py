# This program displays a rectangular pattern
# of asterisks.
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))

# Input validation
if rows <= 0:
    print('Bad input! No negatives or 0 allowed.')
    if cols <= 0:
        print('Bad input! No negatives or 0 allowed.')
else:
    for r in range(rows):
        for c in range(cols):
            print('*', end='')
        print()