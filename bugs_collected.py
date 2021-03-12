"""
1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.

"""


def main():
    # Call an intro function so the user doesn't have to
    # press Enter to start the function.
    intro()

    # Initialize an accumulator variable.
    bugs_collected = 0.0

    # Ask the user to enter the number of bugs collected for each
    # of the 5 days.
    for counter in range(5):
        daily = int(input('Enter the number of bugs collected daily: '))
        bugs_collected = bugs_collected + daily

    # Display the total bugs collected.
    print('The total number of bugs collected over 7 days was', bugs_collected)


def intro():
    # Explain what we are doing.
    print('This program calculates the sum of')
    print('the number of bugs collected over')
    print('a 5 day period.')


# Call the main function.
main()