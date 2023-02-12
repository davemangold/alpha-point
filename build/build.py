from game import Game
from level import Level
from build.buildio import Control
from build.buildui import MainUI
from build.builder import Builder
from config import level_config


class Construct(Game):
    """Customized derivative of Game class used as level builder."""

    # TODO: do I need to init parent class?
    def __init__(self, level=1):

        self.debug = True
        self.build = True
        self.control = Control(self)
        self.level = Level(self)
        self.player = Builder(self)
        self.ui = MainUI(self)
        self.setup(level_number=level)

    def __exit__(self, exc_type, exc_value, exc_traceback):

        return

    def setup_level(self, level_number):
        """Set up the game level."""

        self.level = Level(self, level_number)
        self.level.build()

    def setup_player(self):
        """Set up the player based on the game level"""

        self.player.orientation = 2
        self.player.move_to(0, 0)
        self.player.last_action = None

    def setup(self, level_number):
        """Set up game elements."""

        # setup level before player
        self.setup_level(level_number)
        self.setup_player()

    def mainloop(self):
        """The main game loop."""

        while True:

            self.ui.process_input(self.ui.prompt())
