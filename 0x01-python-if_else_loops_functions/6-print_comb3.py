#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        con = ", " if tens_digit * 10 + ones_digit < 89 else "\n"
        print("{:02d}{:s}".format(tens_digit * 10 + ones_digit, con), end="")
