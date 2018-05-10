from uuid import uuid4


class Item(object):
    """Base class for items found throughout the game."""

    def __init__(self, inventory, *args, **kwargs):
        self.inventory = inventory
        self.id = str(uuid4())
        self.name = ''
        self.description = 'generic item'
        self.visible = True
        self.interactive = True
        self.blocking = False
        self.x = 0
        self.y = 0
        self.msg_action_verb = 'take'
        self.msg_take = 'I took the item.'
        self.msg_give = 'I gave the item.'
        self.msg_equip = 'I equipped the item.'
        self.msg_unequip = 'I unequipped the item.'

    def __str__(self):
        """A brief description."""

        return self.description

    def location(self):
        """Return the (x, y) location of the component."""

        return self.x, self.y

    def take_action_text(self):
        """Return text description of the currently available action."""

        return " ".join([self.msg_action_verb.capitalize(), "the", str(self)])

    def map_to_player(self):
        """Move an item from the map to the player's inventory."""

        game = self.inventory.owner.level.game
        map_cell = game.level.map.get_cell(*self.location())
        game.player.inventory.add_item(self.inventory.remove_item(self))
        map_cell.remove_item(self)
        game.player.update_actions()
