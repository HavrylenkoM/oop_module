import game


class GameOver(Exception):
    """Game saving mechanics"""


    def __init__(self):
        self.save_result()

    def save_result(self):
        with open('scores.txt', 'a') as file:
            return file.write(f"{game.player.name} - {game.player.score} \n")


class EnemyDown(Exception):
    pass
