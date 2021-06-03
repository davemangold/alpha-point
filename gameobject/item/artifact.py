import error
from gameobject.item import Item


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
    def make_artifact(map, artifact_type, *args, **kwargs):

        if artifact_type.lower() == 'generic':
            return Generic(map, *args, **kwargs)
        raise error.GameFactoryError("The specified artifact type does not exist.")

    def make_from_config(self, map, artifact_config):

        new_artifact = self.make_artifact(map, artifact_config['type'])
        new_artifact.config_id = artifact_config['id']
        new_artifact.level_number = map.level.number
        new_artifact.name = artifact_config['name']
        new_artifact.description = artifact_config['description']
        new_artifact.report = artifact_config['report']
        new_artifact.inspectable = artifact_config['inspectable']
        new_artifact.visible = artifact_config['visible']
        new_artifact.interactive = artifact_config['interactive']
        new_artifact.blocking = artifact_config['blocking']
        new_artifact.x = artifact_config['x']
        new_artifact.y = artifact_config['y']

        return new_artifact
