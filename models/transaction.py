class Transaction:

    def __init__(self, name, amount, tag, merchant, id = None):
        self.name = name
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.id = id