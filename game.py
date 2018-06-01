from player import Player
from level import Level
from gameui import MainUI
from gameui import LevelsUI
from gameui import StartUI
from gameui import StoryUI
from gameui import LevelCompleteUI
from config import level_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self):
        self.level = Level(self)
        self.player = Player(self)
        self.gameui = StartUI(self)
        self.setup()

    def setup_level(self, level_number):
        """Setup the game level."""

        level = Level(self)
        level.build(level_number)
        self.level = level

    def setup_player(self):
        """Setup the player based on the game level"""

        map_config = level_config['levels'][self.level.number]['map']
        enter_coords = map_config['coord_enter']
        enter_orientation = map_config['orientation_enter']

        self.player.move_to(*enter_coords)
        self.player.orientation = enter_orientation
        self.player.inventory.clear_items()

    def setup(self, level_number=0):
        """Setup game elements."""

        # setup level before player
        self.setup_level(level_number)
        self.setup_player()

    def mainloop(self):
        """The main game loop."""

        while True:
            if isinstance(self.gameui, MainUI):
                if self.player.cell.has_story_text() and not self.player.cell.story_seen:
                    self.gameui = StoryUI(self)
                if self.level.is_complete():
                    if self.level.number == 0:
                        self.gameui = LevelsUI(self)
                    else:
                        self.gameui = LevelCompleteUI(self)
            self.gameui.process_input(self.gameui.prompt())
