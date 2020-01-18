"""Module for implementing exceptions """


class GameOver(Exception):
    """In my case that is just useless that do nothing."""

    def __init__(self):
        super().__init__()


class EnemyDown(Exception):
    """One more almost useless exception."""
    pass
