
class Resource:
    """
    food, water, exhaust, dashes
    """
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 'unnamed_active_state'
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.refill_triggers = []
        self.charge = kwargs['charge'] if 'charge' in kwargs else None  # class Charge
        self.effect = ''

    def set_refill_triggers(self, triggers):
        allowed_triggers = (
            'short_rest',
            'long_rest',
            'eat',
            'drink',
            'new_day',
        )
        assert all(t in allowed_triggers for t in triggers)
        self.refill_triggers = triggers
