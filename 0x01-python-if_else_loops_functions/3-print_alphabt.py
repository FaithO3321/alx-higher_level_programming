#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z')+1):
    char = chr(ascii_value)
    if char not in 'qe':
        print("{}".format(char), end='')
