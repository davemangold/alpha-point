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
from config import level_config


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

    def next_level(self):
        """Go to the next level."""

        self.game.setup(self.game.level.number + 1)
        self.game.ui = MainUI(self.game)

    def restart_level(self):
        """Restart the current level."""

        self.game.setup(self.game.level.number)
        self.game.ui = MainUI(self.game)


class StartUI(BaseUI):
    """Game level interface for game startup intro."""

    def __init__(self, *args, **kwargs):
        super(StartUI, self).__init__(*args, **kwargs)
        self.skip_intro = False
        self.splash_seen = False
        self.intro_seen_1 = False
        self.intro_seen_2 = False

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        if self.intro_seen_2 is True:
            self.leave()

    def prompt(self):
        """Prompt the player for input."""

        while True:
            # update the display
            self.display()
            message = self.decorate_ui("Press Enter to continue...")
            print(message)
            response = self.game.control.get_keypress()

            if self.skip_intro is True:
                self.leave()

            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_splash_text = self.get_splash_text()
        ui_intro_text_1 = self.get_intro_text_1()
        ui_intro_text_2 = self.get_intro_text_2()

        if self.splash_seen is False:
            ui_body_text = ui_splash_text
        elif self.splash_seen is True and self.intro_seen_1 is False:
            ui_body_text = ui_intro_text_1
        else:
            ui_body_text = ui_intro_text_2

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

        if self.intro_seen_1 is True:
            self.intro_seen_2 = True
        if self.splash_seen is True:
            self.intro_seen_1 = True

        self.splash_seen = True

    def get_splash_text(self):
        """Get the game splash screen text."""

        return game_config['splash_text']

    def get_intro_text_1(self):
        """Return the story intro text."""

        intro_text = game_config['intro_text_1']
        formatted_text = utility.format_ui_text(intro_text)
        return formatted_text

    def get_intro_text_2(self):
        """Return the story intro text."""

        intro_text = game_config['intro_text_2']
        formatted_text = utility.format_ui_text(intro_text)
        return formatted_text

    def leave(self):

        self.game.save['intro_seen'] = True
        # self.game.ui = LevelsUI(self.game)

        if self.game.save.get('game_complete') is True:
            self.game.ui = LevelsUI(self.game)
        else:
            self.game.ui = MainUI(self.game)


class LevelsUI(BaseUI):
    """Game user interface for level selection."""

    def __init__(self, *args, **kwargs):
        super(LevelsUI, self).__init__(*args, **kwargs)

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        # try to start the level
        if value.isdigit():
            try:
                self.start_level(int(value))
            except KeyError:
                self.alert = "Sorry, that's not a valid level."
        # quit the game
        elif value == 'q':
            self.clear_screen()
            sys.exit()
        # reset the game
        elif value == 'r':
            self.display()
            if input(self.decorate_ui('Reset the game and lose all progress (y/n)? ')) == 'y':
                self.game.reset()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self):
        """Prompt the player for input."""

        message = self.decorate_ui("Choose a level: ")

        while True:
            # update the display
            self.display()
            response = self.game.control.get_input(message)
            if utility.is_empty_response(response):
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
        """Return the text that represents available action."""

        highest_level = self.game.save['highest_level']

        if self.game.debug is True:
            highest_level = 99

        ui_actions = '\n'.join(
            ['{0}. {1}'.format(k, v['name'])
             for k, v in sorted(level_config.items())
             if 0 < k <= highest_level + 1])

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = '\nr - reset the game\nq - leave the game'

        return commands

    def start_level(self, level_number):
        """Start the game with the specified level number."""

        highest_level = self.game.save['highest_level']

        if self.game.debug is True:
            highest_level = 99

        if level_number > highest_level + 1:
            raise KeyError('Invalid level number.')

        self.game.setup(level_number)
        self.game.ui = MainUI(self.game)


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
            # process restart or quit input
            elif value == self.game.control.RESTART:
                self.display()
                if input(self.decorate_ui('Are you sure you want to restart (y/n)? ')) == 'y':
                    self.restart_level()
            elif value == self.game.control.QUIT:
                self.display()
                if input(self.decorate_ui('Are you sure you want to quit (y/n)? ')) == 'y':
                    self.leave()
            elif value == self.game.control.INVENTORY:
                self.game.ui = InventoryUI(self.game.player.inventory)
            # the value wasn't handled
            else:
                pass

        except error.MoveError:
            self.alert = "I can't move there."
        except error.ActionError:
            self.alert = "That's not an option."
        except error.InterfaceError:
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
            if self.game.level.number > self.game.save['highest_level']:
                if cell.seen is True:
                    map_list[cell.y][cell.x] = '.'
            else:
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

        player_symbol = self.player_symbols[self.game.player.orientation]

        commands = (
            '\n'
            'up    - move up          r - restart level      {0} - Player\n'
            'down  - move down        q - main menu          . - Path\n'
            'left  - move left        i - inventory\n'
            'right - move right'
        ).format(player_symbol)

        return commands

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        if self.game.debug is True:
            debug_text = (
                'Player X: {0}'.format(self.game.player.x) + '\n' +
                'Player Y: {0}'.format(self.game.player.y) + '\n' +
                'Player orientation: {0}'.format(self.game.player.orientation) + '\n' +
                'Visible items: {0}'.format(self.game.player.get_visible_items()) + '\n' +
                'Visible devices: {0}'.format(self.game.player.get_visible_devices()) + '\n' +
                'Visible interfaces: {0}'.format(self.game.player.get_visible_interfaces()) + '\n' +
                'Map items: {0}'.format(', '.join(str(i) for i in self.game.level.map.items)) + '\n' +
                'Map devices: {0}'.format(', '.join(str(i) for i in self.game.level.map.devices)) + '\n' +
                'Map interfaces: {0}'.format(', '.join(str(i) for i in self.game.level.map.interfaces)) + '\n' +
                'System properties: {0}'.format(', '.join('{0} ({1})'.format(i, i.value) for i in self.game.level.system.properties)))
            ui_elements.append(debug_text)

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
        """Leave the game and return to the levels menu."""

        self.game.ui = LevelsUI(self.game)


