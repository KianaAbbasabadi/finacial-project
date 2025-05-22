import re
from datetime import datetime

def financial_validator(financial):
    errors = []
    if not (type(financial[0]) == int and financial[0] > 0):
        errors.append('Financial ID must be an integer > 0')

    if not (type(financial[1]) == int and financial[1] >= 0):
        errors.append('Amount must be a non-negative integer')

    #date time
    date_time_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    if not re.match(date_time_pattern, financial[2]):
        errors.append('Date and Time must be in the format YYYY-MM-DD HH:MM:SS')

    if financial[3] not in ["pay", "receive"]:
        errors.append('Document Type must be either "pay" or "receive"')

    if not (type(financial[4]) == str and len(financial[4]) > 0):
        errors.append('Description can  not be empty')

    return errors
