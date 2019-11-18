import error
from level.gameobject.item.item import Item


class Artifact(Item):
    """An item that has no specific in-game function but which may be valuable in some way."""

    def __init__(self, *args, **kwargs):
        super(Artifact, self).__init__(*args, **kwargs)


class Generic(Artifact):
    """A class for arbitrary objects that are non-interactive."""

    def __init__(self, *args, **kwargs):
        super(Generic, self).__init__(*args, **kwargs)
        self.interactive = False


class ArtifactFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_artifact(inventory, artifact_type, *args, **kwargs):
        if artifact_type.lower() == 'generic':
            return Generic(inventory, *args, **kwargs)
        raise error.FactoryError("The specified artifact type does not exist.")
