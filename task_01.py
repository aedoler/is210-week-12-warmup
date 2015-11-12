#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Returns input index of object.
    Args:
        var1 (mixed): indexable object
        var2 (int): index of var1 object to return
    Returns:
        input index element, if not input correct index, raises exception
    Examples:
        >>>simple_lookup('hello', 2)
        'l'
        >>>simple_lookup('hello', 10)
        The entered index/key does not exist, hello
        """
    try:
        getindex = var1[var2]
    except LookupError: # or LookupError
        print 'Warning: Your index/key doesn\'t exist', var1
        getindex = None
    return getindex
