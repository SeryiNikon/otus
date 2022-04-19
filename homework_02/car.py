from homework_02.base import TestVehicle

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(TestVehicle):

    def __init__(self):
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
