# file: sc_10_21_vehicle_menu.py
from abc import ABC, abstractmethod
from collections.abc import Iterator


# ---------- The class hierarchy ----------

class Vehicle(ABC):
    def __init__(self, plate: str, brand: str):
        self.plate = plate
        self._brand = brand

    @property
    def plate(self) -> str:
        return self._plate

    @plate.setter
    def plate(self, value: str) -> None:
        value = value.strip().upper()
        if not value:
            raise ValueError("Plate cannot be empty")
        self._plate = value

    @abstractmethod
    def toll_price(self) -> float:
        """Return the price for one toll passage."""
        pass

    def __str__(self) -> str:
        return f"{self._plate} {self._brand}"


class Car(Vehicle):
    BASE_TOLL = 32.0

    def __init__(
        self, plate: str, brand: str, seats: int = 5
    ):
        super().__init__(plate, brand)
        self._seats = seats

    def toll_price(self) -> float:
        return self.BASE_TOLL

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"(car, {self._seats} seats)"
        )


class ElectricCar(Car):
    DISCOUNT = 0.5

    def __init__(
        self, plate: str, brand: str,
        battery_kwh: int, seats: int = 5
    ):
        super().__init__(plate, brand, seats)
        self._battery_kwh = battery_kwh

    def toll_price(self) -> float:
        return super().toll_price() * self.DISCOUNT

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"[electric, {self._battery_kwh} kWh]"
        )


class Truck(Vehicle):
    BASE_TOLL = 96.0
    PRICE_PER_TON = 4.0

    def __init__(
        self, plate: str, brand: str, weight_tons: float
    ):
        super().__init__(plate, brand)
        self._weight_tons = weight_tons

    def toll_price(self) -> float:
        return (
            self.BASE_TOLL
            + self._weight_tons * self.PRICE_PER_TON
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"(truck, {self._weight_tons} tons)"
        )


# ---------- A collection of vehicles ----------

class Fleet:
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    def add(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def total_toll(self) -> float:
        return sum(
            vehicle.toll_price()
            for vehicle in self._vehicles
        )

    def __iter__(self) -> Iterator[Vehicle]:
        return iter(self._vehicles)

    def __len__(self) -> int:
        return len(self._vehicles)


# ---------- The menu ----------

MENU = """
1. Add car
2. Add electric car
3. Add truck
4. Show all vehicles
0. Quit"""


def create_vehicle(choice: str) -> Vehicle:
    """Read the data and create the chosen vehicle type."""
    plate = input("Plate: ")
    brand = input("Brand: ").strip().title()

    match choice:
        case "1":
            return Car(plate, brand)
        case "2":
            battery_kwh = int(input("Battery (kWh): "))
            return ElectricCar(plate, brand, battery_kwh)
        case "3":
            weight_tons = float(input("Weight (tons): "))
            return Truck(plate, brand, weight_tons)
        case _:
            raise ValueError(
                f"Unknown vehicle type: {choice}"
            )


def show_vehicles(fleet: Fleet) -> None:
    if not fleet:
        print("No vehicles registered.")
        return
    for vehicle in fleet:
        print(
            f"{str(vehicle):<45}"
            f"{vehicle.toll_price():>8.2f}"
        )
    print(
        f"{len(fleet)} vehicles, "
        f"total toll: {fleet.total_toll():.2f}"
    )


def main() -> None:
    fleet = Fleet()

    while True:
        print(MENU)
        choice = input("Your choice: ").strip()

        if choice in ("1", "2", "3"):
            vehicle = create_vehicle(choice)
            fleet.add(vehicle)
            print(f"Added: {vehicle}")
        elif choice == "4":
            show_vehicles(fleet)
        elif choice == "0":
            break
        else:
            print("Unknown choice - try again.")

    print("Goodbye!")


if __name__ == "__main__":
    main()
