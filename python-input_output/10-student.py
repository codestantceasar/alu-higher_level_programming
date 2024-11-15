#!/usr/bin/python3
""" Student class definition with attribute filtering """


class Student:
    """ Defines a student with first name, last name, and age """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student with given attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of the Student instance
            If attrs is provided, only attributes in that list are included.
        """
        if attrs is None:
            return self.__dict__

        # Filter attributes based on the given list of attributes
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict
