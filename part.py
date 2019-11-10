import device
import exception
from item import Item


class Part(Item):
    """A part that can be used to enable a device."""

    def __init__(self, *args, **kwargs):
        super(Part, self).__init__(*args, **kwargs)

    def can_enable(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        if (test_device.enabled is False
        and isinstance(test_device, device.Device)):
            return True

    def get_use_action(self, target_device):
        """Return an ad-hoc function for enabling the device."""

        def enable_device():
            target_device.enabled = True

        return enable_device

    def use_action_text(self, target_device):
        """Return text description of the currently available action."""

        return "Repair the {0} with the {1}".format(self, target_device)


class Wires(Part):
    """A part that can be used to enable a switch."""

    def __init__(self, *args, **kwargs):
        super(Wires, self).__init__(*args, **kwargs)

    def can_enable(self, test_device):
        """Returns True if this part enables the type of device provided, otherwise False."""

        if (test_device.enabled is False
        and isinstance(test_device, device.Switch)):
            return True

        return


class PartFactory(object):
    """Makes specific Part type instances."""

    @staticmethod
    def make_part(inventory, part_type, *args, **kwargs):
        if part_type.lower() == 'wires':
            return Wires(inventory, *args, **kwargs)
        raise exception.FactoryError("The specified part type does not exist.")