#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg == 1:
        print("0 arguments.")
    elif arg == 2:
        print("1 argument: ")
    else:
        print("{} arguments: ".format(arg -1))
    for index in range (1, arg):
        print("{}: {}".format(index, sys.argv[index]))

