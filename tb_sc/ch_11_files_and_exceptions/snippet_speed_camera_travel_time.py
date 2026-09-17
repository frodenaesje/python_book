# file: snippet_speed_camera_travel_time.py
# Subtracting two datetime objects gives the travel time.
# Compare it with the minimum time allowed by the speed limit.

from datetime import datetime, timedelta

DISTANCE_KM = 5
SPEED_LIMIT_KMH = 60
MIN_TIME = timedelta(hours=DISTANCE_KM / SPEED_LIMIT_KMH)  # 5 minutes

tA = datetime.strptime("2022-01-03 07:11:41", "%Y-%m-%d %H:%M:%S")
tB = datetime.strptime("2022-01-03 07:20:06", "%Y-%m-%d %H:%M:%S")

travel_time = tB - tA

if travel_time < MIN_TIME:
    print("Driven too fast")
else:
    print("Within the limit")
