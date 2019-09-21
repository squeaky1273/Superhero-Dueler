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
        self.abilities = []
        self.armors = []
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
        total_armor = 0

        for armor in self.armors:
            block = armor.block()
            total_armor = total_armor + block
        return sum
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health = self.current_health - damage

        return self.current_health

    def is_alive(self):
         '''Return True or False depending on whether the hero is alive or not.
         '''
         

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)