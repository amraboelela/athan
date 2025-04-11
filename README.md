# Athan
Open source athan time with call to prayers in python, it automatically detect your location.

## Install

- In terminal run the following to install all the required python packages

```
pip install hijri-converter geocoder schedule playsound==1.2.2 apscheduler 
```

- You need to put the correct Latitude and Longitude of your city, in location.py 

```
current_location = (38.599192, -121.504702)

```

- Or set it to automatic location detection as:

```
adhan_times = adhan(
    day=date.today(),
    location=get_current_location(),
    parameters=params,
    timezone_offset=-8,
)
```

Note, the automatic detection is good when you are traveling, but it can be about 5 minutes inaccurate.

- In order to automatically schedule athan times call for prayers, in a terminal in macOS, or Linux do:

```
% crontab -e
```

Then, enter:

```
0 */4 * * * /path/to/athan_schedule
```

`/path/to/athan_schedule` depends on where you cloned this repo, e.g. `/Users/username/python/athan/athan_schedule`

## List current athan times

```
athan % ./athan_times 
```

Output sample:

```
Current UTC Offset: -8.0
Current Location (latitude, longitude): [37.123, -120.2602]

Prayer Times:
Fajr:           05:28 AM
Sunrise:        06:40 AM
Dhuhr:          12:15 PM
Asr:            03:24 PM
Maghrib:        05:51 PM
Isha:           07:03 PM
```

## To stop athan schedule for today

```
athan % ./stop 
```

## To restart athan schedule for today

```
athan % ./athan_schedule 
```

## Customize athan / alerts

```
athan % vi athan_schedule.py
```

You can choose between an azan or an alert by putting e.g. play_azan1 or play_alert1, as following:

```
prayer_actions = {
    "fajr": play_azan3,
    "shuruq": play_alert1,
    "zuhr": play_alert1,
    "asr": play_alert1,
    "maghrib": play_azan13,
    "isha": play_azan13,
}
```
