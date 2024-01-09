from helpers import default, iterator, random_iterator, br, eq, eqn, default_list
import inspect
from enum import Enum
from typing import List

from effect.country import CountryEffect
from effect.culture import CultureEffect
from effect.state import StateEffect
from effect.region import RegionEffect
from effect.pop import PopEffect
from effect.ig import IGEffect
from effect.party import PartyEffect
from parsing.generated.country import Country
from parsing.generated.interest_group import Interest_group
from parsing.generated.religion import Religion
from parsing.generated.building import Building
from parsing.generated.culture import Culture
from parsing.generated.party import Party
from parsing.generated.state_region import State_region
from parsing.generated.market_goods import Market_goods


class Level(Enum):
    very_low = 1
    low = 2
    medium = 3
    high = 4
    very_high = 5


class StateType(Enum):
    incorporated = 1
    unincorporated = 2
    treaty_port = 3


class Scope:
    """ Currently unfinished in terms of verification and exhaustiveness """

    def __init__(self, key, item, *effects):
        self.prev = "root"
        if isinstance(key, Enum):
            self.id = key.name
        else:
            self.id = key
        self.item = item
        self.content = ""
        for effect in effects:
            self.content += str(effect) + "\n"

    def __str__(self):
        return eq(self.id + ":" + self.item, br(self.content))

    def type(self):
        return "undef"


class CountryS(Scope):
    def __init__(self, country_tag: Country, *effects: CountryEffect):
        super().__init__("c", country_tag, effects)

    def type(self):
        return "country"


class MarketGoodS(Scope):
    def __init__(self, good: Market_goods, *effects):
        super().__init__("mg", good, effects)

    def type(self):
        return "market_goods"


class StateS(Scope):
    def __init__(self, state_tag, *effects: StateEffect):
        super().__init__("s", state_tag, effects)

    def type(self):
        return "state"


class CultureS(Scope):
    def __init__(self, culture: Culture, *effects: CultureEffect):
        super().__init__("cu", culture, effects)

    def type(self):
        return "culture"


class RegionS(Scope):
    def __init__(self, state_region: State_region, *effects: RegionEffect):
        super().__init__("sr", state_region, effects)

    def type(self):
        return "state_region"


class PopS(Scope):
    def __init__(self, pop, *effects: PopEffect):
        super().__init__("pop", pop, effects)

    def type(self):
        return "pop"


class IGS(Scope):
    def __init__(self, ig: Interest_group, *effects: IGEffect):
        super().__init__("ig", ig, effects)

    def type(self):
        return "interest_group"


class PartyS(Scope):
    def __init__(self, party: Party, *effects: PartyEffect):
        super().__init__("py", party, effects)

    def type(self):
        return "party"


global current_scope


# TODO: most effects are unfinished


def activate_production_method(arg):
    """

    Activates the named production method for buildings of a certain type in country/state
    **Supported Scopes**: country, state
    """
    return default("activate_production_method", arg)


def add_character_role(arg):
    """

    Adds a new role to a character
    add_character_role = general
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def add_civil_war_progress(arg):
    """

    Adds the specified number of percentage points to a civil war progress (range is [0, 1], 0.1 means 10 percentage points)
    add_civil_war_progress = 0.1 / -0.1
    **Supported Scopes**: civil_war
    """
    return default("add_civil_war_progress", arg)


def add_commander_rank(arg):
    """

    Promotes/demotes a character a given amount of military ranks
    **Supported Scopes**: character
    """
    return default("add_commander_rank", arg)


def add_diplomatic_play_war_support(target, value):
    """

    Adds war support to the target country in the scoped diplomatic play. The amount will appear under the 'situations' header in tooltips
    add_diplomatic_play_war_support = { target = country value = value }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], br(eq("target", target) + eq("value", value)))


def add_escalation(arg):
    """

    Add escalation to a diplomatic play
    add_escalation = integer
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def add_experience(arg):
    """

    Adds an amount of experience to a commander
    add_experience = 0.2
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def add_initiator_backers(arg):
    """

    Add a tag/scope country to the initiator side of a diplomatic play
    add_initiator_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def add_journal_entry(type, target):
    """

    Adds a journal entry to a scoped country's journal, with optional saved scope target
    add_journal_entry = { type = <key> target = <scope> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], br(eq("type", type) + eq("target", target)))


def add_modifier(arg):
    """

    Adds a timed modifier effect to object in scope
    **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
    """
    return default(inspect.stack()[0][3], arg)


def add_morale(arg):
    """

    Adds the specified amount of Morale to the Combat Unit in scope
    add_morale = -0.2
    **Supported Scopes**: new_combat_unit
    """
    return default(inspect.stack()[0][3], arg)


def add_organization(arg):
    """

    Adds the specified amount of Organization to the Military Formation in scope
    add_organization = -10
    **Supported Scopes**: military_formation
    """
    return default(inspect.stack()[0][3], arg)


