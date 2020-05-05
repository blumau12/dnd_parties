
class Company:
    def __init__(self, name):
        self.name = name
        self.notes = []  # class str
        self.players = []  # class Player
        self.worlds = []  # class World
        self.languages = {}

        self.current_world = None  # class World

    def add_world(self, world):
        self.worlds.append(world)

    def switch_world(self, world):
        self.current_world = world

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_character(self, character):
        assert self.current_world is not None, "choose a world before character creation"
        self.current_world.add_character(character)

    def remove_character(self, character):
        assert self.current_world is not None, "choose a world before character removing"
        self.current_world.remove_character(character)

    def add_item(self, item):
        assert self.current_world is not None, "choose a world before item creation"
        self.current_world.add_item(item)

    def remove_item(self, item):
        assert self.current_world is not None, "choose a world before item removing"
        self.current_world.remove_item(item)

    def add_language(self, name):
        self.languages.setdefault(name, {})

    def add_word_to_language(self, lang, word, meaning):
        self.languages[lang][word] = meaning
