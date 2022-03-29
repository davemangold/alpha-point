import utility
from gameobject import GameObject


class Item(GameObject):
    """Base class for items found throughout the game."""

    def __init__(self, map, *args, **kwargs):
        super(Item, self).__init__(map.level.game, *args, **kwargs)
        self.map = map
        self.inventory = None
        self.description = 'generic item'
        self.visible = True
        self.interactive = True
        self.blocking = False
        self.msg_action_verb = 'take'
        self.msg_take = 'I took the item.'
        self.msg_give = 'I gave the item.'
        self.msg_equip = 'I equipped the item.'
        self.msg_unequip = 'I unequipped the item.'

    def take_action_text(self):
        """Return text description of the currently available action."""

        player = self.game.player
        action_text = " ".join([self.msg_action_verb.capitalize(), "the", str(self)])

        # add relative direction to descriptions for visible map objects with same base description
        if utility.d4_duplicate_description(self, player.get_visible_objects()):
            direction = utility.get_direction(*player.location, *self.location)
            action_text += " " + utility.get_relative_direction_text(player.orientation, direction)

        return action_text

    def map_to_player(self):
        """Move an item from the map to the player's inventory."""

        game = self.inventory.owner.level.game
        map_cell = game.level.map.get_cell(*self.location)
        game.player.inventory.add_item(self.inventory.remove_item(self))
        map_cell.remove_item(self)
        game.player.update_actions()
