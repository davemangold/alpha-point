import utility
from level.map import Map
from level.system import System
from config import level_config


class Level(object):
    """Level with which the player interacts."""

    def __init__(self, game, number=0):
        self.game = game
        self.number = number
        self.name = level_config[self.number]['name']
        self.map = Map(self)
        self.system = System(self)

    def build(self):
        """Build the specified level."""

        # system must be built before map
        self.system.build()
        self.map.build()

    def is_complete(self):
        """Returns True if the player is at the final cell of the level, otherwise False."""

        return self.map.get_cell(*self.game.player.location) is self.map.exit_cell

    def has_next_level(self):
        """Returns True if a next level exists in the config, otherwise False."""

        return utility.level_exists(self.number + 1)
