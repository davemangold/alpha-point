import error
from gameobject.component import Component


# Base Device class


class Device(Component):
    """A piece of mechanical or electrical equipment that may be controlled by an interface."""

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.__add_to_system()
        self.name = 'device'
        self.description = 'device'
        self.active = False
        self.dependencies = []
        self.override_dependencies = False
        self.msg_action_true = "activate"
        self.msg_action_false = "deactivate"
        self.msg_active_true = "active"
        self.msg_active_false = "inactive"
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

        return " ".join([action.capitalize(), "the", self.description])

    def toggle_active_state(self):
        """Toggle this device's active state."""

        toggled = False

        if self.enabled is False:
            self.system.level.game.ui.alert = self.msg_disabled
            return toggled

        if not self.dependencies_met():
            self.system.level.game.ui.alert = self.msg_unmet_dependencies
            return toggled

        self.active = not self.active
        toggled = True

        if self.active is True:
            self.system.level.game.ui.alert = self.msg_toggle_active_true
        else:
            self.system.level.game.ui.alert = self.msg_toggle_active_false

        property_list = self.get_properties()

        # sensors do not affect related property values (no quantum strangeness here)
        if not isinstance(self, Sensor):
            for property in property_list:
                if toggled and self.active is True:
                    property.increase()
                elif toggled and self.active is False:
                    property.decrease()

        return toggled

    def toggle_enabled_state(self):
        """Toggle this device's enabled state."""

        self.enabled = not self.enabled
        toggled = True

        if self.enabled is True:
            self.system.level.game.ui.alert = self.msg_toggle_enabled_true
        else:
            self.system.level.game.ui.alert = self.msg_toggle_enabled_false

        return toggled

    def add_dependency_device(self, device_id, enabled_state, active_state):
        """Add a device dependency that must be met before this device can be activated."""

        if not self.system.has_device(self.system.get_device(device_id)):
            raise error.GameSystemError("The specified device is not in the system.")

        if not isinstance(enabled_state, bool):
            raise TypeError("The enabled state must be a boolean value.")

        if not isinstance(active_state, bool):
            raise TypeError("The active state must be a boolean value.")

        dependency = {
            'type': 'device',
            'device_id': device_id,
            'enabled_state': enabled_state,
            'active_state': active_state}

        if dependency in self.dependencies:
            raise error.GameDeviceError("The dependency already exists for the device.")

        self.dependencies.append(dependency)

    def add_dependency_property(self, property_id, operator, value):
        """Add a property dependency that must be met before this device can be activated."""

        if not self.system.has_property(self.system.get_property(property_id)):
            raise error.GameSystemError("The specified property is not in the system.")

        if operator not in ('lt', 'gt', 'eq'):
            raise TypeError("The operator value must be one of: lt, gt, eq.")

        if not isinstance(value, int) or isinstance(value, float):
            raise TypeError("The provided value must be a number.")

        dependency = {
            'type': 'property',
            'property_id': property_id,
            'operator': operator,
            'value': value}

        if dependency in self.dependencies:
            raise error.GameDeviceError("The dependency already exists for the device.")

        self.dependencies.append(dependency)

    def remove_dependency(self, dependency_type, system_id):
        """Remove the dependencies from the device."""

        if dependency_type == 'device':
            device_id = system_id
            remove_dependencies = [d for d in self.dependencies if d.get('device_id') == device_id]
            for dependency in remove_dependencies:
                self.dependencies.remove(dependency)
        elif dependency_type == 'property':
            property_id = system_id
            remove_dependencies = [d for d in self.dependencies if d.get('property_id') == property_id]
            for dependency in remove_dependencies:
                self.dependencies.remove(dependency)
        else:
            raise ValueError("The dependency_type value is invalid.")

    def dependencies_met(self):
        """True if all dependencies have been met, otherwise False."""

        result = True

        if self.override_dependencies is True:
            return True

        for dependency in self.dependencies:

            if dependency['type'] == 'device':
                device = self.system.get_device(dependency['device_id'])
                if device.enabled != dependency['enabled_state']:
                    result = False
                    break
                if device.active != dependency['active_state']:
                    result = False
                    break

            if dependency['type'] == 'property':
                property = self.system.get_property(dependency['property_id'])
                operator = dependency['operator']

                if operator == 'gt' and not (property.value > dependency['value']):
                    result = False
                    break
                if operator == 'lt' and not (property.value < dependency['value']):
                    result = False
                    break
                if operator == 'eq' and not (property.value == dependency['value']):
                    result = False
                    break

        return result

    def get_properties(self):
        """Return the properties related to this device."""

        return self.system.get_device_properties(self)

    def use(self):
        """Use the device."""

        return self.toggle_active_state()


