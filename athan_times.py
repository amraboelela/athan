from datetime import date, datetime
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD

params = {}
params.update(ISNA)
params.update(ASR_STANDARD)

adhan_times = adhan(
    day=date.today(),
    location=(37.3477, -120.6093),  # Atwater, CA 95301
    parameters=params,
    timezone_offset=-8,
)

"""
adhan_times will be a dict containing datetime objects for the keys 'fajr',
'shuruq', 'zuhr', 'asr', 'maghrib', and 'isha'

"""

# Print all prayer times
print("All Prayer Times:")
print("Fajr:", adhan_times["fajr"])
print("Sunrise:", adhan_times["shuruq"])
print("Dhuhr:", adhan_times["zuhr"])
print("Asr:", adhan_times["asr"])
print("Maghrib:", adhan_times["maghrib"])
print("Isha:", adhan_times["isha"])

