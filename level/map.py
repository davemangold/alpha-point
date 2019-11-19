import error
from level.gameobject.component import device
from level.gameobject.component import interface
from level.gameobject.item.tool import Tool
from level.gameobject.item.tool import ToolFactory
from level.gameobject.item.part import Part
from level.gameobject.item.part import PartFactory
from level.gameobject.item.artifact import Artifact
from level.gameobject.item.artifact import ArtifactFactory
from inventory.inventory import Inventory
from config import level_config


class MapCell(object):
    """A single map cell (tile)."""

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y
        self.interfaces = []
        self.devices = []
        self.tools = []
        self.parts = []
        self.artifacts = []
        self.story = None
        self.story_seen = False
        self.visited = False

    @property
    def components(self):
        """Return all components."""

        return self.interfaces + self.devices

    @property
    def items(self):
        """Return all items."""

        return self.tools + self.parts + self.artifacts

    def is_on_path(self):

        return self.map.path.has_cell(self)

    def is_blocked(self):
        """Returns True if the cell is blocked, otherwise False."""

        blocked_by_interface = False

        blocked_by_device = any([
            True for d in self.devices
            if (isinstance(d, device.Door) or isinstance(d, device.Valve))
            and d.active is False])

        blocked_by_artifact = any([
            True for a in self.artifacts
            if a.blocking is True])

        blocked_by_tool = any([
            True for t in self.tools
            if t.blocking is True])

        blocked_by_part = any([
            True for p in self.parts
            if p.blocking is True])

        is_blocked = any([
            blocked_by_interface,
            blocked_by_device,
            blocked_by_artifact,
            blocked_by_tool,
            blocked_by_part])

        return is_blocked

    def has_interfaces(self):
        """Return True if the map cell has any interfaces, otherwise False."""

        return len(self.interfaces) > 0

    def has_devices(self):
        """Return True if the map cell has any devices, otherwise False."""

        return len(self.devices) > 0

    def has_components(self):
        """Return True if the map cell has any components, otherwise False."""

        return len(self.components) > 0

    def has_tools(self):
        """Return True if the map cell has any tools, otherwise False."""

        return len(self.tools) > 0

    def has_parts(self):
        """Return True if the map cell has any parts, otherwise False."""

        return len(self.parts) > 0

    def has_artifacts(self):
        """Return True if the map cell has any tools, otherwise False."""

        return len(self.artifacts) > 0

    def has_items(self):
        """Return True if the map cell has any components, otherwise False."""

        return len(self.items) > 0

    def has_story(self):
        """Return True if there is story text associated with the cell, otherwise False."""

        return self.story is not None

    def add_interface(self, interface):
        """Adds an interface to the map cell."""

        if interface in self.interfaces:
            raise error.MapError("The interface is already assigned to the map cell.")

        self.interfaces.append(interface)

    def remove_interface(self, interface):
        """Removes the interface from the map cell and return it."""

        if interface not in self.interfaces:
            raise error.MapError("The interface is not assigned to the map cell.")

        return self.interfaces.pop(self.interfaces.index(interface))

    def add_device(self, device):
        """Adds an interface to the map cell."""

        if device in self.devices:
            raise error.MapError("The device is already assigned to the map cell.")

        self.devices.append(device)

    def remove_device(self, device):
        """Removes the interface from the map cell and returns it."""

        if device not in self.interfaces:
            raise error.MapError("The device is not assigned to the map cell.")

        return self.devices.pop(self.devices.index(device))

    def remove_component(self, component):
        """Remove the component from the map cell."""

        if isinstance(component, interface.Interface):
            self.remove_interface(component)
        elif isinstance(component, device.Device):
            self.remove_device(component)
        else:
            raise TypeError("The component must be of type interface or device.")

    def add_tool(self, tool):
        """Adds a tool to the map cell."""

        if tool in self.tools:
            raise error.MapError("The tool is already assigned to the map cell.")

        self.tools.append(tool)

    def remove_tool(self, tool):
        """Removes the interface from the map cell"""

        if tool not in self.tools:
            raise error.MapError("The tool is not assigned to the map cell.")

        return self.tools.pop(self.tools.index(tool))

    def add_part(self, part):
        """Adds a tool to the map cell."""

        if part in self.parts:
            raise error.MapError("The part is already assigned to the map cell.")

        self.parts.append(part)

    def remove_part(self, part):
        """Removes the interface from the map cell"""

        if part not in self.parts:
            raise error.MapError("The part is not assigned to the map cell.")

        return self.parts.pop(self.parts.index(part))

    def add_artifact(self, artifact):
        """Adds a tool to the map cell."""

        if artifact in self.artifacts:
            raise error.MapError("The artifact is already assigned to the map cell.")

        self.artifacts.append(artifact)

    def remove_artifact(self, artifact):
        """Removes the interface from the map cell"""

        if artifact not in self.artifacts:
            raise error.MapError("The artifact is not assigned to the map cell.")

        return self.artifacts.pop(self.artifacts.index(artifact))

    def remove_item(self, item):
        """Remove the item from the map cell."""

        if isinstance(item, Tool):
            self.remove_tool(item)
        elif isinstance(item, Part):
            self.remove_part(item)
        elif isinstance(item, Artifact):
            self.remove_artifact(item)
        else:
            raise TypeError("The item must be of type tool, part or artifact.")


