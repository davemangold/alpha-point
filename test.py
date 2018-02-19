from game import Game
from config import levels_config

level_config = levels_config['levels']['0']

game = Game()
game.level.build_from_config(level_config)

