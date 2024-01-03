#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit_str = number_str[-1]
First = "Last digit of"
Last = "is greater than 5"
Last1 = "is less than 6 and not 0"
if number > 5:
    print("{} {} is {} and {}".format(First, number, last_digit_str, Last))
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit_str))
else:
    if number < 0:
        last_digit_str = "-" + last_digit_str
    print("{} {} is {} and {}".format(First, number, last_digit_str, Last1))
