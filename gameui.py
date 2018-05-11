import os
import sys
import time
import utility
import exception
from random import randrange
from random import random
from config import game_config
from config import levels_config


class BaseUI(object):
    """Base game user interface class."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.alert = None
        self.separator = '-' * game_config['ui']['width']

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        pass

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  What should I do? "

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    @staticmethod
    def clear_screen():
        """Clear the screen."""

        os.system('cls')

    def get_alert(self):
        """Get the alert message, then set to None."""

        alert = self.alert
        self.alert = None
        if alert is not None:
            alert = utility.format_ui_text(alert)
        return alert

    def get_ui(self):
        """Get the UI text."""

        return 'Base UI'

    @staticmethod
    def decorate_ui(ui_text):

        ui_text_decorated = '\n'.join(["  " + line for line in ui_text.split('\n')])
        return ui_text_decorated

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

    def restart_level(self):
        """Restart the current level."""

        self.game.setup(self.game.level.number)
        self.game.gameui = MainUI(self.game)

    def next_level(self):
        """Go to the next level."""

        self.game.setup(self.game.level.number + 1)
        self.game.gameui = MainUI(self.game)


class StartUI(BaseUI):
    """Game user interface for a system terminal object."""

    def __init__(self, *args, **kwargs):
        super(StartUI, self).__init__(*args, **kwargs)
        self.splash_seen = False
        self.story_seen_1 = False
        self.story_seen_2 = False

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        if self.story_seen_2 is True:
            self.leave()

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        self.display()
        message = "  Press Enter to continue..."
        response = input(message)
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_splash_text = self.get_splash_text()
        ui_story_text_1 = self.get_story_text_1()
        ui_story_text_2 = self.get_story_text_2()

        if self.splash_seen is False:
            ui_body_text = ui_splash_text
        elif self.splash_seen is True and self.story_seen_1 is False:
            ui_body_text = ui_story_text_1
        else:
            ui_body_text = ui_story_text_2

        ui_elements.append(self.separator)
        ui_elements.append(ui_body_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def display(self):
        """Display the UI."""

        ui_text = self.decorate_ui(self.get_ui())
        ui_text_lines = ui_text.split('\n')
        show_text = ui_text_lines[0]
        print(show_text)
        for line in ui_text_lines[1:]:
            time.sleep(0.01)
            show_text = '\n'.join([show_text, line])
            self.clear_screen()
            print(show_text)

        if self.story_seen_1 is True:
            self.story_seen_2 = True
        if self.splash_seen is True:
            self.story_seen_1 = True

        self.splash_seen = True

    def get_splash_text(self):
        """Get the game splash screen text."""

        return game_config['splash_text']

    def get_story_text_1(self):
        """Return the story intro text."""

        story_text = game_config['story_text_1']
        formatted_text = utility.format_ui_text(story_text)
        return formatted_text

    def get_story_text_2(self):
        """Return the story intro text."""

        story_text = game_config['story_text_2']
        formatted_text = utility.format_ui_text(story_text)
        return formatted_text

    def leave(self):

        self.game.gameui = LevelsUI(self.game)


class LevelsUI(BaseUI):
    """Game user interface presented to the player when a level is completed."""

    def __init__(self, *args, **kwargs):
        super(LevelsUI, self).__init__(*args, **kwargs)

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        # process action input
        if value.isdigit():
            try:
                self.start_level(int(value))
            except KeyError:
                self.alert = "Sorry, that's not a valid level."
        # process quit input
        elif value == 'q':
            self.clear_screen()
            sys.exit()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  Choose a level: "

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = '\n'.join(
            ['{0}. {1}'.format(k, v['name'])
             for k, v in sorted(levels_config['levels'].items())
             if k > 0])

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = '\nq - leave the game'

        return commands

    def start_level(self, level_number):
        """Start the game with the specified level number."""

        self.game.setup(level_number)
        self.game.gameui = MainUI(self.game)


class MainUI(BaseUI):
    """Main game user interface class."""

    def __init__(self, *args, **kwargs):
        super(MainUI, self).__init__(*args, **kwargs)

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        try:
            # process move input
            if value == 'i':
                self.game.player.move_up()
            elif value == 'l':
                self.game.player.move_right()
            elif value == 'k':
                self.game.player.move_down()
            elif value == 'j':
                self.game.player.move_left()
            # process action input
            elif value.isdigit():
                self.game.player.do_action(int(value))
            # process restart or quit input
            elif value == 'r':
                self.restart_level()
            elif value == 'q':
                self.leave()
            # the value wasn't handled
            else:
                self.alert = "I don't know what you mean."
        except exception.MoveError:
            self.alert = "I can't move there."
        except exception.ActionError:
            self.alert = "That's not an option."
        except exception.InterfaceError:
            self.alert = "Dammit! There's something wrong with this thing."

    def add_map_player(self, text_map):
        """Add the player to the map."""

        chars = {0: '^', 1: '>', 2: 'v', 3: '<'}
        char = chars[self.game.player.orientation]
        map_list = utility.text_map_to_nested_list(text_map)
        map_list[self.game.player.y][self.game.player.x] = char

        return utility.nested_list_to_text_map(map_list)

    def add_map_path(self, text_map):
        """Add map path to this map."""

        map_list = utility.text_map_to_nested_list(text_map)
        for cell in self.game.level.map.path.cells:
            map_list[cell.y][cell.x] = '.'

        return utility.nested_list_to_text_map(map_list)

    def get_base_map(self):
        """Get the base map."""

        game_map = self.game.level.map
        text_map = '\n'.join(
            [' '.join(game_map.x_dim * ' ')
             for y in range(game_map.y_dim)])

        return text_map

    def get_map(self):
        """Get the map text."""

        text_map = self.get_base_map()
        text_map = self.add_map_path(text_map)
        # text_map = self.add_map_devices(text_map)
        # text_map = self.add_map_interfaces(text_map)
        text_map = self.add_map_player(text_map)
        map_width = len(text_map.split('\n')[0])
        buffer_width = int((game_config['ui']['width'] - map_width) / 2)
        text_map = '\n'.join([' ' * buffer_width + line for line in text_map.split('\n')])
        return text_map

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = None
        ui_actions_list = []
        for key, action in sorted(self.game.player.actions.items()):
            ui_action_text = utility.format_ui_text('{0}. {1}'.format(key, action.description))
            ui_action_text = ui_action_text.replace('\n', '\n   ')
            ui_actions_list.append(ui_action_text)
        if len(ui_actions_list) > 0:
            ui_actions = '\n'.join(ui_actions_list)

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('\ni - move up\t\tr - restart level\tP - Player\n'
                    'k - move down\t\tq - main menu\t\t. - Path\n'
                    'j - move left\n'
                    'l - move right')

        return commands

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_map = self.get_map()
        ui_alert = self.get_alert()
        ui_report = utility.format_ui_text(self.game.player.report_visible_objects())
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_map)
        ui_elements.append(self.separator)
        ui_elements.append(ui_report)
        if ui_action is not None:
            ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def leave(self):
        """Leave the game and return to the start menu."""

        self.game.gameui = LevelsUI(self.game)


class TerminalUI(BaseUI):
    """Game user interface for a system terminal object."""

    def __init__(self, terminal, *args, **kwargs):
        super(TerminalUI, self).__init__(terminal.system.level.game, *args, **kwargs)
        self.terminal = terminal
        self.precedent = self.game.gameui
        self.initial_flicker = True

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        try:
            # process action input
            if value.isdigit():
                self.terminal.do_action(int(value))
            # process quit input
            elif value == 'q':
                self.leave()
            # the value wasn't handled
            else:
                self.alert = "Unrecognized command."
        except exception.ActionError:
            self.alert = "Unrecognized command."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  {0}@apex-{1}:~$ ".format(self.game.player.name,
                                            '-'.join(self.terminal.name.split()))

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        if ui_action is not None:
            ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = None
        ui_actions_list = []
        for key, action in sorted(self.terminal.actions.items()):
            ui_actions_list.append('{0}. {1}'.format(key, action.description))
        if len(ui_actions_list) > 0:
            ui_actions = '\n'.join(ui_actions_list)

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('\nq - leave the {0}'.format(self.terminal))

        return commands

    def get_welcome(self):
        """Return terminal welcome message text."""

        return "Terminal: {0}".format(self.terminal.address)

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

        if self.initial_flicker is True:
            self.display_flicker()
            self.initial_flicker = False

    def display_flicker(self):
        """Flicker the terminal display."""

        duration = 0.05
        number = randrange(2, 3, 1)
        intervals = [random() * duration for i in range(number)]

        for i in intervals:
            self.clear_screen()
            time.sleep(i)
            print(self.decorate_ui(self.get_ui()))

    def leave(self):
        # reset gameui to the ui that was active at the time this was created
        self.game.gameui = self.precedent


class LevelCompleteUI(BaseUI):
    """Game user interface presented to the player when a level is completed."""

    def __init__(self, *args, **kwargs):
        super(LevelCompleteUI, self).__init__(*args, **kwargs)

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        if value == '1':
            self.restart_level()
        elif value == '2':
            try:
                self.next_level()
            except KeyError:
                self.alert = "This is the last level."
        elif value == 'q':
            self.leave()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  Choose an option: "

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = ('1. Restart level\n'
                      '2. Play next level')

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = '\nq - main menu'

        return commands

    def get_welcome(self):
        """Return UI welcome message text."""

        return "Congratulations! You completed the level."

    def leave(self):
        """Leave the game and return to the start menu."""

        self.game.gameui = LevelsUI(self.game)


class PlayerDeadUI(BaseUI):
    """Game user interface presented to the player when the player dies."""

    def __init__(self, message, *args, **kwargs):
        super(PlayerDeadUI, self).__init__(*args, **kwargs)
        self.message = message

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        if value == '1':
            self.restart_level()
        elif value == 'q':
            self.leave()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  Choose an option: "

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = '1. Restart level'

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = '\nq - main menu'

        return commands

    def get_welcome(self):
        """Return UI welcome message text."""

        return utility.format_ui_text(self.message)

    def leave(self):
        """Leave the game and return to the start menu."""

        self.game.gameui = LevelsUI(self.game)


class StoryUI(BaseUI):
    """Game user interface for a system terminal object."""

    def __init__(self, *args, **kwargs):
        super(StoryUI, self).__init__(*args, **kwargs)
        self.precedent = self.game.gameui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        self.display()
        message = "  Press Enter to continue..."
        response = input(message)
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_story_text = self.get_story_text()

        ui_elements.append(self.separator)
        ui_elements.append(ui_story_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def display(self):
        """Display the UI."""

        ui_text = self.decorate_ui(self.get_ui())
        ui_text_lines = ui_text.split('\n')
        show_text = ui_text_lines[0]
        print(show_text)
        for line in ui_text_lines[1:]:
            time.sleep(0.01)
            show_text = '\n'.join([show_text, line])
            self.clear_screen()
            print(show_text)

    def get_story_text(self):
        """Get the story text associated with the current cell."""

        story_text = self.game.player.cell.story_text
        formatted_text = utility.format_ui_text(story_text)
        return formatted_text

    def leave(self):
        # reset gameui to the ui that was active at the time this was created
        self.game.player.cell.story_seen = True
        self.game.gameui = self.precedent


# in progress
class GameCompleteUI(BaseUI):
    """Game user interface presented to the player when a level is completed."""

    def __init__(self, *args, **kwargs):
        super(LevelCompleteUI, self).__init__(*args, **kwargs)

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        # process action input
        if value.isdigit():
            if value == '1':
                self.restart_level()
            elif value == '2':
                self.next_level()
        # process quit input
        elif value == 'q':
            self.clear_screen()
            sys.exit()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "  Choose an option: "

        while True:
            # update the display
            self.display()
            response = input(message)
            if utility.is_empty_response(response):
                continue
            if len(valid_responses) > 0 and response not in valid_responses:
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = ('1. Restart level\n'
                      '2. Play next level')

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('\nMISC\n\n'
                    'q - leave the game')

        return commands

    def get_welcome(self):
        """Return terminal welcome message text."""

        return "Congratulations! You completed the level."

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

    def restart_level(self):
        """Restart the current level."""

        # self.alert = 'RESTART LEVEL!'
        this_level = self.game.level.number
        self.game.__init__()
        self.game.setup(level_number=this_level)

    def next_level(self):
        """Go to the next level."""

        # self.alert = 'RESTART LEVEL!'
        this_level = self.game.level.number
        self.game.__init__()
        self.game.setup(level_number=this_level + 1)
