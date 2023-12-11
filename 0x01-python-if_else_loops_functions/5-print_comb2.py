#!/usr/bin/python3
for num in range(100):
    print("{:02}".format(num), end=", " if num < 99 else "\n")
