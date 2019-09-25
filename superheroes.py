import random
from random import choice

class Ability:
    def __init__(self, name, attack_strength): #Initialization function
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
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

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
         if self.current_health < 1:
             return False
         else:
             return True 
    
    def fight(self, opponent):
          ''' Current Hero will take turns fighting the opponent hero passed in.
          '''
          while self.is_alive() == True and opponent.is_alive() == True: # While self and opponent are alive
              if len(self.abilities) > 0 and len(opponent.abilities) > 0: # If both self and opponent are alive
                  self_turn = self.attack() # Self ability/attack
                  opponent.take_damage(self_turn)

                  opponent_turn = opponent.attack() # Opponent ability/attack
                  self.take_damage(opponent_turn)

                  if opponent.is_alive() == False:
                      print(self.name + " wins!") # Self wins
                      self.add_kill(1)
                      opponent.add_deaths(1)
                  else: 
                      print(opponent.name + " wins!") # Opponent wins
                      self.add_deaths(1)
                      opponent.add_kill(1)
             
              elif len(self.abilities) == 0 and len(opponent.abilities) == 0: # If no abilities exist
                  print("Draw!")
                  return False
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        pass

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage // 2, self.max_damage)     

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(hero)
                return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print("{}".format(hero.name))

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)
    
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        self.hero = choice(self.hero)
        opponent = choice(other_team.opponent())
        
        self.hero.fight(opponent)
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_heakth = hero.starting_health
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print("Hero: " + hero.name)
            print("Death: " +str(hero.num_deaths))
            print("Kills: " + str(hero.num_kills))

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        pass

    def cretae_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''  
        pass     

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        pass

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''      
        pass

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''  
        pass

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)