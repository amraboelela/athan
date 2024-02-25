# Athan
Open source athan time with call to prayer in python

# How to run it
```
athan % vi athann-times.py
```

You need to put the correct Latitude and Longitude of your city, and the correct timezone.
```
adhan_times = adhan(
    day=date.today(),
    location=(37.3477, -120.6093),  # Atwater, CA 95301
    parameters=params,
    timezone_offset=-8,
)
```

In a terminal in macOS, or Linux do:

```
% crontab -e
```

Then, put

```
0 1 * * * /usr/bin/python3 /path/to/athan-times.py
```

## If you need to stop it:

```
% ps aux | grep athan
```

Then kill the process, e.g.:

```
% kill 48037
```

## If you need to not play the azan for a certain prayer:

```
athan % vi athan-times.py
```

You can choose between an azan vs an alert by putting play_azan1 or play_alert1, as following:

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
