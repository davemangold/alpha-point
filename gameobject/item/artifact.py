import error
from gameobject.item import Item
from game.gameui import ExaminationUI


class Artifact(Item):
    """An item that has no specific in-game function but which may be valuable in some way."""

    def __init__(self, *args, **kwargs):
        super(Artifact, self).__init__(*args, **kwargs)
        self.inspectable = False
        self.report = 'There\'s nothing interesting about this.'
        self.msg_examine_verb = 'look at'

    def examine_action_text(self):
        """Return text description of the currently available action."""

        return " ".join([self.msg_examine_verb.capitalize(), "the", str(self)])

    def examine(self):
        """Examine the artifact to reveal additional information."""

        self.map.level.game.ui = ExaminationUI(self)


class Generic(Artifact):
    """A class for arbitrary objects that are non-interactive."""

    def __init__(self, *args, **kwargs):
        super(Generic, self).__init__(*args, **kwargs)
        self.interactive = False


class ArtifactFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_artifact(map, artifact_type, *args, **kwargs):
        if artifact_type.lower() == 'generic':
            return Generic(map, *args, **kwargs)
        raise error.FactoryError("The specified artifact type does not exist.")
