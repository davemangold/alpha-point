import msvcrt
from string import ascii_letters
from collections import namedtuple

ascii_digits = ''.join([str(i) for i in range(10)])

__direction__ = namedtuple('Directions', ['UP', 'RIGHT', 'DOWN', 'LEFT'])
__command__ = namedtuple('Commands', ['QUIT', 'RESTART'])

DIRECTIONS = __direction__(*[10, 11, 12, 13])
COMMANDS = __command__(*[14, 15])
ACTIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
UNKNOWN = 0


class Control(object):

    def __init__(self, game, *args, **kwargs):
        self.game = game

    @staticmethod
    def get_input():
        """Return the ASCII integer code for the key pressed."""

        result = None

        try:
            ch = str(msvcrt.getch(), 'utf-8')
            if ch in ascii_letters:
                if ch == 'q':
                    result = COMMANDS.QUIT
                elif ch == 'r':
                    result = COMMANDS.RESTART
                else:
                    result = 0
            elif ch in ascii_digits:
                result = int(ch)
            msvcrt.getch()
        except UnicodeDecodeError:
            ch = str(msvcrt.getch(), 'utf-8')
            if ch == 'H':
                result = DIRECTIONS.UP
            if ch == 'M':
                result = DIRECTIONS.RIGHT
            if ch == 'P':
                result = DIRECTIONS.DOWN
            if ch == 'K':
                result = DIRECTIONS.LEFT

        return result
