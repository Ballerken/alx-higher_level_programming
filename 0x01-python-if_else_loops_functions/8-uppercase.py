#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            diff = ord('A') - ord('a')
            uppercase_char = chr(ord(char) + diff)
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")
    print("")