class MapPath(object):
    """Path that the player can access."""

    def __init__(self, map):
        self.map = map
        self.cells = []

    def add_cell(self, cell):
        """Add a map cell to the path."""

        if self.has_cell(cell):
            raise error.MapError("The cell is already in the path.")

        self.cells.append(cell)

    def remove_cell(self, cell):
        """Remove a map cell from the path and return it."""

        if not self.has_cell(cell):
            raise error.MapError("The cell is not in the path.")

        return self.cells.pop(self.cells.index(cell))

    def has_cell(self, cell):
        """True if the cell is part of the path, otherwise False."""

        return cell in self.cells


class Map(object):
    """The map that a player will navigate."""

    def __init__(self, level):
        self.level = level
        self.inventory = Inventory(self)
        self.x_dim = 0
        self.y_dim = 0
        self.cells = []
        self.cells_dict = {}  # {0: {0: <cell>, 1: <cell>}, 1: {0: <cell>, 1: <cell>},...}
        self.path = MapPath(self)
        self.enter_cell = None
        self.exit_cell = None

    def __build_cells(self, x_dim, y_dim):
        """Build collection of cells based on x and y dimensions."""

        for x in range(x_dim):
            if x not in self.cells_dict:
                self.cells_dict[x] = {}
            for y in range(y_dim):
                if y not in self.cells_dict[x]:
                    cell = MapCell(self, x, y)
                    self.cells_dict[x][y] = cell
                    self.cells.append(cell)

    def build(self, level_number):
        """Build the map from the config for the provided level number."""

        map_config = level_config['level'][level_number]['map']

        self.x_dim = map_config['x_dimension']
        self.y_dim = map_config['y_dimension']
        enter_coord = map_config['coord_enter']
        exit_coord = map_config['coord_exit']

        self.__build_cells(self.x_dim, self.y_dim)

        self.enter_cell = self.get_cell(*enter_coord)
        self.exit_cell = self.get_cell(*exit_coord)

        for config_path_cell in map_config['path_cells']:
            path_cell = self.get_cell(*config_path_cell['coordinates'])
            path_cell.story = config_path_cell['story']
            self.path.add_cell(path_cell)

        for system_interface in self.level.system.interfaces:
            interface_cell = self.get_cell(system_interface.x, system_interface.y)
            interface_cell.add_interface(system_interface)

        for system_device in self.level.system.devices:
            device_cell = self.get_cell(system_device.x, system_device.y)
            device_cell.add_device(system_device)

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

        for config_part in map_config['parts']:
            new_part = PartFactory.make_part(self.inventory, config_part['type'])
            new_part.name = config_part['name']
            new_part.description = config_part['description']
            new_part.visible = config_part['visible']
            new_part.interactive = config_part['interactive']
            new_part.blocking = config_part['blocking']
            new_part.x = config_part['x']
            new_part.y = config_part['y']
            self.inventory.add_item(new_part)

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

        for map_tool in self.inventory.get_tools():
            tool_cell = self.get_cell(map_tool.x, map_tool.y)
            tool_cell.add_tool(map_tool)

        for map_part in self.inventory.get_parts():
            part_cell = self.get_cell(map_part.x, map_part.y)
            part_cell.add_part(map_part)

        for map_artifact in self.inventory.get_artifacts():
            artifact_cell = self.get_cell(map_artifact.x, map_artifact.y)
            artifact_cell.add_artifact(map_artifact)

    @property
    def interfaces(self):
        """Interfaces from all map cells"""

        interfaces = []
        for cell in self.cells:
            interfaces += cell.interfaces
        return interfaces

    @property
    def devices(self):
        """Devices from all map cells"""

        devices = []
        for cell in self.cells:
            devices += cell.devices
        return devices

    @property
    def components(self):
        """Components from all map cells."""

        components = []
        for cell in self.cells:
            components += cell.components
        return components

    @property
    def tools(self):
        """Tools from all map cells"""

        tools = []
        for cell in self.cells:
            tools += cell.tools
        return tools

    @property
    def parts(self):
        """Parts from all map cells"""

        parts = []
        for cell in self.cells:
            parts += cell.parts
        return parts

    @property
    def artifacts(self):
        """Artifacts from all map cells"""

        artifacts = []
        for cell in self.cells:
            artifacts += cell.artifacts
        return artifacts

    @property
    def items(self):
        """Items from all map cells."""

        items = []
        for cell in self.cells:
            items += cell.items
        return items

    def get_cell(self, x, y):
        """Return the cell at the provided coordinates if it exists, otherwise None."""

        try:
            return self.cells_dict[x][y]
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

    def get_d4_parts(self, x, y):
        """Return the tools for the d4 cells around the provided coordinates."""

        d4_parts = []
        for cell in self.get_d4_cells(x, y):
            if isinstance(cell, MapCell):
                d4_parts.append(cell.parts)
            else:
                d4_parts.append([])
        return d4_parts

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
        d4_parts = self.get_d4_parts(x, y)
        d4_artifacts = self.get_d4_artifacts(x, y)
        d4_items = [items[0] + items[1] for items in zip(d4_tools, d4_parts, d4_artifacts)]
        return d4_items

    def has_item(self, item):
        """Returns True if the item is in the map inventory, otherwise False."""

        return item in self.inventory