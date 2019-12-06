# TODO: add a property class to use with sensors
class Property(object):
    """Level property that is used by other game objects."""

    def __init__(self, min_value, max_value, value, increment=1):
        self._min_value = min_value
        self._max_value = max_value
        self._increment = increment
        self.value = value

    @property
    def min_value(self):
        return self._min_value

    @property
    def max_value(self):
        return self._max_value

    @property
    def increment(self):
        return self._increment

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
