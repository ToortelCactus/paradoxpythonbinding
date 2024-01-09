from common import *
from effects import Effect


class RegionEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2):
    return RegionEffect(de(arg1, arg2))


class RE:
    @staticmethod
    def add_arable_land(arg):
        """

        Add/remove arable land from a state region
        **Supported Scopes**: state_region
        """
        return default("add_arable_land", arg)

    @staticmethod
    def add_claim(country):
        """

        Adds scoped state region as a claim for target country
        add_claim = scope/country
        **Supported Scopes**: state_region
        **Supported Targets**: country
        """
        return default("add_claim", country)

    @staticmethod
    def add_devastation(arg):
        """

        Add/remove devastation from a state region
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_homeland(arg):
        """

        Adds scoped state region as Homeland for target culture
         add_homeland = cu:culture
        **Supported Scopes**: state_region
        **Supported Targets**: culture
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_pollution(arg):
        """

        Increase/decrease pollution level in a scoped state region
        add_pollution = 10
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_state_trait(arg):
        """

        add state trait in a scoped state region
        add_state_trait = <state_trait_name>
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def create_state(arg):
        """

        creates a state in a state region
        **Supported Scopes**: state_region
        """
        return default("create_state", arg)

    @staticmethod
    def remove_claim(arg):
        """

        Removes scoped state region as a claim for target country
        add_claim = scope/country
        **Supported Scopes**: state_region
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_homeland(arg):
        """

        Removes scoped state region as Homeland for target culture
        remove_homeland = cu:culture
        **Supported Scopes**: state_region
        **Supported Targets**: culture
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_state_trait(arg):
        """

        remove state trait in a scoped state region
        remove_state_trait = <state_trait_name>
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_devastation(arg):
        """

        Set devastation to a state region
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_owner_of_provinces(country, provinces):
        """

        Gives a set of provinces in a state region to a specific country
        set_owner_of_provinces = { country = <scope> provinces = {} }
        **Supported Scopes**: state_region
        """
        return default(inspect.stack()[0][3], br(eq("country", country) + eq("provinces", provinces)))
