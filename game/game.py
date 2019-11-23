import os
import shelve
from level import Level
from game.gameio import Control
from game.gameui import MainUI
from game.gameui import StartUI
from game.gameui import StoryUI
from game.gameui import GameCompleteUI
from game.gameui import PlayerDeadUI
from game.gameui import LevelsUI
from character.player import Player
from config import level_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self, debug=False):
        self.debug = debug
        self.save = None
        self.control = Control(self)
        self.level = Level(self)
        self.player = Player(self)
        self.ui = StartUI(self)
        self.setup()

    def __enter__(self):
        self.save = shelve.open('.save/save', writeback=True)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.save.close()

    def setup_level(self, level_number):
        """Setup the game level."""

        level = Level(self)
        level.build(level_number)
        self.level = level

    def setup_player(self):
        """Setup the player based on the game level"""

        map_config = level_config['level'][self.level.number]['map']
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

    def reset(self):
        """Reset the game."""

        # close save files
        self.save.close()

        # delete save files
        save_dir = '.save'
        for file_name in os.listdir(save_dir):
            file_path = os.path.join(save_dir, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # launch a new game instance
        with Game(debug=self.debug) as game:
            game.mainloop()

    def mainloop(self):
        """The main game loop."""

        # initialize to zero if not previously set
        if self.save.get('highest_level') is None:
            self.save['highest_level'] = 0

        while True:

            if isinstance(self.ui, StartUI):
                # skip StartUI in debug mode
                if self.debug is True:
                    self.ui = LevelsUI(game=self)
                # skip intro text if returning to game
                if self.save.get('intro_seen') is True:
                    self.ui.skip_intro = True

            if isinstance(self.ui, MainUI):
                if self.player.cell.has_story() and not self.player.cell.story_seen:
                    self.ui = StoryUI(game=self)
                if self.level.system.kills_player():
                    death = self.level.system.get_death()
                    self.ui = PlayerDeadUI(game=self, message=death['description'])
                if self.level.is_complete():
                    if self.level.number > self.save['highest_level']:
                        self.save['highest_level'] = self.level.number
                    if self.level.number == 0:
                        self.ui = LevelsUI(game=self)
                    elif self.level.has_next_level():
                        self.ui.next_level()
                    else:
                        self.ui = GameCompleteUI(game=self)
                    continue

            self.ui.process_input(self.ui.prompt())
