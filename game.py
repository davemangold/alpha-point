import sys
import utility
import exception
from player import Player
from level import Level
from gameui import MainUI
from config import levels_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self):
        self.level = Level(self)  # level must be created before player
        self.player = Player(self)
        self.gameui = MainUI(self)

    def setup(self):
        """Setup game elements before allowing play."""

        level_config = levels_config['levels']['0']
        self.level.build_from_config(level_config)
        self.player.x = level_config['map']['coord_enter'][0]
        self.player.y = level_config['map']['coord_enter'][1]

    def mainloop(self):
        """The main game loop."""

        while True:
            if self.level.is_complete():
                self.gameui.alert = 'Congratulations! You win.'
            self.gameui.process_input(self.gameui.prompt("What should I do? "))
