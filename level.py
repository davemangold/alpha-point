import exception
import device
from device import Device
from device import DeviceFactory
from interface import Interface
from interface import InterfaceFactory
from tool import Tool
from tool import ToolFactory
from artifact import Artifact
from artifact import ArtifactFactory
from inventory import Inventory
from config import level_config


class System(object):
    """A collection of interfaces and devices the player can control."""

    def __init__(self, level, *args, **kwargs):
        self.level = level
        self.devices = []  # [<device>,...]
        self.interfaces = []  # [<interface>,...]
        self.links = []  # [{'interface_id': <interface id>, 'device_id': <device id>},...]
        self.deaths = []

    def build(self, level_number):
        """Build system from config dictionary."""

        system_config = level_config['levels'][level_number]['system']

        for config_interface in system_config['interfaces']:
            new_interface = InterfaceFactory.make_interface(self, config_interface['type'])
            new_interface.config_id = config_interface['id']
            new_interface.name = config_interface['name']
            new_interface.description = config_interface['description']
            new_interface.enabled = config_interface['enabled']
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
            new_device.x = config_device['x']
            new_device.y = config_device['y']
            new_device.msg_action_true = config_device['msg_action_true']
            new_device.msg_action_false = config_device['msg_action_false']
            new_device.msg_active_true = config_device['msg_active_true']
            new_device.msg_active_false = config_device['msg_active_false']
            new_device.msg_toggle_active_true = config_device['msg_toggle_active_true']
            new_device.msg_toggle_active_false = config_device['msg_toggle_active_false']
            new_device.msg_unmet_dependencies = config_device['msg_unmet_dependencies']

        for config_device in system_config['devices']:
            system_device = self.get_device(config_id=config_device['id'])
            for config_dependency in config_device['dependencies']:
                dependency_device = self.get_device(config_id=config_dependency['device_id'])
                system_device.add_dependency(dependency_device.id, config_dependency['active_state'])

        for config_link in system_config['links']:
            link_interface = self.get_interface(config_id=config_link['interface_id'])
            link_device = self.get_device(config_id=config_link['device_id'])
            self.link_components(link_interface, link_device)

        for config_death in system_config['deaths']:
            self.deaths.append(config_death)

    def has_interface(self, interface):
        """Returns True if the system contains the interface, otherwise False."""

        return interface in self.interfaces

    def has_device(self, device):
        """Returns True if the system contains the device, otherwise False."""

        return device in self.devices

    def get_interface(self, interface_id=None, config_id=None):
        """Return the interface if it exists."""

        interface = None

        if interface_id is not None:
            for check_interface in self.interfaces:
                if check_interface.id == interface_id:
                    interface = check_interface
                    break

        if config_id is not None:
            for check_interface in self.interfaces:
                if check_interface.config_id == config_id:
                    interface = check_interface
                    break

        return interface

    def get_device(self, device_id=None, config_id=None):
        """Return the interface if it exists."""

        device = None

        if device_id is not None:
            for check_device in self.devices:
                if check_device.id == device_id:
                    device = check_device
                    break

        if config_id is not None:
            for check_device in self.devices:
                if check_device.config_id == config_id:
                    device = check_device
                    break

        return device

    def get_device_ids(self, interface):
        """Return list of device ids related to interface."""

        if not isinstance(interface, Interface):
            raise TypeError("Object not of type 'Interface'.")

        if not self.has_interface(interface):
            raise exception.SystemError("The interface is not a component of the system.")

        device_ids = []

        for link in self.links:
            if link['interface_id'] == interface.id:
                device_ids.append(link['device_id'])

        return device_ids

    def get_interface_ids(self, device):
        """Return list of interface ids related to device."""

        if not isinstance(device, Device):
            raise TypeError("Object not of type 'Device'.")

        if not self.has_device(device):
            raise exception.SystemError("The device is not a component of the system.")

        interface_ids = []

        for link in self.links:
            if link['device_id'] == device.id:
                interface_ids.append(link['interface_id'])

        return interface_ids

    def get_interface_devices(self, interface):
        """Return a list of all devices linked to an interface."""

        device_ids = self.get_device_ids(interface)
        interface_devices = [device for device in self.devices
                             if device.id in device_ids]

        return interface_devices

    def get_device_interfaces(self, device):
        """Return a list of all interfaces linked to a device."""

        interface_ids = self.get_interface_ids(device)
        device_interfaces = [interface for interface in self.interfaces
                             if interface.id in interface_ids]

        return device_interfaces

    def get_components(self):
        """Return all components."""

        return self.interfaces + self.devices

    def add_interface(self, interface):
        """Add an interface to the system."""

        if interface in self.interfaces:
            raise exception.SystemError("The interface is already a component of the system.")

        self.interfaces.append(interface)

    def remove_interface(self, interface):
        """Remove an interface from the system and return it."""

        if interface not in self.interfaces:
            raise exception.SystemError("The interface is not a component of the system.")

        for link in self.links:
            if link['interface_id'] == interface.id:
                self.links.remove(link)

        return self.interfaces.pop(self.interfaces.index(interface))

    def add_device(self, device):
        """Add a device to the system."""

        if device in self.devices:
            raise exception.SystemError("The device is already a component of the system.")

        self.devices.append(device)

    def remove_device(self, device):
        """Remove a device from the system and return it."""

        if device not in self.devices:
            raise exception.SystemError("The device is not a component of the system.")

        for link in self.links:
            if link['device_id'] == device.id:
                self.links.remove(link)

        return self.devices.pop(self.devices.index(device))

    def link_components(self, interface, device):
        """Link an interface to a device."""

        if interface not in self.interfaces:
            raise exception.SystemError("The interface is not a component of the system.")

        if device not in self.devices:
            raise exception.SystemError("The device is not a component of the system.")

        link = {'interface_id': interface.id, 'device_id': device.id}

        if link in self.links:
            raise exception.SystemError("The link already exists in the system.")

        self.links.append(link)

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


