import random

class Ability:
    def __init__(self, name, attack_strength):
        """
        name: String
        max_damage: Integer

        """
        self.name = name
        self.max_damage = attack_strength

    def attack(self):

        return random.randint(2, 7)