class ExaminationUI(BaseUI):
    """Game user interface used to present detailed artifact examination report."""

    def __init__(self, artifact, *args, **kwargs):
        super(ExaminationUI, self).__init__(artifact.map.level.game, *args, **kwargs)
        self.artifact = artifact
        self.previous_ui = self.game.ui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to return...")
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

        report_text = self.artifact.report
        formatted_text = utility.format_ui_text(report_text)
        return formatted_text

    def leave(self):
        """Return to the previous UI."""

        self.game.ui = self.previous_ui


# TODO: refactor to support inventory artifact examination
class InventoryUI(BaseUI):
    """Game user interface for player inventory."""

    def __init__(self, inventory, *args, **kwargs):

        super(InventoryUI, self).__init__(inventory.owner.game, *args, **kwargs)
        self.inventory = inventory
        self.previous_ui = self.game.ui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to return...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []
        ui_welcome = self.get_welcome()
        ui_items = self.get_items()

        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        if ui_items is not None:
            ui_elements.append(ui_items)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_items(self):
        """Return the text that represents available action."""

        ui_items = None
        ui_items_list = []
        item_counts = Counter([item.description for item in self.inventory.items])

        for item, count in sorted(item_counts.items()):
            ui_items_list.append('{0} ({1})'.format(item, count))

        if len(ui_items_list) == 0:
            ui_items_list.append('-- empty --')

        ui_items = '\n'.join(ui_items_list)

        return ui_items

    def get_welcome(self):
        """Return inventory welcome message text."""

        return "Inventory"

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

    def leave(self):
        # reset gameui to the ui that was active at the time this was created
        self.game.ui = self.previous_ui


