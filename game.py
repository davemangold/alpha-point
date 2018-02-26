from player import Player
from level import Level
from gameui import MainUI
from gameui import StartUI
from gameui import LevelCompleteUI
from config import levels_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self):
        self.level = Level(self)  # level must be created before player
        self.player = Player(self)
        self.gameui = StartUI(self)
        self.setup()

    def set_level(self, level_number=1):
        """Set the game level."""

        level_config = levels_config['levels'][level_number]

        level = Level(self)
        level.build_from_config(level_config)
        level.number = level_number
        self.level = level

    def set_player(self):
        """Set the player based on the game level"""

        level_config = levels_config['levels'][self.level.number]

        player = Player(self)
        player.x = level_config['map']['coord_enter'][0]
        player.y = level_config['map']['coord_enter'][1]
        self.player = player

    def setup(self, level_number=1):
        """Setup game elements before allowing play."""

        self.set_level(level_number)
        self.set_player()  # set based on current level number

    def mainloop(self):
        """The main game loop."""

        while True:
            if self.level.is_complete() and isinstance(self.gameui, MainUI):
                self.gameui = LevelCompleteUI(self)
            self.gameui.process_input(self.gameui.prompt())
