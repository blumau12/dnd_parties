from . import core_classes


class Session:
    """
    Создает все сущности.
    Имеет ссылки ко всем объектам игры.
    """
    def __init__(self, companies):
        self.companies = companies

        self.current_company = None  # class Company

    def switch_company(self, company):
        self.current_company = company

    def add_new_company(self, *args, **kwargs):
        company = core_classes.Company(*args, **kwargs)
        self.companies.append(company)
        if self.current_company is None:
            self.current_company = company

    def add_new_player(self, *args, **kwargs):
        player = core_classes.Player(*args, **kwargs)
        self.current_company.add_player(player)

    def add_new_world(self, *args, **kwargs):
        world = core_classes.World(*args, **kwargs)
        self.current_company.add_world(world)

    def add_new_character(self, **kwargs):
        character = core_classes.Character(
            personal_info=core_classes.PersonalInfo(**kwargs),
            level_based_stats=core_classes.LevelBasedStats(),
            situational_stats=core_classes.SituationalStats())
        self.current_company.add_character(character)

    def add_new_item(self, **kwargs):
        if 'max_charge' in kwargs:
            kwargs['charge'] = core_classes.Charge(kwargs.pop('max_charge'))
        if 'start_minutes' in kwargs and 'shelf_life' in kwargs:
            start_datetime = core_classes.WorldDatetime(kwargs.pop('start_minutes'))
            kwargs['shelf_life'] = core_classes.ShelfLife(start_datetime, kwargs.pop('shelf_life'))
        item = core_classes.Item(**kwargs)
        self.current_company.add_item(item)
