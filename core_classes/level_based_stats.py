
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
