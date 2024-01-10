from transferendum_in_pythonis.common import *
from .effects import Effect


class PopEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2):
    return PopEffect(de(arg1, arg2))


class PopE:
    @staticmethod
    def add_pop_wealth(wealth_distribution, update_loyalties):
        """

        Adds the wealth of the pop
        add_pop_wealth = { wealth_distribution = {...} update_loyalties = true/false }
        Where the distribution adding to wealth of the pop
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], br(eqn("wealth_distribution", wealth_distribution) +
                                                 eq("update_loyalties", update_loyalties)))

    @staticmethod
    def change_pop_culture(target, value):
        """

        Changes the culture of the scoped pop to a specified culture by a specified percentage
        change_pop_culture = { target = cu:spanish value = 0.33 }
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], br(eq("target", target) + eq("value", value)))

    @staticmethod
    def change_pop_religion(target, value):
        """

        Changes the religion of the scoped pop to a specified religion by a specified percentage
        change_pop_religion = { target = rel:catholic value = 0.5 }
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], br(eq("target", target) + eq("value", value)))

    @staticmethod
    def change_poptype(arg):
        """

        Changes the type of the pop to the given type
        **Supported Scopes**: pop
        **Supported Targets**: pop_type
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def move_pop(arg):
        """

        Moves the scoped pop to the specified state (they become unemployed)
        move_pop = s:STATE_TUSCANY.region_state:TUS

        NOTE: VERY IMPORTANT! This effect _may_ change the pop type of the moved pop. This will happen under the following conditions:
        1. if the current pop type cannot be unemployed, the new pop type will be the default one(arg):

        2.if the current pop type is a slave type and the target state does not allow slavery, the new pop type will be the default one(arg):

        **Supported Scopes**: pop
        **Supported Targets**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_pop_literacy(literacy_rate):
        """

        Sets the literacy of the pop
        set_pop_literacy = { literacy_rate = {...} }
        Where the ratio is a script value computing the percentage of (workforce) pops that will be literate
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], br(eq("literacy_rate", literacy_rate)))

    @staticmethod
    def set_pop_qualifications(pop_type, qualifications):
        """

        Sets the pop qualifications of the pop for the given type
        set_pop_qualifications = { pop_type = {} qualifications = {...} }
        Where the qualifications is a script value computing the percentage of (workforce) pops that will have the qualifications
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], br(eq("pop_type", pop_type) + eq("qualifications", qualifications)))

    @staticmethod
    def set_pop_wealth(arg):
        """

        Sets the wealth of the pop
        set_pop_wealth = { wealth_distribution = {...} update_loyalties = true/false }
        Where wealth is a script values
        **Supported Scopes**: pop
        """
        return default(inspect.stack()[0][3], arg)