def add_random_trait(arg):
    """

    Adds a random qualifying Trait of the specified category
    add_random_trait = personality / skill / condition
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def add_target_backers(arg):
    """

    Add a tag/scope country to the target side of a diplomatic play
    add_target_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def add_to_global_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def add_to_list(arg):
    """

    Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the (unbroken) event chain
    add_to_list = <string> NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def add_to_local_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def add_to_temporary_list(arg):
    """

    Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the same effect
    add_to_temporary_list = <string> NOTE, if adding a temporary target to a permanent list, the list will stay permanent
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def add_to_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def add_trait(arg):
    """

    Add a trait to a Character
    add_trait = trait
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def add_war_exhaustion(arg):
    """

    Adds war exhaustion to the target country in the scoped war. The amount will appear under the 'situations' header in tooltips
    add_war_exhaustion = { target = country value = value }
    **Supported Scopes**: war
    """
    return default(inspect.stack()[0][3], arg)


def add_war_goal(arg):
    """

    Adds a war goal to a DP. Same data read in as add_war_goal in create_diplomatic_play
    random_diplomatic_play = { add_war_goal = { holder = initiator type = secession primary_demand = yes }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def add_war_war_support(arg):
    """

    Adds war support to the target country in the scoped war. The amount will appear under the 'situations' header in tooltips
    add_war_war_support = { target = country value = value }
    **Supported Scopes**: war
    """
    return default(inspect.stack()[0][3], arg)


def assert_if(arg):
    """

    Conditionally cause an assert during run time
    assert_if = { limit = { X } text = Y }, where X is a trigger and Y is an optional string
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def assert_read(arg):
    """

    Conditionally cause an assert during read time
    assert_read = X, where X is yes or the string to be printed in the assert
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def change_character_culture(arg):
    """

    Changes the culture of the scoped character
    change_character_culture = cu:colombian
    **Supported Scopes**: character
    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], arg)


def change_character_religion(arg):
    """

    Changes the religion of the scoped character
    change_character_religion = rel:protestant
    **Supported Scopes**: character
    **Supported Targets**: religion
    """
    return default(inspect.stack()[0][3], arg)


def change_global_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def change_local_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def change_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clamp_global_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clamp_local_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clamp_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clear_global_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clear_local_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clear_saved_scope(arg):
    """

    Clears a saved scope from the top scope
    save_scope_as = cool_scope -> clear_saved_scope = cool_scope
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def clear_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


# TODO: creates


def create_character(name: str = "",
                     culture: str = "",
                     religion: str = "",
                     female: bool = False,
                     noble: bool = False,
                     ruler: bool = False,
                     heir: bool = False,
                     historical: bool = False,
                     age: str = "25",
                     ideology: str = "",
                     ig: str = "",
                     template: str = "",
                     on_created: str = "",
                     save_scope_as: str = "",
                     trait_generation: str = "",
                     hq: str = ""
                     ):
    """

    Creates a character, any option can be omitted.
    create_character = {
        name = loc_key or alternatively first_name and last_name separately
        culture = culture_tag
        religion = religion scope (if omitted, it's defined by the character's culture religion)(arg):

        female = bool or character scope (gets the same value from the character)
        noble = bool or character scope (gets the same value from the character)
        ruler = bool
        heir = bool
        historical = bool
        age = integer, range, or character scope (gets the age from a character)
        ideology = ideology key or scope
        interest_group = interest group key or scope
        template = base template to generate the character from
        on_created = effect
        save_scope_as = scope name
        trait_generation = effect
        hq = HQ scope or strategic region scope
    }
    **Supported Scopes**: country
    """
    return default(inspect.stack()[0][3], br(name))  # TODO heavily unfinished


def create_country(arg):
    """

    Creates a new country
    create_country = {
        tag = TAG			# optional, if not specified origin's tag will be used
        origin = country	# optional, newly created country will inherit certain values from the origin country
                            # at least one of tag or origin must be supplied
        state = state		# can be repeated; at least one state or province must be supplied
        province = province	# can be repeated; at least one state or province must be supplied
                            # both states and provinces can be supplied at the same time
        on_created = effect	# optional effect that will be run with the newly created country in scope
    }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def create_dynamic_country(arg):
    """

    Creates a new country with a dynamic tag
    create_dynamic_country = {
     origin = country	# optional, newly created country may inherit certain values from the origin country
     country_type = country type # optional if origin is set, may be repeated, will try to inherit country type from origin if not specified
     tier = country tier # optional if origin is set, may be repeated, will try to inherit country tier from origin if not specified
     culture = culture # optional if origin is set, may be repeated, will try to inherit cultures from origin if not specified
     religion = religion # optional if origin is set, if no religion is specified, will try to inherit religion from origin if not specified
     capital = state		# optional if states have been supplied, will try to set a capital from supplied states if not specified
     cede_state_trigger = trigger # if this trigger is set, each state in the world for which it evaluates true will be ceded to the new country
     color = rgb 		# optional, will try to inherit map color from origin if not specified
     primary_unit_color = rgb 		# optional, will try to inherit unit color from origin if not specified
     secondary_unit_color = rgb 		# optional, will try to inherit unit color from origin if not specified
     tertiary_unit_color = rgb 		# optional, will try to inherit unit color from origin if not specified
     on_created = effect	# optional effect that will be run with the newly created country in scope
    }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def custom_description(arg):
    """

    Wraps effects that get a custom description instead of the auto-generated one
    custom_description = {
        text = <effect_localization_key>
        subject = <optional subject scope> #defaults to current scope(arg):

        object = <optional object scope>
        value = <optional script value>
        ... effects ...
    }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def custom_description_no_bullet(arg):
    """

    Wraps effects that get a custom description instead of the auto-generated one. Also ensures no bullet point appears
    custom_description_no_bullet = {
        text = <effect_localization_key>
        subject = <optional subject scope> #defaults to current scope(arg):

        object = <optional object scope>
        value = <optional script value>
        ... effects ...
    }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def custom_label(arg):
    """

    just a tooltip, the scope as object (for grouping, localization).
    custom_label = key; alternatively custom_label = { text = key subject = scope (optional) <hidden effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def custom_tooltip(arg):
    """

    just a tooltip, the scope as subject (for grouping, localization).
    custom_tooltip = key; alternatively custom_tooltip = { text = key subject = scope (optional) <hidden effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def debug_log(arg):
    """

    Log a string to the debug log when this effect executes, debug_log = message, the message can be a localization string with ROOT, SCOPE and PREV available
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def debug_log_scopes(arg):
    """

    Log the current scope to the debug log when this effect executes
    debug_log_scopes = yes # log full scope info
    debug_log_scopes = no  # log only current scope
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def deploy_to_front(arg):
    """

    Deploys the scope formation to the target front
    deploy_to_front = p:xFAFAFA.front
    **Supported Scopes**: military_formation
    **Supported Targets**: front
    """
    return default(inspect.stack()[0][3], arg)


def disinherit_character(arg):
    """

    Strips the scoped character of their heir status in whichever countries apply.
    scope:larry = { disinherit_character = yes }
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def Else(arg):
    """

    Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met
    if = { limit = { <triggers> } <effects> }
    else = { <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def else_if(arg):
    """

    Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met, and its own limit is met
    if = { limit = { <triggers> } <effects> }
    else_if = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def end_play(arg):
    """

    End a diplomatic play
    end_play = bool
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def every_character(triggers, effects):
    """

    Iterate through all characters globally
    every_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_character_in_exile_pool(triggers, effects):
    """

    Iterate through characters in the exile pool
    every_character_in_exile_pool = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_character_in_void(triggers, effects):
    """

    Iterate through characters in the void
    every_character_in_void = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_combat_unit(triggers, effects):
    """

    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    every_combat_unit = { limit = { <triggers> } <effects> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_country(triggers, effects):
    """

    Iterate through all countries globally
    every_country = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_diplomatic_play(triggers, effects):
    """

    Iterate through all diplomatic plays globally
    every_diplomatic_play = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_in_global_list(triggers, effects):
    """

    Iterate through all items in global list. list = name or variable = name
    every_in_global_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_in_list(triggers, effects):
    """

    Iterate through all items in list. list = name or variable = name
    every_in_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_in_local_list(triggers, effects):
    """

    Iterate through all items in local list. list = name or variable = name
    every_in_local_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_market(triggers, effects):
    """

    Iterate through all markets globally
    every_market = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: market
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_market_goods(triggers, effects):
    """

    Iterate through all active (market) goods in a market
    every_market_goods = { limit = { <triggers> } <effects> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_military_formation(triggers, effects):
    """

    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    every_military_formation = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_neighbouring_state(triggers, effects):
    """

    Iterate through all states neighbouring a state region
    every_neighbouring_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_participant(triggers, effects):
    """

    Any of two participants of the diplomatic pact in a scope
    every_participant = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_primary_culture(triggers, effects):
    """

    Primary cultures of the scoped country or country definition(arg):

    every_primary_culture = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, country_definition, state(arg):

    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_province(triggers, effects):
    """

    Iterate through all Provinces in the scoped State
    every_province = { limit = { <triggers> } <effects> }
    **Supported Scopes**: province
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], iterator(triggers, effects))


def every_scope_admiral(triggers, effects):
    """

    Iterate through all admirals in a: country, interestgroup, or military formation
    every_scope_admiral = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default("every_scope_admiral", iterator(triggers, effects))


def every_scope_ally(triggers, effects):
    """

    Iterate through all allies to a: country
    every_scope_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default("every_scope_ally", iterator(triggers, effects))


def every_scope_building(triggers, effects):
    """

    Iterate through all buildings in a: state, country
    every_scope_building = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: building
    """
    return default("every_scope_building", iterator(triggers, effects))


def every_scope_character(triggers, effects):
    """

    Iterate through all characters in a: country, interestgroup, or front
    every_scope_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default("every_scope_character", iterator(triggers, effects))


def every_scope_country(triggers, effects):
    """

    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    every_scope_country = { limit = { <triggers> } <effects> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country
    """
    return default("every_scope_country", iterator(triggers, effects))


def every_scope_culture(triggers, effects):
    """

    Iterate through all cultures in the scope
    every_scope_culture = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture
    """
    return default("every_scope_culture", iterator(triggers, effects))


def every_scope_front(triggers, effects):
    """

    Iterate through all Fronts related to the scoped War
    every_scope_front = { limit = { <triggers> } <effects> }
    **Supported Scopes**: war
    **Supported Targets**: front
    """
    return default("every_scope_front", iterator(triggers, effects))


def every_scope_general(triggers, effects):
    """

    Iterate through all generals in a: country, interestgroup, front, or military formation
    every_scope_general = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default("every_scope_general", iterator(triggers, effects))


def every_scope_initiator_ally(triggers, effects):
    """

    Iterate through all allies to an initiator in a: diplomatic play
    every_scope_initiator_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default("every_scope_initiator_ally", iterator(triggers, effects))


def every_scope_interest_marker(triggers, effects):
    """

    Iterate through all interest markers in a: country, strategic region
    every_scope_interest_marker = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker
    """
    return default("every_scope_interest_marker", iterator(triggers, effects))


def every_scope_play_involved(triggers, effects):
    """

    Iterate through all involved in a: diplomatic play
    every_scope_play_involved = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default("every_scope_play_involved", iterator(triggers, effects))


def every_scope_politician(triggers, effects):
    """

    Iterate through all politicians in a: country or interestgroup
    every_scope_politician = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default("every_scope_politician", iterator(triggers, effects))


def every_scope_pop(triggers, effects):
    """

    Iterate through all pops in a: country, state, interest group, culture
    every_scope_pop = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, culture, interest_group, state
    **Supported Targets**: pop
    """
    return default("every_scope_pop", iterator(triggers, effects))


def every_scope_state(triggers, effects):
    """

    Iterate through all states including provinces from a: country, state_region, theater, or front
    every_scope_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state
    """
    return default("every_scope_state", iterator(triggers, effects))


def every_scope_target_ally(triggers, effects):
    """

    Iterate through all allies to a target in a: diplomatic play
    every_scope_target_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default("every_scope_target_ally", iterator(triggers, effects))


def every_sea_node_adjacent_state(triggers, effects):
    """

    Iterate through all states that share a sea node with a state
    every_sea_node_adjacent_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: state
    **Supported Targets**: state
    """
    return default("every_sea_node_adjacent_state", iterator(triggers, effects))


def every_state(triggers, effects):
    """

    Iterate through all states globally
    every_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state
    """
    return default("every_state", iterator(triggers, effects))


def every_state_region(triggers, effects):
    """

    Iterate through all state regions
    every_state_region = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region
    """
    return default("every_state_region", iterator(triggers, effects))


def every_supporting_character(triggers, effects):
    """

    Iterate through all characters that support the scoped political movement
    every_supporting_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character
    """
    return default("every_supporting_character", iterator(triggers, effects))


def every_supporting_interest_group(triggers, effects):
    """

    Iterate through all interest groups supporting a political movement
    every_supporting_interest_group = { limit = { <triggers> } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group
    """
    return default("every_supporting_interest_group", iterator(triggers, effects))


def every_trade_route(triggers, effects):
    """

    Iterate through all trade routes in a: market, country, marketgoods
    every_trade_route = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route
    """
    return default("every_trade_route", iterator(triggers, effects))


def exile_character(arg):
    """

    Exile a character to the exile pool
    exile_character = yes
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def free_character_from_void(arg):
    """

    Frees a character from the void, if set to no character is deleted instead
    free_character_from_void = yes
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def fully_mobilize_army(arg):
    """

    Fully mobilizes scope army
    fully_mobilize_army = yes
    **Supported Scopes**: military_formation
    """
    return default(inspect.stack()[0][3], arg)


def hidden_effect(arg):
    """

    Enclosed effects are not shown in tooltips
    hidden_effect = { <more effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def If(arg):
    """

    Executes enclosed effects if limit criteria are met
    if = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def kill_character(arg):
    """

    Kill a character
    kill_character = bool (yes - kill [by default], no - don't do anything)(arg):

    kill_character = {
        hidden = bool (yes - without notification; no - show notification [by default])(arg):

        value = bool (yes - kill [by default], no - don't do anything)(arg):

    }
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def lock_trade_route(years):
    """

    Lock a trade route for a set amount of time, preventing it from being cancelled manually
    lock_trade_route = {
        years = 5
    }
    **Supported Scopes**: trade_route
    """
    return default(inspect.stack()[0][3], br(eq("years", years)))


def mobilize_army(arg):
    """

    Mobilizes scope army
    mobilize_army = yes
    **Supported Scopes**: military_formation
    """
    return default(inspect.stack()[0][3], arg)


# TODO all ordered iterators
# TODO proper country ends here

def ordered_active_party(arg):
    """

    Iterate through all active political parties in a country
    ordered_active_party = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """
    return default(inspect.stack()[0][3], arg)


def ordered_character(arg):
    """

    Iterate through all characters globally
    ordered_character = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_character_in_exile_pool(arg):
    """

    Iterate through characters in the exile pool
    ordered_character_in_exile_pool = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_character_in_void(arg):
    """

    Iterate through characters in the void
    ordered_character_in_void = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_civil_war(arg):
    """

    Iterate through all civil wars related to the scoped country
    ordered_civil_war = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: civil_war
    """
    return default(inspect.stack()[0][3], arg)


def ordered_cobelligerent_in_diplo_play(arg):
    """

    Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
    ordered_cobelligerent_in_diplo_play = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_cobelligerent_in_war(arg):
    """

    Iterate through all co-belligerents of scope country in all wars
    ordered_cobelligerent_in_war = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_combat_unit(arg):
    """

    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    ordered_combat_unit = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit
    """
    return default(inspect.stack()[0][3], arg)


def ordered_company(arg):
    """

    Iterate through all companies in a country
    ordered_company = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: company
    """
    return default(inspect.stack()[0][3], arg)


def ordered_country(arg):
    """

    Iterate through all countries globally
    ordered_country = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_diplomatic_play(arg):
    """

    Iterate through all diplomatic plays globally
    ordered_diplomatic_play = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def ordered_enemy_in_diplo_play(arg):
    """

    Iterate through all enemies of scope country in all diplomatic plays (includes wars)
    ordered_enemy_in_diplo_play = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_enemy_in_war(arg):
    """

    Iterate through all enemies of scope country in all wars
    ordered_enemy_in_war = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_in_global_list(arg):
    """

    Iterate through all items in global list. list = name or variable = name
    ordered_in_global_list = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def ordered_in_hierarchy(arg):
    """

    Any country in current hierarchy, including current
    ordered_in_hierarchy = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_in_list(arg):
    """

    Iterate through all items in list. list = name or variable = name
    ordered_in_list = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def ordered_in_local_list(arg):
    """

    Iterate through all items in local list. list = name or variable = name
    ordered_in_local_list = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def ordered_interest_group(arg):
    """

    Iterate through all interest groups in a country
    ordered_interest_group = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_group
    """
    return default(inspect.stack()[0][3], arg)


def ordered_law(arg):
    """

    Iterate through all laws in a country
    ordered_law = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: law
    """
    return default(inspect.stack()[0][3], arg)


def ordered_market(arg):
    """

    Iterate through all markets globally
    ordered_market = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: market
    """
    return default(inspect.stack()[0][3], arg)


def ordered_market_goods(arg):
    """

    Iterate through all active (market) goods in a market
    ordered_market_goods = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods
    """
    return default(inspect.stack()[0][3], arg)



def ordered_military_formation(arg):
    """

    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    ordered_military_formation = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation
    """
    return default(inspect.stack()[0][3], arg)


def ordered_neighbouring_state(arg):
    """

    Iterate through all states neighbouring a state region
    ordered_neighbouring_state = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_overlord_or_above(arg):
    """

    Any country above current in hierarchy
    ordered_overlord_or_above = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_participant(arg):
    """

    Any of two participants of the diplomatic pact in a scope
    ordered_participant = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_political_movement(arg):
    """

    Iterate through all political movements in a country
    ordered_political_movement = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: political_movement
    """
    return default(inspect.stack()[0][3], arg)


def ordered_potential_party(arg):
    """

    Iterate through all potential political parties in a country
    ordered_potential_party = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """
    return default(inspect.stack()[0][3], arg)


def ordered_preferred_law(arg):
    """

    Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law
    ordered_preferred_law = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: interest_group
    **Supported Targets**: law
    """
    return default(inspect.stack()[0][3], arg)


def ordered_primary_culture(arg):
    """

    Primary cultures of the scoped country or country definition(arg):

    ordered_primary_culture = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, country_definition, state(arg):

    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], arg)


def ordered_province(arg):
    """

    Iterate through all Provinces in the scoped State
    ordered_province = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: province
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_rival_country(arg):
    """

    Any country that is rival to the country in a scope
    ordered_rival_country = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_admiral(arg):
    """

    Iterate through all admirals in a: country, interestgroup, or military formation
    ordered_scope_admiral = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_ally(arg):
    """

    Iterate through all allies to a: country
    ordered_scope_ally = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_building(arg):
    """

    Iterate through all buildings in a: state, country
    ordered_scope_building = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: building
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_character(arg):
    """

    Iterate through all characters in a: country, interestgroup, or front
    ordered_scope_character = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_country(arg):
    """

    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    ordered_scope_country = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_culture(arg):
    """

    Iterate through all cultures in the scope
    ordered_scope_culture = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_diplomatic_pact(arg):
    """

    Any diplomatic pact of the country in a scope
    ordered_scope_diplomatic_pact = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: diplomatic_pact
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_front(arg):
    """

    Iterate through all Fronts related to the scoped War
    ordered_scope_front = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: war
    **Supported Targets**: front
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_general(arg):
    """

    Iterate through all generals in a: country, interestgroup, front, or military formation
    ordered_scope_general = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_held_interest_marker(arg):
    """

    Iterate through all interest markers held by a country
    ordered_scope_held_interest_marker = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_marker
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_initiator_ally(arg):
    """

    Iterate through all allies to an initiator in a: diplomatic play
    ordered_scope_initiator_ally = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_interest_marker(arg):
    """

    Iterate through all interest markers in a: country, strategic region
    ordered_scope_interest_marker = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_play_involved(arg):
    """

    Iterate through all involved in a: diplomatic play
    ordered_scope_play_involved = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_politician(arg):
    """

    Iterate through all politicians in a: country or interestgroup
    ordered_scope_politician = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


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


def ordered_scope_state(arg):
    """

    Iterate through all states including provinces from a: country, state_region, theater, or front
    ordered_scope_state = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_target_ally(arg):
    """

    Iterate through all allies to a target in a: diplomatic play
    ordered_scope_target_ally = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_theater(arg):
    """

    Iterate through all theaters in a: country
    ordered_scope_theater = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: theater
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_violate_sovereignty_interested_parties(arg):
    """

    Iterate through all countries that would be interested if country in scope has their sovereignty violated
    ordered_scope_violate_sovereignty_interested_parties = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_violate_sovereignty_wars(arg):
    """

    Iterate through all relevant wars if target country had their sovereignty violated by scoped country
    ordered_scope_violate_sovereignty_wars = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """
    return default(inspect.stack()[0][3], arg)


def ordered_scope_war(arg):
    """

    Iterate through all wars related to the scope
    ordered_scope_war = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """
    return default(inspect.stack()[0][3], arg)


def ordered_sea_node_adjacent_state(arg):
    """

    Iterate through all states that share a sea node with a state
    ordered_sea_node_adjacent_state = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: state
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_state(arg):
    """

    Iterate through all states globally
    ordered_state = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_state_region(arg):
    """

    Iterate through all state regions
    ordered_state_region = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region
    """
    return default(inspect.stack()[0][3], arg)


def ordered_strategic_objective(arg):
    """

    Iterate through all Strategic Objective states from the scoped Country
    ordered_strategic_objective = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], arg)


def ordered_subject_or_below(arg):
    """

    Any country below current in hierarchy
    ordered_subject_or_below = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def ordered_supporting_character(arg):
    """

    Iterate through all characters that support the scoped political movement
    ordered_supporting_character = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], arg)


def ordered_supporting_interest_group(arg):
    """

    Iterate through all interest groups supporting a political movement
    ordered_supporting_interest_group = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group
    """
    return default(inspect.stack()[0][3], arg)


def ordered_trade_route(arg):
    """

    Iterate through all trade routes in a: market, country, marketgoods
    ordered_trade_route = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route
    """
    return default(inspect.stack()[0][3], arg)


def ordered_valid_mass_migration_culture(arg):
    """

    Lists for cultures in the scoped country that are valid for mass migration
    ordered_valid_mass_migration_culture = {
    limit = { <triggers> }
    order_by = script_value
    position = int
    min = int
    max = script_value
    check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max
    <effects> }
    **Supported Scopes**: country
    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], arg)


