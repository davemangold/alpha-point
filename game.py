from player import Player
from level import Level
from gameui import MainUI
from gameui import LevelCompleteUI
from config import levels_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self):
        self.level = Level(self)  # level must be created before player
        self.player = Player(self)
        self.gameui = MainUI(self)

    def setup(self, level_number=0):
        """Setup game elements before allowing play."""

        level_config = levels_config['levels'][level_number]
        self.level.build_from_config(level_config)
        self.level.number = level_number
        self.player.x = level_config['map']['coord_enter'][0]
        self.player.y = level_config['map']['coord_enter'][1]

    def mainloop(self):
        """The main game loop."""

        while True:
            if self.level.is_complete() and isinstance(self.gameui, MainUI):
                self.gameui = LevelCompleteUI(self)
            self.gameui.process_input(self.gameui.prompt())
