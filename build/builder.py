from character import Character


class Builder(Character):
    """Character controlled by human player."""

    def __init__(self, *args, **kwargs):
        super(Builder, self).__init__(*args, **kwargs)
        self.name = 'builder'

    def is_valid_move(self, cell):
        """Override to allow movement anywhere in map."""

        return False if cell is None else True
