
class SituationalStats:
    def __init__(self):
        self.classes = {}  # {'rogue': 6, 'fighter': 3}
        self.stats = {}  # {'str': 19, 'dex': 18, ...}
        self.stat_mods = {}  # {'str': 4, 'dex': 4, ...}
        self.saving_throw_mods = {}  # {'str': 4, 'dex': 4, ...}
        self.skills = {}  # {'athletics': 8, ...}
        self.passive_perception_mod = 0
        self.initiative_mod = 0
        self.speed = 0
        self.hp = 0
        self.temp_hp = 0
        self.hit_dice = ''
        self.ac = 0
        self.languages = []
        self.instruments = []
        self.vision = []
        self.inspiration = []
        self.active_states = []
        self.fits = []
        self.abilities = []
        self.food_fill = 0
        self.water_fill = 0
