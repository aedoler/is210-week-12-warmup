#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """ Logs information into file.

    Attributes:
        close(): closes program
    """

    def __init__(self, logfilename):
        """Docstring"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Writes information to file.
        msg (str):
            message to write to file
        timestamp:
            Defaults to none, saves timestamp to file
        Returns:
            Saves message to file
        Examples:
            >>>
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Opens file and writes message to file.
        Args:
            None, self
        Returns:
            Opens file and writes message to file. If exception, writes
            exception.
        Exmaples:
            >>>
            """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as open_error:
            self.log('Failed to open file')
            raise open_error

        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('Could not write to file')
                break
            # except:
                # self.log('General error encountered')
            # Wanted to add this statement to catch all other errors -
            # But throws Pylint error

        fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
