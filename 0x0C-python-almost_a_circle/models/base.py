#!/usr/bin/python3
"""
Write the first class Base:
"""
import json
import os
import csv


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in projects 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string of a list of dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class constructor"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """class constructor"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class constructor"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """class constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """class constructor"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
        instances = []
        instances = [cls.create(**dictionary) for dictionary in list_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """y overriding the __str__ method"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id,
                                    obj.width, obj.height,
                                    obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """instance with the character #"""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    instance = cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4])
                            )
                elif cls.__name__ == 'Square':
                    instance = cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3])
                            )
                    instances.append(instance)
        return instances
