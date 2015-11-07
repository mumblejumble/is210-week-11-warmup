#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Working with time module """


import time


class Snapshot(object):
    """ Object that retores time data.

    Attributes:
        created(mixed): the current Unix Timestamp.
    """
    def __init__(self):
        """Constructor for Snapshot() class.

        Attributes:
            created(mixed): the current Unix Timestamp.
        """
        self.created = time.time()
