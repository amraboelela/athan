from datetime import *
from hijri_converter import *

def today_hijri_date():
    # Get the current date
    current_date = datetime.today()

    # Convert the current date to Hijri
    hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()

    hijri_date_str = str(hijri_date)
    year, month, day = map(int, hijri_date_str.split('-'))

    # Mapping between numerical month values and their corresponding Hijri month names
    hijri_month_names = {
        1: "Muharram",
        2: "Safar",
        3: "Rabi al-Awwal",
        4: "Rabi al-Thani",
        5: "Jumada al-Awwal",
        6: "Jumada al-Thani",
        7: "Rajab",
        8: "Sha'ban",
        9: "Ramadan",
        10: "Shawwal",
        11: "Dhu al-Qi'dah",
        12: "Dhu al-Hijjah"
    }

    # Format the Hijri date
    formatted_hijri_date = f"{hijri_month_names[month]} {day}, {year}"

    return formatted_hijri_date

