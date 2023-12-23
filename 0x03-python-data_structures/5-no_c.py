#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for i in range(len(my_string)):
        if (my_string[i] == 'c') or (my_string[i] == 'C'):
            result
        else:
            result += my_string[i]
    return result
