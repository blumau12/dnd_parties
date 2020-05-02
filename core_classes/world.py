
class World:
    def __init__(self, description, start_minute):
        self.description = description
        self.start_minute = start_minute
        self.current_datetime = None  # WorldDatetime class
        self.characters = []
        self.items = []

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)