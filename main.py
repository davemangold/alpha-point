import argparse
import utility
from game import Game
from build import Construct

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', required=False, help='run the game in debug mode', action='store_true')
parser.add_argument('-l', '--level', required=False, type=int, nargs=1, help='start level for debug mode')
parser.add_argument('-b', '--build', required=False, help='run the game in build mode', action='store_true')
args = parser.parse_args()


def main():

    level = args.level[0] if args.level else 1

    if args.build:

        with Construct(level=level) as construct:
            construct.mainloop()

    elif args.debug:

        with Game(debug=args.debug, level=level) as game:
            game.mainloop()

    else:

        if utility.save_exists('game_exit'):
            with utility.load_object('game_exit') as game:
                game.mainloop()
        else:
            with Game() as game:
                game.mainloop()


if __name__ == "__main__":
    main()
