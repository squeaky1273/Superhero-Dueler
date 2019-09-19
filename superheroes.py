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

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())