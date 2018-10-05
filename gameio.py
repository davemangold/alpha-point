import msvcrt
from collections import namedtuple

__ASCII_CODE_DIRECTIONS__ = [72, 77, 80, 75]
__ASCII_CODE_COMMANDS__ = [113, 114]
__ASCII_CODE_ACTIONS__ = [49, 50, 51, 52, 53, 54, 55, 56, 57]

__ASCII_TEXT_DIRECTIONS__ = ['u', 'r', 'd', 'l']
__ASCII_TEXT_COMMANDS__ = ['q', 'r']
__ASCII_TEXT_ACTIONS__ = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

__direction__ = namedtuple('Directions', ['UP', 'RIGHT', 'DOWN', 'LEFT'])
__command__ = namedtuple('Commands', ['QUIT', 'RESTART'])
__action__ = namedtuple('Commands', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'])

DIRECTIONS = __direction__(*__ASCII_TEXT_DIRECTIONS__)
COMMANDS = __command__(*__ASCII_TEXT_COMMANDS__)
ACTIONS = __action__(*__ASCII_TEXT_ACTIONS__)


class Control(object):

    def __init__(self):
        self.__direction_dict__ = dict(zip(__ASCII_CODE_DIRECTIONS__, __ASCII_TEXT_DIRECTIONS__))
        self.__command_dict__ = dict(zip(__ASCII_CODE_COMMANDS__, __ASCII_TEXT_COMMANDS__))
        self.__action_dict__ = dict(zip(__ASCII_CODE_ACTIONS__, __ASCII_TEXT_ACTIONS__))
        self.directions = self.__direction_dict__.values()
        self.commands = self.__command_dict__.values()
        self.actions = self.__action_dict__.values()

    def get_keypress(self):
        """Return the key character pressed."""

        keycode = self.get_keycode()
        keypress = self.convert_keycode(keycode)
        return keypress

    def convert_keycode(self, keycode):
        """Return the text character corresponding to the ASCII integer code."""

        result = None

        if keycode in self.__direction_dict__:
            result = self.__direction_dict__[keycode]
        elif keycode in self.__command_dict__:
            result = self.__command_dict__[keycode]
        elif keycode in self.__action_dict__:
            result = self.__action_dict__[keycode]

        return result

    def get_keycode(self):
        """Return the ASCII integer code for the key pressed."""

        keycode = ord(msvcrt.getch())

        # special keys
        if keycode == 224:
            keycode = ord(msvcrt.getch())

        return int(repr(keycode))
