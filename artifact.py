import exception
from item import Item


class Artifact(Item):
    """An item that has no specific in-game function but which may be valuable in some way."""

    def __init__(self, *args, **kwargs):
        super(self, Artifact).__init__(*args, **kwargs)


class Cup(Artifact):
    """It's just a cup."""

    def __init__(self, *args, **kwargs):
        super(self, Cup).__init__(*args, **kwargs)


class ArtifactFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_artifact(inventory, artifact_type):
        if artifact_type.lower() == 'cup':
            return Cup(inventory)
        raise exception.FactoryError("The specified artifact type does not exist.")
