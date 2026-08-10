# file: ex_10_03_vehicle_hierarchy_start.py

class Vehicle:
    def __init__(self, make, model, year):
        # TODO: store _make, _model, _year and initialise _fuel_level to 0
        pass

    def refuel(self, amount):
        # TODO: increase _fuel_level by amount, cap at 100
        pass

    def drive(self, km):
        # TODO: decrease _fuel_level by km * 0.08
        # Print "Not enough fuel." if fuel would go below 0
        pass

    def __str__(self):
        # TODO: e.g. "2022 Toyota Corolla (fuel: 75%)"
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors=4):
        # TODO: call super().__init__() and store _num_doors
        pass

    def __str__(self):
        # TODO: extend Vehicle's __str__ with door count
        # Hint: super().__str__() + f" [Car, {self._num_doors} doors]"
        pass


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kwh, num_doors=4):
        # TODO: call super().__init__() and store _battery_kwh
        # TODO: initialise _charge_level to 0
        pass

    def charge(self, amount):
        # TODO: increase _charge_level by amount, cap at 100
        pass

    def drive(self, km):
        # TODO: decrease _charge_level by km * 0.2 kWh as percentage of battery
        # Hint: kwh_used = km * 0.2
        #       percent_used = kwh_used / self._battery_kwh * 100
        pass

    def __str__(self):
        # TODO: show charge level instead of fuel level
        # e.g. "2023 Tesla Model 3 (charge: 80%) [Car, 4 doors]"
        pass


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_tonnes):
        # TODO: call super().__init__() and store _payload_tonnes
        pass

    def drive(self, km):
        # TODO: trucks use more fuel: km * 0.15
        pass

    def __str__(self):
        # TODO: extend Vehicle's __str__ with payload
        pass


if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Corolla", 2022),
        ElectricCar("Tesla", "Model 3", 2023, battery_kwh=75),
        Truck("Volvo", "FH", 2021, payload_tonnes=20),
    ]

    # TODO: use isinstance() to charge ElectricCars and refuel others
    for v in vehicles:
        pass

    print("Before driving:")
    for v in vehicles:
        print(f"  {v}")

    for v in vehicles:
        v.drive(200)

    print("\nAfter driving 200 km:")
    for v in vehicles:
        print(f"  {v}")
