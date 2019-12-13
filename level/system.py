import error
from level.property import Property
from level.property import PropertyFactory
from gameobject.component.device import Device
from gameobject.component.device import DeviceFactory
from gameobject.component.interface import Interface
from gameobject.component.interface import InterfaceFactory
from config import level_config


class System(object):
    """A collection of interfaces and devices the player can control."""

    def __init__(self, level):
        self.level = level
        self.interfaces = []  # [<interface>,...]
        self.devices = []  # [<device>,...]
        self.properties = []  # [<property>,...]
        self.links = []  # [{'interface_id': <device id>},...]
        self.relates = []  # [{'device_id': <property_id>},...]
        self.deaths = []

    def build(self):
        """Build system from config dictionary."""

        system_config = level_config[self.level.number]['system']

        for config_interface in system_config['interfaces']:
            new_interface = InterfaceFactory.make_interface(self, config_interface['type'])
            new_interface.config_id = config_interface['id']
            new_interface.name = config_interface['name']
            new_interface.description = config_interface['description']
            new_interface.enabled = config_interface['enabled']
            new_interface.corrupt = config_interface['corrupt']
            new_interface.x = config_interface['x']
            new_interface.y = config_interface['y']
            new_interface.orientation = config_interface['orientation']
            new_interface.msg_action_verb = config_interface['msg_action_verb']

        for config_device in system_config['devices']:
            new_device = DeviceFactory.make_device(self, config_device['type'])
            new_device.config_id = config_device['id']
            new_device.name = config_device['name']
            new_device.description = config_device['description']
            new_device.enabled = config_device['enabled']
            new_device.active = config_device['active']
            new_device.visible = config_device['visible']
            new_device.x = config_device['x']
            new_device.y = config_device['y']
            new_device.msg_action_true = config_device['msg_action_true']
            new_device.msg_action_false = config_device['msg_action_false']
            new_device.msg_active_true = config_device['msg_active_true']
            new_device.msg_active_false = config_device['msg_active_false']
            new_device.msg_toggle_active_true = config_device['msg_toggle_active_true']
            new_device.msg_toggle_active_false = config_device['msg_toggle_active_false']
            new_device.msg_unmet_dependencies = config_device['msg_unmet_dependencies']

        for config_property in system_config['properties']:
            new_property = PropertyFactory.make_property(self, config_property['type'])
            new_property.config_id = config_property['id']
            new_property.name = config_property['name']
            new_property.description = config_property['description']
            new_property.min_value = config_property['min_value']
            new_property.max_value = config_property['max_value']
            new_property.increment = config_property['increment']
            new_property.value = config_property['value']

        for config_device in system_config['devices']:
            system_device = self.get_device(config_id=config_device['id'])
            for config_dependency in config_device['dependencies']:
                dependency_device = self.get_device(config_id=config_dependency['device_id'])
                system_device.add_dependency(
                    dependency_device.id,
                    config_dependency['enabled_state'],
                    config_dependency['active_state'])

        for config_link in system_config['links']:
            link_interface = self.get_interface(config_id=config_link['interface_id'])
            link_device = self.get_device(config_id=config_link['device_id'])
            self.link_device(link_interface, link_device)

        for config_relate in system_config['relates']:
            relate_device = self.get_device(config_id=config_relate['device_id'])
            relate_property = self.get_property(config_id=config_relate['property_id'])
            self.relate_property(relate_device, relate_property)

        for config_death in system_config['deaths']:
            self.deaths.append(config_death)

    def has_interface(self, interface):
        """Returns True if the system contains the interface, otherwise False."""

        return interface in self.interfaces

    def has_device(self, device):
        """Returns True if the system contains the device, otherwise False."""

        return device in self.devices

    def has_property(self, property):
        """Returns True if the system contains the property, otherwise False."""

        return property in self.properties

    def get_interface(self, interface_id=None, config_id=None):
        """Return the interface if it exists."""

        interface = None

        if interface_id is not None:
            for check_interface in self.interfaces:
                if check_interface.id == interface_id:
                    interface = check_interface
                    break

        elif config_id is not None:
            for check_interface in self.interfaces:
                if check_interface.config_id == config_id:
                    interface = check_interface
                    break

        return interface

    def get_device(self, device_id=None, config_id=None):
        """Return the device if it exists."""

        device = None

        if device_id is not None:
            for check_device in self.devices:
                if check_device.id == device_id:
                    device = check_device
                    break

        elif config_id is not None:
            for check_device in self.devices:
                if check_device.config_id == config_id:
                    device = check_device
                    break

        return device

    def get_property(self, property_id=None, config_id=None):
        """Return the property if it exists."""

        property = None

        if property_id is not None:
            for check_property in self.properties:
                if check_property.id == property_id:
                    property = check_property
                    break

        elif config_id is not None:
            for check_property in self.properties:
                if check_property.config_id == config_id:
                    property = check_property
                    break

        return property

    def get_interface_ids(self, device):
        """Return list of interface ids related to device."""

        if not isinstance(device, Device):
            raise TypeError("Object not of type 'Device'.")

        if not self.has_device(device):
            raise error.SystemError("The device is not a component of the system.")

        interface_ids = []

        for link in self.links:
            if link['device_id'] == device.id:
                interface_ids.append(link['interface_id'])

        return interface_ids

    def get_device_ids(self, interface=None, property=None):
        """Return list of device ids linked to interface or related to property."""

        device_ids = []

        if interface is not None:

            if not isinstance(interface, Interface):
                raise TypeError("Object not of type 'Interface'.")

            if not self.has_interface(interface):
                raise error.SystemError("The interface is not in the system.")

            for link in self.links:
                if link['interface_id'] == interface.id:
                    device_ids.append(link['device_id'])

        elif property is not None:

            if not isinstance(property, Property):
                raise TypeError("Object not of type 'Property'.")

            if not self.has_property(property):
                raise error.SystemError("The property is not in the system.")

            for relate in self.relates:
                if relate['property_id'] == property.id:
                    device_ids.append(relate['device_id'])

        return device_ids

    def get_property_ids(self, device):
        """Return list of property ids related to device."""

        if not isinstance(device, Device):
            raise TypeError("Object not of type 'Device'.")

        if not self.has_device(device):
            raise error.SystemError("The device is not in the system.")

        property_ids = []

        for relate in self.relates:
            if relate['device_id'] == device.id:
                property_ids.append(relate['property_id'])

        return property_ids

    def get_interface_devices(self, interface):
        """Return a list of all devices linked to an interface."""

        device_ids = self.get_device_ids(interface=interface)
        interface_devices = [device for device in self.devices
                             if device.id in device_ids]

        return interface_devices

    def get_device_interfaces(self, device):
        """Return a list of all interfaces linked to a device."""

        interface_ids = self.get_interface_ids(device)
        device_interfaces = [interface for interface in self.interfaces
                             if interface.id in interface_ids]

        return device_interfaces

    def get_device_properties(self, device):
        """Return a list of all properties related to a device."""

        property_ids = self.get_property_ids(device)
        device_properties = [property for property in self.properties
                             if property.id in property_ids]

        return device_properties

    def get_property_devices(self, property):
        """Return a list of all devices related to a property."""

        device_ids = self.get_device_ids(property=property)
        property_devices = [device for device in self.devices
                            if device.id in device_ids]

        return property_devices

    def get_components(self):
        """Return all components."""

        return self.interfaces + self.devices

    def add_interface(self, interface):
        """Add an interface to the system."""

        if interface in self.interfaces:
            raise error.SystemError("The interface is already in the system.")

        self.interfaces.append(interface)

    def remove_interface(self, interface):
        """Remove an interface from the system and return it."""

        if interface not in self.interfaces:
            raise error.SystemError("The interface is not in the system.")

        for link in self.links:
            if link['interface_id'] == interface.id:
                self.links.remove(link)

        return self.interfaces.pop(self.interfaces.index(interface))

    def add_device(self, device):
        """Add a device to the system."""

        if device in self.devices:
            raise error.SystemError("The device is already in the system.")

        self.devices.append(device)

    def remove_device(self, device):
        """Remove a device from the system and return it."""

        if device not in self.devices:
            raise error.SystemError("The device is not in the system.")

        for link in self.links:
            if link['device_id'] == device.id:
                self.links.remove(link)

        return self.devices.pop(self.devices.index(device))

    def add_property(self, property):
        """Add a property to the system."""

        if property in self.properties:
            raise error.SystemError("The property is already in the system.")

        self.properties.append(property)

    def remove_property(self, property):
        """Remove a property from the system and return it."""

        if property not in self.properties:
            raise error.SystemError("The property is not in the system.")

        for relate in self.relates:
            if relate['property_id'] == property.id:
                self.relates.remove(property)

        return self.properties.pop(self.properties.index(property))

    def link_device(self, interface, device):
        """Link an interface to a device."""

        if interface not in self.interfaces:
            raise error.SystemError("The interface is not in the system.")

        if device not in self.devices:
            raise error.SystemError("The device is not in the system.")

        link = {'interface_id': interface.id, 'device_id': device.id}

        if link in self.links:
            raise error.SystemError("The link already exists in the system.")

        self.links.append(link)

    def relate_property(self, device, property):
        """Relate a device to a property."""

        if device not in self.devices:
            raise error.SystemError("The device is not in the system.")

        if property not in self.properties:
            raise error.SystemError("The property is not in the system.")

        relate = {'device_id': device.id, 'property_id': property.id}

        if relate in self.relates:
            raise error.SystemError("The relate already exists in the system.")

        self.relates.append(relate)

    def activate_device(self, device):
        """Activate an inactive device."""

        if device.active is True:
            return "The device is already active."

        return device.toggle_active_state()

    def deactivate_device(self, device):
        """Deactivate and active device."""

        if device.active is False:
            return "The device is already inactive."

        return device.toggle_active_state()

    def get_death(self):
        """Return the first death dictionary satisfied, otherwise None."""

        config_satisfied = False
        location_satisfied = False

        for death in self.deaths:

            config_satisfied = True
            location_satisfied = True

            for device_state in death['configuration']:
                this_device = self.get_device(config_id=device_state['device_id'])

                if this_device.active != device_state['active_state']:
                    config_satisfied = False
                    break

            if death['location'] is not None and death['location'] != self.level.game.player.location():
                location_satisfied = False

        if config_satisfied is True and location_satisfied is True:
            return death

        return None

    def kills_player(self):
        """Return True if the level is in a state that kills the player, otherwise False."""

        death = self.get_death()

        if death is not None:
            return True

        return False