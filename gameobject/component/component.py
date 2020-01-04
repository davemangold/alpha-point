from random import randint
from gameobject import GameObject


class Component(GameObject):
    """A system component. Interfaces and Devices are Components."""

    def __init__(self, system, *args, **kwargs):
        super(Component, self).__init__(system.level.game, *args, **kwargs)
        self.system = system
        self.address = ":".join((("%x" % randint(0, 16 ** 4)).zfill(4) for i in range(6)))
        self.description = 'generic component'
        self.enabled = True
        self.visible = False
        self.interactive = True
        self.orientation = 0
        self.msg_enabled = "Something happened."
        self.msg_disabled = "Nothing happened."
