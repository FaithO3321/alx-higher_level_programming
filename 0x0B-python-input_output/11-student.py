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
        if attrs is None or not isinstance(attrs, list):
            return vars(self)
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
