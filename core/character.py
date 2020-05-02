
class Character:
    def __init__(self, personal_info, char_based_stats, situational_stats):
        self.personal_info = personal_info
        self.char_based_stats = char_based_stats
        self.situational_stats = situational_stats
        self.items = []
        self.active_states = []
