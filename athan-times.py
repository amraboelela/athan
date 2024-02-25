from datetime import date
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD
from datetime import datetime
import schedule
import playsound  # Install using pip install playsound
from apscheduler.schedulers.blocking import BlockingScheduler

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

def play_azan3():
    playsound.playsound("azan3.mp3")
  
def play_azan13():
    playsound.playsound("azan13.mp3")
    
prayer_actions = {
    "fajr": play_azan3,
    "zuhr": play_azan3,
    "ash": play_azan3,
    "maghrib": play_azan13,
    "isha": play_azan13,
}

for prayer, prayer_time in adhan_times.items():
    # Extract the individual components
    year = prayer_time.year
    month = prayer_time.month
    day = prayer_time.day
    hour = prayer_time.hour
    minute = prayer_time.minute
    second = prayer_time.second

    # Print the individual components
    print(prayer, "Time:")
    print("Year:", year)
    print("Month:", month)
    print("Day:", day)
    print("Hour:", hour)
    print("Minute:", minute)
    print("Second:", second)
    print("")

    # Set the target date and time
    #target_time = datetime(2024, 2, 24, 5, 31, 0)  # Year, month, day, hour, minute, second

    target_time = datetime(year, month, day, hour, minute, second)
    #target_time = datetime(2024, 2, 24, 20, 34, 0)
    
    # Create scheduler
    scheduler = BlockingScheduler()

    scheduler.add_job(prayer_actions[prayer], 'date', run_date=target_time)
    
    # Start scheduler
    scheduler.start()
