import re


def financial_validator(financial):
    errors = []
    if not (type(financial.id) == int and financial.id > 0):
        errors.append('Financial ID must be an integer > 0')

    if not (type(financial.amount) == int and financial.amount >= 0):
        errors.append('Amount must be a non-negative integer')

    # date time

    if financial.document_type not in ["Income", "Outcome"]:
        errors.append('Document Type must be either "Income" or "Outcome"')

    if not (type(financial.comment) == str and len(financial.comment) > 0):
        errors.append('Comment can  not be empty')
    return errors