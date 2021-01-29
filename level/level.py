import utility
from level.map import Map
from level.system import System
from level.death import DeathFactory
from config import level_config


class Level(object):
    """Level with which the player interacts."""

    def __init__(self, game, number=1):
        self.game = game
        self.number = number
        self.name = level_config[self.number]['name']
        self.weather = level_config[self.number]['weather']
        self.system = System(self)
        self.map = Map(self)
        self.deaths = []

    def build(self):
        """Build the specified level."""

        # system must be built before map
        self.system.build()
        self.map.build()

        # add death scenarios (requires built system and map)
        for death_config in level_config[self.number]['deaths']:
            self.deaths.append(DeathFactory.make_from_config(self, death_config))

    def is_complete(self):
        """Returns True if the player is at the final cell of the level, otherwise False."""

        return self.map.get_cell(*self.game.player.location) is self.map.exit_cell

    def has_next_level(self):
        """Returns True if a next level exists in the config, otherwise False."""

        return utility.level_exists(self.number + 1)

    def get_death(self):
        """Return the first death config satisfied, otherwise None."""

        for death in self.deaths:
            if death.scenario_satisfied():
                return death

        return None

    def kills_player(self):
        """Return True if the level is in a state that kills the player, otherwise False."""

        death = self.get_death()

        if death is not None:
            return True

        return False
