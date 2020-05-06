
class Charge:
    def __init__(self, max_charge):
        self.charge = 0
        self.max_charge = max_charge

    def refill(self, amount=None):
        if not amount:
            amount = self.max_charge - self.charge
        self.charge += amount
