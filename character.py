import exception
import utility
from inventory import Inventory
from device import Door
from device import Valve


class Character(object):
    """Character class used for player and NPCs."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.inventory = Inventory(self)
        self.name = 'character'
        self.x = 0
        self.y = 0
        self.orientation = 0
        self.actions = {}
        self.cell = self.get_map_cell()

    def __is_valid_move(self, cell):

        if cell is None:
            raise exception.MoveError("There's no cell there.")

        is_on_path = self.game.level.map.path.has_cell(cell)
        is_blocked = any([True for device in cell.devices
                          if (isinstance(device, Door)
                              or isinstance(device, Valve))
                          and device.active is False])
        if not is_on_path:
            raise exception.MoveError("Player cannot move to cell. The cell is not on the path.")
        if is_blocked:
            raise exception.MoveError("Player cannot move to cell. The cell is blocked.")

        return True

    def location(self):
        """Returns character location as (x, y) tuple."""

        return self.x, self.y

    def get_map_cell(self):
        """Get the cell at the location of this character."""

        return self.game.level.map.get_cell(*self.location())

    def on_move_update(self):
        """Update attributes that are location-dependent."""

        self.update_actions()
        self.cell = self.get_map_cell()

    def move_to(self, x, y):
        """Move character to specified x, y if it is a valid cell."""

        to_cell = self.game.level.map.get_cell(x, y)
        if self.__is_valid_move(to_cell):
            self.x = x
            self.y = y
            self.on_move_update()

    def move_up(self):
        """Move character up one cell if possible"""

        self.orientation = 0
        self.move_to(self.x, self.y - 1)

    def move_right(self):
        """Move character right one cell if possible"""

        self.orientation = 1
        self.move_to(self.x + 1, self.y)

    def move_down(self):
        """Move character down one cell if possible"""

        self.orientation = 2
        self.move_to(self.x, self.y + 1)

    def move_left(self):
        """Move character left one cell if possible"""

        self.orientation = 3
        self.move_to(self.x - 1, self.y)

    def get_visible_components(self):
        """Return d4 components visible to the player."""

        visible_interfaces = self.get_visible_interfaces()
        visible_devices = self.get_visible_devices()
        visible_components = [items[0] + items[1] for items in zip(visible_interfaces, visible_devices)]
        return visible_components

    def get_visible_interfaces(self):
        """Return d4 interfaces visible to the player."""

        d4_visible_interfaces = []
        d4_interfaces = self.game.level.map.get_d4_interfaces(*self.location())
        for interface_list in d4_interfaces:
            visible_interfaces = []
            for interface in interface_list:
                if interface.visible is True:
                    if utility.d4_inverse(interface.orientation) == d4_interfaces.index(interface_list):
                        visible_interfaces.append(interface)
            d4_visible_interfaces.append(visible_interfaces)
        return d4_visible_interfaces

    def get_visible_devices(self):
        """Return d4 devices visible to the player."""

        d4_visible_devices = []
        d4_devices = self.game.level.map.get_d4_devices(*self.location())
        for device_list in d4_devices:
            visible_devices = []
            for device in device_list:
                device_cell = self.game.level.map.get_cell(*device.location())
                if device.visible is True and self.game.level.map.path.has_cell(device_cell):
                    visible_devices.append(device)
            d4_visible_devices.append(visible_devices)
        return d4_visible_devices

    def report_visible_components(self):
        """Return string description of visible interfaces and devices."""

        visible_components = self.get_visible_components()
        return utility.build_component_report_text(self.orientation, visible_components)

    def report_visible_interfaces(self):
        """Return string description of visible interfaces."""

        visible_interfaces = self.get_visible_interfaces()
        return utility.build_component_report_text(self.orientation, visible_interfaces)

    def report_visible_devices(self):
        """Return string description of visible devices."""

        visible_devices = self.get_visible_devices()
        return utility.build_component_report_text(self.orientation, visible_devices)

    def get_actions(self):
        """Return dictionary of actions based on d4 interfaces."""

        interface_list = [iface
                          for iface_list in self.get_visible_interfaces()
                          for iface in iface_list]
        actions = {interface_list.index(interface) + 1: interface.use
                   for interface in interface_list}
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
