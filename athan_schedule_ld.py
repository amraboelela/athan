from datetime import datetime
import os

now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

from athan_times import *

def generate_plist(play_time: datetime, audio_file: str, plist_name: str):
    plist_path = os.path.expanduser(f"~/Library/LaunchAgents/{plist_name}.plist")
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{plist_name}</string>

    <key>ProgramArguments</key>
    <array>
        <string>afplay</string>
        <string>/Users/amraboelela/python/athan/{audio_file}</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>{play_time.hour}</integer>
        <key>Minute</key>
        <integer>{play_time.minute}</integer>
    </dict>

    <key>RunAtLoad</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/tmp/{plist_name}.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/{plist_name}.err</string>
</dict>
</plist>"""

    with open(plist_path, "w") as f:
        f.write(plist_content)

    print(f"Created: {plist_path}")
    return plist_path

prayer_sound = {
    "fajr": "azan4.mp3",
    "shuruq": "alert3.wav",
    "zuhr": "azan1.wav",
    "asr": "azan4.wav",
    "maghrib": "azan10.mp3",
    "isha": "azan3.wav",
}

for prayer, prayer_time in adhan_times.items():
    # Extract the individual components
    year = prayer_time.year
    month = prayer_time.month
    day = prayer_time.day
    hour = prayer_time.hour
    minute = prayer_time.minute
    second = prayer_time.second

    target_time = datetime(year, month, day, hour, minute, second)
    plist_path = generate_plist(target_time, prayer_sound[prayer], "org.amr.athan." + prayer)
    os.system(f"launchctl unload {plist_path}")
    os.system(f"launchctl load {plist_path}")
    print(f"Scheduled {(prayer + ' athan/alert at: '):<25} {prayer_time.strftime('%I:%M %p')}")

print("")

#plist_path = generate_plist(datetime(2025, 4, 19, 9, 0), "alert3.wav", "org.amr.athan.test")
#os.system(f"launchctl unload {plist_path}")
#os.system(f"launchctl load {plist_path}")
