from msvcrt import getch


class Control(object):

    def __init__(self, *args, **kwargs):
        self._digits = {48: 0, 49: 1, 50: 2, 51: 3, 52: 4,
                        53: 5, 54: 6, 55: 7, 56: 8, 57: 9}
        self.QUIT = 113
        self.RESTART = 114
        self.UP = 72
        self.LEFT = 75
        self.RIGHT = 77
        self.DOWN = 80

    def get_input(self):
        return input()

    def get_keypress(self):

        while True:

            keycode = ord(getch())

            # q, r
            if keycode in (113, 114):
                return keycode
            # digits (0-9)
            if 48 <= keycode <= 57:
                return self._digits[keycode]

            elif keycode == 224:  # special keys (arrows, f-keys, etc...)

                keycode = ord(getch())

                # arrow-up, arrow-left, arrow-right, arrow-down
                if keycode in (72, 75, 77, 80):
                    return keycode


c = Control()
while True:
    print(c.get_input())