def place_character_in_void(arg):
    """

    Banishes a character to the void, duration is how long character is kept before being deleted
    place_character_in_void = months
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def post_notification(arg):
    """

    Posts notification
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def post_proposal(arg):
    """

    Posts proposal
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def random(arg):
    """

    run an effect depending on a random chance, do nothing otherwise.
    random = {
        chance = 0-100     # random chance in percent. can also be a script value or complex math
        modifier = { ... } # optional MTTH-style modifier for the chance
        effects...         # effects to run if the random roll succeeds
    }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def random_character(triggers, effects, mtth=""):
    """

    Iterate through all characters globally
    random_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_character_in_exile_pool(triggers, effects, mtth=""):
    """

    Iterate through characters in the exile pool
    random_character_in_exile_pool = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_character_in_void(triggers, effects, mtth=""):
    """

    Iterate through characters in the void
    random_character_in_void = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_civil_war(triggers, effects, mtth=""):
    """

    Iterate through all civil wars related to the scoped country
    random_civil_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: civil_war
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_cobelligerent_in_diplo_play(triggers, effects, mtth=""):
    """

    Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
    random_cobelligerent_in_diplo_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_cobelligerent_in_war(triggers, effects, mtth=""):
    """

    Iterate through all co-belligerents of scope country in all wars
    random_cobelligerent_in_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_combat_unit(triggers, effects, mtth=""):
    """

    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    random_combat_unit = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_company(triggers, effects, mtth=""):
    """

    Iterate through all companies in a country
    random_company = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: company
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_country(triggers, effects, mtth=""):
    """

    Iterate through all countries globally
    random_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_diplomatic_play(triggers, effects, mtth=""):
    """

    Iterate through all diplomatic plays globally
    random_diplomatic_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_enemy_in_diplo_play(triggers, effects, mtth=""):
    """

    Iterate through all enemies of scope country in all diplomatic plays (includes wars)
    random_enemy_in_diplo_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_enemy_in_war(triggers, effects, mtth=""):
    """

    Iterate through all enemies of scope country in all wars
    random_enemy_in_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_in_global_list(triggers, effects, mtth=""):
    """

    Iterate through all items in global list. list = name or variable = name
    random_in_global_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_in_hierarchy(triggers, effects, mtth=""):
    """

    Any country in current hierarchy, including current
    random_in_hierarchy = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_in_list(triggers, effects, mtth=""):
    """

    Iterate through all items in list. list = name or variable = name
    random_in_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_in_local_list(triggers, effects, mtth=""):
    """

    Iterate through all items in local list. list = name or variable = name
    random_in_local_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_interest_group(triggers, effects, mtth=""):
    """

    Iterate through all interest groups in a country
    random_interest_group = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_group
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_law(triggers, effects, mtth=""):
    """

    Iterate through all laws in a country
    random_law = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: law
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_list(arg):
    """

    a random list effect
    random_list = { X1 = { trigger = { enables/disable this effect} modifier = Y1 effect1 } X2 = { trigger = { enables/disable this effect} modifier = Y2 effect2 } ... }
    Selects one effect from the list and fires it. The effects are weighted by numbers X1, X2... (the higher the number, the higher the chance of the effect being picked).
    The chances can be modified by optional value modifier lists Y1, Y2... (AKA MTTH constructs)
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def random_log_scopes(arg):
    """

    Log the current scope to the random log when this effect executes.
    Only use temprorarily for debugging purposes as it can introduce localized strings into the random log.
    random_log_scopes = yes # log full scope info
    random_log_scopes = no  # log only current scope
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def random_market(triggers, effects, mtth=""):
    """

    Iterate through all markets globally
    random_market = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: market
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_market_goods(triggers, effects, mtth=""):
    """

    Iterate through all active (market) goods in a market
    random_market_goods = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_military_formation(triggers, effects, mtth=""):
    """

    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    random_military_formation = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_neighbouring_state(triggers, effects, mtth=""):
    """

    Iterate through all states neighbouring a state region
    random_neighbouring_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_overlord_or_above(triggers, effects, mtth=""):
    """

    Any country above current in hierarchy
    random_overlord_or_above = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_participant(triggers, effects, mtth=""):
    """

    Any of two participants of the diplomatic pact in a scope
    random_participant = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_political_movement(triggers, effects, mtth=""):
    """

    Iterate through all political movements in a country
    random_political_movement = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: political_movement
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_potential_party(triggers, effects, mtth=""):
    """

    Iterate through all potential political parties in a country
    random_potential_party = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_preferred_law(triggers, effects, mtth=""):
    """

    Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law
    random_preferred_law = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: interest_group
    **Supported Targets**: law
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_primary_culture(triggers, effects, mtth=""):
    """

    Primary cultures of the scoped country or country definition(triggers, effects, mtth=""):

    random_primary_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, country_definition, state(triggers, effects, mtth=""):

    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_province(triggers, effects, mtth=""):
    """

    Iterate through all Provinces in the scoped State
    random_province = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: province
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_rival_country(triggers, effects, mtth=""):
    """

    Any country that is rival to the country in a scope
    random_rival_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_admiral(triggers, effects, mtth=""):
    """

    Iterate through all admirals in a: country, interestgroup, or military formation
    random_scope_admiral = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_ally(triggers, effects, mtth=""):
    """

    Iterate through all allies to a: country
    random_scope_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_building(triggers, effects, mtth=""):
    """

    Iterate through all buildings in a: state, country
    random_scope_building = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: building
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_character(triggers, effects, mtth=""):
    """

    Iterate through all characters in a: country, interestgroup, or front
    random_scope_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_country(triggers, effects, mtth=""):
    """

    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    random_scope_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_culture(triggers, effects, mtth=""):
    """

    Iterate through all cultures in the scope
    random_scope_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_diplomatic_pact(triggers, effects, mtth=""):
    """

    Any diplomatic pact of the country in a scope
    random_scope_diplomatic_pact = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: diplomatic_pact
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_front(triggers, effects, mtth=""):
    """

    Iterate through all Fronts related to the scoped War
    random_scope_front = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: war
    **Supported Targets**: front
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_general(triggers, effects, mtth=""):
    """

    Iterate through all generals in a: country, interestgroup, front, or military formation
    random_scope_general = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_held_interest_marker(triggers, effects, mtth=""):
    """

    Iterate through all interest markers held by a country
    random_scope_held_interest_marker = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_marker
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_initiator_ally(triggers, effects, mtth=""):
    """

    Iterate through all allies to an initiator in a: diplomatic play
    random_scope_initiator_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_interest_marker(triggers, effects, mtth=""):
    """

    Iterate through all interest markers in a: country, strategic region
    random_scope_interest_marker = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_play_involved(triggers, effects, mtth=""):
    """

    Iterate through all involved in a: diplomatic play
    random_scope_play_involved = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_politician(triggers, effects, mtth=""):
    """

    Iterate through all politicians in a: country or interestgroup
    random_scope_politician = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_pop(triggers, effects, mtth=""):
    """

    Iterate through all pops in a: country, state, interest group, culture
    random_scope_pop = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, culture, interest_group, state
    **Supported Targets**: pop
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_state(triggers, effects, mtth=""):
    """

    Iterate through all states including provinces from a: country, state_region, theater, or front
    random_scope_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_target_ally(triggers, effects, mtth=""):
    """

    Iterate through all allies to a target in a: diplomatic play
    random_scope_target_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_theater(triggers, effects, mtth=""):
    """

    Iterate through all theaters in a: country
    random_scope_theater = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: theater
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_violate_sovereignty_interested_parties(triggers, effects, mtth=""):
    """

    Iterate through all countries that would be interested if country in scope has their sovereignty violated
    random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_violate_sovereignty_wars(triggers, effects, mtth=""):
    """

    Iterate through all relevant wars if target country had their sovereignty violated by scoped country
    random_scope_violate_sovereignty_wars = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_scope_war(triggers, effects, mtth=""):
    """

    Iterate through all wars related to the scope
    random_scope_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_sea_node_adjacent_state(triggers, effects, mtth=""):
    """

    Iterate through all states that share a sea node with a state
    random_sea_node_adjacent_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: state
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_state(triggers, effects, mtth=""):
    """

    Iterate through all states globally
    random_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_state_region(triggers, effects, mtth=""):
    """

    Iterate through all state regions
    random_state_region = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_strategic_objective(triggers, effects, mtth=""):
    """

    Iterate through all Strategic Objective states from the scoped Country
    random_strategic_objective = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: state
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_subject_or_below(triggers, effects, mtth=""):
    """

    Any country below current in hierarchy
    random_subject_or_below = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_supporting_character(triggers, effects, mtth=""):
    """

    Iterate through all characters that support the scoped political movement
    random_supporting_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_supporting_interest_group(triggers, effects, mtth=""):
    """

    Iterate through all interest groups supporting a political movement
    random_supporting_interest_group = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_trade_route(triggers, effects, mtth=""):
    """

    Iterate through all trade routes in a: market, country, marketgoods
    random_trade_route = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def random_valid_mass_migration_culture(triggers, effects, mtth=""):
    """

    Lists for cultures in the scoped country that are valid for mass migration
    random_valid_mass_migration_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: culture
    """
    return default(inspect.stack()[0][3], random_iterator(triggers, effects, mtth))


def remove_as_interest_group_leader(arg):
    """

    Removes a character from position as interest group leader
    remove_as_interest_group_leader = yes
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def remove_character_role(arg):
    """

    Removes an existing role from a character
    remove_character_role = general
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def remove_from_list(arg):
    """

    Removes the current scope from a named list remove_from_list = <string>
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_global_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_initiator_backers(arg):
    """

    Remove a tag/scope country from the initiator side of a diplomatic play
    remove_initiator_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def remove_list_global_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_list_local_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_list_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_local_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_modifier(arg):
    """

    Removes a timed modifier effect to object in scope
    **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
    """
    return default(inspect.stack()[0][3], arg)


def remove_target_backers(arg):
    """

    Remove a tag/scope country to the target side of a diplomatic play
    remove_target_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def remove_trait(arg):
    """

    Remove a trait from a Character
    remove_trait = trait
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def remove_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def remove_war_goal(who, war_goal):
    """

    Removes a war goal from a DP.
    any_diplomatic_play = { limit = { has_war_goal = return_state }
    remove_war_goal = { who = initiator war_goal = return_state } }
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], br(eq("who", who) + eq("war_goal", war_goal)))


