#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_pr = my_list[:]
    if idx >= 0 and idx < len(new_pr):
        new_pr[idx] = element
    return new_pr
