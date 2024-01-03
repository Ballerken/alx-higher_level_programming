#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    char = chr(char_code)
    if chr(char_code) != 'e' and char != 'q':
        print("{}".format(chr(char_code)), end="")
