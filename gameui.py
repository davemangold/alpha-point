import os
import sys
import time
import utility
import exception
from random import randrange
from random import random


class BaseUI(object):
    """Base game user interface class."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.alert = None

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        pass

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "What should I do? "

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
        return alert

    def get_ui(self):
        """Get the UI text."""

        return 'Base UI'

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.get_ui())

# in progress
class StartUI(BaseUI):
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

        message = "Choose a level: "

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

        ui_separator = 44 * '-'
        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(ui_separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(ui_separator)

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
        print(self.get_ui())

    def restart_level(self):
        """Restart the current level."""

        self.alert = 'RESTART LEVEL!'

    def next_level(self):
        """Go to the next level."""

        self.alert = 'NEXT LEVEL!'


class MainUI(BaseUI):
    """Main game user interface class."""

    def __init__(self, *args, **kwargs):
        super(MainUI, self).__init__(*args, **kwargs)

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_separator = 44 * '-'
        ui_commands = self.get_commands()
        ui_map = self.get_map()
        ui_alert = self.get_alert()
        ui_report = self.game.player.report_visible_components()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(ui_separator)
        ui_elements.append(ui_map)
        ui_elements.append(ui_report)
        if ui_action is not None:
            ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(ui_separator)

        return '\n\n'.join(ui_elements) + '\n'

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
                self.clear_screen()
                sys.exit()
            # the value wasn't handled
            else:
                self.alert = "I don't know what you mean."
        except exception.MoveError:
            self.alert = "I can't move there."
        except exception.ActionError:
            self.alert = "That's not an option."
        except exception.InterfaceError:
            self.alert = "There's something wrong with this thing!"

    def add_map_player(self, text_map):
        """Add the player to the map."""

        map_list = utility.text_map_to_nested_list(text_map)
        map_list[self.game.player.y][self.game.player.x] = 'P'

        return utility.nested_list_to_text_map(map_list)

    def add_map_interfaces(self, text_map):
        """Add system interfaces to the map."""

        map_list = utility.text_map_to_nested_list(text_map)
        for interface in self.game.level.system.interfaces:
            map_list[interface.y][interface.x] = 'I'

        return utility.nested_list_to_text_map(map_list)

    def add_map_devices(self, text_map):
        """Add system interfaces to the map."""

        map_list = utility.text_map_to_nested_list(text_map)
        for device in self.game.level.system.devices:
            map_list[device.y][device.x] = 'D'

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
        return text_map + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = None
        player_actions = self.game.player.get_actions()
        ui_actions_list = ['{0}. Use the {1}'.format(key, action.__self__)
                           for key, action in sorted(player_actions.items())]
        if len(ui_actions_list) > 0:
            ui_actions = '\n'.join(ui_actions_list)

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('\nMOVEMENT\tMAP\t\tMISC\n\n'
                    'i - move up\tP - Player\tr - restart\n'
                    'k - move down\t. - Path\tq - quit\n'
                    'j - move left\n'
                    'l - move right')

        return commands

    def restart_level(self):
        """Restart the current level."""

        # self.alert = 'RESTART LEVEL!'
        this_level = self.game.level.number
        self.game.__init__()
        self.game.setup(level_number=this_level)


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

        message = "{0}@apex-{1}:~$ ".format(self.game.player.name,
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

        ui_separator = 44 * '-'
        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(ui_separator)
        ui_elements.append(ui_welcome)
        if ui_action is not None:
            ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(ui_separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available actions."""

        ui_actions = None
        terminal_actions = self.terminal.get_actions()
        ui_actions_list = ['{0}. Toggle the {1}'.format(key, action.__self__)
                           for key, action in sorted(terminal_actions.items())]
        if len(ui_actions_list) > 0:
            ui_actions = '\n'.join(ui_actions_list)

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('\nMISC\n\n'
                    'q - leave the {0}'.format(self.terminal))

        return commands

    def get_welcome(self):
        """Return terminal welcome message text."""

        return "Terminal: {0}".format(self.terminal.address)

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.get_ui())

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
            print(self.get_ui())

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
            self.next_level()
        elif value == 'q':
            self.clear_screen()
            sys.exit()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self, valid_responses=[]):
        """Prompt the player for input."""

        message = "Choose an option: "

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

        ui_separator = 44 * '-'
        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(ui_separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(ui_separator)

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
        print(self.get_ui())

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

        message = "Choose an option: "

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

        ui_separator = 44 * '-'
        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()

        ui_elements.append(ui_commands)
        ui_elements.append(ui_separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(ui_separator)

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
        print(self.get_ui())

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
