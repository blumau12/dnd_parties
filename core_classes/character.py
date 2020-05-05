from uuid import uuid4
from .tool_classes import Resource, Charge


class Character:
    def __init__(self, **kwargs):
        self.personal_info = PersonalInfo(**kwargs)
        self.level_based_stats = LevelBasedStats()
        self.situational_stats = SituationalStats()
        self.effects = ''  # blessed, ill, or just a good boy
        self.resources = [
            Resource(name='food', refill_triggers=['eat'], charge=Charge(2)),
            Resource(name='water', refill_triggers=['drink'], charge=Charge(2)),
            Resource(name='exhaust', refill_triggers=['short_rest'], charge=Charge(2)),
            Resource(name='dashes', refill_triggers=['eat'], charge=Charge(2)),
        ]  # class Resource food, water, exhaust, dashes

        self.id = uuid4()

    def do_short_rest(self):
        for res in self.resources:
            if 'short_rest' in res.refill_triggers:
                res.charge.refill()

    def do_long_rest(self):
        for res in self.resources:
            if 'long_rest' in res.refill_triggers:
                res.charge.refill()


class PersonalInfo:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_character'
        self.race = kwargs['race'] if 'race' in kwargs else None
        self.background = kwargs['background'] if 'background' in kwargs else None
        self.alignment = kwargs['alignment'] if 'alignment' in kwargs else None
        self.skin_color = kwargs['skin_color'] if 'skin_color' in kwargs else None
        self.eyes_color = kwargs['eyes_color'] if 'eyes_color' in kwargs else None
        self.hair_color = kwargs['hair_color'] if 'hair_color' in kwargs else None
        self.other_styling = kwargs['other_styling'] if 'other_styling' in kwargs else None
        self.personality_traits = kwargs['personality_traits'] if 'personality_traits' in kwargs else None
        self.ideals = kwargs['ideals'] if 'ideals' in kwargs else None
        self.bonds = kwargs['bonds'] if 'bonds' in kwargs else None
        self.flaws = kwargs['flaws'] if 'flaws' in kwargs else None
        self.height = kwargs['height'] if 'height' in kwargs else None
        self.weight = kwargs['weight'] if 'weight' in kwargs else None
        self.gender = kwargs['gender'] if 'gender' in kwargs else None
        self.body_form = kwargs['body_form'] if 'body_form' in kwargs else None
        self.birth_year = kwargs['birth_year'] if 'birth_year' in kwargs else None


class LevelBasedStats:
    def __init__(self):
        self.level = 0
        self.stats = {
            'STR': 0,
            'CON': 0,
            'DEX': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0,
        }
        self.stat_mods = {
            'STR': 0,
            'CON': 0,
            'DEX': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0,
        }
        self.saving_throw_mods = {
            'STR': 0,
            'CON': 0,
            'DEX': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0,
        }
        self.skills = {
            'Athletics': 0,
            'Acrobatics': 0,
            'Sleight of hand': 0,
            'Stealth': 0,
            'Arcana': 0,
            'History': 0,
            'Investigation': 0,
            'Nature': 0,
            'Religion': 0,
            'Animal handling': 0,
            'Insight': 0,
            'Medicine': 0,
            'Perception': 0,
            'Survival': 0,
            'Deception': 0,
            'Intimidation': 0,
            'Performance': 0,
            'Persuasion': 0,
        }
        self.proficiency_mod = 0
        self.passive_perception_mod = 0
        self.initiative_mod = 0
        self.speed = 0
        self.hp = 0
        self.hit_dice = ''
        self.ac = 0


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
