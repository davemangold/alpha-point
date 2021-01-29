class Action(object):
    """Defines an action."""

    def __init__(self, game, function, description, *args, **kwargs):
        self.game = game
        self.function = function
        self.description = description

    def __str__(self):
        return self.description

    def __eq__(self, other):
        if not isinstance(other, Action):
            return NotImplemented

        return self.description == other.description

    def do(self):
        self.game.player.last_action = self
        self.function()


class InterfaceAction(Action):
    """Defines an action performed by an interface on a device."""

    def __init__(self, interface, device, *args, **kwargs):
        super(InterfaceAction, self).__init__(*args, **kwargs)
        self.origin = interface
        self.target = device


class PlayerAction(Action):
    """Defines an action performed by the player."""

    def __init__(self, target, *args, **kwargs):
        super(PlayerAction, self).__init__(*args, **kwargs)
        self.origin = self.game.player
        self.target = target


class ItemAction(Action):
    """Defines an action performed by an item on a device."""

    def __init__(self, item, device, *args, **kwargs):
        super(ItemAction, self).__init__(*args, **kwargs)
        self.origin = item
        self.target = device
