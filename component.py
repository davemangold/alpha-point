from random import randint
from uuid import uuid4


class Component(object):
    """A system component. Interfaces and Devices are Components."""

    def __init__(self, system, *args, **kwargs):
        self.system = system
        self.config_id = None
        self.id = str(uuid4())
        self.address = ":".join((("%x" % randint(0, 16 ** 4)).zfill(4) for i in range(6)))
        self.name = 'component'
        self.description = 'generic component'
        self.enabled = True
        self.x = 0
        self.y = 0
        self.orientation = 0
        self.visible = False
        self.msg_enabled = "Something happened."
        self.msg_disabled = "Nothing happened."

    def __str__(self):
        """A brief description."""

        return self.description

    def location(self):
        """Return the (x, y) location of the component."""

        return self.x, self.y
