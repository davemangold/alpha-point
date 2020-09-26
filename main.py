import argparse
import utility
from game import Game

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', required=False, help='run the game in debug mode', action='store_true')
parser.add_argument('-l', '--level', required=False, type=int, nargs=1, help='start level for debug mode')
args = parser.parse_args()


def main():

    if args.debug:

        debug = args.debug
        level = args.level[0] if args.level else 1

        with Game(debug=debug, level=level) as game:
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
