#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-10-30
# This program outputs the sum of all integer preceding the user's
# integer.


def main():

    # Tries to get the user_number as a positive integer.
    try:
        user_number = int(input("Enter a positive integer: "))

    # If the user does not enter a number
    except ValueError:
        print("You need to enter a positive integer.")
        main()
    # If the user enters a negative number it Restarts the program
    if user_number < 0:
        print("You need to enter a positive integer.")
        main()
    # Counter and sum variables
    counter = 0
    sum = 0

    # Executed continually until user_number is equal to counter
    while user_number >= counter and user_number >= 0:
        sum = sum + counter
        print(f"Looped through {counter} times.")
        counter += 1

    # The total of all numbers that come before the user's number is displayed.

    if user_number >= 0:
        print(
            f"The sum of the consecutive positive integers preceding {user_number} is {sum}."
        )


if __name__ == "__main__":
    main()
