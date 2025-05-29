from validator import financial_validator


class Financial:
    def __init__(self, id, amount, date_time, document_type, comment):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self.document_type = document_type
        self.comment = comment

    def save(self):
        print(self.amount, self.date_time, self.document_type, self.comment)

    def to_tuple(self):
        return (self.id, self.amount, self.date_time, self.document_type, self.comment)

    def validator(self):
       return financial_validator(self)
