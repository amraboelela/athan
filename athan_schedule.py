from athan_times import *
import schedule
import playsound  # Install using pip install playsound
from apscheduler.schedulers.blocking import BlockingScheduler

def play_alert1():
    playsound.playsound("alert1.wav")
    
def play_azan1():
    playsound.playsound("azan1.mp3")
    
def play_azan3():
    playsound.playsound("azan3.mp3")
  
def play_azan4():
    playsound.playsound("azan4.mp3")
  
def play_azan10():
    playsound.playsound("azan10.mp3")
    
def play_azan13():
    playsound.playsound("azan13.mp3")
    
prayer_actions = {
    "fajr": play_azan4,
    "shuruq": play_alert1,
    "zuhr": play_alert1,
    "asr": play_alert1,
    "maghrib": play_azan10,
    "isha": play_azan13,
}

scheduler = BlockingScheduler()

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

    target_time = datetime(year, month, day, hour, minute, second)

    scheduler.add_job(prayer_actions[prayer], 'date', run_date=target_time)

#print("Fajr:", adhan_times["fajr"])
#
#target_time = datetime(2024, 2, 24, 21, 34, 0)
#
## Create scheduler
#
#scheduler.add_job(play_alert1, 'date', run_date=target_time)
#
## Start scheduler
##scheduler.start()
#
#print("Dhuhr:", adhan_times["zuhr"])
#
#target_time = datetime(2024, 2, 24, 21, 15, 0)
#    
## Create scheduler
##scheduler = BlockingScheduler()
#
#scheduler.add_job(play_azan13, 'date', run_date=target_time)

# Start scheduler
scheduler.start()
