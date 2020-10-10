import error
from game.gameui import TerminalUI
from game.gameui import ConsoleUI
from game.gameui import WeatherStationUI
from gameobject.component import Component
from gameobject.component.device import Sensor
from action import Action


# Base Interface class


class Interface(Component):
    """Interface where character can take action to use devices."""

    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)
        self.__add_to_system()
        self.name = 'interface'
        self.description = 'interface'
        self.visible = True
        self.corrupt = False
        self.msg_action_verb = 'use'

    def __add_to_system(self):
        """Add the interface to the parent system."""

        self.system.add_interface(self)

    def action_text(self):
        """Return text description of the currently available action."""

        return " ".join([self.msg_action_verb.capitalize(), "the", str(self)])

    def get_devices(self, device_id=None):
        """Return the devices linked to this interface."""

        devices = self.system.get_interface_devices(self)

        if device_id is not None:
            devices = [d for d in devices if device_id == d.id[:len(device_id)]]

        return devices

    def use(self):
        """Use the interface."""

        device_list = self.get_devices()
        if len(device_list) == 0:
            raise error.InterfaceError("No devices linked to interface.")
        for device in device_list:
            device.use()


# Interface sub-classes which can be used to control devices


class Terminal(Interface):
    """A terminal that provides system information and accepts user commands to control many remote devices."""

    def __init__(self, *args, **kwargs):
        super(Terminal, self).__init__(*args, **kwargs)
        self.name = 'terminal'
        self.description = 'terminal'
        self.msg_action_verb = 'use'
        self.actions = {}

    def use(self):
        """Interface loop that allows player to interact with the interface."""

        self.update_actions()
        self.system.level.game.ui = TerminalUI(self)

    def get_actions(self):
        """Return dictionary of action based on enabled, terminal-linked devices."""

        device_list = self.get_devices()
        actions_list = [Action(device.use, device.action_text())
                        for device in device_list
                        if device.enabled is True]
        actions = {actions_list.index(action) + 1: action
                   for action in actions_list}

        return actions

    def update_actions(self):
        """Set the currently available action."""

        self.actions = self.get_actions()

    def do_action(self, key):
        """Call the function associated with the provided key."""

        try:
            action = self.actions[key]
            action.do()
            self.update_actions()
        except KeyError:
            raise error.ActionError("There is no action defined for that key.")


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


class Console(Interface):
    """A console that provides a sensor readout but accepts no commands."""

    def __init__(self, *args, **kwargs):
        super(Console, self).__init__(*args, **kwargs)
        self.name = 'monitor'
        self.description = 'monitor'
        self.msg_action_verb = 'use'

    def get_sensors(self):
        """Return list of sensors connected to the console."""

        sensors = [d for d in self.system.get_interface_devices(self)
                   if isinstance(d, Sensor)]

        return sensors

    def use(self):
        """Interface loop that allows player to interact with the interface."""

        self.system.level.game.ui = ConsoleUI(self)


class WeatherStation(Interface):
    """A station that provides local weather (actual Mars weather from NASA InSight lander) but accepts no commands."""

    def __init__(self, *args, **kwargs):
        super(WeatherStation, self).__init__(*args, **kwargs)
        self.name = 'weather station'
        self.description = 'weather station'
        self.msg_action_verb = 'use'

    def use(self):
        """Interface loop that allows player to interact with the interface."""

        self.system.level.game.ui = WeatherStationUI(self)


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
        if interface_type.lower() == 'console':
            return Console(system, *args, **kwargs)
        if interface_type.lower() == 'weatherstation':
            return WeatherStation(system, *args, **kwargs)
        # if interface_type.lower() == 'viewer':
        #     return Viewer(system)
        raise error.FactoryError("The specified interface type does not exist.")

    def make_from_config(self, system, interface_config, level_number):

        new_interface = self.make_interface(system, interface_config['type'])
        new_interface.config_id = interface_config['id']
        new_interface.level_number = level_number
        new_interface.name = interface_config['name']
        new_interface.description = interface_config['description']
        new_interface.report = interface_config['report']
        new_interface.inspectable = interface_config['inspectable']
        new_interface.enabled = interface_config['enabled']
        new_interface.corrupt = interface_config['corrupt']
        new_interface.x = interface_config['x']
        new_interface.y = interface_config['y']
        new_interface.orientation = interface_config['orientation']
        new_interface.msg_action_verb = interface_config['msg_action_verb']

        return new_interface

