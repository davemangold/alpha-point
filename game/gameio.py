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
        self.RESTART = 114
        self.INVENTORY = 105
        self.UP = 72
        self.LEFT = 75
        self.RIGHT = 77
        self.DOWN = 80
        self.NULL = -1

    def get_input(self, message):

        return input(message)

    def get_keypress(self):

        while True:

            keycode = ord(getch())

            # enter
            if keycode == 13:
                return keycode
            # q, r, i
            if keycode in (113, 114, 105):
                return keycode
            # digits (0-9)
            if 48 <= keycode <= 57:
                return self.DIGITS[keycode]

            elif keycode == 224:  # special keys (arrows, f-keys, etc...)

                keycode = ord(getch())

                # arrow-up, arrow-left, arrow-right, arrow-down
                if keycode in (72, 75, 77, 80):
                    return keycode
