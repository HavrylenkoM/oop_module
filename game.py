import models
import exceptions


def play():
    global name
    print("Enter your name")
    name = input()
    print("Enter start")
    start = input()
    player = models.Player(name)
    level = 1
    enemy = models.Enemy(level)
    global score
    score = 0
    score = models.Player(score)
  
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except exceptions.EnemyDown:
            level += 1
            print("Enemy down, meet new enemy with level ", level)
            enemy = models.Enemy(level)

try:
    play()
except exceptions.GameOver:
    print("Game over:(")
    print('Your score is ', score)
    print(score)
finally:
    print("Good bye!")
