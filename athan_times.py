from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD
from hijri_date import *
from location import *

#print("")
print("Date:\t\t", today_hijri_date())
print("")
 
params = {}
params.update(ISNA)
params.update(ASR_STANDARD)

adhan_times = adhan(
    day=date.today(),
    location=(37.345590, -120.578162), #get_current_location(),
    parameters=params,
    timezone_offset=get_current_utc_offset(),
)

# Print all prayer times
print("Prayer Times:")
print("Fajr:\t\t", adhan_times["fajr"].strftime("%I:%M %p"))
print("Sunrise:\t", adhan_times["shuruq"].strftime("%I:%M %p"))
print("Dhuhr:\t\t", adhan_times["zuhr"].strftime("%I:%M %p"))
print("Asr:\t\t", adhan_times["asr"].strftime("%I:%M %p"))
print("Maghrib:\t", adhan_times["maghrib"].strftime("%I:%M %p"))
print("Isha:\t\t", adhan_times["isha"].strftime("%I:%M %p"))

# Initialize alert times
alert_times = {}

# Calculate alert times (15 minutes earlier for each adhan)
for key, value in adhan_times.items():
    alert_times[key] = value - timedelta(minutes=15)

#print("")
#print("Alert Times (15 minutes earlier):", alert_times)
