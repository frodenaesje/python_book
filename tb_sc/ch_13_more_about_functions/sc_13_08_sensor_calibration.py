# file: sc_13_08_sensor_calibration.py


def make_correction(offset):
    """Create a function with a fixed temperature correction."""
    def correct(measured):
        return measured + offset

    return correct


if __name__ == "__main__":
    # Sensor A reads 0.4 degrees too high; B reads 0.3 too low.
    correct_a = make_correction(-0.4)
    correct_b = make_correction(0.3)

    readings_a = [20.4, 21.4, 19.4]
    readings_b = [19.7, 20.7, 18.7]

    corrected_a = list(map(correct_a, readings_a))
    corrected_b = list(map(correct_b, readings_b))

    print("Sensor A:", [round(t, 1) for t in corrected_a])
    print("Sensor B:", [round(t, 1) for t in corrected_b])
    print(f"New reading from A: {correct_a(22.4):.1f} C")
