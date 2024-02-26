# Athan
Open source athan time with call to prayers in python, it automatically detect your location.

# How to install it

In a terminal in macOS, or Linux do:

```
% crontab -e
```

Then, put

```
0 0 * * * /path/to/athan_schedule
0 12 * * * /path/to/athan_schedule
```

## To list the athan time for today

```
athan % ./athan_times 
```

## If you need to stop it:

```
athan % ./stop 
```

## If you want to customize athan / alerts for each prayer:

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
