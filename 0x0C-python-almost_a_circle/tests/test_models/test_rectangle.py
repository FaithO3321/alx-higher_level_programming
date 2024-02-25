#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Test object creation and attribute assignment"""
    def test_initialization(self):
        """Test if the ID is assigned when an ID is provided"""
        rect = Rectangle(10, 20, 3, 5, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)
        self.assertEqual(rect.id, 1)

    def test_attribute_setters(self):
        """Test if the ID increments when no ID is provided"""
        rect = Rectangle(10, 20)
        rect.width = 15
        rect.height = 25
        rect.x = 5
        rect.y = 10
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)

    def test_attribute_setters_invalid_values(self):
        """Test attribute setters with invalid values"""
        rect = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rect.width = "Invalid"
        with self.assertRaises(ValueError):
            rect.width = 0
        with self.assertRaises(TypeError):
            rect.height = "Invalid"
        with self.assertRaises(ValueError):
            rect.height = -5
        with self.assertRaises(TypeError):
            rect.x = "Invalid"
        with self.assertRaises(ValueError):
            rect.x = -3
        with self.assertRaises(TypeError):
            rect.y = "Invalid"
        with self.assertRaises(ValueError):
            rect.y = -4

    def test_area_method(self):
        """Test the area() method functionality"""
        rect = Rectangle(10, 20)
        self.assertEqual(rect.area(), 200)

    def test_display_method(self):
        """Test the display() method functionality"""
        rect = Rectangle(3, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        expected_output = "###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        """Test the __str__() method functionality"""
        rect = Rectangle(10, 20, 5, 5, 1)
        expected_str = "[Rectangle] (1) 5/5 - 10/20"
        self.assertEqual(str(rect), expected_str)

    def test_display_with_x_and_y(self):
        """Create a rectangle with specific x, y positions"""
        rect = Rectangle(5, 4, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue()
        expected_output = "\n  #####\n  #####\n  #####\n  #####\n"
        self.assertEqual(result, expected_output)

    def test_display_without_x_and_y(self):
        """Create a rectangle with default x, y positions (0, 0)"""
        rect = Rectangle(3, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue()
        expected_output = "###\n###\n"
        self.assertEqual(result, expected_output)

    def test_update_method(self):
        """Create a rectangle with initial attributes"""
        rect = Rectangle(5, 10, 1, 2, 10)
        rect.update(20, 7, 15, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_method_with_kwargs(self):
        """Create a rectangle with initial attributes"""
        rect = Rectangle(5, 10, 1, 2, 10)
        rect.update(id=30, width=8, height=16, x=4, y=5)
        self.assertEqual(rect.id, 30)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 16)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_method_with_mixed_args_and_kwargs(self):
        """Create a rectangle with initial attributes"""
        rect = Rectangle(5, 10, 1, 2, 10)
        rect.update(25, 6, 10, 1, 7)
        self.assertEqual(rect.id, 25)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 7)

    def test_rectangle_to_dictionary(self):
        """Create a rectangle with initial attributes"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertDictEqual(r1_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
