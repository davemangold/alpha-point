import utility
from game import Game

game1 = Game(debug=False)
del game1.weather_thread
utility.set_save_game(game1)
game2 = utility.get_save_game()

print('TEST')
