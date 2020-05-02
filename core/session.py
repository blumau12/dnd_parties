
class Session:
    def __init__(self, company, world):
        self.company = company  # class Company
        self.description = ''
        self.experience = {}
        self.logs = []

        self.world = world  # class World
