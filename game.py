from player import Player
from level import Level
from gameui import MainUI
from gameui import StartUI
from gameui import StoryUI
from gameui import LevelCompleteUI
from config import levels_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self):
        self.level = Level(self)  # level must be created before player
        self.player = Player(self)
        self.gameui = StartUI(self)
        self.setup()

    def set_level(self, level_number=0):
        """Set the game level."""

        level = Level(self)
        level.build(level_number)
        self.level = level

    def set_player(self):
        """Set the player based on the game level"""

        enter_coords = levels_config['levels'][self.level.number]['map']['coord_enter']

        player = Player(self)
        player.move_to(*enter_coords)
        self.player = player

    def setup(self, level_number=0):
        """Setup game elements before allowing play."""

        # set level before setting player
        self.set_level(level_number)
        self.set_player()

    def mainloop(self):
        """The main game loop."""

        while True:
            if isinstance(self.gameui, MainUI):
                if self.player.cell.has_story_text() and not self.player.cell.story_seen:
                    self.gameui = StoryUI(self)
                if self.level.is_complete():
                    if self.level.number == 0:
                        self.gameui = StartUI(self)
                    else:
                        self.gameui = LevelCompleteUI(self)
            self.gameui.process_input(self.gameui.prompt())
