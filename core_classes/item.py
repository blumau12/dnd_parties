from uuid import uuid4


class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_item'
        self.notes = kwargs['notes'] if 'notes' in kwargs else []
        self.weight = kwargs['weight'] if 'weight' in kwargs else 0
        self.cost = kwargs['cost'] if 'cost' in kwargs else 0
        self.shelf_life = kwargs['shelf_life'] if 'shelf_life' in kwargs else None  # class ShelfLife
        self.effects = kwargs['effects'] if 'effects' in kwargs else ''  # sets str=19
        self.resources = []  # class Resource

        self.is_unique = kwargs['is_unique'] if 'is_unique' in kwargs else False
        self.is_map = kwargs['is_map'] if 'is_map' in kwargs else False
        self.is_text_paper = kwargs['is_text_paper'] if 'is_text_paper' in kwargs else False

        self.character = kwargs['character'] if 'character' in kwargs else None  # class Character
        self.equiped_as = None
        self.charge = kwargs['charge'] if 'charge' in kwargs else None  # class Charge

        self.id = uuid4()

    def equip(self, _as):
        assert _as in (
            None,
            'helmet', 'medallion',
            'right_hand_carry', 'left_hand_carry',
            'right_hand_wear', 'left_hand_wear',
            'both_hands_carry', 'both_hands_wear',
            'shirt', 'belt',
            'right_leg_wear', 'left_leg_wear', 'both_legs_wear',
            'left_foot_wear', 'right_foot_wear', 'both_feet_wear')
        self.equiped_as = _as
