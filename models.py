import exceptions
import random
import settings



class Player:
    """ Main class for game mechanics"""


    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES
        self.score = 0


    @staticmethod
    def fight(attack, defense):
        """Main game rules"""
        if attack == defense:
            return 0
        elif (attack == settings.WARRIOR and defense == settings.ROGUE) or \
            (attack == settings.ROGUE and defense == settings.WIZARD) or \
            (attack == settings.WIZARD and defense == settings.WARRIOR):
            return 1
        else:
            return -1

    def attack(self, enemy):
        """Attack mechanics for player"""
        print(self.name + ' attack now:')
        while True:
            print('Choose your hero: 1 for Warrior, 2 for Wizard, 3 for Rogue')
            your_attack = int(input())
            if your_attack in [settings.WARRIOR, settings.WIZARD, settings.ROGUE]:
                break

        enemy_attack = Enemy.select_attack()
        print('Enemy choose is ', enemy_attack)

        result = Player.fight(your_attack, enemy_attack)
        if result == 0:
            print("Tie")
        elif result == 1:
            enemy.decrease_lives()
            self.score += 1
            print("You win")
            print('Enemy has ', enemy.lives, 'lives left')
        elif result == -1:
            self.decrease_lives()
            print('Enemy wins')
            print('You have ', self.lives, 'lives left')

    def defense(self, enemy):
        """Defense mechanics for player"""
        print('Choose your hero for defence')
        while(True):
            print('Enter 1 for Warrior, 2 for Wizard, 3 for Rogue')
            your_attack = int(input())
            if (your_attack in [settings.WARRIOR, settings.WIZARD, settings.ROGUE]):
                break

        enemy_attack = Enemy.select_attack()
        print('Enemy choise is', enemy_attack)

        result = Player.fight(enemy_attack, your_attack)
        if result == 0:
            print('Tie')
        elif result == 1:
            self.decrease_lives()
            print('Enemy wins')
            print('You have ', self.lives, ' lives left')
        elif result == -1:
            enemy.decrease_lives()
            print('You win')
            print('Enemy has ', enemy.lives, ' lives left')

    def decrease_lives(self):
        self.lives -= 1
        if (self.lives == 0):
            raise exceptions.GameOver()


class Enemy:
    """Class for game mechanics of computer player"""


    def __init__(self, level):
        self.lives = self.level = level

    @staticmethod
    def select_attack():
        """Random hero choosing for computer"""
        return random.choice([settings.WARRIOR, settings.WIZARD, settings.ROGUE])

    def decrease_lives(self):
        """HP decreasing for computer, after loosing deffence phase"""
        self.lives -= 1
        if (self.lives == 0):
            raise exceptions.EnemyDown()
