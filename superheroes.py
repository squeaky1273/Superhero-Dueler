import random

class Ability:
    def __init__(self, name, attack_strength): #Initialization function
        """
        name: String
        max_damage: Integer
        """
        self.name = name
        self.max_damage = attack_strength

    def attack(self): # 
      ''' Return a value between 0 and the value set by self.max_damage.'''
      return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block): #Initialization function
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
    def __init__(self, name, starting_health = 100): #Initialization function
        """Instance properties
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list (append)'''
        self.abilities.append(ability)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
          '''
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total 

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object
        '''
        self.armors.append(armor)
    
    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
        Returns sum of all blocks
        '''  

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())