# Device sub-classes that can be controlled by interfaces, activated with tools, and repaired with parts

class Generic(Device):
    """An arbitrary device."""

    def __init__(self, *args, **kwargs):
        super(Generic, self).__init__(*args, **kwargs)


class Door(Device):
    """A portal to a passageway that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Door, self).__init__(*args, **kwargs)
        self.description = 'door'
        self.name = 'door'
        self.msg_action_true = "open"
        self.msg_action_false = "close"
        self.msg_active_true = "open"
        self.msg_active_false = "closed"
        self.msg_toggle_active_true = "The door opened."
        self.msg_toggle_active_false = "The door closed."
        self.msg_unmet_dependencies = "The door is unresponsive."

    def __str__(self):
        """Overload the default string conversion for doors."""

        return '{0} {1}'.format(self.msg_active_true if self.active else self.msg_active_false, self.description)


class Switch(Device):
    """An electrical flow-control device that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Switch, self).__init__(*args, **kwargs)
        self.name = 'switch'
        self.description = 'switch'
        self.msg_action_true = "close"
        self.msg_action_false = "open"
        self.msg_active_true = "closed"
        self.msg_active_false = "open"
        self.msg_toggle_active_true = "The switch closed."
        self.msg_toggle_active_false = "The switch opened."
        self.msg_unmet_dependencies = "The switch is inoperable."


class Valve(Device):
    """A fluid flow-control device that can be opened or closed."""

    def __init__(self, *args, **kwargs):
        super(Valve, self).__init__(*args, **kwargs)
        self.name = 'valve'
        self.description = 'valve'
        self.msg_action_true = "open"
        self.msg_action_false = "close"
        self.msg_active_true = "open"
        self.msg_active_false = "closed"
        self.msg_toggle_active_true = "The valve opened."
        self.msg_toggle_active_false = "The valve closed."
        self.msg_unmet_dependencies = "The valve is inoperable."


class Camera(Device):
    """A camera that shows an environment which can be on or off."""

    def __init__(self, *args, **kwargs):
        super(Camera, self).__init__(*args, **kwargs)
        self.name = 'camera'
        self.description = 'camera'
        self.msg_action_true = "turn on"
        self.msg_action_false = "turn off"
        self.msg_active_true = "on"
        self.msg_active_false = "off"
        self.msg_toggle_active_true = "The camera turned on."
        self.msg_toggle_active_false = "The camera turned off."
        self.msg_unmet_dependencies = "The camera is inoperable."


class Sensor(Device):
    """A measurement device that can be on or off."""

    def __init__(self, *args, **kwargs):
        super(Sensor, self).__init__(*args, **kwargs)
        self.name = 'sensor'
        self.description = 'sensor'
        self.value = None
        self.msg_action_true = "turn on"
        self.msg_action_false = "turn off"
        self.msg_active_true = "on"
        self.msg_active_false = "off"
        self.msg_toggle_active_true = "The sensor turned on."
        self.msg_toggle_active_false = "The sensor turned off."
        self.msg_unmet_dependencies = "The sensor is inoperable."


# Device factory for making devices

class DeviceFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_device(system, device_type, *args, **kwargs):

        if device_type.lower() == 'generic':
            return Generic(system, *args, **kwargs)
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

        raise error.GameFactoryError("The specified device type does not exist.")

    def make_from_config(self, system, device_config):

        new_device = self.make_device(system, device_config['type'])
        new_device.config_id = device_config['id']
        new_device.level_number = system.level.number
        new_device.name = device_config['name']
        new_device.description = device_config['description']
        new_device.report = device_config['report']
        new_device.inspectable = device_config['inspectable']
        new_device.enabled = device_config['enabled']
        new_device.active = device_config['active']
        new_device.visible = device_config['visible']
        new_device.x = device_config['x']
        new_device.y = device_config['y']
        new_device.msg_action_true = device_config['msg_action_true']
        new_device.msg_action_false = device_config['msg_action_false']
        new_device.msg_active_true = device_config['msg_active_true']
        new_device.msg_active_false = device_config['msg_active_false']
        new_device.msg_toggle_active_true = device_config['msg_toggle_active_true']
        new_device.msg_toggle_active_false = device_config['msg_toggle_active_false']
        new_device.msg_unmet_dependencies = device_config['msg_unmet_dependencies']

        return new_device
