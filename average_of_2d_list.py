#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program finds the average of a 2d list

import random


def av_of_numbers(lst, rows_val, cols_val):
    # this function finds the average value of the list
    total = 0

    for row_counter in lst:
        for col_counter in row_counter:
            total += col_counter
    average = total / (rows_val * cols_val)

    return average


def main():
    # this function generates random numbers and calls another function

    # list declaration
    lst = []

    # input
    rows_string = input("How many rows would you like?: ")
    cols_string = input("How many columns would you like?: ")

    # process -- create 2d list and generate numbers
    try:
        rows_val = int(rows_string)
        cols_val = int(cols_string)
        for counter_rows in range(0, rows_val):
            columns = []
            for counter_cols in range(0, cols_val):
                single_number = random.randint(1, 50)
                columns.append(single_number)
            lst.append(columns)
            print("{0} ".format(columns))  # output

        # output
        average = av_of_numbers(lst, rows_val, cols_val)
        print("The average is {0}".format(average))
    except(Exception):
        print("Invalid Input\nDone.")


if __name__ == "__main__":
    main()
