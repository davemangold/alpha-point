import error
from gameobject.item import Item


# TODO: add action to examine artifact (launch ExaminationUI)
class Artifact(Item):
    """An item that has no specific in-game function but which may be valuable in some way."""

    def __init__(self, *args, **kwargs):
        super(Artifact, self).__init__(*args, **kwargs)
        self.inspectable = False
        self.report = 'There\'s nothing interesting about this.'


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
