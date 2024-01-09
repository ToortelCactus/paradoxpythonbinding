from common import *
from effect.effects import Effect


class IGEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2):
    return IGEffect(de(arg1, arg2))


class IGE:
    @staticmethod
    def abandon_revolution():
        """
        Removes interest group from revolution
        abandon_revolution = yes
        **Supported Scopes**: interest_group
        """
        return default("abandon_revolution", "yes")

    @staticmethod
    def add_ideology(arg):
        """

        Adds an ideology to scoped interest group
        add_ideology = x
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_ig_to_party(arg):
        """

        Adds target interest group to scope party
        py:py_key = {
            add_ig_to_party = ig:ig_key
        }
        **Supported Scopes**: party
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_ruling_interest_group():
        """

        Adds interest group to government
        add_ruling_interest_group = yes
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], "yes")

    @staticmethod
    def remove_ruling_interest_group():
        """

        Removes interest group in scope from government
        remove_ruling_interest_group = yes
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], "yes")

    @staticmethod
    def every_preferred_law(triggers, effects):
        """

        Iterate through all active and possible laws in an interest group's country,
        ordered by how much they prefer that law
        every_preferred_law = { limit = { <triggers> } <effects> }
        **Supported Scopes**: interest_group
        **Supported Targets**: law
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def join_revolution():
        """

        Adds interest group to ongoing revolution
        join_revolution = yes
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], "yes")

    @staticmethod
    def remove_ideology(arg):
        """

        Removes an ideology from scoped interest group
        remove_ideology = x
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_ig_bolstering(arg):
        """

        Starts/stops bolstering the interest group in scope
        set_ig_bolstering = yes/no
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_ig_suppression(arg):
        """

        Starts/stops suppressing the interest group in scope
        set_ig_suppression = yes/no
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_ig_trait(arg):
        """

        Adds a trait to the Interest Group, or replaces their current trait with the same approval level
        set_ig_trait = ig_trait:ig_trait_engines_of_progress
        **Supported Scopes**: interest_group
        **Supported Targets**: interest_group_trait
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_interest_group_name(arg):
        """

        Renames interest group to the specified loc key
        set_interest_group_name = x
        **Supported Scopes**: interest_group
        """
        return default(inspect.stack()[0][3], arg)
