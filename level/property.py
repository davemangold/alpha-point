import error
from uuid import uuid4


# Base Property class

class Property(object):
    """System property that is used by other game objects."""

    def __init__(self, system, *args, **kwargs):
        self.system = system
        self.id = str(uuid4()).split('-')[0]
        self.config_id = None
        self.name = 'property'
        self.description = 'property'
        self.min_value = 0
        self.max_value = 0
        self.units = ''
        self.increment = 0
        self.msg_action_verb = 'examine'
        self._value = 0
        self.__add_to_system()

    def __add_to_system(self):
        """Add the property to the parent system."""

        self.system.add_property(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError("Value must be between min_value ({1}) and max_value ({2}).".format(
                    value, self.min_value, self.max_value))
        self._value = value

    def increase(self):
        self.value += self.increment

    def decrease(self):
        self.value -= self.increment


# Property sub-classes that can be affected by devices

class Pressure(Property):
    """Fluid pressure."""

    def __init__(self, *args, **kwargs):
        super(Pressure, self).__init__(*args, **kwargs)
        self.name = 'pressure'
        self.description = 'pressure'


class Voltage(Property):
    """Electrical voltage."""

    def __init__(self, *args, **kwargs):
        super(Voltage, self).__init__(*args, **kwargs)
        self.name = 'voltage'
        self.description = 'voltage'


# Property factory for making properties

class PropertyFactory(object):
    """Makes specific Property type instances."""

    @staticmethod
    def make_property(system, property_type, *args, **kwargs):

        if property_type.lower() == 'pressure':
            return Pressure(system, *args, **kwargs)
        if property_type.lower() == 'voltage':
            return Voltage(system, *args, **kwargs)

        raise error.GameFactoryError("The specified property type does not exist.")
    
    def make_from_config(self, system, property_config):

        new_property = self.make_property(system, property_config['type'])
        new_property.config_id = property_config['id']
        new_property.name = property_config['name']
        new_property.description = property_config['description']
        new_property.min_value = property_config['min_value']
        new_property.max_value = property_config['max_value']
        new_property.units = property_config['units']
        new_property.increment = property_config['increment']
        new_property.value = property_config['value']

        return new_property
