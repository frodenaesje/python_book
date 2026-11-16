# file: sc_03_08_sensor_status.py

LOW_BATTERY = 0b00000001
MEASUREMENT_ERROR = 0b00000010
MEMORY_FULL = 0b00000100

status = int(input("Sensor status (0-7): "))

low_battery = bool(status & LOW_BATTERY)
measurement_error = bool(status & MEASUREMENT_ERROR)
memory_full = bool(status & MEMORY_FULL)

print(f"Status bits:       {status:08b}")
print(f"Low battery:       {low_battery}")
print(f"Measurement error: {measurement_error}")
print(f"Memory full:       {memory_full}")
