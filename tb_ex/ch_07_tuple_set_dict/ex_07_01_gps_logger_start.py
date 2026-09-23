# file: ex_07_01_gps_logger_start.py

track = [
    ( 78.2232,  15.6267, "Longyearbyen"),  # Svalbard, Norway
    ( 68.4384,  17.4279, "Narvik"),         # Norway
    ( 64.1355, -21.8954, "Reykjavik"),      # Iceland
    ( 51.5074,  -0.1278, "London"),         # UK
    ( 48.8566,   2.3522, "Paris"),          # France
    ( 40.7128, -74.0060, "New York"),       # USA
    ( -3.1190, -60.0217, "Manaus"),         # Brazil
    (-33.8688, 151.2093, "Sydney"),         # Australia
    ( 35.6762, 139.6503, "Tokyo"),          # Japan
    (-90.0000,   0.0000, "South Pole"),     # Antarctica
]

# max() and min() can use a key function to decide which value
# in each tuple should be compared. The functions below return
# the latitude or longitude from a position tuple.
def get_latitude(position):
    return position[0]


def get_longitude(position):
    return position[1]


# TODO: Print a header showing the number of positions.
#       Example: "GPS log - 10 positions:"

# TODO: Use tuple unpacking to process and display all positions.
#       Follow the coordinate/output requirements in the exercise.

# TODO: Find and print the northernmost place.
#       Use max() or min() with the appropriate key function.

# TODO: Find and print the southernmost place.
#       Use max() or min() with the appropriate key function.

# TODO: Find and print the westernmost place.
#       Use max() or min() with the appropriate key function.
