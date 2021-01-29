import error
from gameobject.component import device
from gameobject.item import Item


class Tool(Item):
    """An item that can be used to activate a device."""

    def __init__(self, *args, **kwargs):
        super(Tool, self).__init__(*args, **kwargs)

    def can_activate(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        return (test_device.enabled is True
                and test_device.active is False
                and isinstance(test_device, device.Device)
                and self.level_number == test_device.level_number)

    def get_use_function(self, target_device):
        """Return an ad-hoc function for activating the device."""

        def use_device():
            override_state = target_device.override_dependencies
            target_device.override_dependencies = True
            target_device.use()
            target_device.override_dependencies = override_state

        return use_device

    def use_action_text(self, target_device):
        """Return text description of the currently available action."""

        return "Use the {0} on the {1}".format(self, target_device)


class Wrench(Tool):
    """A tool that can be used to activate a valve."""

    def __init__(self, *args, **kwargs):
        super(Wrench, self).__init__(*args, **kwargs)

    def can_activate(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        return (test_device.enabled is True
                and test_device.active is False
                and isinstance(test_device, device.Valve)
                and self.level_number == test_device.level_number)


class PryBar(Tool):
    """A tool that can be used to activate a door."""

    def __init__(self, *args, **kwargs):
        super(PryBar, self).__init__(*args, **kwargs)

    def can_activate(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        return (test_device.enabled is True
                and test_device.active is False
                and isinstance(test_device, device.Door)
                and self.level_number == test_device.level_number)


class ToolFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_tool(map, tool_type, *args, **kwargs):

        if tool_type.lower() == 'wrench':
            return Wrench(map, *args, **kwargs)
        if tool_type.lower() == 'prybar':
            return PryBar(map, *args, **kwargs)
        raise error.FactoryError("The specified tool type does not exist.")

    def make_from_config(self, map, tool_config, level_number):

        new_tool = self.make_tool(map, tool_config['type'])
        new_tool.config_id = tool_config['id']
        new_tool.level_number = level_number
        new_tool.name = tool_config['name']
        new_tool.description = tool_config['description']
        new_tool.report = tool_config['report']
        new_tool.inspectable = tool_config['inspectable']
        new_tool.visible = tool_config['visible']
        new_tool.interactive = tool_config['interactive']
        new_tool.blocking = tool_config['blocking']
        new_tool.x = tool_config['x']
        new_tool.y = tool_config['y']

        return new_tool
