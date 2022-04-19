from abc import ABC
import homework_02.exceptions as exceptions


class Vehicle(ABC):
    weight: int = 1300
    started: bool = False
    fuel: int = 0
    fuel_consumption: int = 8

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        fuel_required = distance * self.fuel_consumption
        if self.fuel >= fuel_required:
            self.fuel -= fuel_required
        else:
            raise exceptions.NotEnoughFuel()
