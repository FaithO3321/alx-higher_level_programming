#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Square is a special Rectangle"""
    def test_square_creation(self):
        """Create a square with initial attributes"""
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_str_representation(self):
        """Create a square"""
        square = Square(5, 2, 3, 10)
        string_repr = str(square)
        self.assertEqual(string_repr, "[Square] (10) 2/3 - 5")

    def test_square_size_getter(self):
        """Create a square"""
        square = Square(5)
        size = square.size
        self.assertEqual(size, square.width)

    def test_square_size_setter(self):
        """Create a square"""
        square = Square(5)
        square.size = 8
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_square_update_with_args(self):
        """Create a square"""
        square = Square(5, 2, 3, 10)
        square.update(25, 8, 4, 5)
        self.assertEqual(square.id, 25)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_square_update_with_kwargs(self):
        """Create a square"""
        square = Square(5, 2, 3, 10)
        square.update(id=30, y=7)
        self.assertEqual(square.id, 30)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 7)

    def test_square_update_mixed_args_kwargs(self):
        """Create a square"""
        square = Square(5, 2, 3, 10)
        square.update(25, 8, 2, 7)
        self.assertEqual(square.id, 25)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 7)

    def test_square_to_dictionary(self):
        """Create a square"""
        s1 = Square(5, 2, 3, 1)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s1_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
