from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD
from location import *

params = {}
params.update(ISNA)
params.update(ASR_STANDARD)

adhan_times = adhan(
    day=date.today(),
    location=get_current_location(),  # Atwater, CA 95301
    parameters=params,
    timezone_offset=get_current_utc_offset(),
)

"""
adhan_times will be a dict containing datetime objects for the keys 'fajr',
'shuruq', 'zuhr', 'asr', 'maghrib', and 'isha'

"""

# Print all prayer times
print("")
print("Prayer Times:")
print("Fajr:\t\t", adhan_times["fajr"].strftime("%I:%M %p"))
print("Sunrise:\t", adhan_times["shuruq"].strftime("%I:%M %p"))
print("Dhuhr:\t\t", adhan_times["zuhr"].strftime("%I:%M %p"))
print("Asr:\t\t", adhan_times["asr"].strftime("%I:%M %p"))
print("Maghrib:\t", adhan_times["maghrib"].strftime("%I:%M %p"))
print("Isha:\t\t", adhan_times["isha"].strftime("%I:%M %p"))

