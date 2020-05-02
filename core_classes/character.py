
class Character:
    def __init__(self, personal_info, level_based_stats, situational_stats):
        self.personal_info = personal_info
        self.level_based_stats = level_based_stats
        self.situational_stats = situational_stats
        self.items = []
        self.active_states = []
