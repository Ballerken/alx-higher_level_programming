#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print(f"{num_arguments} arguments.")
    else:
        plural = "s" if num_arguments > 1 else ""
        print(f"{num_arguments} argument{plural}:")

        for idx, arg in enumerate(arguments, start=1):
            print(f"{idx}: {arg}")


if __name__ == "__main__":
    main()
