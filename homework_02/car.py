from homework_02.base import Vehicle
"""
создайте класс `Car`, наследник `Vehicle`
"""
class Car(Vehicle):
     engine: Engine

     def set_engine(self, engine):
         self.engine = engine
