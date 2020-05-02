
class WorldDatetime:
    def __init__(self, start_minutes=0):
        self.minutes = start_minutes

    def datetime(self):
        total_minutes = self.minutes
        years = total_minutes // 525600
        total_minutes -= years * 525600
        months = total_minutes // 43200
        total_minutes -= months * 43200
        decades = total_minutes // 14400
        total_minutes -= decades * 14400
        days = total_minutes // 1440
        total_minutes -= days * 1440
        hours = total_minutes // 60
        total_minutes -= hours * 60
        minutes = total_minutes
        result = {
            'year': years + 1,
            'month': months + 1,
            'decade': decades + 1,
            'day': days + 1,
            'hour': hours,
            'minute': minutes,
        }
        return result

    def day_number(self):
        return (self.minutes // 1440) + 1

    def __add__(self, minutes):
        return self.minutes + minutes

    def __sub__(self, minutes):
        return self.minutes - minutes

    def __iadd__(self, minutes):
        self.minutes += minutes

    def __isub__(self, minutes):
        self.minutes -= minutes
