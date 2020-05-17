import utility
from uuid import uuid4
from game.gameui import ExaminationUI


class GameObject(object):
    """Base class for all game objects."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.id = str(uuid4()).split('-')[0]
        self.config_id = None
        self.name = ''
        self.description = 'generic object'
        self.inspectable = False
        self.visible = True
        self.interactive = True
        self.blocking = False
        self.x = 0
        self.y = 0
        self.msg_examine_verb = 'look at'
        self.report = 'There\'s nothing interesting about this.'

    def __str__(self):
        """A brief description."""

        return self.description

    def location(self):
        """Return the (x, y) location of the item."""

        return self.x, self.y

    def examine_action_text(self):
        """Return text description of the currently available action."""

        player = self.game.player
        action_text = " ".join([self.msg_examine_verb.capitalize(), "the", str(self)])

        # add relative direction to descriptions for visible map objects with same base description
        if (self.game.level.map.inventory.has_item(self)
        and utility.d4_duplicate_description(self, player.get_visible_objects())):
            direction = utility.get_direction(*player.location, *self.location())
            action_text += " " + utility.get_relative_direction_text(player.orientation, direction)

        return action_text

    def examine(self):
        """Examine the artifact to reveal additional information."""

        self.game.ui = ExaminationUI(self)
