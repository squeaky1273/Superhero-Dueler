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
      ''' Return a value between 0 and the value set by self.max_damage.'''
      return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        """
        name: String
        max_block: integer
        """
        self.name: name
        self.max_block: max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        """
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        

if __name__ == "__main__":
    # Test the Ability class
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())