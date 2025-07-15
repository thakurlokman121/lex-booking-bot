import re
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_guest_count(count_str):
    return re.match(r'^[1-9][0-9]*$', count_str) is not None