def resolve_play_for(arg):
    """

    effect end diplo play for one side, with it gaining war goals
    resolve_play_for = initiator
    resolve_play_for = scope:custom_scoped_country
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def round_global_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def round_local_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def round_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def save_scope_as(arg):
    """

    Saves the current scope as an arbitrarily-named target to be referenced later in the (unbroken) event chain
    save_scope_as = <string>
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def save_scope_value_as(arg):
    """

    Saves a numerical or bool value as an arbitrarily-named target to be referenced later in the (unbroken) event chain
    save_scope_value_as = { name = <string> value = x }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], br(arg))


def save_temporary_scope_as(arg):
    """

    Saves the current scope as an arbitrarily-named temporary target to be referenced later in the same effect
    save_temporary_scope_as = <string>
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def save_temporary_scope_value_as(arg):
    """

    Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect
    save_temporary_scope_value_as = { name = <string> value = x }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], br(arg))


def seize_investment_pool(arg):  # TODO borked?
    """

    Seize investment pool for the treasury and transfer all private construction queue elements to the government queue = bool
    **Supported Scopes**: country
    """
    return default(inspect.stack()[0][3], arg)


def set_as_interest_group_leader(arg):
    """

    Sets a character as interest group leader
    set_as_interest_group_leader = yes
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def set_character_as_ruler(arg):
    """

    Set scoped character as ruler in their country.
    scope:larry = { set_character_as_ruler = yes }
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def set_character_busy_and_immortal(arg):
    """

    Mark a character as busy and immortal or clear said mark
    set_character_busy = bool
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def set_character_immortal(arg):
    """

    Set scoped character as immortal.
    scope:larry = { set_character_immortal = yes/no }
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def set_commander_rank(arg):
    """

    Promotes/demotes a character to a given military rank value
    set_commander_rank = 3
    **Supported Scopes**: character
    """
    return default(inspect.stack()[0][3], arg)


def set_company_establishment_date(arg):
    """

    Sets the establishment date of scope company
    set_company_establishment_date = 1782.7.18
    **Supported Scopes**: company
    """
    return default(inspect.stack()[0][3], arg)


def set_global_variable(arg):
    """

    Sets a variable
    set_variable = { name = X value = Y days = Z }
    Where X is the name of the variable used to then access it
    Where Y is any event target, bool, value, script value or flag (flag:W)
    An optional days where Z is the number of days or script value
    This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope
    Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], br(arg))


