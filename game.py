import exceptions
import models



def play():
    """Main game function, with name inputing and level upgrading"""
    print("Enter your name")
    name = input()
    print("Enter start")
    start = input()
    if start == 'start':
        pass
    global player
    player = models.Player(name)
    level = 1
    enemy = models.Enemy(level)
  
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except exceptions.EnemyDown:
            level += 1
            player.score += 5
            print("Enemy down, meet new enemy with level ", level)
            enemy = models.Enemy(level)


#if __name__ == "__main__":
try:
    play()
except exceptions.GameOver:
    print("Game over:(")
    print('Your score is ', player.score)
finally:
    print("Good bye!")
