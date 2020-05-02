
class ShelfLife:
    def __init__(self, start_day, shelf_life):
        self.start_day = start_day
        self.shelf_life = shelf_life
        self.expiration_day = start_day + shelf_life
