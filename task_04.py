#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Updating car module """


import car


class CustomCar(car.Car):
    """a subclass of class Car() from car module"""

    def __init__(self, color='red', tires=None):
        """Constructor for CustomCar() class.

        Args:
            tires(list): A list of CustomTire(), has a default None.
            color(string): color of car, defaulted to 'red'.

        Attributions:
            car.Car(class): calling the Car() class.
            tires(list): to determine miles on tires.
        """
        car.Car.__init__(self, color)
        self.tires = tires if tires is not None else [
            CustomTire() for _ in range(4)]


class CustomTire(car.Tire):
    """a subclass of class Tire()

    Attributes:
        miles (integer): The number of miles on the Tire.
    """
    __maximum_miles = 500
