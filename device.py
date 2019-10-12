import exception
from component import Component


# Base Device class


class Device(Component):
    """A piece of mechanical or electrical equipment that may be controlled by an interface."""

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.__add_to_system()
        self.name = 'device'
        self.description = 'generic device'
        self.active = False
        self.dependencies = []
        self.override_dependencies = False
        self.msg_action_true = "activate"
        self.msg_action_false = "deactivate"
        self.msg_active_true = "The device is active."
        self.msg_active_false = "The device is not active."
        self.msg_toggle_active_true = "The device was activated."
        self.msg_toggle_active_false = "The device was deactivated."
        self.msg_toggle_enabled_true = "The device was enabled."
        self.msg_toggle_enabled_false = "The device was disabled."
        self.msg_unmet_dependencies = "The device has unmet dependencies."

    def __add_to_system(self):
        """Add the device to the parent system."""

        self.system.add_device(self)

    def action_text(self):
        """Return text description of the currently available action."""

        action = self.msg_action_true

        if self.active is True:
            action = self.msg_action_false

        return " ".join([action.capitalize(), "the", str(self)])

    def toggle_active_state(self):
        """Toggle this device's active state."""

        if self.enabled is False:
            self.system.level.game.gameui.alert = self.msg_disabled
            return

        if not self.dependencies_met():
            self.system.level.game.gameui.alert = self.msg_unmet_dependencies
            return

        self.active = not self.active

        if self.active is True:
            self.system.level.game.gameui.alert = self.msg_toggle_active_true
        else:
            self.system.level.game.gameui.alert = self.msg_toggle_active_false

    def toggle_enabled_state(self):
        """Toggle this device's enabled state."""

        self.enabled = not self.enabled

        if self.enabled is True:
            self.system.level.game.gameui.alert = self.msg_toggle_enabled_true
        else:
            self.system.level.game.gameui.alert = self.msg_toggle_enabled_false

    def add_dependency(self, device_id, active_state):
        """Add a dependency that must be met before this device can be activated."""

        if not self.system.has_device(self.system.get_device(device_id)):
            raise exception.SystemError("The specified device is not in the system.")

        if not isinstance(active_state, bool):
            raise TypeError("The active state must be a boolean value.")

        dependency = {'device_id': device_id, 'active_state': active_state}

        if dependency in self.dependencies:
            raise exception.DeviceError("The dependency already exists for the device.")

        self.dependencies.append(dependency)

    def remove_dependency(self, device_id):
        """Remove the dependencies from the device."""

        remove_dependencies = [d for d in self.dependencies if d['device_id'] == device_id]
        for dependency in remove_dependencies:
            self.dependencies.remove(dependency)

    def dependencies_met(self):
        """True if all dependencies have been met, otherwise False."""

        if self.override_dependencies is True:
            return True

        for dependency in self.dependencies:
            device = self.system.get_device(dependency['device_id'])
            if device.active != dependency['active_state']:
                return False
        return True

    def use(self):
        """Use the device."""

        self.toggle_active_state()


# Device sub-classes that can be controlled by interfaces


class Door(Device):
    """A portal to a passageway that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Door, self).__init__(*args, **kwargs)
        self.name = 'door'
        self.description = 'door'
        self.visible = True  # only on map.path
        self.msg_action_true = "open"
        self.msg_action_false = "close"
        self.msg_active_true = "The door is open."
        self.msg_active_false = "The door is closed."
        self.msg_toggle_active_true = "The door opened."
        self.msg_toggle_active_false = "The door closed."
        self.msg_unmet_dependencies = "The door is unresponsive."


class Switch(Device):
    """An electrical flow-control device that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Switch, self).__init__(*args, **kwargs)
        self.name = 'switch'
        self.description = 'switch'
        self.msg_action_true = "close"
        self.msg_action_false = "open"
        self.msg_active_true = "The switch is closed."
        self.msg_active_false = "The switch is opened."
        self.msg_toggle_active_true = "The switch closed."
        self.msg_toggle_active_false = "The switch opened."
        self.msg_unmet_dependencies = "The switch is inoperable."


class Valve(Device):
    """A fluid flow-control device that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Valve, self).__init__(*args, **kwargs)
        self.name = 'valve'
        self.description = 'valve'
        self.visible = True  # only on map.path
        self.msg_action_true = "open"
        self.msg_action_false = "close"
        self.msg_active_true = "The valve is open."
        self.msg_active_false = "The valve is closed."
        self.msg_toggle_active_true = "The valve opened."
        self.msg_toggle_active_false = "The valve closed."
        self.msg_unmet_dependencies = "The valve is inoperable."


class Camera(Device):
    """A camera that shows an environment which can be on or off."""

    def __init__(self, *args, **kwargs):
        super(Camera, self).__init__(*args, **kwargs)
        self.name = 'camera'
        self.description = 'camera'
        self.visible = True  # only on map.path
        self.msg_action_true = "turn on"
        self.msg_action_false = "turn off"
        self.msg_active_true = "The camera is on."
        self.msg_active_false = "The camera is off."
        self.msg_toggle_active_true = "The camera turned on."
        self.msg_toggle_active_false = "The camera turned off."
        self.msg_unmet_dependencies = "The camera is inoperable."


class Sensor(Device):
    """A measurement device that can be on or off."""

    def __init__(self, *args, **kwargs):
        super(Sensor, self).__init__(*args, **kwargs)
        self.name = 'sensor'
        self.description = 'sensor'
        self.msg_action_true = "turn on"
        self.msg_action_false = "turn off"
        self.msg_active_true = "The sensor is on."
        self.msg_active_false = "The sensor is off."
        self.msg_toggle_active_true = "The sensor turned on."
        self.msg_toggle_active_false = "The sensor turned off."
        self.msg_unmet_dependencies = "The sensor is inoperable."


# Device factory for making devices

class DeviceFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_device(system, device_type, *args, **kwargs):
        if device_type.lower() == 'door':
            return Door(system, *args, **kwargs)
        if device_type.lower() == 'switch':
            return Switch(system, *args, **kwargs)
        if device_type.lower() == 'valve':
            return Valve(system, *args, **kwargs)
        if device_type.lower() == 'camera':
            return Camera(system, *args, **kwargs)
        if device_type.lower() == 'sensor':
            return Sensor(system, *args, **kwargs)
        raise exception.FactoryError("The specified device type does not exist.")