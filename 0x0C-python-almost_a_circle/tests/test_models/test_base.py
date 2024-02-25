#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.base import Base
import os
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects to 0 before each test"""
        Base._Base__nb_objects = 0
        with open("Rectangle.json", "w") as file:
            file.write('[{"width": 5, "height": 10}, '
                       '{"width": 3, "height": 7}]')
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")

    def test_id_assignment_with_id_argument(self):
        """Test if the ID is assigned when an ID is provided"""
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

    def test_id_assignment_without_id_argument(self):
        """Test if the ID increments when no ID is provided"""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_id_assignment_multiple_instances(self):
        """Test if IDs are unique for multiple instances"""
        base_instance1 = Base()
        base_instance2 = Base()
        base_instance3 = Base()
        self.assertNotEqual(base_instance1.id, base_instance2.id)
        self.assertNotEqual(base_instance2.id, base_instance3.id)
        self.assertNotEqual(base_instance1.id, base_instance3.id)

    def test_to_json_string_empty_list(self):
        """Test if IDs are unique for multiple instances"""
        empty_list = []
        result = Base.to_json_string(empty_list)
        self.assertEqual(result, [])

    def test_to_json_string_none(self):
        """Test if IDs are unique for multiple instances"""
        result = Base.to_json_string(None)
        self.assertEqual(result, [])

    def test_to_json_string_list_of_dicts(self):
        """Test if IDs are unique for multiple instances"""
        list_dicts = [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'},
                ]
        expect_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = Base.to_json_string(list_dicts)
        self.assertEqual(result, expect_json)

    def test_save_to_file(self):
        """Test if IDs are unique for multiple instances"""
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 7)
        Rectangle.save_to_file([rect1, rect2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        square = Square(6)
        Square.save_to_file([square])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_from_json_string_empty(self):
        """Test if IDs are unique for multiple instances"""
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """Test if IDs are unique for multiple instances"""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test if IDs are unique for multiple instances"""
        json_string = '[{"width": 5, "height": 10}, {"width": 3, "height": 7}]'
        result = Base.from_json_string(json_string)
        expected = [{'width': 5, 'height': 10}, {'width': 3, 'height': 7}]
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        """Test if IDs are unique for multiple instances"""
        rect_dict = {'width': 5, 'height': 10}
        rect_instance = Rectangle.create(**rect_dict)
        expected_rect = Rectangle(5, 10)
        self.assertEqual(rect_instance, expected_rect)

    def test_create_square(self):
        """Test if IDs are unique for multiple instances"""
        square_dict = {'size': 7}
        square_instance = Square.create(**square_dict)
        expected_square = Square(7)
        self.assertEqual(square_instance, expected_square)

    def test_update_method(self):
        """Test if IDs are unique for multiple instances"""
        square_dict = {'size': 7}
        square_instance = Square(1)
        square_instance.update(**square_dict)
        expected_square = Square(7)
        self.assertEqual(square_instance, expected_square)

    def test_load_from_file_rectangle(self):
        """Test if IDs are unique for multiple instances"""
        instances = Rectangle.load_from_file()
        expected_instances = [Rectangle(5, 10), Rectangle(3, 7)]
        self.assertEqual(instances, expected_instances)

    def test_csv_save_load(self):
        """Test if IDs are unique for multiple instances"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertNotEqual(
                len(list_rectangles_input),
                len(list_rectangles_output)
                )
        for input_rect, output_rect in zip(
                list_rectangles_input,
                list_rectangles_output
                ):
            self.assertEqual(vars(input_rect), vars(output_rect))

    def tearDown(self):
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")


if __name__ == '__main__':
    unittest.main()
