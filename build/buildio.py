import utility

operating_system = utility.get_os()

# windows
if operating_system == 'windows':
    from msvcrt import getch

# linux
elif operating_system == 'linux':
    import sys
    import termios
    import tty
    import readline

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

# not supported
else:
    raise SystemError('Operating system {0} not supported.'.format(operating_system))


class Control(object):

    def __init__(self, game):
        self.game = game
        self.DIGITS = {48: 0, 49: 1, 50: 2, 51: 3, 52: 4,
                       53: 5, 54: 6, 55: 7, 56: 8, 57: 9}
        self.ENTER = 13
        self.QUIT = 113
        self.UP = 72
        self.LEFT = 75
        self.RIGHT = 77
        self.DOWN = 80
        self.NULL = -1
        self._translate = {
            'special': {  # remap special keys from linux to windows codes
                65: 72,
                68: 75,
                67: 77,
                66: 80
            }
        }

    @property
    def _special(self):

        if operating_system == 'windows':
            return 224
        elif operating_system == 'linux':
            return 27
        else:
            raise SystemError('Operating system {0} not recognized.'.format(operating_system))

    def get_input(self, message):

        return input(message)

    def get_keypress(self):

        while True:

            keycode = ord(getch())

            # enter, e, i, q, r
            if keycode in (self.ENTER, self.QUIT):
                return keycode
            # digits (0-9)
            if keycode in self.DIGITS.keys():
                return self.DIGITS[keycode]

            # windows special keys (arrows, f-keys, etc...)
            if operating_system == 'windows':
                if keycode == self._special:

                    keycode = ord(getch())

                    # arrow-up, arrow-left, arrow-right, arrow-down
                    if keycode in (self.UP, self.LEFT, self.DOWN, self.RIGHT):
                        return keycode

            # linux special keys (arrows, f-keys, etc...)
            if operating_system == 'linux':
                if keycode == self._special:

                    trash = getch()
                    keycode = ord(getch())

                    # arrow-up, arrow-left, arrow-right, arrow-down
                    if keycode in self._translate['special'].keys():
                        return self._translate['special'][keycode]

            return
