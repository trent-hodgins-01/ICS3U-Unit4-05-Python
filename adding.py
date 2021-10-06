# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/05/2021
# This is an adding program
# The user enters in the number of numbers they would like to add
# The user then enters the numbers they would like to add


def main():
    # this function does addition math
    answer = 0

    # input
    number_of_numbers = input("How many numbers are you going to add: ")

    # input process and output
    try:
        number_of_numbers_integer = int(number_of_numbers)
        for loop_counter in range(number_of_numbers_integer):
            number_to_add = input("Enter a number to add: ")
            number_to_add_as_int = int(number_to_add)
            if number_to_add_as_int < 0:
                continue
            answer = answer + number_to_add_as_int

        print("Sum of the positive numbers is: {0}".format(answer))

    except Exception:
        print("You didn’t enter in a number.")

    print("\nDone")


if __name__ == "__main__":
    main()
