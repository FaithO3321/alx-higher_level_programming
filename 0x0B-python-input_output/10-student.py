#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attributes = vars(self)
        if attrs is None:
            return attributes

        serializable_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                serializable_dict[attr] = getattr(self, attr)
        return serializable_dict
