import exception
from item import Item
from tool import Tool
from artifact import Artifact


class Inventory(object):
    """Inventory class to hold items."""

    def __init__(self, owner, *args, **kwargs):
        self.owner = owner  # character or level
        self.items = []

    def add_item(self, item):
        """Add the item to the inventory."""

        if not isinstance(item, Item):
            raise exception.InventoryError("Inventory can only store objects of type 'Item'.")

        if item in self.items:
            raise exception.InventoryError("The item already exists in the inventory.")

        self.items.append(item)

    def remove_item(self, item):
        """Remove the item from the inventory and return it."""

        if item not in self.items:
            raise exception.InventoryError("The item does not exist in the inventory.")

        return self.items.pop(self.items.index(item))

    def clear_items(self):
        """Remove all items from the inventory without returning them."""

        self.items = []

    def get_tools(self):
        """Return all items that are Tool instances."""

        return [item for item in self.items if isinstance(item, Tool)]

    def get_artifacts(self):
        """Return all items that are Tool instances."""

        return [item for item in self.items if isinstance(item, Artifact)]

    def get_items_by_type(self, instance):
        """Return all items that match the type of the provided instance."""

        return [item for item in self.items if type(item) == type(instance)]

    def get_items_by_name(self, name):
        """Return all items that match the provided name."""

        return [item for item in self.items if name.lower() in item.name.lower()]
