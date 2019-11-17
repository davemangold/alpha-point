import os
import sys
from game import Game


# dirty hack...
DEBUG = (sys.argv[1] == '--debug') if len(sys.argv) > 1 else False


def reset():

    for f in os.listdir('.save'):
        path = os.join('.save', f)
        if os.path.isfile(path):
            os.remove(path)

    main()


def main(debug=DEBUG):

    with Game(debug=debug) as game:
        game.mainloop()


if __name__ == "__main__":
    main()
