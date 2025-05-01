from datetime import datetime
import os

now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

from athan_times import *

def generate_shell_script(audio_file: str, script_name: str):
    script_path = os.path.expanduser(f"~/python/athan/{script_name}.sh")
    script_content = f"""#!/bin/bash
sleep 10
afplay /Users/amraboelela/python/athan/{audio_file}
"""

    with open(script_path, "w") as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)
    return script_path

def generate_plist(play_time: datetime, shell_script_path: str, plist_name: str):
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
        <string>{shell_script_path}</string>
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
    "zuhr": "alert1.wav",
    "asr": "alert4.wav",
    "maghrib": "azan10.mp3",
    "isha": "alert3.wav",
}

for prayer, prayer_time in adhan_times.items():
    script_name = f"play_{prayer}"
    shell_script_path = generate_shell_script(prayer_sound[prayer], script_name)

    plist_path = generate_plist(prayer_time, shell_script_path, "org.amr.athan." + prayer)
    os.system(f"launchctl unload {plist_path} 2>/dev/null")
    os.system(f"launchctl load {plist_path}")
    print(f"Scheduled {(prayer + ' athan/alert at: '):<25} {prayer_time.strftime('%I:%M %p')}")

print("")
