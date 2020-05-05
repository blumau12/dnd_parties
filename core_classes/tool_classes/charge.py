
class Charge:
    def __init__(self, max_charge):
        self.charge = 0
        self.max_charge = max_charge

    def refill(self, amount=None):
        if amount is None:
            amount = self.max_charge
        self.charge = amount
