
class ShelfLife:
    def __init__(self, start_datetime, shelf_life):
        self.start_datetime = start_datetime  # class WorldDatetime
        self.shelf_life = shelf_life  # class int
        self.expiration_datetime = start_datetime + shelf_life
