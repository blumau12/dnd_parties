
class ActiveState:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_active_state'
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.refill_triggers = []
        self.charge = None  # class Charge
        self.effect = None  # class Effect
        self.works_always = False
        self.is_active = None
