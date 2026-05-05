from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        pass

class Fireball(Spell):
    def __init__(self):
        super().__init__("Огненный шар", 35, 15)
    
    def cast(self):
        return self.damage

class IceLance(Spell):
    def __init__(self):
        super().__init__("Ледяное копьё", 25, 10)
    
    def cast(self):
        return self.damage

class LightningBolt(Spell):
    def __init__(self):
        super().__init__("Молния", 40, 20)
    
    def cast(self):
        return self.damage