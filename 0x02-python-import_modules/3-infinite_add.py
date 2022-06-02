#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    Add = 0
    for num in range(1, count):
        Add += int(sys.argv[num])
    print("{}".format(Add))
