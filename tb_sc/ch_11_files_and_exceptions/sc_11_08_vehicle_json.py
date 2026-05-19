# file: sc_11_08_vehicle_json.py
import json
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

    def to_dict(self) -> dict[str, str | int]:
        """Convert to a dictionary for JSON serialization."""
        return {
            "reg_no": self._reg_no,
            "brand":  self._brand,
            "model":  self._model,
            "year":   self._year,
        }

    @staticmethod
    def from_dict(data: dict[str, str | int]) -> "Vehicle":
        """Create a Vehicle from a dictionary."""
        return Vehicle(data["reg_no"], data["brand"],
                       data["model"],  data["year"])

VehicleRegistry = dict[str, Vehicle]          # type alias
FILENAME = Path(__file__).resolve().parent / "vehicles.json"

def _is_vehicle_data(data: object) -> bool:
    if not isinstance(data, dict):
        return False
    return (
        isinstance(data.get("reg_no"), str)
        and isinstance(data.get("brand"), str)
        and isinstance(data.get("model"), str)
        and isinstance(data.get("year"), int)
    )

def load_vehicles() -> VehicleRegistry:
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("The file does not contain "
                  "a vehicle registry.")
            return {}
        for reg_no, vehicle_data in data.items():
            if (not isinstance(reg_no, str)
                    or not _is_vehicle_data(vehicle_data)):
                print("The vehicle registry has "
                      "an invalid structure.")
                return {}
        vehicles: VehicleRegistry = {
            k: Vehicle.from_dict(v)
            for k, v in data.items()
        }
        print(f"Loaded {len(vehicles)} vehicles from file.")
        return vehicles
    except FileNotFoundError:
        print("No saved data - starting with an empty list.")
        return {}
    except json.JSONDecodeError:
        print("The file contains invalid JSON.")
        return {}

def save_vehicles(vehicles: VehicleRegistry) -> None:
    try:
        data = {k: v.to_dict() for k, v in vehicles.items()}
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(vehicles)} vehicles.")
    except IOError as e:
        print(f"Error while saving: {e}")

# Add a similar menu from the pickle example if needed.

if __name__ == "__main__":
    vehicles: VehicleRegistry = load_vehicles()

    vehicles["EL67820"] = Vehicle(
        "EL67820", "Tesla", "Model 3", 2021)
    vehicles["NB72826"] = Vehicle(
        "NB72826", "Toyota", "Yaris", 2019)

    save_vehicles(vehicles)

    vehicles = load_vehicles()   # read back from file
    for v in vehicles.values():
        print(v)