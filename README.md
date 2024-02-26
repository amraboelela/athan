# Athan
Open source athan time with call to prayers in python, it automatically detect your location.

## Install

In a terminal in macOS, or Linux do:

```
% crontab -e
```

Then, put

```
0 0 * * * /path/to/athan_schedule
0 12 * * * /path/to/athan_schedule
```

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
