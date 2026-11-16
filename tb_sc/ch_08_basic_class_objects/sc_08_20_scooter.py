# file: sc_08_20_scooter.py

class Scooter:
    # Class variables: shared by all scooters
    _unlock_fee = 10.0
    _price_per_minute = 3.0
    _scooter_count = 0

    # Minimum battery percentage for starting a ride
    MIN_BATTERY = 15
    BATTERY_PER_MINUTE = 2     # percent used per minute

    def __init__(
        self, scooter_id: str, battery_level: int = 100
    ):
        self._scooter_id = scooter_id
        # Use the setter to validate the initial level.
        self.battery_level = battery_level
        Scooter._scooter_count += 1

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value: int) -> None:
        if not Scooter.is_valid_battery(value):
            raise ValueError(
                f"Battery level {value} "
                "is not between 0 and 100"
            )
        self._battery_level = value

    @property
    def is_available(self) -> bool:
        return self._battery_level >= Scooter.MIN_BATTERY

    @staticmethod
    def is_valid_battery(value: int) -> bool:
        return 0 <= value <= 100

    @classmethod
    def set_price_per_minute(
        cls, new_price: float
    ) -> None:
        if new_price > 0:
            cls._price_per_minute = new_price

    @classmethod
    def get_scooter_count(cls) -> int:
        return cls._scooter_count

    def ride(self, minutes: int) -> float:
        """Update the battery and return the price."""
        if not self.is_available:
            print(
                f"{self._scooter_id}: battery too low"
                " - find another scooter."
            )
            return 0.0
        used = minutes * Scooter.BATTERY_PER_MINUTE
        self.battery_level = max(
            0, self._battery_level - used
        )
        return (
            Scooter._unlock_fee
            + minutes * Scooter._price_per_minute
        )

    def __str__(self) -> str:
        status = (
            "available" if self.is_available
            else "needs charging"
        )
        return (
            f"Scooter {self._scooter_id}: "
            f"{self._battery_level}% ({status})"
        )


if __name__ == "__main__":
    scooter1 = Scooter("TR-101")
    scooter2 = Scooter("TR-102", battery_level=20)

    print(f"Ride 1: {scooter1.ride(12):.2f} NOK")
    print(f"Ride 2: {scooter2.ride(8):.2f} NOK")
    print(f"Ride 3: {scooter2.ride(5):.2f} NOK")

    # Change the price for all scooters.
    Scooter.set_price_per_minute(3.5)
    print(f"Ride 4: {scooter1.ride(12):.2f} NOK")

    print(scooter1)
    print(scooter2)
    print(
        f"Scooters in total: {Scooter.get_scooter_count()}"
    )

    # Recharge; the setter validates the new level.
    scooter2.battery_level = 100
    print(scooter2)
    # Deliberate error: raises ValueError.
    scooter2.battery_level = 120
