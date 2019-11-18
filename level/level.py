from level.map import Map
from level.system import System
from config import level_config


class Level(object):
    """Level with which the player interacts."""

    def __init__(self, game):
        self.game = game
        self.map = Map(self)
        self.system = System(self)
        self.number = 0
        self.name = ''

    def build(self, level_number):
        """Build the specified level."""

        # system must be built before map
        self.system.build(level_number)
        self.map.build(level_number)
        self.number = level_number

    def is_complete(self):
        """Returns True if the player is at the final cell of the level, otherwise False."""

        return self.map.get_cell(*self.game.player.location()) is self.map.exit_cell

    def has_next_level(self):

        return bool(level_config['level'].get(self.number + 1))
