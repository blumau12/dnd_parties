from datetime import datetime


class Company:
    def __init__(self, name):
        self.name = name
        self.notes = []
        self.players = []

        self.created = datetime.today()
