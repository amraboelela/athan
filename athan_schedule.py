from datetime import datetime

now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

from athan_times import *
import schedule
import time
import playsound  # Install using pip install playsound
from apscheduler.schedulers.blocking import BlockingScheduler

def play_alert1():
    playsound.playsound("alert1.wav")
  
def play_alert2():
    playsound.playsound("alert2.wav")
 
def play_alert3():
    playsound.playsound("alert3.wav")
    
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
    
alert_actions = {
    "fajr": play_alert2,
    "shuruq": play_alert2,
    "zuhr": play_alert2,
    "asr": play_alert2,
    "maghrib": play_alert2,
    "isha": play_alert2,
}

prayer_actions = {
    "fajr": play_azan4,
    "shuruq": play_alert3,
    "zuhr": play_alert3,
    "asr": play_alert3,
    "maghrib": play_azan10,
    "isha": play_alert3,
}

scheduler = BlockingScheduler()

for prayer, alert_time in alert_times.items():
    # Extract the individual components
    year = alert_time.year
    month = alert_time.month
    day = alert_time.day
    hour = alert_time.hour
    minute = alert_time.minute
    second = alert_time.second

    target_time = datetime(year, month, day, hour, minute, second)
    scheduler.add_job(alert_actions[prayer], 'date', run_date=target_time)
    
print("")

for prayer, prayer_time in adhan_times.items():
    # Extract the individual components
    year = prayer_time.year
    month = prayer_time.month
    day = prayer_time.day
    hour = prayer_time.hour
    minute = prayer_time.minute
    second = prayer_time.second

    target_time = datetime(year, month, day, hour, minute, second)
    scheduler.add_job(prayer_actions[prayer], 'date', run_date=target_time)
    print(f"Scheduled {(prayer + ' athan/alert at: '):<25} {prayer_time.strftime('%I:%M %p')}")

print("")

target_time = datetime(2025, 5, 1, 10, 43, 0)
# Create scheduler
scheduler.add_job(play_azan4, 'date', run_date=target_time)

# Start scheduler
scheduler.start()

