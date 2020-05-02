
class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_item'
        self.notes = kwargs['notes'] if 'notes' in kwargs else []
        self.weight = kwargs['weight'] if 'weight' in kwargs else 0
        self.cost = kwargs['cost'] if 'cost' in kwargs else 0
        self.character = kwargs['character'] if 'character' in kwargs else None
        self.active_states = kwargs['active_states'] if 'active_states' in kwargs else []
        self.charge = kwargs['charge'] if 'charge' in kwargs else None  # class Charge
        self.shelf_life = kwargs['shelf_life'] if 'shelf_life' in kwargs else None  # class ShelfLife
        self.is_unique = kwargs['is_unique'] if 'is_unique' in kwargs else False
        self.is_map = kwargs['is_map'] if 'is_map' in kwargs else False
        self.is_text_paper = kwargs['is_text_paper'] if 'is_text_paper' in kwargs else False
        self.is_equiped = False
