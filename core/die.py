from random import randint


class Die:
    def __init__(self, size):
        self.size = size

    def roll(self):
        return randint(1, self.size)
