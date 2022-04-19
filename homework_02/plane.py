from homework_02.base import Vehicle
import homework_02.exceptions as exceptions


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 1000

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if new_cargo + self.cargo <= self.max_cargo:
            self.cargo = new_cargo + self.cargo
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
