import os
import utility
from level import Level
from game.gameio import Control
from game.gameui import MainUI
from game.gameui import StartUI
from game.gameui import StoryUI
from game.gameui import GameCompleteUI
from game.gameui import PlayerDeadUI
from character.player import Player
from config import level_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self, debug=False, level=1):

        self.debug = debug
        self.control = Control(self)
        self.level = Level(self)
        self.player = Player(self)
        self.ui = StartUI(self)
        self.setup(level_number=level)

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):

        if not self.debug:
            utility.save_object(self, 'game_exit')

    def setup_level(self, level_number):
        """Setup the game level."""

        self.level = Level(self, level_number)
        self.level.build()

        if not self.debug:
            utility.save_object(self, 'level_start')

    def setup_player(self):
        """Setup the player based on the game level"""

        map_config = level_config[self.level.number]['map']
        enter_coords = map_config['coord_enter']
        enter_orientation = map_config['orientation_enter']

        self.player.orientation = enter_orientation
        self.player.move_to(*enter_coords)
        self.player.last_action = None

    def setup(self, level_number):
        """Setup game elements."""

        # create save folder, if needed
        if not os.path.isdir('.save'):
            os.mkdir('.save')

        # setup level before player
        self.setup_level(level_number)
        self.setup_player()

    def reset(self):
        """Reset the game."""

        self.__init__()

    def mainloop(self):
        """The main game loop."""

        while True:

            if isinstance(self.ui, StartUI):
                if self.debug is True:
                    self.ui = MainUI(game=self)

            if isinstance(self.ui, MainUI):
                if self.player.cell.has_story() and not self.player.cell.story_seen:
                    self.ui = StoryUI(game=self)
                if self.level.kills_player():
                    death = self.level.get_death()
                    self.ui = PlayerDeadUI(game=self, message=death.description)
                if self.level.is_complete():
                    if self.level.has_next_level():
                        self.ui.next_level()
                    else:
                        self.ui = GameCompleteUI(game=self)
                    continue

            self.ui.process_input(self.ui.prompt())
