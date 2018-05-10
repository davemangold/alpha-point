class Action(object):
    """Defines an action."""

    def __init__(self, function, description):
        self.function = function
        self.description = description

    def do(self):
        self.function()
