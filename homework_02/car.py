from homework_02.base import Vehicle
from homework_02.engine import Engine
"""
создайте класс `Car`, наследник `Vehicle`
"""
class Car(Vehicle):
     engene: Engene

     def set_engine(self, engine):
         self.engine = engine
