from transferendum_in_pythonis.common import *
from .effects import Effect


class DipPlayEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2):
    return DipPlayEffect(de(arg1, arg2))


class DPE:
    @staticmethod
    def add_diplomatic_play_war_support(target, value):
        """

        Adds war support to the target country in the scoped diplomatic play.
        The amount will appear under the 'situations' header in tooltips
        add_diplomatic_play_war_support = { target = country value = value }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], br(eq("target", target) + eq("value", value)))

    @staticmethod
    def add_escalation(arg):
        """

        Add escalation to a diplomatic play
        add_escalation = integer
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_initiator_backers(arg):
        """

        Add a tag/scope country to the initiator side of a diplomatic play
        add_initiator_backers = { list of scopes/tags }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_target_backers(arg):
        """

        Add a tag/scope country to the target side of a diplomatic play
        add_target_backers = { list of scopes/tags }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_war_goal(arg):
        """

        Adds a war goal to a DP. Same data read in as add_war_goal in create_diplomatic_play
        random_diplomatic_play = { add_war_goal = { holder = initiator type = secession primary_demand = yes }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def end_play(arg):
        """

        End a diplomatic play
        end_play = bool
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def every_scope_initiator_ally(triggers, effects):
        """

        Iterate through all allies to an initiator in a: diplomatic play
        every_scope_initiator_ally = { limit = { <triggers> } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default("every_scope_initiator_ally", iterator(triggers, effects))

    @staticmethod
    def every_scope_play_involved(triggers, effects):
        """

        Iterate through all involved in a: diplomatic play
        every_scope_play_involved = { limit = { <triggers> } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default("every_scope_play_involved", iterator(triggers, effects))

    @staticmethod
    def every_scope_target_ally(triggers, effects):
        """

        Iterate through all allies to a target in a: diplomatic play
        every_scope_target_ally = { limit = { <triggers> } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default("every_scope_target_ally", iterator(triggers, effects))

    @staticmethod
    def random_scope_initiator_ally(triggers, effects, mtth=""):
        """

        Iterate through all allies to an initiator in a: diplomatic play
        random_scope_initiator_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))

    @staticmethod
    def random_scope_play_involved(triggers, effects, mtth=""):
        """

        Iterate through all involved in a: diplomatic play
        random_scope_play_involved = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))

    @staticmethod
    def random_scope_target_ally(triggers, effects, mtth=""):
        """

        Iterate through all allies to a target in a: diplomatic play
        random_scope_target_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))

    @staticmethod
    def remove_initiator_backers(arg):
        """

        Remove a tag/scope country from the initiator side of a diplomatic play
        remove_initiator_backers = { list of scopes/tags }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_target_backers(arg):
        """

        Remove a tag/scope country to the target side of a diplomatic play
        remove_target_backers = { list of scopes/tags }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_war_goal(who, war_goal):
        """

        Removes a war goal from a DP.
        any_diplomatic_play = { limit = { has_war_goal = return_state }
        remove_war_goal = { who = initiator war_goal = return_state } }
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], br(eq("who", who) + eq("war_goal", war_goal)))


    @staticmethod
    def resolve_play_for(arg):
        """

        effect end diplo play for one side, with it gaining war goals
        resolve_play_for = initiator
        resolve_play_for = scope:custom_scoped_country
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_key(arg):
        """

        Set name to a diplomatic play
        set_key = loc_key
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_war(arg):
        """

        Set a diplomatic play to be a war
        set_war = bool
        **Supported Scopes**: diplomatic_play
        """
        return default(inspect.stack()[0][3], arg)

