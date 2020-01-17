import game


class GameOver(Exception):
    def __init__(self):
        self.saveResult()
    
    def saveResult(self):
        with open('scores.txt', 'a') as f:
            return f.write(f"{game.name}, ' '{game.score}, '\n'")
            
                

class EnemyDown(Exception):
    pass

class UnexpectedException(Exception):
    pass
