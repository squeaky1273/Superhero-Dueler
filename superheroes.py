import random
from random import randint

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
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name: name
        self.max_block: max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, int(self.max_block))

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
        self.starting_health = self.current_health = starting_health
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
            total_attack += ability.attack()
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
            block = armor.block()
            total_armor = total_armor + block

        sum = total_armor - damage_amt 
        return sum
   
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health = self.current_health - damage

        return self.current_health
   
    def is_alive(self):
         '''Return True or False depending on whether the hero is alive or not.
         '''
         if int(self.current_health) < 1:
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
                      self.add_kill(1)
                      opponent.add_deaths(1)
                      print(self.name + " wins!") # Self wins
                  else: 
                      self.add_deaths(1)
                      opponent.add_kill(1)
                      print(opponent.name + " wins!") # Opponent wins
             
              elif len(self.abilities) == 0 and len(opponent.abilities) == 0: # If no abilities exist
                  print("Draw!")
    
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
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print("{}".format(hero.name))

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)
        print(hero) 
    
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        your_team = self.survived()
        other_team = other_team.survived()
            
        return your_team.fight(other_team)
    
    def survived(self): # helps the attack function right above
        while True:
            survive = random.choice(self.heroes)
            print(survive)
            if survive == True:
                return survive
    
    def revive_heroes(self, starting_health=100):
        ''' Reset all heroes health to starting_health'''
        self.current_health = starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def is_alive(self):
        if self.current_health < 0:
            return False
        else: 
            return True
           
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print("Hero: " + hero.name)
            print("Death: " + str(hero.num_deaths))
            print("Kills: " + str(hero.num_kills))

class Arena:
    def __init__(self): # Initialization function
        self.team_one: None
        self.team_two: None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability_name = input("Enter a name for your new ability")
        ability_strength = int(input("Enter an the strength for your ability: "))
        return Ability(ability_name, ability_strength)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''      
        weapon_name = input("Enter a name for your new weapon")
        weapon_strength = input("Enter a strength: ")
        return Weapon(weapon_name, int(weapon_strength))

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''  
        armor_name = input("Enter a name for your new armor")
        armor_block = int(input("Enter a block power: "))
        return Armor(armor_name, armor_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''  
        new_hero = input("Enter a name for your hero: ") 
        self.hero = Hero(new_hero)
        
        # enter inputs for the two teams for a fight
        add = True
        while add == True:
            choose = input("Enter:\nA to add Ability\nB to add Armor\nC for a Weapon")
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
                weapon = self.create_weapon
                self.hero.add_weapon(weapon)
        
        return self.hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''    
        team_one_name = input("Enter a name for Team One: ")
        self.team_one = Team(team_one_name)
        team_size = input("Enter how many team members in Team One: ")

        add_hero = 0
        while add_hero < int(team_size):
            self.team_one.add_hero(add_hero)
            add_hero += 1

        return self.team_one

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_two_name = input("Enter a name for Team Two: ")
        self.team_two = Team(team_two_name)
        team_size = input("Enter how many team members in Team Two: ")

        add_hero = 0
        while add_hero < int(team_size):
            self.team_two.add_hero(add_hero)
            add_hero += 1

        return self.team_two

    def team_battle(self):
        '''Battle team_one and team_two together.''' 
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''   
        team_one_live_heroes_names = [] # names of the living heroes in Team 1
        team_two_live_heroes_names = [] # names of the living heroes in Team 2

        # deciding which team wins by how many living heroes they have
        # Team 1
        live_one_heroes = 0 
        for hero in self.team_one.heroes:
            if hero.is_alive():
                live_one_heroes += 1
                team_one_live_heroes_names.append(hero.name)
        # Team 2
        live_two_heroes = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                live_two_heroes += 1
                team_two_live_heroes_names.append(hero.name)

        # which team won
        if live_one_heroes > live_two_heroes: # if there are more living heroes in team 1
            print("Team One wins!!!") # Team 1 wins
        elif live_one_heroes < live_two_heroes: # if there are more living heroes in team 2
            print("Team Two wins!!!") # Team 2 wins
        else:
            print("No winner!!!") # draw/no winner

        # show stats for Team 1
        print("Stats for Team One:")
        self.team_one.stats()
        for name in team_one_live_heroes_names:
            print(name)

        # show stats for Team 2
        print("Stats for Team Two:")
        self.team_two.stats()
        for name in team_two_live_heroes_names:
            print(name)

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