from character import Character
from config import player_config


class Player(Character):
    """Character controlled by human player."""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = player_config['name']
        self.last_action = None
