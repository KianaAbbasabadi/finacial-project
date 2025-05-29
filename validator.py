import re


def financial_validator(financial):
    errors = []
    if not (type(financial.id) == int and financial.id > 0):
        errors.append('Financial ID must be an integer > 0')

    if not (type(financial.amount) == int and financial.amount >= 0):
        errors.append('Amount must be a non-negative integer')

    # date time

    if financial.document_type not in ["pay", "receive"]:
        errors.append('Document Type must be either "pay" or "receive"')

    if not (type(financial.description) == str and len(financial.description) > 0):
        errors.append('Description can  not be empty')
    return errors