#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor: """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """Class constructor: """
        return {
                'x': self.x,
                'width': self.width,
                'id': self.id,
                'height': self.height,
                'y': self.y
                }

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the area value of the Rectangle instance."""
        return self.width * self.height

    def __eq__(self, other):
        """instance with the character #"""
        return (
                isinstance(other, Rectangle) and
                self.width == other.width and
                self.height == other.height
                )

    def display(self):
        """instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """y overriding the __str__ method"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
            if len(args) > 4:
                setattr(self, 'y', args[4])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                elif key == 'y':
                    setattr(self, 'y', value)

    def __str__(self):
        """y overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
