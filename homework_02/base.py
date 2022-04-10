from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class TestVehicle(ABC):
    def __init__(self, weight=1000, fuel=50):
        super().__init__()
        self.weight = weight
        self.fuel = fuel
        self.started = False
        
    def start(self):
    if not self.started:
        if self.fuel > 0:
            self.started = True
            print('Двигатель заведен')
        else:
            raise LowFuelError
    else:
        print('Дивгатель уже заведен')
        
        
    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if distance <= max_distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
            return
        raise NotEnoughFuel
