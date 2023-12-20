#!/usr/bin/python3

def raise_exception_msg(message=""):
    """that raises a name exception with a message."""
    try:
        raise NameError(message)
    except NameError as ne:
        print(ne)
