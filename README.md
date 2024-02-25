# Athan
Open source athan time with call to prayer in python

# How to run it

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

Then comment out the prayer that you don't want it to call out using `#`. e.g for zuhr azan:

```
prayer_actions = {
    "fajr": play_azan3,
#    "zuhr": play_azan3,
    "ash": play_azan3,
    "maghrib": play_azan13,
    "isha": play_azan13,
}
```
