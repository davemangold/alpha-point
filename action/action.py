class Action(object):
    """Defines an action."""

    def __init__(self, gameobject, function, description):
        self.gameobject = gameobject
        self.function = function
        self.description = description

    def do(self):
        self.function()
