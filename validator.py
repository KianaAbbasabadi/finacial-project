import re

def financial_validator(financial):
    errors = []
    if not (type(financial[0]) == int and financial[0] > 0):
        errors.append('Financial ID must be an integer > 0')

    if not (type(financial[1]) == int and financial[1] >= 0):
        errors.append('Amount must be a non-negative integer')

    #date time


    if financial[3] not in ["pay", "receive"]:
        errors.append('Document Type must be either "pay" or "receive"')

    if not (type(financial[4]) == str and len(financial[4]) > 0):
        errors.append('Description can  not be empty')

    return errors
