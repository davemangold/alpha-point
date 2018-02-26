from character import Character


class Player(Character):
    """Character controlled by human player."""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = self.__get_name()

    def __get_name(self):

        return 'Marcus'
