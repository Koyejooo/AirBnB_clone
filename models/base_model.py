#!/usr/bin/python3
"""Create parent class/base model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Define all common attributes/methods for other sub-classes"""

    def __init__(self, *args, **kwargs):
        """Initialise BaseModel objects"""
        if kwargs != {} and kwargs is not None:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Print a string representation of the object."""
        return "[{}] ({}) {}".\
                format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' attribute with current datetime."""
        current_datetime = datetime.now()

        self.updated_at = current_datetime

    def to_dict(self):
        """Return a dict populated with key/value of object's __dict__."""
        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
