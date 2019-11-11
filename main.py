import sys
from game.game import Game


DEBUG = (sys.argv[1] == '--debug') if len(sys.argv) > 1 else False


def main(debug=DEBUG):
    game = Game(debug=debug)
    game.mainloop()


if __name__ == "__main__":
    main()
