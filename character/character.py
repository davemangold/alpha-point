import error
import utility
from action import PlayerAction
from action import ItemAction
from inventory import Inventory


class Character(object):
    """Character class used for player."""

    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.inventory = Inventory(self)
        self.name = 'character'
        self.x = 0
        self.y = 0
        self.orientation = 0
        self.actions = {}
        self.last_action = None
        self.cell = self.get_map_cell()

    def __str__(self):
        """String conversion for character."""

        return self.name

    def __is_valid_move(self, cell):
        """Returns True if moving to cell is valid in current map, otherwise False."""

        valid_move = True

        if cell is None or cell.is_blocked() or not cell.is_on_path():
            valid_move = False

        return valid_move

    def __on_move_update(self):
        """Update attributes that are location-dependent."""

        self.update_actions()
        self.cell = self.get_map_cell()
        for item in self.inventory.items:
            item.x, item.y = self.x, self.y
        for cell in self.game.level.map.get_d4_cells(*self.location):
            if cell is not None:
                cell.seen = True

    @property
    def location(self):
        """Returns character location as (x, y) tuple."""

        return self.x, self.y

    def get_map_cell(self):
        """Get the cell at the location of this character."""

        return self.game.level.map.get_cell(*self.location)

    def move_to(self, x, y):
        """Move character to cell at x, y if it's a valid move."""

        to_cell = self.game.level.map.get_cell(x, y)
        valid_move = self.__is_valid_move(to_cell)

        if valid_move:
            self.x = x
            self.y = y
            self.__on_move_update()
        else:
            self.__on_move_update()
            raise error.GameMoveError("The requested move is invalid.")

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

    def take_item(self, item):
        """Remove item from its current inventory and add it to the character's inventory."""

        self.inventory.add_item(item.inventory.remove_item(item))

    def give_item(self, item):
        """Return item after removing it from the character's inventory."""

        return self.inventory.remove_item(item)

    def get_visible_tools(self):
        """Return d4 tools visible to the player."""

        d4_visible_tools = []
        d4_tools = self.game.level.map.get_d4_tools(*self.location)

        for tool_list in d4_tools:
            visible_tools = [tool for tool in tool_list if tool.visible is True]
            d4_visible_tools.append(visible_tools)

        return d4_visible_tools

    def get_visible_parts(self):
        """Return d4 tools visible to the player."""

        d4_visible_parts = []
        d4_parts = self.game.level.map.get_d4_parts(*self.location)

        for part_list in d4_parts:
            visible_parts = [part for part in part_list if part.visible is True]
            d4_visible_parts.append(visible_parts)

        return d4_visible_parts

    def get_visible_artifacts(self):
        """Return d4 artifacts visible to the player."""

        d4_visible_artifacts = []
        d4_artifacts = self.game.level.map.get_d4_artifacts(*self.location)

        for artifact_list in d4_artifacts:
            visible_artifacts = [artifact for artifact in artifact_list if artifact.visible is True]
            d4_visible_artifacts.append(visible_artifacts)

        return d4_visible_artifacts

    def get_visible_items(self):
        """Return d4 items visible to the player."""

        visible_tools = self.get_visible_tools()
        visible_parts = self.get_visible_parts()
        visible_artifacts = self.get_visible_artifacts()
        visible_items = [items[0] + items[1] + items[2]
                         for items in zip(visible_artifacts, visible_tools, visible_parts)]

        return visible_items

    def get_visible_interfaces(self):
        """Return d4 interfaces visible to the player."""

        d4_visible_interfaces = []
        d4_interfaces = self.game.level.map.get_d4_interfaces(*self.location)

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
        d4_devices = self.game.level.map.get_d4_devices(*self.location)

        for device_list in d4_devices:
            visible_devices = []
            for device in device_list:
                if device.visible is True:
                    visible_devices.append(device)
            d4_visible_devices.append(visible_devices)

        return d4_visible_devices

    def get_visible_components(self):
        """Return d4 components visible to the player."""

        visible_interfaces = self.get_visible_interfaces()
        visible_devices = self.get_visible_devices()
        visible_components = [items[0] + items[1] for items in zip(visible_interfaces, visible_devices)]

        return visible_components

    def get_visible_objects(self):
        """Return all objects visible to the player."""

        visible_components = self.get_visible_components()
        visible_items = self.get_visible_items()
        visible_objects = [items[0] + items[1] for items in zip(visible_components, visible_items)]

        return visible_objects

    def get_interactive_objects(self):
        """Return all visible objects with which the player can interact."""

        interactive_objects = []
        visible_objects = self.get_visible_objects()

        for obj_list in visible_objects:
            int_obj_list = [obj for obj in obj_list if obj.interactive is True]
            interactive_objects.append(int_obj_list)

        return interactive_objects

    def report_visible_tools(self):
        """Return string description of visible tools."""

        visible_tools = self.get_visible_tools()

        return utility.build_object_report_text(self.orientation, visible_tools)

    def report_visible_parts(self):
        """Return string description of visible parts."""

        visible_parts = self.get_visible_parts()

        return utility.build_object_report_text(self.orientation, visible_parts)

    def report_visible_artifacts(self):
        """Return string description of visible artifacts."""

        visible_artifacts = self.get_visible_artifacts()

        return utility.build_object_report_text(self.orientation, visible_artifacts)

    def report_visible_items(self):
        """Return string description of visible items (tools, parts, and artifacts)."""

        visible_items = self.get_visible_items()

        return utility.build_object_report_text(self.orientation, visible_items)

    def report_visible_interfaces(self):
        """Return string description of visible interfaces."""

        visible_interfaces = self.get_visible_interfaces()

        return utility.build_object_report_text(self.orientation, visible_interfaces)

    def report_visible_devices(self):
        """Return string description of visible devices."""

        visible_devices = self.get_visible_devices()

        return utility.build_object_report_text(self.orientation, visible_devices)

    def report_visible_components(self):
        """Return string description of visible components (interfaces and devices)."""

        visible_components = self.get_visible_components()

        return utility.build_object_report_text(self.orientation, visible_components)

    def report_visible_objects(self):
        """Return string description of visible objects (components and items)."""

        visible_objects = self.get_visible_objects()

        return utility.build_object_report_text(self.orientation, visible_objects)

    def get_actions(self):
        """Return dictionary of actions based on player inventory and d4 visible objects."""

        # tools in the player inventory
        character_tool_list = self.inventory.get_tools()

        # parts in the player inventory
        character_part_list = self.inventory.get_parts()

        # visible devices on the map
        map_device_list = [device
            for device_list in utility.d4_to_player_list(self.orientation, self.get_visible_devices())
            for device in device_list
            if device.interactive is True]

        # visible interfaces on the map
        map_interface_list = [interface
            for interface_list in utility.d4_to_player_list(self.orientation, self.get_visible_interfaces())
            for interface in interface_list
            if interface.interactive is True]

        # visible game objects on the map
        map_gameobject_list = [gameobject
            for gameobject_list in utility.d4_to_player_list(self.orientation, self.get_visible_objects())
            for gameobject in gameobject_list
            if gameobject.inspectable is True]

        # visible items on the map (includes tools)
        map_item_list = [item
            for item_list in utility.d4_to_player_list(self.orientation, self.get_visible_items())
            for item in item_list
            if item.interactive is True]

        # actions to use tools on devices
        tool_actions = [
            ItemAction(
                game=self.game,
                function=tool.get_use_function(device),
                description=tool.use_action_text(device),
                item=tool,
                device=device)
            for tool in character_tool_list
            for device in map_device_list
            if tool.can_activate(device)]

        # actions to use parts on devices
        part_actions = [
            ItemAction(
                game=self.game,
                function=part.get_use_function(device),
                description=part.use_action_text(device),
                item=part,
                device=device)
            for part in character_part_list
            for device in map_device_list
            if part.can_enable(device)]

        # actions for player to use interfaces
        interface_actions = [
            PlayerAction(
                game=self.game,
                function=interface.use,
                description=interface.action_text(),
                target=interface)
            for interface in map_interface_list]

        # actions for player to examine game objects
        gameobject_actions = [
            PlayerAction(
                game=self.game,
                function=gameobject.examine,
                description=gameobject.examine_action_text(),
                target=gameobject)
            for gameobject in map_gameobject_list]

        # actions for player to take items from map
        item_actions = [
            PlayerAction(
                game=self.game,
                function=item.map_to_player,
                description=item.take_action_text(),
                target=item)
            for item in map_item_list]

        # combined list of all actions
        actions_list = interface_actions + tool_actions + part_actions + gameobject_actions + item_actions

        # dictionary of key: action object pairs
        actions = {actions_list.index(action) + 1: action for action in actions_list}

        return actions

    def update_actions(self):
        """Set the currently available actions."""

        self.actions = self.get_actions()

    def do_action(self, key):
        """Call the action function associated with the provided key."""

        try:
            action = self.actions[key]
            action.do()
            self.update_actions()

        except KeyError:
            raise error.GameActionError("There is no action defined for the provided key.")
