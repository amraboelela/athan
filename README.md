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

If you need to stop it:

```
% ps aux | grep athan
```

Then kill the process, e.g.:

```
% kill 48037
```
