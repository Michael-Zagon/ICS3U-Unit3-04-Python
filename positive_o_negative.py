#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program determines if a number is positive, negative or neutral.


def main():
    # This function determines if a number is positive, negative or neutral.

    # Input
    integer = int(input("Enter an integer: "))
    print("")

    # Process and output
    if integer > 0:
        print("This is a positive number")
    elif integer < 0:
        print("This is a negative number")
    else:
        print("This is a neutral number")

    print("\nDone.")


if __name__ == "__main__":
    main()