class MapCell(object):
    """A single map cell (tile)."""

    def __init__(self, map, x, y, *args, **kwargs):
        self.map = map
        self.x = x
        self.y = y
        self.interfaces = []
        self.devices = []
        self.tools = []
        self.artifacts = []
        self.story_text = None
        self.story_seen = False
        self.visited = False

    def is_on_path(self):

        return self.map.path.has_cell(self)

    def is_blocked(self):
        """Returns True if the cell is blocked, otherwise False."""

        blocked_by_interface = False

        blocked_by_device = any([True for d in self.devices
                                 if (isinstance(d, device.Door)
                                     or isinstance(d, device.Valve))
                                 and d.active is False])

        blocked_by_artifact = any([True for a in self.artifacts
                                   if a.blocking is True])

        blocked_by_tool = any([True for t in self.tools
                               if t.blocking is True])

        is_blocked = (blocked_by_interface
                      or blocked_by_device
                      or blocked_by_artifact
                      or blocked_by_tool)

        return is_blocked

    def add_interface(self, interface):
        """Adds an interface to the map cell."""

        if interface in self.interfaces:
            raise exception.MapError("The interface is already assigned to the map cell.")
        self.interfaces.append(interface)

    def remove_interface(self, interface):
        """Removes the interface from the map cell and return it."""

        if interface not in self.interfaces:
            raise exception.MapError("The interface is not assigned to the map cell.")
        return self.interfaces.pop(self.interfaces.index(interface))

    def add_device(self, device):
        """Adds an interface to the map cell."""

        if device in self.devices:
            raise exception.MapError("The device is already assigned to the map cell.")
        self.devices.append(device)

    def remove_device(self, device):
        """Removes the interface from the map cell and returns it."""

        if device not in self.interfaces:
            raise exception.MapError("The device is not assigned to the map cell.")
        return self.devices.pop(self.devices.index(device))

    def remove_component(self, component):
        """Remove the component from the map cell."""

        if isinstance(component, Interface):
            self.remove_interface(component)
        elif isinstance(component, Device):
            self.remove_device(component)
        else:
            raise TypeError("The component must be of type interface or device.")

    def add_tool(self, tool):
        """Adds a tool to the map cell."""

        if tool in self.tools:
            raise exception.MapError("The tool is already assigned to the map cell.")
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Removes the interface from the map cell"""

        if tool not in self.tools:
            raise exception.MapError("The tool is not assigned to the map cell.")
        return self.tools.pop(self.tools.index(tool))

    def add_artifact(self, artifact):
        """Adds a tool to the map cell."""

        if artifact in self.artifacts:
            raise exception.MapError("The artifact is already assigned to the map cell.")
        self.artifacts.append(artifact)

    def remove_artifact(self, artifact):
        """Removes the interface from the map cell"""

        if artifact not in self.artifacts:
            raise exception.MapError("The artifact is not assigned to the map cell.")
        return self.artifacts.pop(self.artifacts.index(artifact))

    def remove_item(self, item):
        """Remove the item from the map cell."""

        if isinstance(item, Tool):
            self.remove_tool(item)
        elif isinstance(item, Artifact):
            self.remove_artifact(item)
        else:
            raise TypeError("The item must be of type tool or artifact.")

    def has_interfaces(self):
        """Return True if the map cell has any interfaces, otherwise False."""

        return len(self.interfaces) > 0

    def has_devices(self):
        """Return True if the map cell has any devices, otherwise False."""

        return len(self.devices) > 0

    def has_tools(self):
        """Return True if the map cell has any tools, otherwise False."""

        return len(self.tools) > 0

    def has_artifacts(self):
        """Return True if the map cell has any tools, otherwise False."""

        return len(self.artifacts) > 0

    def has_components(self):
        """Return True if the map cell has any components, otherwise False."""

        return self.has_interfaces() or self.has_devices()

    def has_items(self):
        """Return True if the map cell has any components, otherwise False."""

        return self.has_tools() or self.has_artifacts()

    def has_story_text(self):
        """Return True if there is story text associated with the cell, otherwise False."""

        return self.story_text is not None


class MapPath(object):
    """Path that the player can access."""

    def __init__(self, map, *args, **kwargs):
        self.map = map
        self.cells = []

    def add_cell(self, cell):
        """Add a map cell to the path."""

        if self.has_cell(cell):
            raise exception.MapError("The cell is already in the path.")
        self.cells.append(cell)

    def remove_cell(self, cell):
        """Remove a map cell from the path and return it."""

        if not self.has_cell(cell):
            raise exception.MapError("The cell is not in the path.")
        return self.cells.pop(self.cells.index(cell))

    def has_cell(self, cell):
        """True if the cell is part of the path, otherwise False."""

        return cell in self.cells


class Map(object):
    """The map that a player will navigate."""

    def __init__(self, level, *args, **kwargs):
        self.level = level
        self.inventory = Inventory(self)
        self.x_dim = 0
        self.y_dim = 0
        self.cells = {}  # {0: {0: <cell>, 1: <cell>}, 1: {0: <cell>, 1: <cell>},...}
        self.path = MapPath(self)
        self.enter_cell = None
        self.exit_cell = None

    def __build_cells(self, x_dim, y_dim):
        """Build collection of cells based on x and y dimensions."""

        for x in range(x_dim):
            if x not in self.cells:
                self.cells[x] = {}
            for y in range(y_dim):
                if y not in self.cells[x]:
                    self.cells[x][y] = MapCell(self, x, y)

    def build(self, level_number):
        """Build the map from the config for the provided level number."""

        map_config = level_config['levels'][level_number]['map']

        self.x_dim = map_config['x_dimension']
        self.y_dim = map_config['y_dimension']
        enter_coord = map_config['coord_enter']
        exit_coord = map_config['coord_exit']

        self.__build_cells(self.x_dim, self.y_dim)

        self.enter_cell = self.get_cell(*enter_coord)
        self.exit_cell = self.get_cell(*exit_coord)

        for config_tool in map_config['tools']:
            new_tool = ToolFactory.make_tool(self.inventory, config_tool['type'])
            new_tool.name = config_tool['name']
            new_tool.description = config_tool['description']
            new_tool.visible = config_tool['visible']
            new_tool.interactive = config_tool['interactive']
            new_tool.blocking = config_tool['blocking']
            new_tool.x = config_tool['x']
            new_tool.y = config_tool['y']
            self.inventory.add_item(new_tool)

        for config_artifact in map_config['artifacts']:
            new_artifact = ArtifactFactory.make_artifact(self.inventory, config_artifact['type'])
            new_artifact.name = config_artifact['name']
            new_artifact.description = config_artifact['description']
            new_artifact.visible = config_artifact['visible']
            new_artifact.interactive = config_artifact['interactive']
            new_artifact.blocking = config_artifact['blocking']
            new_artifact.x = config_artifact['x']
            new_artifact.y = config_artifact['y']
            self.inventory.add_item(new_artifact)

        for config_path_cell in map_config['path_cells']:
            path_cell = self.get_cell(*config_path_cell['coordinates'])
            path_cell.story_text = config_path_cell['story_text']
            self.path.add_cell(path_cell)

        for system_interface in self.level.system.interfaces:
            interface_cell = self.get_cell(system_interface.x, system_interface.y)
            interface_cell.add_interface(system_interface)

        for system_device in self.level.system.devices:
            device_cell = self.get_cell(system_device.x, system_device.y)
            device_cell.add_device(system_device)

        for map_tool in self.inventory.get_tools():
            tool_cell = self.get_cell(map_tool.x, map_tool.y)
            tool_cell.add_tool(map_tool)

        for map_artifact in self.inventory.get_artifacts():
            artifact_cell = self.get_cell(map_artifact.x, map_artifact.y)
            artifact_cell.add_artifact(map_artifact)

    def get_cell(self, x, y):
        """Return the cell at the provided coordinates if it exists, otherwise None."""

        try:
            return self.cells[x][y]
        except KeyError:
            return None

    def get_d4_cells(self, x, y):
        """Return the cells above, right, below, and left of the provided coordinates."""

        d4_cells = []
        d4_coords = [(x, y - 1),
                     (x + 1, y),
                     (x, y + 1),
                     (x - 1, y)]

        for coord in d4_coords:
            d4_cells.append(self.get_cell(*coord))
        return d4_cells

    def get_d4_interfaces(self, x, y):
        """Return the interfaces for the d4 cells around the provided coordinates."""

        d4_interfaces = []
        for cell in self.get_d4_cells(x, y):
            if isinstance(cell, MapCell):
                d4_interfaces.append(cell.interfaces)
            else:
                d4_interfaces.append([])
        return d4_interfaces

    def get_d4_devices(self, x, y):
        """Return the devices for the d4 cells around the provided coordinates."""

        d4_devices = []
        for cell in self.get_d4_cells(x, y):
            if isinstance(cell, MapCell):
                d4_devices.append(cell.devices)
            else:
                d4_devices.append([])
        return d4_devices

    def get_d4_components(self, x, y):
        """Return the components for the d4 cells around the provided coordinates."""

        d4_interfaces = self.get_d4_interfaces(x, y)
        d4_devices = self.get_d4_devices(x, y)
        d4_components = [items[0] + items[1] for items in zip(d4_interfaces, d4_devices)]
        return d4_components

    def get_d4_tools(self, x, y):
        """Return the tools for the d4 cells around the provided coordinates."""

        d4_tools = []
        for cell in self.get_d4_cells(x, y):
            if isinstance(cell, MapCell):
                d4_tools.append(cell.tools)
            else:
                d4_tools.append([])
        return d4_tools

    def get_d4_artifacts(self, x, y):
        """Return the artifacts for the d4 cells around the provided coordinates."""

        d4_artifacts = []
        for cell in self.get_d4_cells(x, y):
            if isinstance(cell, MapCell):
                d4_artifacts.append(cell.artifacts)
            else:
                d4_artifacts.append([])
        return d4_artifacts

    def get_d4_items(self, x, y):
        """Return the items for the d4 cells around the provided coordinates."""

        d4_tools = self.get_d4_tools(x, y)
        d4_artifacts = self.get_d4_artifacts(x, y)
        d4_items = [items[0] + items[1] for items in zip(d4_tools, d4_artifacts)]
        return d4_items

    def has_item(self, item):
        """Returns True if the item is in the map inventory, otherwise False."""

        return item in self.inventory


class Level(object):
    """Level with which the player interacts."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.map = Map(self)
        self.system = System(self)
        self.number = 0

    def build(self, level_number):
        """Build the specified level."""

        # system must be built before map
        self.system.build(level_number)
        self.map.build(level_number)
        self.number = level_number

    def is_complete(self):
        """Returns True if the player is at the final cell of the level, otherwise False."""

        return self.map.get_cell(*self.game.player.location()) is self.map.exit_cell

    def has_next_level(self):

        return bool(level_config['levels'].get(self.number + 1))
