class Financial:
    def __init__(self, id, amount, date_time, document_type, description):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self.document_type = document_type
        self.description = description

    def save(self):
        print(self.amount, self.date_time, self.document_type, self.description)

    def find_by_id(self):
        pass

    def validator(self):
        errors = []
        if not (type(self.id) == int and self.id > 0):
            errors.append('Financial ID must be an integer > 0')

        if not (type(self.amount) == int and self.amount >= 0):
            errors.append('Amount must be a non-negative integer')

        # date time


        if self.document_type not in ["pay", "receive"]:
            errors.append('Document Type must be either "pay" or "receive"')

        if not (type(self.description) == str and len(self.description) > 0):
            errors.append('Description can  not be empty')
        return errors
