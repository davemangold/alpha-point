from uuid import uuid4


class Item(object):
    """Base class for items found throughout the game."""

    def __init__(self, inventory, *args, **kwargs):
        self.inventory = inventory
        self.id = str(uuid4())
        self.name = ''
        self.description = 'generic item'
        self.visible = True
        self.x = 0
        self.y = 0
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