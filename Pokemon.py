class Pokemon:
    def __init__(self, name, level, nickname=None, base_hp=10):
        self.name = name
        self.level = level
        self.nickname = nickname
        self.base_hp = base_hp
        self.health = self.get_max_health
    
    
class FireType(Pokemon):
    def __init__(self, name, level, nickname=None):
        self.flame_power = 10

        super().__init__(name, level, 80, nickname)

class WaterType(Pokemon):
    def __init__(self, name, level, nickname=None):
        self.water_resistance = 8

        super().__init__(name, level, 90, nickname)

class GrassType(Pokemon):
    def __init__(self, name, level, nickname=None):
        self.regeneration = 5

        super().__init__(name, level, 85, nickname)