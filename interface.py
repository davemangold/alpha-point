import exception
from gameui import TerminalUI
from component import Component


# Base Interface class


class Interface(Component):
    """Interface where character can take action to use devices."""

    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)
        self.__add_to_system()
        self.name = 'interface'
        self.description = 'generic interface'
        self.visible = True

    def __add_to_system(self):
        """Add the interface to the parent system."""

        self.system.add_interface(self)

    def get_devices(self):
        """Return the devices linked to the interface."""

        return self.system.get_interface_devices(self)

    def use(self):
        """Use the interface."""

        device_list = self.get_devices()
        if len(device_list) == 0:
            raise exception.InterfaceError("No devices linked to interface.")
        if len(device_list) > 1:
            raise exception.InterfaceError("More than one device linked to interface.")
        device = device_list[0]
        device.toggle_active_state()


# Interface sub-classes with which characters can interact


class Terminal(Interface):
    """A terminal that provides system information and accepts user commands to control many remote devices."""

    def __init__(self, *args, **kwargs):
        super(Terminal, self).__init__(*args, **kwargs)
        self.name = 'terminal'
        self.description = 'terminal'
        self.actions = {}

    def use(self):
        """Interface loop that allows player to interact with the interface."""

        self.update_actions()
        self.system.level.game.gameui = TerminalUI(self)

    def get_actions(self):
        """Return dictionary of actions based on terminal-linked devices."""

        device_list = self.get_devices()
        actions = {device_list.index(device) + 1: device.toggle_active_state
                   for device in device_list}
        return actions

    def update_actions(self):
        """Set the currently available actions."""

        self.actions = self.get_actions()

    def do_action(self, key):
        """Call the function associated with the provided key."""

        try:
            self.actions[key]()
        except KeyError:
            raise exception.ActionError("There is no action defined for that key.")


class Button(Interface):
    """A button that controls a door."""

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.name = 'button'
        self.description = 'button'


class Toggleswitch(Interface):
    """A toggle that controls an electrical switch."""

    def __init__(self, *args, **kwargs):
        super(Toggleswitch, self).__init__(*args, **kwargs)
        self.name = 'toggleswitch'
        self.description = 'toggleswitch'


class Handwheel(Interface):
    """A hand wheel that controls a valve."""

    def __init__(self, *args, **kwargs):
        super(Handwheel, self).__init__(*args, **kwargs)
        self.name = 'handwheel'
        self.description = 'handwheel'


class Viewer(Interface):
    """A viewer that provides a video feed but accepts no commands."""

    def __init__(self, *args, **kwargs):
        super(Viewer, self).__init__(*args, **kwargs)
        self.name = 'viewer'
        self.description = 'viewer'


class Console(Interface):
    """A console that provides a sensor readout but accepts no commands."""

    def __init__(self, *args, **kwargs):
        super(Console, self).__init__(*args, **kwargs)
        self.name = 'monitor'
        self.description = 'monitor'


# Interface factory

class InterfaceFactory(object):
    """Makes specific Interface type instances."""

    @staticmethod
    def make_interface(system, interface_type):
        if interface_type.lower() == 'terminal':
            return Terminal(system)
        if interface_type.lower() == 'button':
            return Button(system)
        if interface_type.lower() == 'toggleswitch':
            return Toggleswitch(system)
        if interface_type.lower() == 'handwheel':
            return Handwheel(system)
        if interface_type.lower() == 'viewer':
            return Viewer(system)
        if interface_type.lower() == 'console':
            return Console(system)
        raise exception.InterfaceFactoryError("The specified interface type does not exist.")
