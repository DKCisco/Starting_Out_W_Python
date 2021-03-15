"""
3. Lap Times
Write a program that asks the user to enter the number of times that they have run around
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
When the loop finishes, the program should display the time of their fastest lap, the time of
their slowest lap, and their average lap time.

"""

# Get the number of laps from user
laps_ran = int(input('Enter the number of laps you ran: '))

# Get the lap times

total_time = 0
slowest_time = 0
fastest_time = 0

for laps in range(1, laps_ran + 1):
    current_lap_time = eval(input("What's the lap time? "))

    # if it's the first lap, it will be our starting point
    if laps_ran == 1:
        slowest_time = current_lap_time
        fastest_time = current_lap_time

     # check if the current lap time is the slowest
    if current_lap_time > slowest_time:
        slowest_time = current_lap_time

    # check if the current lap time is the fastest
    if current_lap_time < fastest_time:
        fastest_time = current_lap_time

    # calculate total time
    total_time += current_lap_time

    # calculate average time
    average_time = total_time / laps_ran

    print('Your fastest lap time is: ', format(average_time, '.1f'), sep='')
    print('Your slowest lap time is: ', format(average_time, '.1f'), sep='')
    print('Your average time is: ', format(average_time, '.1f'), sep='')