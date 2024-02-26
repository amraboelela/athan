from datetime import date, datetime
import pytz
import geocoder

def get_current_utc_offset():
    # Get the current time
    now = datetime.now()

    # Get the timezone information for the current time
    timezone = now.astimezone().tzinfo

    # Get the UTC offset in minutes
    utc_offset_minutes = timezone.utcoffset(now).total_seconds() // 60

    # Convert minutes to hours
    utc_offset_hours = utc_offset_minutes // 60

    return utc_offset_hours

# Get the current UTC offset
current_utc_offset = get_current_utc_offset()

print("Time zone:\t", current_utc_offset)

def get_current_location():
    location = geocoder.ip('me')
    return location.latlng  # Returns latitude and longitude

current_location = get_current_location()
print("Location:\t", current_location)
