from unit import Unit

class Character(Unit):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        
        self.character_class = character_class.lower()
        
        if self.character_class not in ['warrior', 'mage', 'hunter']:
            raise ValueError("Неверный класс персонажа")
        
        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.mana = self.calculate_max_mana()
    
    def calculate_max_health(self):
        return self.constitution * 10 + self.strength // 2
    
    def calculate_max_mana(self):
        if self.character_class == 'warrior':
            return self.intelligence + self.strength // 2
        elif self.character_class == 'mage':
            return self.intelligence * 3 + self.wisdom
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.5) + self.wisdom // 2
    
    def calculate_damage(self):
        if self.character_class == 'warrior':
            return int(self.strength * 2.2) + self.constitution // 3
        elif self.character_class == 'mage':
            return int(self.intelligence * 2.5) + self.wisdom // 2
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.9) + self.strength // 3
    
    def calculate_defense(self):
        if self.character_class == 'warrior':
            return int(self.constitution * 1.8) + self.strength // 4
        elif self.character_class == 'mage':
            return int(self.wisdom * 1.3) + self.intelligence // 6
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.6) + self.constitution // 5