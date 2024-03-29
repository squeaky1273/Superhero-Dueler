import random
from random import randint, choice

class Ability:
    def __init__(self, name, max_strength): #Initialization function
        """
        name: String
        max_damage: Integer
        """
        self.name = name
        self.max_damage = max_strength

    def attack(self): 
      ''' Return a value between 0 and the value set by self.max_damage.'''
      return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block): #Initialization function
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return randint(0, int(self.max_block))

class Hero:
    def __init__(self, name, starting_health = 100): #Initialization function
        """ Instance properties
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """   
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list (append)'''
        self.abilities.append(ability)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
          '''
        total_attack = 0
        for ability in self.abilities:
            attack = ability.attack()
            total_attack = total_attack + attack

        return total_attack

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object
        '''
        self.armors.append(armor)
        
    def defend(self, damage_amt=0):
        '''Runs `block` method on each armor.
        Returns sum of all blocks
        '''  
        total_armor = 0

        for armor in self.armors:
            total_armor = total_armor + armor.block()

        difference = total_armor - damage_amt 
        return difference
   
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health = int(self.current_health) - int(damage)

        return self.current_health
   
    def is_alive(self):
         '''Return True or False depending on whether the hero is alive or not.
         '''
         if int(self.current_health) <= 0:
             return False
         else:
             return True 

    def fight(self, opponent):
          ''' Current Hero will take turns fighting the opponent hero passed in.
          '''
          while self.is_alive() and opponent.is_alive(): # While self and opponent are alive
              if len(self.abilities) > 0 and len(opponent.abilities) > 0: # If both self and opponent are alive
                  
                  self_turn = self.attack() # Self ability/attack
                  opponent.take_damage(self_turn)

                  opponent_turn = opponent.attack() # Opponent ability/attack
                  self.take_damage(opponent_turn)

                  if opponent.is_alive() == False:
                      self.add_kill(1)
                      opponent.add_deaths(1)
                      print(self.name + " wins!") # Self wins
                  else: 
                      self.add_deaths(1)
                      opponent.add_kill(1)
                      print(opponent.name + " wins!") # Opponent wins
             
              elif len(self.abilities) == 0 and len(opponent.abilities) == 0: # If no abilities exist
                  print("Draw!")
                  print("----")
                  return
    
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        """This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage//2, self.max_damage)     

class Team():
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
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)
    
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        #Thanks/credit to Aucoeur Ngo
        while len(self.survived()) > 0 or len(other_team.survived() > 0):
            self.hero = choice(self.survived())
            self.opponent = choice(other_team.survived())

            return self.hero.fight(self.opponent)
    
    def survived(self): # helps the attack function right above
        alive = [hero for hero in self.heroes if hero.is_alive()]
        return alive
    
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print("Hero: " + hero.name)
            print("Death: " + str(hero.deaths))
            print("Kills: " + str(hero.kills))

class Arena:
    def __init__(self): # Initialization function
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability_name = input("Enter a name for your new ability: ")
        ability_strength = int(input("Enter the strength for your ability: "))
        return Ability(ability_name, ability_strength)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''      
        weapon_name = input("Enter a name for your new weapon: ")
        weapon_strength = int(input("Enter how much damage it makes: "))
        
        return Weapon(weapon_name, weapon_strength)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''  
        armor_name = input("Enter a name for your new armor: ")
        armor_block = int(input("Enter how much damage the armor blocks: "))
        return Armor(armor_name, armor_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''  
        new_hero = input("Enter a name for your hero: ")
        self.starting_health = 100 
        self.hero = Hero(new_hero, self.starting_health)
        
        # enter inputs for the two teams for a fight
        add = True
        while add == True:
            choose = input("Enter:\nA to add Ability: \nB to add Armor: \nC to add a Weapon: \nD to Finish: ")
            # ability
            if choose == "A":
                ability = self.create_ability()
                self.hero.add_ability(ability)
            # armor
            elif choose == "B":
                armor = self.create_armor()
                self.hero.add_armor(armor)
            # weapon
            elif choose == "C":
                weapon = self.create_weapon()
                self.hero.add_weapon(weapon)
            elif choose == "D":
                add = False
            else: 
                print("Please choose one.")
        
        return self.hero

    def build_team_one(self):
        '''Prompt the user to build teams'''
        team_name = input("Enter a name for Team 1: ")
        self.team_one = Team(team_name)
        team_size = input("Enter how many team members in the team: ")
        
        player = 0
        while player < int(team_size):
            new_team_player = self.create_hero()
            self.team_one.add_hero(new_team_player)
            player += 1
    
        self.team_one.view_all_heroes()
        return self.team_one

    def build_team_two(self):
        '''Prompt the user to build teams'''
        team_name = input("Enter a name for Team 2: ")
        self.team_two = Team(team_name)
        team_size = input("Enter how many team members in the team: ")

        player = 0
        while player < int(team_size):
            new_hero_player = self.create_hero()
            self.team_two.add_hero(new_hero_player)
            player += 1 

        self.team_two.view_all_heroes()
        return self.team_two
    
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print(self.team_battle())

        self.team_one_living_heroes = []
        self.team_two_living_heroes = []

        self.team_one.stats()
        self.team_two.stats()

        for hero in self.team_one_living_heroes:
            if hero.is_alive():
                print("Survivors: " + hero.name)

        for hero in self.team_two_living_heroes:
            if hero.is_alive():
                print("Survivors: " + hero.name)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()