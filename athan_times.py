from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD
from location import *
from hijri_converter import *

# Get the current date
current_date = datetime.today()

# Convert the current date to Hijri
hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()

hijri_date_str = str(hijri_date)
year, month, day = map(int, hijri_date_str.split('-'))

#print("Year:", year)
#print("Month:", month)
#print("Day:", day)
#
#print("Current Hijri Date:", hijri_date)


import datetime
from hijri_converter import convert

# Mapping between numerical month values and their corresponding Hijri month names
hijri_month_names = {
    1: "Muharram",
    2: "Safar",
    3: "Rabi al-Awwal",
    4: "Rabi al-Thani",
    5: "Jumada al-Awwal",
    6: "Jumada al-Thani",
    7: "Rajab",
    8: "Sha'ban",
    9: "Ramadan",
    10: "Shawwal",
    11: "Dhu al-Qi'dah",
    12: "Dhu al-Hijjah"
}

# Get the current date
current_date = datetime.datetime.today().date()

# Convert the current date to Hijri
hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()

# Format the Hijri date
formatted_hijri_date = f"{hijri_month_names[month]} {day}, {year}"

print("")
print(formatted_hijri_date)


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
print("Prayer Times:")
print("Fajr:\t\t", adhan_times["fajr"].strftime("%I:%M %p"))
print("Sunrise:\t", adhan_times["shuruq"].strftime("%I:%M %p"))
print("Dhuhr:\t\t", adhan_times["zuhr"].strftime("%I:%M %p"))
print("Asr:\t\t", adhan_times["asr"].strftime("%I:%M %p"))
print("Maghrib:\t", adhan_times["maghrib"].strftime("%I:%M %p"))
print("Isha:\t\t", adhan_times["isha"].strftime("%I:%M %p"))

