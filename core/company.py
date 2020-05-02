from datetime import datetime


class Company:
    def __init__(self, name):
        self.name = name
        self.notes = []
        self.players = []  # class Player
        self.worlds = []  # class World

        self.created = datetime.today()
