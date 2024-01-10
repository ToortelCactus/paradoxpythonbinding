from transferendum_in_pythonis.common import *
from .effects import Effect, E

from transferendum_in_pythonis.parsing.generated.building import Building


class StateType(Enum):
    incorporated = 1
    unincorporated = 2
    treaty_port = 3


class StateEffect(Effect):
    """ Wrapper around effect functions """


def default(arg1, arg2): # TODO: put inside SE and others?
    return StateEffect(de(arg1, arg2))


class SE(E):
    @staticmethod
    def activate_building(building: Building):
        """

        Activate a building in a state
        activate_building = { building = building_key }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], br(eq("building", building.name)))

    @staticmethod
    def activate_production_method(arg):
        """

        Activates the named production method for buildings of a certain type in country/state
        **Supported Scopes**: country, state
        """
        return default("activate_production_method", arg)

    @staticmethod
    def add_culture_standard_of_living_modifier(arg):
        """

        Apply a standard of living modifier in the scoped state for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier.
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_loyalists_in_state(value, ig, pop_type, strata, culture, religion):
        """

        Adds loyalists to pops in scope state, all parameters except value are optional,
        if interest_group is specified pops gain loyalists based on their ig membership,
        pop type and strata cannot be used at the same time
        add_radicals_in_state = {
            value = x
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
        }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], br(eqn("value", value) +
                                                 eqn("interest_group", ig) +
                                                 eqn("pop_type", pop_type) +
                                                 eqn("strata", strata) +
                                                 eqn("culture", culture) +
                                                 eq("religion", religion)))

    @staticmethod
    def add_modifier(arg):
        """

        Adds a timed modifier effect to object in scope
        **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_radicals_in_state(value, ig, pop_type, strata, culture, religion):
        """

        Adds radicals to pops in scope state, all parameters except value are optional,
        if interest_group is specified pops gain radicals based on their ig membership,
        pop type and strata cannot be used at the same time
        add_radicals_in_state = {
            value = x
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
        }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], br(eqn("value", value) +
                                                 eqn("interest_group", ig) +
                                                 eqn("pop_type", pop_type) +
                                                 eqn("strata", strata) +
                                                 eqn("culture", culture) +
                                                 eq("religion", religion)))

    @staticmethod
    def add_religion_standard_of_living_modifier(arg):
        """

        Apply a standard of living modifier in the scoped state for the given religion. Other than the required religion argument, this effect has the same syntax as add_modifier.
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def convert_population(target, value):
        """

        Changes X% of the different religion population to the specified religion.
        convert_population = { target = rel:catholic value = 0.5 }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], br(eq("target", target) + eq("value", value)))

    @staticmethod
    def create_building(arg):
        """

        Creates a building in the scoped state. Supported values are:
            building = <building>
            activate_production_methods = { <production_methods> }
            subsidized = yes/no
            reserves = [0..1] (percentage of cash reserves the building should be created with)
            level = arable_land/integer

        If level is "arable_land", the building will be of the necessary level to exhaust all available arable land in the state.
        If level is "urbanization", the building will be of the necessary level to exhaust all available urbanzation in the state.
        If level is an integer, the building will be of that level

        Please note: this effect works a little differently if there already is a building of the specified type in the state. If that happens:
            1. the level will be the maximum between the scripted level and the level of the existing building
            2. the cash reserves will be the maximum between the scripted value and the existing cash reserves
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def create_mass_migration(origin, culture):
        """

        Initiates mass migration of a specific culture from a origin country to a scoped state
        create_mass_migration = {
            origin = c:GBR
            culture = cu:english
        }
        **Supported Scopes**: state
        """
        return default_list(inspect.stack()[0][3],
                            [
                                eq("origin", origin),
                                eq("culture", culture)
                            ])

    @staticmethod
    def create_pop(arg):
        """

        Creates a pop in the scoped state
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def deactivate_building(arg):
        """

        # Deactivate a building in a state
        deactivate_building = { building = building_key }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def every_neighbouring_state(triggers, effects):
        """

        Iterate through all states neighbouring a state region
        every_neighbouring_state = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, state, state_region, strategic_region
        **Supported Targets**: state
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_scope_building(triggers, effects):
        """

        Iterate through all buildings in a: state, country
        every_scope_building = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, state
        **Supported Targets**: building
        """
        return default("every_scope_building", iterator(triggers, effects))

    @staticmethod
    def force_resource_depletion(arg):
        """

        Forces a resource depletion in state
        force_resource_depletion = bg_gold_mining
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def force_resource_discovery(arg):
        """

        Forces a resource discovery in state
        force_resource_discovery = bg_gold_mining
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def kill_population_in_state(arg):
        """

        Kills a number of individuals in the population in the scoped state.

        All parameters except percent are optional. Pop type and strata cannot be used at the same time.
        kill_population = {
            value = <integer value>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
        }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def kill_population_percent_in_state(arg):
        """

        Kills a percentage of the population in the scoped state.

        All parameters except percent are optional. Pop type and strata cannot be used at the same time.
        kill_population_percent = {
            percent = <decimal value>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
        }
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_building(arg):
        """

        Remove a building in the scope state
        remove_building = building_key
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_available_for_autonomous_investment(arg):
        """

        Sets a building type as available for autonomous investment in the current scoped State
        set_available_for_autonomous_investment = building type scope
        **Supported Scopes**: state
        **Supported Targets**: building_type
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_state_owner(arg):
        """

        Set State Owner
        set_state_owner = scope
        **Supported Scopes**: state
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_state_type(type: StateType):
        """

        Sets a state to a certain type (incorporated, unincorporated, treaty_port)
        **Supported Scopes**: state
        """
        assert isinstance(type, StateType)
        return default(inspect.stack()[0][3], type.name)

    @staticmethod
    def start_building_construction(arg):
        """

        Start constructing a building in a scoped state as a government construction
        start_building_construction = building_barracks
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def start_privately_funded_building_construction(arg):
        """

        Start constructing a building in a scoped state as a private construction
        start_privately_funded_building_construction = building_barracks
        **Supported Scopes**: state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def unset_available_for_autonomous_investment(arg):
        """

        Sets a building type as unavailable for autonomous investment in the current scoped State
        unset_available_for_autonomous_investment = building type scope
        **Supported Scopes**: state
        **Supported Targets**: building_type
        """
        return default(inspect.stack()[0][3], arg)
