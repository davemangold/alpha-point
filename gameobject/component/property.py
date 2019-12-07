import error


# Base Property class

class Property(object):
    """Level property that is used by other game objects."""

    def __init__(self, system, *args, **kwargs):
        self.system = system
        self.config_id = None
        self.name = 'property'
        self.description = 'property'
        self.min_value = 0
        self.max_value = 0
        self.increment = 1
        self._value = 0
        self.__add_to_system()

    def __str__(self):
        """A brief description."""

        return self.description

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
    """Gas pressure."""

    def __init__(self, *args, **kwargs):
        super(Pressure, self).__init__(*args, **kwargs)
        self.name = 'pressure'
        self.description = 'pressure'


# Property factory for making properties

class PropertyFactory(object):
    """Makes specific Property type instances."""

    @staticmethod
    def make_property(system, property_type, *args, **kwargs):

        if property_type.lower() == 'pressure':
            return Pressure(system, *args, **kwargs)

        raise error.FactoryError("The specified property type does not exist.")
