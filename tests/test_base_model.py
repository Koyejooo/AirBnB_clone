#!/usr/bin/python3
"""Test units of BaseModel parent class."""
from models.base_model import BaseModel
from datetime import datetime
import unittest
from uuid import uuid4
import time


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class cases."""
    
    def test_class_instantiation(self):
        """Test instantiation of BaseModel() object."""
        test_city = BaseModel()
        self.assertEqual(str(type(test_city)),\
                "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(test_city, BaseModel)
        self.assertTrue(issubclass(type(test_city), BaseModel))

    def test_init_with_no_args(self):
        """Test object instantiation with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        err_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err_msg)

    def test_init_with_args(self):
        """Test object instantiation with arguments"""
        args = [i for i in range(700)]
        test_city = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        test_city = BaseModel(*args)

    def test_datetime_creation(self):
        """Test for accrurate creation of updated_at & created_at attribute."""
        ref_date = datetime.now()
        test_city = BaseModel()
        diff = test_city.created_at - test_city.updated_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = test_city.created_at - ref_date
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_unique_id(self):
        """Test that all users get unique IDs."""
        new_obj = [BaseModel().id for i in range(3000)]
        self.assertEqual(len(set(new_obj)), len(new_obj))

    def test_save_method(self):
        """Test the save() public instance method."""
        ref_date = datetime.now()
        test_city = BaseModel()

        test_city.save()
        diff = test_city.updated_at - ref_date
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str_representation(self):
        """Test for correct string representation of '__str__' method"""
        test_city = BaseModel()
        self.assertEqual(str(test_city),
                         "[BaseModel] ({}) {}"\
                                 .format(test_city.id, test_city.__dict__))

    def test_to_dict_method(self):
        """Test the to_dict() methods for correct output"""
        test_city = BaseModel()
        test_city.name = "Abuja"
        t_city_dict = test_city.to_dict()
        self.assertEqual(t_city_dict["id"], test_city.id)
        self.assertEqual(t_city_dict["__class__"], type(test_city).__name__)
        self.assertEqual(t_city_dict["created_at"],\
                test_city.created_at.isoformat())
        self.assertEqual(t_city_dict["updated_at"],\
                test_city.updated_at.isoformat())
        self.assertEqual(t_city_dict["name"], test_city.name)

    def test_to_dict_with_no_args(self):
        """Test to_dict method with no argument"""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        err_msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err_msg)

    def test_to_dict_with_excess_args(self):
        """Test to_dict method with more than one argument"""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, "Abuja")
        err_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), err_msg)



if __name__ == '__main__':
    unittest.main()
