import os
import sys
import time
import error
import utility
from random import random
from random import randrange
from random import choices
from random import sample
from collections import Counter
from config import game_config


class BaseUI(object):
    """Base game user interface class."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.alert = None
        self.width = game_config['ui']['width']
        self.separator = '-' * self.width

    @staticmethod
    def clear_screen():
        """Clear the screen."""

        operating_system = utility.get_os()

        if operating_system == 'windows':
            os.system('cls')
        elif operating_system == 'linux':
            os.system('clear')
        else:
            raise SystemError('Operating system {0} not supported.'.format(operating_system))

    def decorate_ui(self, ui_text):

        terminal_width = os.get_terminal_size().columns

        h_offset = int((terminal_width - self.width) / 2)
        v_offset = 0

        ui_text_decorated = '\n'.join([" " * h_offset + line for line in ui_text.split('\n')])
        return ui_text_decorated

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        pass

    def prompt(self):
        """Prompt the player for input."""

        self.decorate_ui("What should I do? ")

        while True:

            self.display()
            response = self.game.control.get_keypress()
            if response is None:
                continue
            return response

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

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

    def display_corrupt(self):
        """Build the terminal display with corrupted data."""

        ui_text = self.get_ui()
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        hextet_size = 2
        hextet_gaps = 4

        data_cols = int(self.width / (hextet_size + 1))  # + 1 to account for spaces
        data_rows = len(ui_text.split('\n')) + 2  # + 2 to account for prompt

        duration = 0.3
        number = 6

        add_gaps = int((data_cols - hextet_gaps) / number)

        data = [[
            ''.join(choices(hex_digits, k=hextet_size))
            for m in range(data_cols)]
            for n in range(data_rows)]

        for n in range(number):
            for row in data:
                for i in sample(range(data_cols), hextet_gaps):
                    row[i] = ' ' * hextet_size

            corrupted_text = '\n'.join([' '.join(row) for row in data])

            self.clear_screen()
            print(self.decorate_ui(utility.merge_text(ui_text, corrupted_text)))
            time.sleep(duration)

            hextet_gaps += add_gaps

        self.clear_screen()
        print(self.decorate_ui(ui_text))


class MainUI(BaseUI):
    """Game user interface for in-level game play."""

    def __init__(self, *args, **kwargs):
        super(MainUI, self).__init__(*args, **kwargs)
        self.player_symbols = {0: '^', 1: '>', 2: 'v', 3: '<'}

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        try:
            # process move input
            if value == self.game.control.UP:
                self.game.player.move_up()
            elif value == self.game.control.RIGHT:
                self.game.player.move_right()
            elif value == self.game.control.DOWN:
                self.game.player.move_down()
            elif value == self.game.control.LEFT:
                self.game.player.move_left()
            # process action input
            elif value in self.game.control.DIGITS.values():
                self.game.player.do_action(int(value))
            elif value == self.game.control.QUIT:
                self.display()
                if input(self.decorate_ui('Are you sure you want to quit the game (y/n)? ')) == 'y':
                    self.leave()
            # the value wasn't handled
            else:
                pass

        except error.GameMoveError:
            self.alert = "I can't move there."
        except error.GameActionError:
            self.alert = "That's not an option."
        except error.GameInterfaceError:
            self.alert = "This doesn't work."

    def prompt(self):
        """Prompt the player for input."""

        while True:

            self.display()

            response = self.game.control.get_keypress()
            if response is None:
                continue

            return response

    def add_map_player(self, text_map):
        """Add the player to the map."""

        player_symbol = self.player_symbols[self.game.player.orientation]
        map_list = utility.text_map_to_nested_list(text_map)
        map_list[self.game.player.y][self.game.player.x] = player_symbol

        return utility.nested_list_to_text_map(map_list)

    def add_map_path(self, text_map):
        """Add map path to this map."""

        map_list = utility.text_map_to_nested_list(text_map)
        for cell in self.game.level.map.path.cells:
            if cell.seen is True:
                map_list[cell.y][cell.x] = '.'

        return utility.nested_list_to_text_map(map_list)

    def get_base_map(self):
        """Get the base map."""

        text_map = '\n'.join(
            [' '.join(self.game.level.map.x_dim * ' ')
             for y in range(self.game.level.map.y_dim)])

        return text_map

    def get_map(self):
        """Get the map text."""

        text_map = self.get_base_map()
        text_map = self.add_map_path(text_map)
        text_map = self.add_map_player(text_map)
        map_width = len(text_map.split('\n')[0])
        buffer_width = int((self.width - map_width) / 2)
        text_map = '\n'.join([' ' * buffer_width + line for line in text_map.split('\n')])
        return text_map

    def get_actions(self):
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

        player_symbol = self.player_symbols[self.game.player.orientation]

        commands = (
            'up    - move up          q - save and quit      {0} - Player\n'
            'down  - move down                               . - Path\n'
            'left  - move left\n'
            'right - move right'
        ).format(player_symbol)

        return commands

    def get_title(self):
        """Return the upper-case level name."""

        level_number = self.game.level.number
        level_name = self.game.level.name
        level_title = 'level {0} - {1}'.format(level_number, level_name).upper()
        level_title_centered = int((self.width - len(level_title)) / 2) * ' ' + level_title

        return '\n' + level_title_centered

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_title = self.get_title()
        ui_commands = self.get_commands()
        ui_map = self.get_map()
        ui_alert = self.get_alert()
        ui_report = utility.format_ui_text(self.game.player.report_visible_objects())
        ui_action = self.get_actions()

        ui_elements.append(ui_title)
        ui_elements.append(self.separator)
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

        if self.game.debug is True:

            system_properties = self.game.level.system.properties
            system_properties_text = ', '.join('{0} ({1})'.format(i, i.value) for i in system_properties)

            debug_text = (
                'Player X: {0}'.format(self.game.player.x) + '\n' +
                'Player Y: {0}'.format(self.game.player.y) + '\n' +
                'Player orientation: {0}'.format(self.game.player.orientation) + '\n' +
                'Visible items: {0}'.format(self.game.player.get_visible_items()) + '\n' +
                'Visible devices: {0}'.format(self.game.player.get_visible_devices()) + '\n' +
                'Visible interfaces: {0}'.format(self.game.player.get_visible_interfaces()) + '\n' +
                'Visible objects: {0}'.format(self.game.player.get_visible_objects()) + '\n' +
                # 'Map items: {0}'.format(', '.join(str(i) for i in self.game.level.map.items)) + '\n' +
                'Map devices: {0}'.format(', '.join(str(i) for i in self.game.level.map.devices)) + '\n' +
                'Map interfaces: {0}'.format(', '.join(str(i) for i in self.game.level.map.interfaces)) + '\n' +
                'System properties: {0}'.format(system_properties_text if len(system_properties) > 0 else None) + '\n' +
                'Last player action: {0}'.format(self.game.player.last_action)
            )
            ui_elements.append(debug_text)

        return '\n\n'.join(ui_elements) + '\n'

    def leave(self):
        """Leave the game."""

        self.clear_screen()
        sys.exit()


class ExaminationUI(BaseUI):
    """Game user interface used to present detailed artifact examination report."""

    def __init__(self, gameobject, *args, **kwargs):
        super(ExaminationUI, self).__init__(gameobject.game, *args, **kwargs)
        self.gameobject = gameobject
        self.previous_ui = self.game.ui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press any key to return...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_report_text = self.get_examination_report()

        ui_elements.append(self.separator)
        ui_elements.append(ui_report_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def get_examination_report(self):
        """Get the report associated with the examined artifact."""

        report_text = utility.build_examination_report_text(self.gameobject, self.game.level)
        formatted_text = utility.format_ui_text(report_text)
        return formatted_text

    def leave(self):
        """Return to the previous UI."""

        self.game.ui = self.previous_ui
