from gameobject.item import Item

class Action(object):
    """Defines an action."""

    def __init__(self, game, origin, target, function, description):
        self.game = game
        self.origin = origin
        self.target = target
        self.function = function
        self.description = description

    def __str__(self):
        return self.description

    def do(self):
        self.game.player.last_action = self
        self.function()
