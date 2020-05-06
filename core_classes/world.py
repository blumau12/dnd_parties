from core_classes.tool_classes.world_datetime import WorldDatetime


class World:
    def __init__(self, description, start_minute):
        self.description = description
        self.start_minute = start_minute
        self.current_datetime = WorldDatetime(start_minute)  # class WorldDatetime
        self.characters = []
        self.items = []

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_time(self, minutes):
        old_day = self.current_datetime.day_number()
        self.current_datetime += minutes
        if self.current_datetime.day_number() > old_day:
            for obj in self.characters + self.items:
                for res in obj.resources:
                    if 'new_day' in res.refill_triggers:
                        res.charge.refill()

    def trigger(self, trigger):
        for obj in self.characters + self.items:
            for res in obj.resources:
                if trigger in res.refill_triggers:
                    res.charge.refill(res.refill_triggers[trigger])

    def do_short_rest(self, add_60_minutes=False):
        self.trigger('short_rest')
        if add_60_minutes:
            self.add_time(minutes=60)

    def do_long_rest(self, add_8_hours=False):
        self.trigger('long_rest')
        if add_8_hours:
            self.add_time(minutes=8*60)

    def eat_half(self):
        self.trigger('eat_half')

    def drink(self):
        self.trigger('drink_half')

    def eat_full(self):
        self.trigger('eat_full')

    def drink_full(self):
        self.trigger('drink_full')

    def get_character_by_name(self, name):
        for char in self.characters:
            if char.personal_info.name == name:
                return char

    def get_character_by_id(self, _id):
        for char in self.characters:
            if char.id == _id:
                return char
