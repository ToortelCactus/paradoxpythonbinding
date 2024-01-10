from transferendum_in_pythonis.common import *
from .effects import Effect


class CultureEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2):
    return CultureEffect(de(arg1, arg2))


class CuE:
    @staticmethod
    def add_cultural_obsession(good: Market_goods):
        """

        Adds a new obsession to the culture in scope
        add_cultural_obsession = X
        Where X is a goods
        **Supported Scopes**: culture
        """
        return default("add_cultural_obsession", good)

    @staticmethod
    def remove_cultural_obsession(good: Market_goods):
        """

        Removes a new obsession to the culture in scope
        remove_cultural_obsession = X
        Where X is a goods
        **Supported Scopes**: culture
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def every_scope_pop(triggers, effects):
        """

        Iterate through all pops in a: country, state, interest group, culture
        every_scope_pop = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, culture, interest_group, state
        **Supported Targets**: pop
        """
        return default("every_scope_pop", iterator(triggers, effects))

    @staticmethod
    def ordered_scope_pop(arg):
        """

        Iterate through all pops in a: country, state, interest group, culture
        ordered_scope_pop = {
        limit = { <triggers> }
        order_by = script_value
        position = int
        min = int
        max = script_value
        check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
        <effects> }
        **Supported Scopes**: country, culture, interest_group, state
        **Supported Targets**: pop
        """
        return default(inspect.stack()[0][3], arg)

