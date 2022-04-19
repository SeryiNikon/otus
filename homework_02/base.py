from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class TestVehicle(ABC):
    def __init__(self, weight=1000, fuel=50):
        super().__init__()
        self.weight = weight
        self.fuel = fuel
        self.started = False
    

    def __repr__(self):
        return f'{__class__.__name__} (weight: {self.weight}, ' \
               f'fuel: {self.fuel}, started: {self.started})'
    
        
    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if distance <= max_distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
            return
        raise NotEnoughFuel
