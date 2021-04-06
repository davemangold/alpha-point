import error
from gameobject.item import Item
from gameobject.item.tool import Tool
from gameobject.item.part import Part
from gameobject.item.artifact import Artifact


class Inventory(object):
    """Inventory class to hold and manage items."""

    def __init__(self, owner):
        self.owner = owner  # character or map
        self.items = []

    def add_item(self, item):
        """Add the item to the inventory."""

        if not isinstance(item, Item):
            raise error.GameInventoryError("Inventory can only store object of type 'Item'.")

        if item in self.items:
            raise error.GameInventoryError("The item already exists in the inventory.")

        item.inventory = self
        self.items.append(item)

    def remove_item(self, item):
        """Remove the item from the inventory and return it."""

        if item not in self.items:
            raise error.GameInventoryError("The item does not exist in the inventory.")

        item.inventory = None
        return self.items.pop(self.items.index(item))

    def remove_item_by_id(self, item_id):
        """Remove the item with the provided id from the inventory and return it."""

        for item in self.items:
            if item.id == item_id:
                return self.remove_item(item)

    def clear_items(self):
        """Remove all items from the inventory without returning them."""

        self.items = []

    def has_item(self, item):
        """Return True if the item is in the inventory."""

        return item in self.items

    def get_tools(self):
        """Return all items that are Tool instances."""

        return [item for item in self.items if isinstance(item, Tool)]

    def get_tool(self, tool_id=None, config_id=None):
        """Return the device if it exists."""

        tools = self.get_tools()

        if tool_id is not None:
            for check_tool in tools:
                if check_tool.id == tool_id:
                    return check_tool

        elif config_id is not None:
            for check_tool in tools:
                if check_tool.config_id == config_id:
                    return check_tool

    def get_parts(self):
        """Return all items that are Part instances."""

        return [item for item in self.items if isinstance(item, Part)]

    def get_part(self, part_id=None, config_id=None):
        """Return the device if it exists."""

        parts = self.get_parts()

        if part_id is not None:
            for check_part in parts:
                if check_part.id == part_id:
                    return check_part

        elif config_id is not None:
            for check_part in parts:
                if check_part.config_id == config_id:
                    return check_part

    def get_artifacts(self):
        """Return all items that are Artifact instances."""

        return [item for item in self.items if isinstance(item, Artifact)]

    def get_artifact(self, artifact_id=None, config_id=None):
        """Return the device if it exists."""

        artifacts = self.get_artifacts()

        if artifact_id is not None:
            for check_artifact in artifacts:
                if check_artifact.id == artifact_id:
                    return check_artifact

        elif config_id is not None:
            for check_artifact in artifacts:
                if check_artifact.config_id == config_id:
                    return check_artifact

    def get_items_by_type(self, instance):
        """Return all items that match the type of the provided instance."""

        return [item for item in self.items if type(item) == type(instance)]

    def get_items_by_name(self, name):
        """Return all items that match the provided name."""

        return [item for item in self.items if name.lower() in item.name.lower()]

    def get_items_by_description(self, description):
        """Return all items that match the provided description."""

        return [item for item in self.items if description.lower() in item.description.lower()]
