#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Working with produce module """


import produce


TOMATO = produce.Produce()

EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
