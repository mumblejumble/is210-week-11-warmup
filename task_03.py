#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Updating produce module """


import produce


class Apple(produce.Produce):
    """this sub-class updates duration value in produce module only in this
    module.

    Attributes:
        duration(int): new value for duration.
    """
    def __init__(self):
        self.duration = 5356800
