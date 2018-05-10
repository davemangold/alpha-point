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
        self.msg_action_verb = 'use'

    def __add_to_system(self):
        """Add the interface to the parent system."""

        self.system.add_interface(self)

    def action_text(self):
        """Return text description of the currently available action."""

        return " ".join([self.msg_action_verb.capitalize(), "the", str(self)])

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
        device.use()


# Interface sub-classes with which characters can interact


class Terminal(Interface):
    """A terminal that provides system information and accepts user commands to control many remote devices."""

    def __init__(self, *args, **kwargs):
        super(Terminal, self).__init__(*args, **kwargs)
        self.name = 'terminal'
        self.description = 'terminal'
        self.msg_action_verb = 'use'
        self.actions = {}

    def use(self, game):
        """Interface loop that allows player to interact with the interface."""

        self.update_actions()
        self.system.level.game.gameui = TerminalUI(self)

    def get_actions(self):
        """Return dictionary of actions based on terminal-linked devices."""

        device_list = self.get_devices()
        actions = {device_list.index(device) + 1: device.use
                   for device in device_list}
        return actions

    def update_actions(self):
        """Set the currently available actions."""

        self.actions = self.get_actions()

    def do_action(self, key, game):
        """Call the function associated with the provided key."""

        try:
            self.actions[key](game)
        except KeyError:
            raise exception.ActionError("There is no action defined for that key.")


class Button(Interface):
    """A button that controls a door."""

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.name = 'button'
        self.description = 'button'
        self.msg_action_verb = 'push'


class Toggleswitch(Interface):
    """A toggle that controls an electrical switch."""

    def __init__(self, *args, **kwargs):
        super(Toggleswitch, self).__init__(*args, **kwargs)
        self.name = 'toggleswitch'
        self.description = 'toggleswitch'
        self.msg_action_verb = 'flip'


class Handwheel(Interface):
    """A hand wheel that controls a valve."""

    def __init__(self, *args, **kwargs):
        super(Handwheel, self).__init__(*args, **kwargs)
        self.name = 'handwheel'
        self.description = 'handwheel'
        self.msg_action_verb = 'turn'


# class Viewer(Interface):
#     """A viewer that provides a video feed but accepts no commands."""
#
#     def __init__(self, *args, **kwargs):
#         super(Viewer, self).__init__(*args, **kwargs)
#         self.name = 'viewer'
#         self.description = 'viewer'
#         self.msg_action_verb = 'use'
#
#
# class Console(Interface):
#     """A console that provides a sensor readout but accepts no commands."""
#
#     def __init__(self, *args, **kwargs):
#         super(Console, self).__init__(*args, **kwargs)
#         self.name = 'monitor'
#         self.description = 'monitor'
#         self.msg_action_verb = 'use'


# Interface factory

class InterfaceFactory(object):
    """Makes specific Interface type instances."""

    @staticmethod
    def make_interface(system, interface_type, *args, **kwargs):
        if interface_type.lower() == 'terminal':
            return Terminal(system, *args, **kwargs)
        if interface_type.lower() == 'button':
            return Button(system, *args, **kwargs)
        if interface_type.lower() == 'toggleswitch':
            return Toggleswitch(system, *args, **kwargs)
        if interface_type.lower() == 'handwheel':
            return Handwheel(system, *args, **kwargs)
        # if interface_type.lower() == 'viewer':
        #     return Viewer(system)
        # if interface_type.lower() == 'console':
        #     return Console(system)
        raise exception.InterfaceFactoryError("The specified interface type does not exist.")
