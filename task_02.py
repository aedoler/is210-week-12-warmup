#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Tests for invalid age"""
    pass


def get_age(birthyear):
    """returns age based on input birthyear.
    Args:
        birthyear (int): year of birth
    Returns:
        Age of person, unless supposed age is less than 0
    Examples:
        >>>get_age(1990)
        25
        >>>get_age(2017)
        Traceback (most recent call last):
          File "<pyshell#1>", line 1, in <module>
            get_age(2017)
          File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py",
          line 15, in get_age
            raise InvalidAgeError('Invalid age')
        InvalidAgeError: Invalid age
        """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError('Invalid age')
    else:
        return age