def set_home_country(arg):
    """

    Set a character's home country. This makes them start considering themselves as having been exiled, i.e. was_exiled starts evaluating to yes for them.
    set_home_country = c:FRA
    **Supported Scopes**: character
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def set_home_country_definition(arg):
    """

    Set a character's home country directly to a tag, you can use this to avoid making sure that the tag exists, this makes them an exile
    set_home_country_definition = cd:FRA(arg):

    **Supported Scopes**: character
    **Supported Targets**: country_definition(arg):

    """
    return default(inspect.stack()[0][3], arg)


def set_ideology(arg):
    """

    Changes scoped character's ideology
    set_ideology = x
    **Supported Scopes**: character
    **Supported Targets**: ideology
    """
    return default(inspect.stack()[0][3], arg)


def set_key(arg):
    """

    Set name to a diplomatic play
    set_key = loc_key
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def set_local_variable(arg):
    """

    Sets a variable
    set_variable = { name = X value = Y days = Z }
    Where X is the name of the variable used to then access it
    Where Y is any event target, bool, value, script value or flag (flag:W)
    An optional days where Z is the number of days or script value
    This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope
    Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def set_subsidized(arg):
    """

    Sets whether a building is subsidized
    set_subsidized = yes/no
    **Supported Scopes**: building
    """
    return default(inspect.stack()[0][3], arg)


def set_target_technology(arg):
    """

    Sets a (new) target technology scope for a journal entry
    set_target_technology = <scope>
    **Supported Scopes**: journalentry
    """
    return default(inspect.stack()[0][3], arg)


def set_variable(arg):
    """

    Sets a variable
    set_variable = { name = X value = Y days = Z }
    Where X is the name of the variable used to then access it
    Where Y is any event target, bool, value, script value or flag (flag:W)
    An optional days where Z is the number of days or script value
    This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope
    Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def set_war(arg):
    """

    Set a diplomatic play to be a war
    set_war = bool
    **Supported Scopes**: diplomatic_play
    """
    return default(inspect.stack()[0][3], arg)


