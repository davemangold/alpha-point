import os
import json
import shelve
import threading
import urllib.request
import utility
from datetime import datetime
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

        self.save = self.init_save()
        self.weather_data = None
        self.weather_thread = threading.Thread(target=self.__set_weather_data)
        self.weather_thread.start()
        self.debug = debug
        self.control = Control(self)
        self.level = Level(self)
        self.player = Player(self)
        self.ui = StartUI(self)
        self.setup(level_number=utility.start_level(self.save))

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):

        self.save.close()

    def __set_weather_data(self):
        """Get latest Mars weather from NASA InSight API."""

        def clean(value):

            return '-' if value in (0, None) else value

        weather_data = {
            'sol': '-',
            'time': '-',
            'temperature': {
                'value': '-',
                'units': 'C'
            },
            'wind': {
                'speed': {
                    'value': '-',
                    'units': 'KPH'
                },
                'direction': {
                    'value': '-',
                    'units': 'Deg'
                }
            },
            'pressure': {
                'value': '-',
                'units': 'Pa'
            }
        }

        request_url = 'https://mars.nasa.gov/rss/api?feed=weather&category=insight&feedtype=json&ver=1.0'

        try:
            with urllib.request.urlopen(request_url) as response:
                data = json.loads(response.read())

            latest_sol = data['sol_keys'][0]
            earliest_weather = data[latest_sol]  # not latest, but older days are more likely complete

        except:
            return weather_data

        try:
            timestring = datetime.now().strftime('%H:%M:%S')  # use current local time for game
            weather_data['sol'] = latest_sol
            weather_data['time'] = timestring

        except (ValueError, TypeError):  # bad or missing timestamp
            return weather_data

        # get weather measurements
        try:
            weather_data['temperature']['value'] = clean(
                earliest_weather
                .get('AT')
                .get('av'))

        except (KeyError, AttributeError):
            pass

        try:
            weather_data['wind']['speed']['value'] = clean(
                earliest_weather
                .get('HWS')
                .get('av'))

        except (KeyError, AttributeError):
            pass

        try:
            weather_data['wind']['direction']['value'] = clean(
                earliest_weather
                .get('WD')
                .get('most_common')
                .get('compass_degrees'))

        except (KeyError, AttributeError):
            pass

        try:
            weather_data['pressure']['value'] = clean(
                earliest_weather
                .get('PRE')
                .get('av'))

        except (KeyError, AttributeError):
            pass

        self.weather_data = weather_data

    def init_save(self):
        """Setup save environment, if necessary."""

        if not os.path.isdir('.save'):
            os.mkdir('.save')

        save = shelve.open('.save/save', writeback=True)
        return save

    def setup_level(self, level_number):
        """Setup the game level."""

        level = Level(self, level_number)
        level.build()
        self.level = level

    def setup_player(self):
        """Setup the player based on the game level"""

        map_config = level_config[self.level.number]['map']
        enter_coords = map_config['coord_enter']
        enter_orientation = map_config['orientation_enter']

        self.player.orientation = enter_orientation  # set before player move
        self.player.move_to(*enter_coords)
        self.player.inventory.clear_items()

    def setup(self, level_number):
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
                        self.save['game_complete'] = True
                        self.ui = GameCompleteUI(game=self)
                    continue

            self.ui.process_input(self.ui.prompt())
