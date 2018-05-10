import exception
import device
from item import Item


class Tool(Item):
    """An item that can be used to activate a device."""

    def __init__(self, *args, **kwargs):
        super(Tool, self).__init__(*args, **kwargs)

    def can_activate(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        if test_device.enabled is True and isinstance(test_device, device.Device):
            return True

        return False

    def get_use(self, target_device):
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

        if test_device.enabled is True and test_device.active is False and isinstance(test_device, device.Valve):
            return True

        return False


class PryBar(Tool):
    """A tool that can be used to activate a door."""

    def __init__(self, *args, **kwargs):
        super(PryBar, self).__init__(*args, **kwargs)

    def can_activate(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        if test_device.enabled is True and test_device.active is False and isinstance(test_device, device.Door):
            return True

        return False


class ToolFactory(object):
    """Makes specific Device type instances."""

    @staticmethod
    def make_tool(inventory, tool_type, *args, **kwargs):
        if tool_type.lower() == 'wrench':
            return Wrench(inventory, *args, **kwargs)
        if tool_type.lower() == 'prybar':
            return PryBar(inventory, *args, **kwargs)
        raise exception.FactoryError("The specified tool type does not exist.")