def show_as_tooltip(arg):
    """

    Enclosed effects are only shown in tooltips (but are not actually executed)
    show_as_tooltip = { <more effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def start_tutorial_lesson(arg):
    """

    Starts the tutorial lesson with the given key. Does nothing if the tutorial is not running, the lesson is completed
    (or already running), or the lesson cannot be triggered (e.g. trigger fails)
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def switch(arg):  # TODO multiple args
    """

    Switch on a trigger for the evaluation of another trigger with an optional fallback trigger.
    switch = {
        trigger = simple_assign_trigger
        case_1 = { <effects> }
        case_2 = { <effects> }
        case_n = { <effects> }
        fallback = { <effects> }
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def teleport_to_front(arg):
    """

    Teleports the scope formation to the target front
    teleport_to_front = p:xFAFAFA.front
    **Supported Scopes**: military_formation
    **Supported Targets**: front
    """
    return default(inspect.stack()[0][3], arg)


def transfer_character(arg):
    """

    Transfers current scope character to target country
    transfer_character = country
    **Supported Scopes**: character
    **Supported Targets**: country
    """
    return default(inspect.stack()[0][3], arg)


def transfer_to_formation(arg):
    """

    Transfers scope character to target formation
    transfer_to_formation = scope:formation
    **Supported Scopes**: character
    **Supported Targets**: military_formation
    """
    return default(inspect.stack()[0][3], arg)


def trigger_event(arg):
    """

    Triggers an event for the current scope
    trigger_event = X
    trigger_event = { id = X days/weeks/months/years = Y }
    Where X is an event ID and Y is an integer to delay the event by
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)


def While(triggers, effects):
    """

    Repeats enclosed effects while limit criteria are met
    while = { limit = { <triggers> } <effects> }

    **Supported Scopes**: none/all
        """
    return default("while", iterator(triggers, effects))


def Whilefor(count, effects):
    """

    Repeats enclosed effects until set iteration count is reached
     while = { count = 3 <effects> }
        default max of 1000.(arg):

    **Supported Scopes**: none/all
        """
    return default("while", br(eq("count", count) + effects))
