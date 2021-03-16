"""
4. Distance Traveled
The distance a vehicle travels can be calculated as follows:
distance = speed * time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is
120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
and the number of hours it has traveled. It should then use a loop to display the distance
the vehicle has traveled for each hour of that time period. Here is an example of the desired
output:
What is the speed of the vehicle in mph? 40 Enter
How many hours has it traveled? 3 Enter
Hour Distance Traveled
1 40
2 80
3 120

"""

# Assign variables based on user input
vehicleSpeed = float(input("What is the speed of the vehicle: "))
timeTraveled = int(input("How many hours has it traveled?: "))

# Calculate and print Hours and Distance Traveled
print("Hour", "\tDistance Traveled")
for currentHour in range(1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t", distanceTraveled)






