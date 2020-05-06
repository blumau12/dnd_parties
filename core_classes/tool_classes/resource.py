
class Resource:
    """
    food, water, exhaust, dashes
    """
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_active_state'
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.refill_triggers = kwargs['refill_triggers'] if 'refill_triggers' in kwargs else {}
        # self.refill_triggers = {'short_rest': 2, } (0 if refill all)
        self.charge = kwargs['charge'] if 'charge' in kwargs else None  # class Charge
        self.effect = ''

    def set_refill_triggers(self, triggers):
        allowed_triggers = (
            'short_rest',
            'long_rest',
            'eat_full',
            'drink_full',
            'eat_half',
            'drink_half',
            'new_day',
        )
        assert all(t in allowed_triggers for t in triggers)
        self.refill_triggers = triggers
