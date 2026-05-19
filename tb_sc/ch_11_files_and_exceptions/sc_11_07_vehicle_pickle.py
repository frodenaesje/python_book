# file: sc_11_07_vehicle_pickle.py
import pickle
from pathlib import Path

class Vehicle:
    def __init__(
            self, reg_no: str, brand: str,
            model: str, year: int):
        self._reg_no = reg_no
        self._brand  = brand
        self._model  = model
        self._year   = year

    def __str__(self):
        return (f"{self._reg_no} - {self._brand} "
                f"{self._model} ({self._year})")

VehicleRegistry = dict[str, Vehicle]          # type alias
FILENAME = Path(__file__).resolve().parent / "vehicles.pkl"

def load_vehicles() -> VehicleRegistry:
    """Load vehicles from a file.
     Return an empty dict if the file does not exist."""
    try:
        with open(FILENAME, "rb") as f:
            vehicles: VehicleRegistry = pickle.load(f)
        if not isinstance(vehicles, dict):
            print("The file does not contain "
                  "a vehicle registry.")
            return {}
        for reg_no, vehicle in vehicles.items():
            if (not isinstance(reg_no, str)
                    or not isinstance(vehicle, Vehicle)):
                print("The vehicle registry has "
                      "an invalid structure.")
                return {}
        print(f"Loaded {len(vehicles)} vehicles from file.")
        return vehicles
    except FileNotFoundError:
        print("No saved data - starting with an empty list.")
        return {}
    except (pickle.UnpicklingError, EOFError):
        print("The file is corrupted or invalid.")
        return {}

def save_vehicles(vehicles: VehicleRegistry) -> None:
    """Save vehicles to a file."""
    try:
        with open(FILENAME, "wb") as f:
            pickle.dump(vehicles, f)
        print(f"Saved {len(vehicles)} vehicles.")
    except IOError as e:
        print(f"Error while saving: {e}")

def list_vehicles(vehicles: VehicleRegistry) -> None:
    if not vehicles:
        print("No vehicles registered.")
        return
    for v in vehicles.values():
        print(v)

def add_vehicle(vehicles: VehicleRegistry) -> None:
    try:
        reg_no = input("Registration no.: ").strip().upper()
        if reg_no in vehicles:
            print(f"{reg_no} already exists.")
            return
        brand = input("Brand: ").strip()
        model = input("Model: ").strip()
        year  = int(input("Year: "))
        vehicles[reg_no] = Vehicle(reg_no, brand, model, year)
        print(f"Added: {vehicles[reg_no]}")
    except ValueError:
        print("Year must be an integer.")

def main():
    vehicles: VehicleRegistry = load_vehicles()
    print("\nCommands: [l]ist, [a]dd, [s]ave, [q]uit")

    while True:
        choice = input("\nChoice: ").strip().lower()
        if choice == "q":
            save_vehicles(vehicles)
            break
        elif choice == "l":
            list_vehicles(vehicles)
        elif choice == "a":
            add_vehicle(vehicles)
        elif choice == "s":
            save_vehicles(vehicles)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()