
class PersonalInfo:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else None
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
