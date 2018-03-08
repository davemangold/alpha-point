import exception
from item import Item


class Tool(Item):
    """An item that can be used on a system component."""

    def __init__(self, *args, **kwargs):
        super(self, Item).__init__(*args, **kwargs)


class Wrench(Tool):
    """A tool that can be used to force a valve."""

    def __init__(self, *args, **kwargs):
        super(self, Wrench).__init__(*args, **kwargs)


class ToolFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_tool(inventory, tool_type):
        if tool_type.lower() == 'wrench':
            return Wrench(inventory)
        raise exception.FactoryError("The specified tool type does not exist.")
