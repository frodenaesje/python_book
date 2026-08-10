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
    ( 90.0000,   0.0000, "South Pole"),     # Antarctica
]

# TODO: Print header with number of positions
#       Example: "GPS log - 10 positions:"

# TODO: Print all positions using tuple unpacking
#       for lat, lon, name in track:
#       Show N/S for latitude, E/W for longitude
#       Format: "  Narvik          68.4384 N   17.4279 E"
#       Hint: use abs(lat) and check if lat >= 0 for N or S

# TODO: Find and print the northernmost place (highest latitude)
#       Hint: max(track, key=lambda p: p[0])

# TODO: Find and print the southernmost place (lowest latitude)

# TODO: Find and print the westernmost place (lowest longitude)
