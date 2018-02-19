import utility
from game import Game

game = Game()
game.setup()
game.player.move_to(4, 3)
game.mainloop()
