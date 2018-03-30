import exception
from item import Item


class Tool(Item):
    """An item that can be used to enable a system component."""

    def __init__(self, *args, **kwargs):
        super(Tool, self).__init__(*args, **kwargs)



class Wrench(Tool):
    """A tool that can be used to enable a valve."""

    def __init__(self, *args, **kwargs):
        super(Wrench, self).__init__(*args, **kwargs)


class PryBar(Tool):
    """A tool that can be used to enable a door."""

    def __init__(self, *args, **kwargs):
        super(PryBar, self).__init__(*args, **kwargs)


class ToolFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_tool(inventory, tool_type, *args, **kwargs):
        if tool_type.lower() == 'wrench':
            return Wrench(inventory, *args, **kwargs)
        raise exception.FactoryError("The specified tool type does not exist.")
