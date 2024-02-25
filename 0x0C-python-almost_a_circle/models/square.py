#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle:"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor:"""
        super().__init__(size, size, x, y, id)

    def __eq__(self, other):
        """Class constructor:"""
        return isinstance(other, Square) and self.size == other.size

    def to_dictionary(self):
        """Class constructor:"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    @property
    def size(self):
        """The setter """
        return self.width

    @size.setter
    def size(self, value):
        """The setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The setter """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def __str__(self):
        """The overloading __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
