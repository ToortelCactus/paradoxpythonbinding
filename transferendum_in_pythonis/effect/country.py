from transferendum_in_pythonis.common import *
from .effects import Effect


from transferendum_in_pythonis.parsing.generated.dip_play import Dip_play
from transferendum_in_pythonis.parsing.generated.dip_action import Dip_action
from transferendum_in_pythonis.parsing.generated.state_region import State_region
from transferendum_in_pythonis.parsing.generated.country import Country
from transferendum_in_pythonis.parsing.generated.law import Law


class Level(Enum):
    very_low = 1
    low = 2
    medium = 3
    high = 4
    very_high = 5


class CountryEffect(Effect):
    """ Wrapper around effect functions """
    def __init__(self, content: str):
        super().__init__(content)


def default(arg1, arg2):
    return CountryEffect(de(arg1, arg2))


class CE:
    @staticmethod
    def activate_law(law: Law):
        """

        Activates a law for a country
        **Supported Scopes**: country
        **Supported Targets**: law_type
        """
        return default("activate_law", law.name)

    @staticmethod
    def activate_production_method(arg):
        """

        Activates the named production method for buildings of a certain type in country/state
        **Supported Scopes**: country, state
        """
        return default("activate_production_method", arg)

    @staticmethod
    def add_banned_goods(good: Market_goods):
        """

        Adds a total ban of a good to a country
        add_banned_goods = <goods key/scope>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default("add_banned_goods", good)

    @staticmethod
    def add_change_relations_progress(target, value):
        """

        Add progress towards changing relations between two countries
        add_change_relations_progress = {
            tcountry = country scope/tag
            value = amount
        }
        **Supported Scopes**: country
        """
        return default("add_change_relations_progress", br(eq("tcountry", target) + eq("value", value)))

    @staticmethod
    def add_company(arg):
        """

        Adds company type to a country's companies
        add_company = company_type:key
        **Supported Scopes**: country
        **Supported Targets**: company_type
        """
        return default("add_company", arg)

    @staticmethod
    def add_declared_interest(arg):
        """

        Will create a declared interest in the target strategic region
        c:FRA = { add_declared_interest = region_nile_basin }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_enactment_modifier(arg):
        """

        Adds an enactment-related timed modifier effect to object in scope
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_enactment_phase(arg):
        """

        Changes the current law enactment phase in scope country by an added amount. The result will be clamped between 0 and NPolitics::LAW_ENACTMENT_MAX_PHASES. The enacting law will pass if the resulting value equals NPolitics::LAW_ENACTMENT_MAX_PHASES.
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_enactment_setback(arg):
        """

        Changes the current law enactment setback count in scope country by an added amount. The result will be clamped between 0 and NPolitics::LAW_ENACTMENT_MAX_SETBACKS. The law enactment will fail if the resulting value equals NPolitics::LAW_ENACTMENT_MAX_SETBACKS.
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_era_researched(arg):
        """

        Add specified era as researched in a country scope
        add_era_researched = era
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_investment_pool(arg):
        """

        Directly adds money to the investment pool
        add_investment_pool = 50
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_law_progress(arg):
        """

        Adds x% progress to the current checkpoint of the law being passed (range is [0, 1], 0.1 means 10 percentage points)
        add_law_progress = 0.1 / -0.1
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_loyalists(value, ig, pop_type, strata, culture, religion):
        """

        Adds loyalists to pops in scope country, all parameters except value are optional,
        if interest_group is specified pops gain loyalists based on their ig membership,
        pop type and strata cannot be used at the same time
        add_radicals = {
            value = x
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
        }
        **Supported Scopes**: country
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
    def add_primary_culture(arg):
        """

        Adds a culture to the primary cultures of a country
        add_primary_culture = X
        Where X is a culture scope
        **Supported Scopes**: country
        **Supported Targets**: culture
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_radicals(value, ig, pop_type, strata, culture, religion):
        """

        Adds radicals to pops in scope country, all parameters except value are optional,
        if interest_group is specified pops gain radicals based on their ig membership,
        pop type and strata cannot be used at the same time
        add_radicals = {
            value = x
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eqn("value", value) +
                                                 eqn("interest_group", ig) +
                                                 eqn("pop_type", pop_type) +
                                                 eqn("strata", strata) +
                                                 eqn("culture", culture) +
                                                 eq("religion", religion)))

    @staticmethod
    def add_taxed_goods(good: Market_goods):
        """

        Adds consumption taxes on a good to a country
        add_taxed_goods = <goods key/scope>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def add_technology_progress(arg):
        """

        Add technology progress
        add_technology_progress = { progress = X technology = Y }
        Where X is a fixed point and Y is an technology
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_technology_researched(arg):
        """

        Research the specified technology in a country scope
        add_technology_researched = technology
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def add_treasury(arg):
        """

        Add/remove money from a country
        add_treasury = fixed point
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def annex(arg):
        """

        Annexes a country
        annex = scope
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def annex_as_civil_war(arg):
        """

        Annexes a country with all the inheritance effects of a victorious side in a civil war
        annex_as_civil_war = scope
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def annex_with_incorporation(arg):
        """

        Annexes a country, inheriting incorporation of their states
        annex_with_incorporation = scope
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def call_election(months: int):
        """

        Sets the next election date for country in N months
        call_election = {
            months = 6
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("months", str(months))))

    @staticmethod
    def cancel_enactment(arg):
        """

        Stops enacting the country's currently enacting law
        cancel_enactment = yes
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def change_infamy(arg):
        """

        Change infamy of scope country
        change_infamy = amount
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def change_institution_investment_level(institution, investment):
        """

        Add/remove the investment level for the institution
        change_institution_investment_level = {
            institution = institution_police
            investment = -1
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eqn("institution", institution) +
                                                 eq("investment", investment)))

    @staticmethod
    def change_relations(target, value):
        """

        Change relations between two countries
        change_relations = {
            tcountry = country scope/tag
            value = amount
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("value", value)))

    @staticmethod
    def change_subject_type(arg):
        """

        Will change the subject type of the country that is the current scope.
        change_subject_type = subject_type_dominion
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def change_tag(tag: Country):
        """

        Change the tag for the scoped country
        c:GBR = { change_tag = FRA }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], tag.name)

    @staticmethod
    def change_tension(target, value):
        """

        Change tension between two countries
        change_tension = {
            tcountry = country scope/tag
            value = amount
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("value", value)))

    @staticmethod
    def clear_debt(arg):
        """

        Clear country loans = bool
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def clear_enactment_modifier(arg):
        """

        Clears the current law enactment modifier of scope country.
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def clear_scaled_debt(arg):
        """

        Clears an amount of debt equal to the defined multiplier on target's max credit(arg):

        clear_scaled_debt = value
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def complete_objective_subgoal(arg):
        """

        Completes an objective subgoal
        complete_objective_subgoal = <key>
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def copy_laws(arg):
        """

        Copies the constitution of the target country scope
        Warning: This stops any current enactment.
        copy_laws = scope
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def create_diplomatic_pact(country, first_state, second_state, type: Dip_action):
        """

        Create a diplomatic pact between two countries, with scope country as initiator
        create_diplomatic_pact = {
            country = country scope/tag
            first_state = state scope/tag
            second_state = state scope/tag
            type = diplomatic action type
        }
        **Supported Scopes**: country
        """
        return default_list(inspect.stack()[0][3], [eq("country", country),
                                                    eq("first_state", first_state),
                                                    eq("second_state", second_state),
                                                    eq("type", type.name)])

    @staticmethod
    def create_diplomatic_play(name,
                               escalation,
                               initiator,
                               type: Dip_play,
                               war: bool = False,
                               civil_war: bool = False,
                               initiator_backers: List[str] = [],
                               target_backers: List[str] = [],
                               wargoal="USE THE FUNCTION"):  # TODO find a better solution
        """

        Create a diplomatic play with the scoped object as target
        create_diplomatic_play = {
            name = loc_key
            escalation = integer between 0 and 100
            war = bool
            initiator = country scope/tag
            type = diplomatic play type
            handle_annexation_as_civil_war = yes/no
            add_initiator_backers = { list of country scopes/tags }
            add_target_backers = { list of country scopes/tags }
            add_war_goal = { holder = country scope/tag, type = x, state = <state target>, country = <country target,> region = <region target>  }
        }
        **Supported Scopes**: country
        """
        return default_list(inspect.stack()[0][3],
                            [
                                eq("name", name),
                                eq("escalation", escalation),
                                eq("war", str(war).lower()),
                                eq("initiator", initiator),
                                eq("type", type.name),
                                eq("handle_annexation_as_civil_war", str(civil_war).lower()),
                                default_list("add_initiator_backers", initiator_backers),
                                default_list("add_target_backers", target_backers),
                                wargoal
                            ])

    @staticmethod
    def create_incident(target, value):
        """

        Creates a diplomatic incident that generates infamy, with target country as the victim
        create_incident = {
            tcountry = country scope/tag
            value = infamy amount
        }
        **Supported Scopes**: country
        """
        return default_list(inspect.stack()[0][3],
                            [
                                eq("tcountry", target),
                                eq("value", value)
                            ])

    @staticmethod
    def create_military_formation(arg):
        """

        Creates a military formation
        create_military_formation = {
            # Optional name
            name = "name"
            # type defaults to army(arg):

            type = army/fleet
            hq_region = sr:region_russia
            # Add as many combat_unit specifications as necessary
            combat_unit = {
                type = unit_type:combat_unit_type_irregular_infantry
                # service_type defaults to regular and conscript is not applicable for fleets(arg):

                service_type = regular/conscript
                state_region = s:STATE_MOSCOW
                count = 5
            }
            # mobilization_options are not applicable for fleets
            mobilization_options = {
                mobilization_option:mobilization_option_basic_supplies
                mobilization_option:mobilization_option_truck_transport
            }
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def create_import_route(goods: Market_goods, level: Level, origin: State_region, target: State_region):
        """

        Creates a new Trade Route
        trade_route = {
            goods = x
            level = x
            import = yes
            origin = state_region
            target = state_region
        }
        **Supported Scopes**: country
        """
        return default_list("trade_route",
                            [
                                eq("goods", goods.name),
                                eq("level", level.name),
                                eq("import", "yes"),
                                eq("origin", str(origin)),
                                eq("target", str(target))
                            ])

    @staticmethod
    def create_export_route(goods: Market_goods, level: Level, origin: State_region, target: State_region):
        """

        Creates a new Trade Route
        trade_route = {
            goods = x
            level = x
            import = no
            origin = state_region
            target = state_region
        }
        **Supported Scopes**: country
        """
        return default_list("trade_route",
                            [
                                eq("goods", goods.name),
                                eq("level", level.name),
                                eq("import", "no"),
                                eq("origin", str(origin)),
                                eq("target", str(target))
                            ])

    @staticmethod
    def create_truce(target: Country, months):
        """

        Create a truce betweeen two countries
        create_truce = {
            tcountry = country scope/tag
            months = integer
        }
        **Supported Scopes**: country
        """
        return default_list(inspect.stack()[0][3],
                            [
                                eq("tcountry", str(target)),
                                eq("months", months)
                            ])

    @staticmethod
    def deactivate_law(law: Law):
        """
        Deactivates a law for a country
        **Supported Scopes**: country
        **Supported Targets**: law_type
        """
        return default(inspect.stack()[0][3], law.name)

    @staticmethod
    def deactivate_parties(arg):
        """

        Deactivates parties in scoped country.
        deactivate_parties = yes
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def end_truce(arg):
        """

        Ends a truce betweeen two countries
        end_truce = {
            tcountry = country scope/tag
            months = integer
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def every_active_party(triggers, effects):
        """

        Iterate through all active political parties in a country
        every_active_party = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: party
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_civil_war(triggers, effects):
        """

        Iterate through all civil wars related to the scoped country
        every_civil_war = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: civil_war
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_cobelligerent_in_diplo_play(triggers, effects):
        """

        Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
        every_cobelligerent_in_diplo_play = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_cobelligerent_in_war(triggers, effects):
        """

        Iterate through all co-belligerents of scope country in all wars
        every_cobelligerent_in_war = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_company(triggers, effects):
        """

        Iterate through all companies in a country
        every_company = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: company
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_enemy_in_diplo_play(triggers, effects):
        """

        Iterate through all enemies of scope country in all diplomatic plays (includes wars)
        every_enemy_in_diplo_play = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_enemy_in_war(triggers, effects):
        """

        Iterate through all enemies of scope country in all wars
        every_enemy_in_war = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_in_hierarchy(triggers, effects):
        """

        Any country in current hierarchy, including current
        every_in_hierarchy = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_interest_group(triggers, effects):
        """

        Iterate through all interest groups in a country
        every_interest_group = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: interest_group
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_law(triggers, effects):
        """

        Iterate through all laws in a country
        every_law = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: law
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_military_formation(triggers, effects):
        """

        Iterate through all military formations currently present at input scope
        Supported scopes: country, front, hq
        every_military_formation = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, hq
        **Supported Targets**: military_formation
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

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
    def every_overlord_or_above(triggers, effects):
        """

        Any country above current in hierarchy
        every_overlord_or_above = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_political_movement(triggers, effects):
        """

        Iterate through all political movements in a country
        every_political_movement = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: political_movement
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_potential_party(triggers, effects):
        """

        Iterate through all potential political parties in a country
        every_potential_party = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: party
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_primary_culture(triggers, effects):
        """

        Primary cultures of the scoped country or country definition(arg):

        every_primary_culture = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, country_definition, state(arg):

        **Supported Targets**: culture
        """
        return default(inspect.stack()[0][3], iterator(triggers, effects))

    @staticmethod
    def every_rival_country(triggers, effects):
        """

        Any country that is rival to the country in a scope
        every_rival_country = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default("every_rival_country", iterator(triggers, effects))

    @staticmethod
    def every_scope_admiral(triggers, effects):
        """

        Iterate through all admirals in a: country, interestgroup, or military formation
        every_scope_admiral = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, interest_group, military_formation
        **Supported Targets**: character
        """
        return default("every_scope_admiral", iterator(triggers, effects))

    @staticmethod
    def every_scope_ally(triggers, effects):
        """

        Iterate through all allies to a: country
        every_scope_ally = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default("every_scope_ally", iterator(triggers, effects))

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
    def every_scope_character(triggers, effects):
        """

        Iterate through all characters in a: country, interestgroup, or front
        every_scope_character = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, interest_group, military_formation
        **Supported Targets**: character
        """
        return default("every_scope_character", iterator(triggers, effects))

    @staticmethod
    def every_scope_culture(triggers, effects):
        """

        Iterate through all cultures in the scope
        every_scope_culture = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, state
        **Supported Targets**: culture
        """
        return default("every_scope_culture", iterator(triggers, effects))

    @staticmethod
    def every_scope_diplomatic_pact(triggers, effects):
        """

        Any diplomatic pact of the country in a scope
        every_scope_diplomatic_pact = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: diplomatic_pact
        """
        return default("every_scope_diplomatic_pact", iterator(triggers, effects))

    @staticmethod
    def every_scope_general(triggers, effects):
        """

        Iterate through all generals in a: country, interestgroup, front, or military formation
        every_scope_general = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, interest_group, military_formation
        **Supported Targets**: character
        """
        return default("every_scope_general", iterator(triggers, effects))

    @staticmethod
    def every_scope_held_interest_marker(triggers, effects):
        """

        Iterate through all interest markers held by a country
        every_scope_held_interest_marker = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: interest_marker
        """
        return default("every_scope_held_interest_marker", iterator(triggers, effects))

    @staticmethod
    def every_scope_interest_marker(triggers, effects):
        """

        Iterate through all interest markers in a: country, strategic region
        every_scope_interest_marker = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, strategic_region
        **Supported Targets**: interest_marker
        """
        return default("every_scope_interest_marker", iterator(triggers, effects))

    @staticmethod
    def every_scope_politician(triggers, effects):
        """

        Iterate through all politicians in a: country or interestgroup
        every_scope_politician = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, interest_group, military_formation
        **Supported Targets**: character
        """
        return default("every_scope_politician", iterator(triggers, effects))

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
    def every_scope_state(triggers, effects):
        """

        Iterate through all states including provinces from a: country, state_region, theater, or front
        every_scope_state = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, front, state_region, strategic_region, theater
        **Supported Targets**: state
        """
        return default("every_scope_state", iterator(triggers, effects))

    @staticmethod
    def every_scope_theater(triggers, effects):
        """

        Iterate through all theaters in a: country
        every_scope_theater = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: theater
        """
        return default("every_scope_theater", iterator(triggers, effects))

    @staticmethod
    def every_scope_violate_sovereignty_interested_parties(triggers, effects):
        """

        Iterate through all countries that would be interested if country in scope has their sovereignty violated
        every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default("every_scope_violate_sovereignty_interested_parties", iterator(triggers, effects))

    @staticmethod
    def every_scope_violate_sovereignty_wars(triggers, effects):
        """

        Iterate through all relevant wars if target country had their sovereignty violated by scoped country
        every_scope_violate_sovereignty_wars = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: war
        """
        return default("every_scope_violate_sovereignty_wars", iterator(triggers, effects))

    @staticmethod
    def every_scope_war(triggers, effects):
        """

        Iterate through all wars related to the scope
        every_scope_war = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: war
        """
        return default("every_scope_war", iterator(triggers, effects))

    @staticmethod
    def every_strategic_objective(triggers, effects):
        """

        Iterate through all Strategic Objective states from the scoped Country
        every_strategic_objective = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: state
        """
        return default("every_strategic_objective", iterator(triggers, effects))

    @staticmethod
    def every_subject_or_below(triggers, effects):
        """

        Any country below current in hierarchy
        every_subject_or_below = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default("every_subject_or_below", iterator(triggers, effects))

    @staticmethod
    def every_trade_route(triggers, effects):
        """

        Iterate through all trade routes in a: market, country, marketgoods
        every_trade_route = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country, market, market_goods
        **Supported Targets**: trade_route
        """
        return default("every_trade_route", iterator(triggers, effects))

    @staticmethod
    def every_valid_mass_migration_culture(triggers, effects):
        """

        Lists for cultures in the scoped country that are valid for mass migration
        every_valid_mass_migration_culture = { limit = { <triggers> } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: culture
        """
        return default("every_valid_mass_migration_culture", iterator(triggers, effects))

    @staticmethod
    def kill_population(arg):
        """

        Kills a number of individuals in the population in the scoped country.

        All parameters except percent are optional. Pop type and strata cannot be used at the same time.
        kill_population = {
            value = <integer value>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def kill_population_percent(arg):
        """

        Kills a percentage of the population in the scoped country.

        All parameters except percent are optional. Pop type and strata cannot be used at the same time.
        kill_population_percent = {
            percent = <decimal value>
            culture = <scope/cu:key>
            religion = <scope/rel:key>
            interest_group = <scope/ig:key>
            pop_type = <scope/pop_type:key>
            strata = <key>
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def make_independent(arg):
        """

        Makes a country independent.
        make_independent = bool
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def play_as(arg):
        """

        Change which country scoped country's player will play as
        play_as = <scope>
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def random_active_party(triggers, effects, mtth=""):
        """

        Iterate through all active political parties in a country
        random_active_party = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
        **Supported Scopes**: country
        **Supported Targets**: party
        """
        return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))

    @staticmethod
    def recalculate_pop_ig_support(arg):
        """

        Recalculates and updates a country's pop IG memberships = bool
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)


    @staticmethod
    def remove_active_objective_subgoal(arg):
        """

        Removes an active objective subgoal
        remove_active_objective_subgoal = <key>
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_banned_goods(good: Market_goods):
        """

        Removes a total ban of a good from a country
        remove_banned_goods = <goods key/scope>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def remove_company(arg):
        """

        Removes company type from a country's companies
        remove_company = company_type:key
        **Supported Scopes**: country
        **Supported Targets**: company_type
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_diplomatic_pact(arg):
        """

        Removes a diplomatic pact between two countries, with scope country as initiator
        remove_diplomatic_pact = {
            country = country scope/tag
            type = diplomatic action type
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_enactment_modifier(arg):
        """

        Removes an enactment-related timed modifier effect to object in scope
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_modifier(arg):
        """

        Removes a timed modifier effect to object in scope
        **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_primary_culture(arg):
        """

        Removes a culture from the primary cultures of a country
        remove_primary_culture = X
        Where X is a culture scope
        **Supported Scopes**: country
        **Supported Targets**: culture
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def remove_taxed_goods(good: Market_goods):
        """

        Removes consumption taxes on a good from a country
        remove_taxed_goods = <goods key/scope>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def set_capital(arg):
        """

        Set capital state in a country scope
        set_capital = X
        Where X is a state region
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_country_type(arg):
        """

        Sets the type of country for a country, for history
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_diplomats_expelled(arg):
        """

        Set diplomats expelled = bool
        **Supported Scopes**: country
        **Supported Targets**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_government_wage_level(level: Level):
        """

        Sets the government wage level of scoped country
        set_government_wage_level = very_low/low/medium/high/very_high
        **Supported Scopes**: country
        """
        assert isinstance(level, Level)
        return default(inspect.stack()[0][3], level.name)

    @staticmethod
    def set_immune_to_revolutions(arg):
        """

        Makes a country immune to revolutions or removes such immunity.
        set_immune_to_revolutions = yes/no
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_institution_investment_level(institution, level):
        """

        Sets the investment level for an institution
        set_institution_investment_level = { institution = <key> level = x }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("institution", institution) + eq("level", level)))

    @staticmethod
    def set_market_capital(arg):
        """

        Set market capital in a country scope
        set_market_capital = X
        Where X is a state region
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_military_wage_level(level: Level):
        """

        Sets the military wage level of scoped country
        set_military_wage_level = very_low/low/medium/high/very_high
        **Supported Scopes**: country
        """
        assert isinstance(level, Level)
        return default(inspect.stack()[0][3], level.name)

    @staticmethod
    def set_mutual_secret_goal(target, goal):
        """

        Set mutual secret AI goal for scope country and target country
        set_mutual_secret_goal = {
            tcountry = country scope/tag
            secret_goal = secret goal type
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("secret_goal", goal)))

    @staticmethod
    def set_next_election_date(arg):
        """

        Set next election date for country
        set_next_election_date = year.month.day
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_owes_obligation_to(country, setting):
        """

        Set whether a country owes another a obligation
        set_owes_obligation = {
            country = country scope/tag
            setting = yes/no
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("country", country) + eq("setting", setting)))

    @staticmethod
    def set_relations(target, value):
        """

        Set relations between two countries
        set_relations = {
            tcountry = country scope/tag
            value = amount
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("value", value)))

    @staticmethod
    def set_ruling_interest_groups(arg):
        """

        Creates a government for the country in scope from a set of interest groups
        set_ruling_interest_groups = { ig_tag1 ig_tag2 }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_secret_goal(target, goal):
        """

        Set a secret AI goal for scope country towards another country
        set_secret_goal = {
            tcountry = country scope/tag
            secret_goal = secret goal type
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("secret_goal", goal)))

    @staticmethod
    def set_state_religion(arg):
        """

        Changes the state religion of the country to the specified religion
        set_state_religion = X
        Where X is a religion scope
        **Supported Scopes**: country
        **Supported Targets**: religion
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_strategy(arg):
        """

        Set AI strategy for scope country
        set_strategy = <key>
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def set_tariffs_export_priority(good: Market_goods):
        """

        Sets Export Prioritized tariffs for a good in scoped country
        set_tariffs_export_priority = <scope/key>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def set_tariffs_import_priority(good: Market_goods):
        """

        Sets Import Prioritized tariffs for a good in scoped country
        set_tariffs_import_priority = <scope/key>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def set_tariffs_no_priority(good: Market_goods):
        """

        Sets tariffs to have no import/export priority for a good in scoped country
        set_tariffs_no_priority = <scope/key>
        **Supported Scopes**: country
        **Supported Targets**: goods
        """
        return default(inspect.stack()[0][3], good)

    @staticmethod
    def set_tax_level(level: Level):
        """

        Sets the overall tax level of scoped country
        set_tax_level = very_low/low/medium/high/very_high
        **Supported Scopes**: country
        """
        assert isinstance(level, Level)
        return default(inspect.stack()[0][3], level.name)

    @staticmethod
    def set_tension(target, value):
        """

        Set tension between two countries
        set_tension = {
            tcountry = country scope/tag
            value = amount
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("tcountry", target) + eq("value", value)))

    @staticmethod
    def start_enactment(law: Law):
        """

        Starts enacting the specified law type for the country in scope
        start_enactment = law_type:law_multicultural
        **Supported Scopes**: country
        **Supported Targets**: law_type
        """
        return default(inspect.stack()[0][3], law.name)

    @staticmethod
    def start_research_random_technology(arg):
        """

        Scoped country starts research of any random technology they can
        start_research_random_technology = yes
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def take_on_scaled_debt(who, value):
        """

        Transfers an amount of debt equal to the defined multiplier on target's max credit(arg):

        take_on_scaled_debt = {
            who = <country>
            value = decimal value
        }
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], br(eq("who", who) + eq("value", value)))

    @staticmethod
    def update_party_support(arg):
        """

        Updates party support in scoped country.
        update_party_support = yes
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def validate_subsidies(arg):
        """

        Validates subsidies across a country's buildings.
        validate_subsidies = bool
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def violate_sovereignty_join(arg):
        """

        Target joins scoped war
        violate_sovereignty_accept = <country>
        **Supported Scopes**: country
        """
        return default(inspect.stack()[0][3], arg)
