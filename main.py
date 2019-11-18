import argparse
from game import Game

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', help='run the game in debug mode', action='store_true')
args = parser.parse_args()


def main():

    with Game(debug=args.debug) as game:
        game.mainloop()


if __name__ == "__main__":
    main()
