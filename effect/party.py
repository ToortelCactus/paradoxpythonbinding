from common import *

from effects import IGS


class PartyEffect:
    """ Wrapper around effect functions """

    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return self.content


def default(arg1, arg2):
    return PartyEffect(de(arg1, arg2))


class PE:
    @staticmethod
    def add_momentum(arg):
        """

        Adds momentum to a Party during a campaign perioddd_momentum = value
        **Supported Scopes**: party
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def disband_party():
        """

        Removes all interest groups from the party, causing it to disband
        disband_party = yes
        **Supported Scopes**: party
        """
        return default(inspect.stack()[0][3], "yes")

    @staticmethod
    def every_member(triggers, effects):
        """

        Iterate through all interest group members of a party
        every_member = { limit = { <triggers> } <effects> }
        **Supported Scopes**: party
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def ordered_member(arg):
        """

        Iterate through all interest group members of a party
        ordered_member = {
        limit = { <triggers> }
        order_by = script_value
        position = int
        min = int
        max = script_value
        check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
        <effects> }
        **Supported Scopes**: party
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def random_member(triggers, effects, mtth=""):
        """

        Iterate through all interest group members of a party
        random_member = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
        **Supported Scopes**: party
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))

    @staticmethod
    def remove_ig_from_party(ig: IGS):
        """

        Removes target interest group from scope party
        py:py_key = {
            remove_ig_from_party = ig:ig_key
        }
        **Supported Scopes**: party
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], str(ig))

    @staticmethod
    def set_ruling_party():
        """

        Adds all interest groups in a party to government and removes all other interest groups from the government
        set_ruling_party = yes
        **Supported Scopes**: party
        """
        return default(inspect.stack()[0][3], "yes")


