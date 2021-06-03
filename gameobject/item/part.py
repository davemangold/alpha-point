import error
from gameobject.component import device
from gameobject.item import Item


class Part(Item):
    """A part that can be used to enable a device."""

    def __init__(self, *args, **kwargs):
        super(Part, self).__init__(*args, **kwargs)

    def can_enable(self, test_device):
        """Returns True if this tool activates the type of device provided, otherwise False."""

        return (test_device.enabled is False
                and isinstance(test_device, device.Device))

    def get_use_function(self, target_device):
        """Return an ad-hoc function for enabling the device."""

        part_inventory = self.inventory
        part_id = self.id

        def enable_device():
            target_device.enabled = True
            part_inventory.remove_item_by_id(part_id)

        return enable_device

    def use_action_text(self, target_device):
        """Return text description of the currently available action."""

        return "Repair the {0} with the {1}".format(target_device, self)


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
    def make_part(map, part_type, *args, **kwargs):

        if part_type.lower() == 'wires':
            return Wires(map, *args, **kwargs)
        raise error.GameFactoryError("The specified part type does not exist.")

    def make_from_config(self, map, part_config):

        new_part = self.make_part(map, part_config['type'])
        new_part.config_id = part_config['id']
        new_part.level_number = map.level.number
        new_part.name = part_config['name']
        new_part.description = part_config['description']
        new_part.report = part_config['report']
        new_part.inspectable = part_config['inspectable']
        new_part.visible = part_config['visible']
        new_part.interactive = part_config['interactive']
        new_part.blocking = part_config['blocking']
        new_part.x = part_config['x']
        new_part.y = part_config['y']

        return new_part