class TerminalUI(BaseUI):
    """Game user interface for a system terminal object."""

    def __init__(self, terminal, *args, **kwargs):
        super(TerminalUI, self).__init__(terminal.system.level.game, *args, **kwargs)
        self.terminal = terminal
        self.output = None
        self.previous_ui = self.game.ui
        self.flicker = True
        self.corrupt = self.terminal.corrupt

    @property
    def flicker(self):

        return self._flicker

    @flicker.setter
    def flicker(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property flicker must be a boolean value.")

        if value is True:
            self._corrupt = not value

        self._flicker = value

    @property
    def corrupt(self):

        return self._corrupt

    @corrupt.setter
    def corrupt(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property corrupt must be a boolean value.")

        if value is True:
            self._flicker = not value

        self._corrupt = value

    def get_output(self):
        """Get terminal command output."""

        output = self.output
        self.output = None
        return output

    def process_command(self, command):
        """Process system terminal commands."""

        # command functions
        def help():

            return ('help\n'
                    'exit\n'
                    'clear\n'
                    'get-device [id]\n'
                    'set-device [id -active value]')

        def exit():
            self.leave()

        def clear():
            pass

        def get_device(*args):
            # args: {id} optional

            try:
                device_id = args[0]
            except IndexError:
                device_id = None

            devices = [d for d in self.game.level.system.devices]

            if device_id is not None:
                devices = [d for d in devices if d.id == device_id]

            if len(devices) > 0:
                return '\n\n'.join([
                    '{0}: {1}\n  '
                      'inet6 {2}\n  '
                      'enabled: {3}\n  '
                      'active: {4}'.format(d.id, d.name, d.address, d.enabled, d.active)
                    for d in devices])
            else:
                raise error.CommandError('Device not found.')

        def set_device(*args):
            # args: {id} {-property} {value}

            # property name: valid values
            valid_properties = {'active': (0, 1)}

            try:
                device_id = args[0]
                property_name = args[1].replace('-', '')
                property_value = int(args[2])
            except IndexError:
                raise error.CommandError('Missing arguments for set-device.')
            except (AttributeError, ValueError):
                raise error.CommandError('Invalid arguments for set-device.')

            if property_name not in valid_properties:
                raise error.CommandError('Invalid arguments for set-device.')

            if property_value not in valid_properties[property_name]:
                raise error.CommandError('Invalid arguments for set-device.')
            else:
                property_value = bool(property_value)

            device = self.game.level.system.get_device(device_id=device_id)

            if device is None:
                raise error.CommandError('Device not found.')

            if property_name == 'active':
                if property_value is True:
                    result = self.game.level.system.activate_device(device)
                else:
                    result = self.game.level.system.deactivate_device(device)

            if isinstance(result, str):
                raise error.CommandError(result)

        valid_commands = {
            'help': help,
            'exit': exit,
            'clear': clear,
            'get-device': get_device,
            'set-device': set_device
        }

        asroot = False
        clean = command.lower().strip()
        parts = clean.split()

        if parts[0] == 'sudo':
            asroot = True
            parts = parts[1:]

        if len(parts) == 0:
            if asroot:
                raise error.CommandError('Specify command to execute as root.'.format(command))
        else:
            command_key = parts[0]
            command_args = parts[1:]
            if command_key in ('help', 'exit', 'clear'):
                self.output = valid_commands[command_key]()
            elif command_key == 'get-device':
                if asroot:
                    self.output = valid_commands[command_key](*command_args)
                else:
                    raise error.CommandError('Permission denied. Try sudo [command].')
            elif command_key == 'set-device':
                if asroot:
                    self.output = valid_commands[command_key](*command_args)
                else:
                    raise error.CommandError('Permission denied. Try sudo [command].')
            else:
                raise error.CommandError('Command \'{0}\' not found.'.format(command))

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        try:
            # process quit input
            if value == 'q':
                self.leave()
            # process action input
            elif value.isdigit():
                self.terminal.do_action(int(value))
            # process as system command
            else:
                self.process_command(value)
        except error.ActionError:
            self.alert = "Invalid option."
        except error.CommandError as e:
            self.output = str(e)

    def prompt(self):
        """Prompt the player for input."""

        message = self.decorate_ui(
            "{0}@apex-{1}:~$ ".format(self.game.player.name, '-'.join(self.terminal.name.split())))

        while True:
            # update the display
            self.display()
            response = self.game.control.get_input(message=message)
            if utility.is_empty_response(response):
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()
        ui_action = self.get_action()
        ui_output = self.get_output()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        if ui_action is not None:
            ui_elements.append(ui_action)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)
        if ui_output is not None:
            ui_elements.append(ui_output)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def get_action(self):
        """Return the text that represents available action."""

        ui_actions = None
        ui_actions_list = []
        for key, action in sorted(self.terminal.actions.items()):
            ui_actions_list.append('{0}. {1}'.format(key, action.description))
        if len(ui_actions_list) > 0:
            ui_actions = '\n'.join(ui_actions_list)

        return ui_actions

    def get_commands(self):
        """Return the universal commands."""

        commands = ('q - leave the {0}'.format(self.terminal))

        return commands

    def get_welcome(self):
        """Return terminal welcome message text."""

        return "Terminal {0}".format(self.terminal.address)

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

        if self.flicker is True:
            self.display_flicker()
            self.flicker = False

        elif self.corrupt is True:
            self.display_corrupt()
            # self.corrupt = False

    def display_flicker(self):
        """Flicker the terminal display."""

        duration = 0.05
        number = randrange(2, 3, 1)
        intervals = [random() * duration for i in range(number)]

        for i in intervals:
            self.clear_screen()
            time.sleep(i)
            print(self.decorate_ui(self.get_ui()))

    def display_corrupt(self):
        """Build the terminal display with corrupted data."""

        ui_text = self.get_ui()
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        hextet_size = 4
        hextet_gaps = 4

        data_cols = int(self.width / (hextet_size + 1))  # + 1 to account for spaces
        data_rows = len(self.get_ui().split('\n')) + 2  # + 2 to account for prompt

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
        print(self.decorate_ui(self.get_ui()))

    def leave(self):
        # reset gameui to the ui that was active at the time this was created
        self.game.ui = self.previous_ui


class ConsoleUI(BaseUI):
    """Game user interface for a sensor console object."""

    def __init__(self, console, *args, **kwargs):
        super(ConsoleUI, self).__init__(console.system.level.game, *args, **kwargs)
        self.console = console
        self.previous_ui = self.game.ui
        self.flicker = True
        self.corrupt = self.console.corrupt

    @property
    def flicker(self):

        return self._flicker

    @flicker.setter
    def flicker(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property flicker must be a boolean value.")

        if value is True:
            self._corrupt = not value

        self._flicker = value

    @property
    def corrupt(self):

        return self._corrupt

    @corrupt.setter
    def corrupt(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property corrupt must be a boolean value.")

        if value is True:
            self._flicker = not value

        self._corrupt = value

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to return...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_welcome = self.get_welcome()
        ui_report_text = self.get_sensor_readout()

        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_report_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def get_sensor_readout(self):
        """Get the readout for sensors connected to the console."""

        return utility.build_sensor_readout_text(self.console.get_sensors())

    def get_welcome(self):
        """Return sensor console welcome message text."""

        return "Measurements"

    def display(self):
        """Display the UI."""

        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

        if self.flicker is True:
            self.display_flicker()
            self.flicker = False

        elif self.corrupt is True:
            self.display_corrupt()
            self.corrupt = False

    def display_flicker(self):
        """Flicker the terminal display."""

        duration = 0.05
        number = randrange(2, 3, 1)
        intervals = [random() * duration for i in range(number)]

        for i in intervals:
            self.clear_screen()
            time.sleep(i)
            print(self.decorate_ui(self.get_ui()))

    def display_corrupt(self):
        """Build the terminal display with corrupted data."""

        ui_text = self.get_ui()
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        hextet_size = 4
        hextet_gaps = 4

        data_cols = int(self.width / (hextet_size + 1))  # + 1 to account for spaces
        data_rows = len(self.get_ui().split('\n')) + 2  # + 2 to account for prompt

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
        print(self.decorate_ui(self.get_ui()))

    def leave(self):
        """Return to the previous UI."""

        self.game.ui = self.previous_ui


class WeatherStationUI(BaseUI):
    """Game user interface for a weather station object."""

    def __init__(self, weather_station, *args, **kwargs):
        super(WeatherStationUI, self).__init__(weather_station.system.level.game, *args, **kwargs)
        self.weather_station = weather_station
        self.previous_ui = self.game.ui
        self.flicker = True
        self.corrupt = self.weather_station.corrupt

    @property
    def flicker(self):

        return self._flicker

    @flicker.setter
    def flicker(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property flicker must be a boolean value.")

        if value is True:
            self._corrupt = not value

        self._flicker = value

    @property
    def corrupt(self):

        return self._corrupt

    @corrupt.setter
    def corrupt(self, value):

        if not isinstance(value, bool):
            raise ValueError("Property corrupt must be a boolean value.")

        if value is True:
            self._flicker = not value

        self._corrupt = value

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to return...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_welcome = self.get_welcome()
        ui_report_text = self.get_weather_readout()

        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        ui_elements.append(ui_report_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def get_weather_readout(self):
        """Get the readout for current weather."""

        return utility.build_weather_readout_text(self.game)

    def get_welcome(self):
        """Return weather station welcome message text."""

        return "Weather"

    def display(self):
        """Display the UI."""

        self.game.weather_thread.join()
        self.clear_screen()
        print(self.decorate_ui(self.get_ui()))

        if self.flicker is True:
            self.display_flicker()
            self.flicker = False

        elif self.corrupt is True:
            self.display_corrupt()
            self.corrupt = False

    def display_flicker(self):
        """Flicker the terminal display."""

        duration = 0.05
        number = randrange(2, 3, 1)
        intervals = [random() * duration for i in range(number)]

        for i in intervals:
            self.clear_screen()
            time.sleep(i)
            print(self.decorate_ui(self.get_ui()))

    def display_corrupt(self):
        """Build the terminal display with corrupted data."""

        ui_text = self.get_ui()
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        hextet_size = 4
        hextet_gaps = 4

        data_cols = int(self.width / (hextet_size + 1))  # + 1 to account for spaces
        data_rows = len(self.get_ui().split('\n')) + 2  # + 2 to account for prompt

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
        print(self.decorate_ui(self.get_ui()))

    def leave(self):
        """Return to the previous UI."""

        self.game.ui = self.previous_ui


class PlayerDeadUI(BaseUI):
    """Game user interface presented to the player when the player dies."""

    def __init__(self, message, *args, **kwargs):
        super(PlayerDeadUI, self).__init__(*args, **kwargs)
        self.message = message

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        if value == 'r':
            self.restart_level()
        elif value == 'q':
            self.leave()
        # the value wasn't handled
        else:
            self.alert = "Sorry, that's not an option."

    def prompt(self):
        """Prompt the player for input."""

        message = self.decorate_ui("What would you like to do? ")

        while True:
            # update the display
            self.display()
            response = self.game.control.get_input(message=message)
            if utility.is_empty_response(response):
                continue
            return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_commands = self.get_commands()
        ui_welcome = self.get_welcome()
        ui_alert = self.get_alert()

        ui_elements.append(ui_commands)
        ui_elements.append(self.separator)
        ui_elements.append(ui_welcome)
        if ui_alert is not None:
            ui_elements.append(ui_alert)
        ui_elements.append(self.separator)

        return '\n\n'.join(ui_elements) + '\n'

    def get_commands(self):
        """Return the universal commands."""

        commands = '\nr - restart level\nq - main menu'

        return commands

    def get_welcome(self):
        """Return UI welcome message text."""

        return utility.format_ui_text(self.message)

    def leave(self):
        """Leave the game and return to the start menu."""

        self.game.ui = LevelsUI(self.game)


class StoryUI(BaseUI):
    """Game user interface used to present in-level story narratives."""

    def __init__(self, *args, **kwargs):
        super(StoryUI, self).__init__(*args, **kwargs)
        self.previous_ui = self.game.ui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to continue...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_story_title = self.get_story_title()
        ui_story_text = self.get_story_text()

        if len(ui_story_title) > 0:
            ui_elements.append(ui_story_title)
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

    def get_story_title(self):
        """Get the story text associated with the current cell."""

        player_cell = self.game.player.cell
        story_title = ''

        if player_cell.has_story() and player_cell.story['title'] is not None:
            story_title = player_cell.story['title']

        formatted_title = utility.format_ui_text(story_title)
        return formatted_title

    def get_story_text(self):
        """Get the story text associated with the current cell."""

        player_cell = self.game.player.cell
        story_text = ''

        if player_cell.has_story() and player_cell.story['text'] is not None:
            story_text = player_cell.story['text']

        formatted_text = utility.format_ui_text(story_text)
        return formatted_text

    def leave(self):
        # reset gameui to the ui that was active at the time this was created
        self.game.player.cell.story_seen = True
        self.game.ui = self.previous_ui


class GameCompleteUI(BaseUI):
    """Game user interface presented to the player when the game is completed."""

    def __init__(self, *args, **kwargs):
        super(GameCompleteUI, self).__init__(*args, **kwargs)
        self.previous_ui = self.game.ui

    def process_input(self, value):
        """Call the appropriate method based on input value."""

        self.leave()

    def prompt(self):
        """Prompt the player for input."""

        self.display()
        message = self.decorate_ui("Press Enter to return to the main menu...")
        print(message)
        response = self.game.control.get_keypress()
        return response

    def get_ui(self):
        """Get the full UI text."""

        ui_elements = []

        ui_gameover_text = self.get_gameover_text()

        ui_elements.append(self.separator)
        ui_elements.append(ui_gameover_text)
        ui_elements.append(self.separator)

        return '\n' + '\n\n'.join(ui_elements) + '\n'

    def get_gameover_text(self):
        """Get the story text associated with the current cell."""

        gameover_text = game_config['gameover_text']
        formatted_text = utility.format_ui_text(gameover_text)
        return formatted_text

    def leave(self):
        # return to the main Levels UI
        self.game.ui = LevelsUI(self.game)
