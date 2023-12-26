import inspect
from helpers import default, iterator, br, eq

    
def active_lens(arg):
    """
    Checks if the specified lens is open
    active_lens = lensAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all    
    """
    return default(inspect.stack()[0][3], arg)
    
    
def active_lens_option(arg):
    """
    Checks if the specified lens option is activated
    active_lens_option = lens_option_keyAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
def add_to_temporary_list(arg):
    """
    Saves a temporary target for use during the trigger execution
    This is used to build lists in triggers.
    If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop.
    In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger (so that every condition is evaluated for every iteration).
    **Supported Scopes**: none/all
    """
    return default(inspect.stack()[0][3], arg)
    
    
def additional_war_exhaustion(arg):
    """
    Compares the additional war exhaustion the scoped country has accumulated from scripted events in the target diplomatic play
    additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def age(arg):
    """
    Compares the character age
    age > 20Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def aggressive_diplomatic_plays_permitted(arg):
    """
    True if country is independent or permitted to start their own Diplomatic Plays
    aggressive_diplomatic_plays_permitted = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def all_false(arg):
    """
    true if all children are false (equivalent to NOR)
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def always(arg):
    """
    checks if the assigned yes/no value is true
    always = yes # always succeeds
    always = no  # always fails
    always = scope:a_boolean_value # evaluated at runtime
    Traits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def And(arg):
    """
    all inside trigger must be true
    **Supported Scopes**: none/all"""
    return default("and", arg)
    
    
def any_active_party(arg):
    """
    Iterate through all active political parties in a country
    any_active_party = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_character(arg):
    """
    Iterate through all characters globally
    any_character = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_character_in_exile_pool(arg):
    """
    Iterate through characters in the exile pool
    any_character_in_exile_pool = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_character_in_void(arg):
    """
    Iterate through characters in the void
    any_character_in_void = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_civil_war(arg):
    """
    Iterate through all civil wars related to the scoped country
    any_civil_war = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: civil_war"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_cobelligerent_in_diplo_play(arg):
    """
    Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
    any_cobelligerent_in_diplo_play = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_cobelligerent_in_war(arg):
    """
    Iterate through all co-belligerents of scope country in all wars
    any_cobelligerent_in_war = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_combat_unit(arg):
    """
    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    any_combat_unit = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_company(arg):
    """
    Iterate through all companies in a country
    any_company = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: company"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_country(arg):
    """
    Iterate through all countries globally
    any_country = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_diplomatic_play(arg):
    """
    Iterate through all diplomatic plays globally
    any_diplomatic_play = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_enemy_in_diplo_play(arg):
    """
    Iterate through all enemies of scope country in all diplomatic plays (includes wars)
    any_enemy_in_diplo_play = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_enemy_in_war(arg):
    """
    Iterate through all enemies of scope country in all wars
    any_enemy_in_war = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_false(arg):
    """
    true if any child is false (equivalent to NAND)
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_in_global_list(arg):
    """
    Iterate through all items in global list. list = name or variable = name
    any_in_global_list = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_in_hierarchy(arg):
    """
    Any country in current hierarchy, including current
    any_in_hierarchy = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_in_list(arg):
    """
    Iterate through all items in list. list = name or variable = name
    any_in_list = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_in_local_list(arg):
    """
    Iterate through all items in local list. list = name or variable = name
    any_in_local_list = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_interest_group(arg):
    """
    Iterate through all interest groups in a country
    any_interest_group = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_law(arg):
    """
    Iterate through all laws in a country
    any_law = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: law"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_market(arg):
    """
    Iterate through all markets globally
    any_market = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: market"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_market_goods(arg):
    """
    Iterate through all active (market) goods in a market
    any_market_goods = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_member(arg):
    """
    Iterate through all interest group members of a party
    any_member = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: party
    **Supported Targets**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_military_formation(arg):
    """
    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    any_military_formation = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_neighbouring_state(arg):
    """
    Iterate through all states neighbouring a state region
    any_neighbouring_state = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_overlord_or_above(arg):
    """
    Any country above current in hierarchy
    any_overlord_or_above = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_participant(arg):
    """
    Any of two participants of the diplomatic pact in a scope
    any_participant = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_political_movement(arg):
    """
    Iterate through all political movements in a country
    any_political_movement = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: political_movement"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_potential_party(arg):
    """
    Iterate through all potential political parties in a country
    any_potential_party = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_preferred_law(arg):
    """
    Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law
    any_preferred_law = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: interest_group
    **Supported Targets**: law"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_primary_culture(arg):
    """
    Primary cultures of the scoped country or country     return default(inspect.stack()[0][3], arg)
    
    
definition
    any_primary_culture = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, country_    return default(inspect.stack()[0][3], arg)
    
    
definition, state
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_province(arg):
    """
    Iterate through all Provinces in the scoped State
    any_province = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: province
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_rival_country(arg):
    """
    Any country that is rival to the country in a scope
    any_rival_country = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_admiral(arg):
    """
    Iterate through all admirals in a: country, interestgroup, or military formation
    any_scope_admiral = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_ally(arg):
    """
    Iterate through all allies to a: country
    any_scope_ally = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_building(arg):
    """
    Iterate through all buildings in a: state, country
    any_scope_building = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, state
    **Supported Targets**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_character(arg):
    """
    Iterate through all characters in a: country, interestgroup, or front
    any_scope_character = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_country(arg):
    """
    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    any_scope_country = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_culture(arg):
    """
    Iterate through all cultures in the scope
    any_scope_culture = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_diplomatic_pact(arg):
    """
    Any diplomatic pact of the country in a scope
    any_scope_diplomatic_pact = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: diplomatic_pact"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_front(arg):
    """
    Iterate through all Fronts related to the scoped War
    any_scope_front = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: war
    **Supported Targets**: front"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_general(arg):
    """
    Iterate through all generals in a: country, interestgroup, front, or military formation
    any_scope_general = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_held_interest_marker(arg):
    """
    Iterate through all interest markers held by a country
    any_scope_held_interest_marker = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: interest_marker"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_initiator_ally(arg):
    """
    Iterate through all allies to an initiator in a: diplomatic play
    any_scope_initiator_ally = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_interest_marker(arg):
    """
    Iterate through all interest markers in a: country, strategic region
    any_scope_interest_marker = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_play_involved(arg):
    """
    Iterate through all involved in a: diplomatic play
    any_scope_play_involved = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_politician(arg):
    """
    Iterate through all politicians in a: country or interestgroup
    any_scope_politician = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_pop(arg):
    """
    Iterate through all pops in a: country, state, interest group, culture
    any_scope_pop = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, culture, interest_group, state
    **Supported Targets**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_state(arg):
    """
    Iterate through all states including provinces from a: country, state_region, theater, or front
    any_scope_state = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_target_ally(arg):
    """
    Iterate through all allies to a target in a: diplomatic play
    any_scope_target_ally = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_theater(arg):
    """
    Iterate through all theaters in a: country
    any_scope_theater = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: theater"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_violate_sovereignty_interested_parties(arg):
    """
    Iterate through all countries that would be interested if country in scope has their sovereignty violated
    any_scope_violate_sovereignty_interested_parties = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_violate_sovereignty_wars(arg):
    """
    Iterate through all relevant wars if target country had their sovereignty violated by scoped country
    any_scope_violate_sovereignty_wars = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_scope_war(arg):
    """
    Iterate through all wars related to the scope
    any_scope_war = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_sea_node_adjacent_state(arg):
    """
    Iterate through all states that share a sea node with a state
    any_sea_node_adjacent_state = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: state
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_state(arg):
    """
    Iterate through all states globally
    any_state = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_state_region(arg):
    """
    Iterate through all state regions
    any_state_region = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_strategic_objective(arg):
    """
    Iterate through all Strategic Objective states from the scoped Country
    any_strategic_objective = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_subject_or_below(arg):
    """
    Any country below current in hierarchy
    any_subject_or_below = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_supporting_character(arg):
    """
    Iterate through all characters that support the scoped political movement
    any_supporting_character = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_supporting_interest_group(arg):
    """
    Iterate through all interest groups supporting a political movement
    any_supporting_interest_group = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_trade_route(arg):
    """
    Iterate through all trade routes in a: market, country, marketgoods
    any_trade_route = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route"""
    return default(inspect.stack()[0][3], arg)
    
    
def any_valid_mass_migration_culture(arg):
    """
    Lists for cultures in the scoped country that are valid for mass migration
    any_valid_mass_migration_culture = { <count=num/all> / <percent=fixed_point> <triggers> }
    **Supported Scopes**: country
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def approaching_bureaucracy_shortage(arg):
    """
    Check if Institutions in the country will incur a Bureaucracy shortage eventuallyTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def arable_land(arg):
    """
    Check arable land in state
    arable_land > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def arable_land_country(arg):
    """
    Compare arable land in *all* states
    arable_land_country > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def army_mobilization_option_fraction(arg):
    """
    Checks that a countries army has a certain percentage of units with a specific monbilization option
    scope:country = {
    army_mobilization_option_fraction = {
    target = mobilization_option:key
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def army_reserves(arg):
    """
    Compare the amount of Army ReservesTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def assert_if(arg):
    """
    Conditionally cause an assert during run time
    assert_if = { limit = { X } text = Y }, where X is a trigger and Y is an optional string
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def assert_read(arg):
    """
    Conditionally cause an assert during read time
    assert_read = X, where X is yes or the string to be printed in the assert
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def authority(arg):
    """
    Compares the available authority of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def available_jobs(arg):
    """
    Checks the state's number of available jobs in non-subsistence buildings
    available_jobs > 10000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def average_country_infrastructure(arg):
    """
    Check average infrastructure in all states owned by scope country
    average_country_infrastructure = 3Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def average_incorporated_country_infrastructure(arg):
    """
    Check average infrastructure in incorporated states owned by the scope country
    average_incorporated_country_infrastructure = 3Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def battalion_manpower(arg):
    """
    Compares the current total manpower of a country's Battalions
    battalion_manpower > 15000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def battle_side_pm_usage(arg):
    """
    Checks how the ratio of Combat Units on the scoped Battle, on the target country's side, with the specified Production Method compares to the value
    battle_side_pm_usage = { target = X production_method = Y value <comparator> Z}
    where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: battle"""
    return default(inspect.stack()[0][3], arg)
    
    
def building_has_goods_shortage(arg):
    """
    Check if building has a shortage of any of its inputs
    building_has_goods_shortage = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def bureaucracy(arg):
    """
    Compares the available bureaucracy of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def calc_true_if(arg):
    """
    Returns true if the specified number of sub-triggers return true
    calc_true_if = { amount = 2 <trigger> <trigger> <trigger> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_activate_production_method(arg):
    """
    Checks if the building of a particular type in scoped state is able to active the specified production method
    can_activate_production_method = { building_type = <key> production_method = <key> }
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_afford_diplomatic_action(arg):
    """
    Checks if the country in scope can afford the Influence for the specified diplomatic action (pact or ongoing)
    can_afford_diplomatic_action = { target = X type = Y }
    Where X = country and Y = diplomatic action type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_agitate(arg):
    """
    Check if the scope character can agitate the target country
    can_agitate = <scope/c:TAG>Traits: country scope
    **Supported Scopes**: character
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_be_enacted(arg):
    """
    Checks if a law could be enacted by its country, considering its current situation
    can_be_enacted = yesTraits: yes/no
    **Supported Scopes**: law"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_establish_any_export_route(arg):
    """
    Check if a country can establish any export routes
    can_establish_any_export_route = <goods key/scope>
    Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_establish_any_import_route(arg):
    """
    Check if a country can establish any import routes
    can_establish_any_import_route = <goods key/scope>
    Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_establish_company(arg):
    """
    Check if the country can establish a new companyTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_form_nation(arg):
    """
    Check if the target country is able to potentially form a nation
    can_form_nation = <tag>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_have_as_subject(arg):
    """
    Checks if a country can have another country as a particular type of subject
    can_have_as_subject = { who = X type = Y }
    Where X = country and Y = subject type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_have_declared_interest_here(arg):
    """
    Check if the target country scope fulfills the rules for conditions for having a declared interest in the strategic region in scope. Does not check for availability of declared interests.
    can_have_declared_interest_here = c:SWETraits: country scope
    **Supported Scopes**: strategic_region
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_have_political_movement(arg):
    """
    Checks if a political movement for the specified law can arise in scope country
    can_have_political_movement = law_type:law_landed_votingTraits: law_type scope
    **Supported Scopes**: country
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_have_subjects(arg):
    """
    Check if the country is able to have subjects of it sownTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_queue_building_levels(arg):
    """
    Checks if the building's owner could queue the provided number of additional levels without hitting a level or resource potential cap
    can_queue_building_levels = number
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_research(arg):
    """
    True if a country can research an technology
    can_research = technology
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_start_tutorial_lesson(arg):
    """
    Can the specified tutorial lesson be started?
    can_start_tutorial_lesson = reactive_advice_successionAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def can_take_on_scaled_debt(arg):
    """
    Checks if scoped country can take on a certain amount of scaled debt from another country
    can_take_on_scaled_debt = { who = X value = Y }
    Where X = country and Y = decimal value
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def cash_reserves_available(arg):
    """
    Evaluates a production building's available cash reserves
    cash_reserves_available > 25000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def cash_reserves_ratio(arg):
    """
    Evaluates a production building's available cash reserve ratio compared to its maximum
    Returns 1 if the building has no maximum cash reserves
    cash_reserves_ratio > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def character_is_discriminated(arg):
    """
    Checks if character is discriminated against
    character_is_discriminated = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def character_supports_political_movement(arg):
    """
    Checks whether the scoped character supports a political movement
    character_supports_political_movement = yes/noTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def check_area(arg):
    """
    Compares areas of object to another object
    **Supported Scopes**: country, province, state, state_region, strategic_region, theater"""
    return default(inspect.stack()[0][3], arg)
    
    
def civil_war_progress(arg):
    """
    Compare progress of civil war
    civil_war_progress > 0.50Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: civil_war"""
    return default(inspect.stack()[0][3], arg)
    
    
def commander_is_available(arg):
    """
    Check if a commander is not busy
    commander_is_available = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def commander_pm_usage(arg):
    """
    Checks how the ratio of Combat Units on the scoped Commander, on the target country's side, with the specified Production Method compares to the value
    commander_pm_usage = { target = X production_method = Y value <comparator> Z}
    where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def commander_rank(arg):
    """
    Compares the commanders rank
    commander_rank > 2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_duration(arg):
    """
    Compares the maximum of all the very roughly approximated weeks remaining to finish the constructions in any queue: construction_queue_duration < 52Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_government_duration(arg):
    """
    Compares the very roughly approximated weeks remaining to finish the constructions in the government queue: construction_queue_government_duration < 52Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_num_queued_government_levels(arg):
    """
    Compares the number of government constructed building levels in the construction queueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_num_queued_levels(arg):
    """
    Compares the number of building levels in the construction queueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_num_queued_private_levels(arg):
    """
    Compares the number of privately constructed building levels in the construction queueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def construction_queue_private_duration(arg):
    """
    Compares the very roughly approximated weeks remaining to finish the constructions in the private queue: construction_queue_private_duration < 52Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def contains_capital_of(arg):
    """
    Checks if scoped state region contains the capital of target tag
    contains_capital_of = country scope/tag
    **Supported Scopes**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_army_unit_type_fraction(arg):
    """
    Checks that a country has a certain percentage of a specific army unit type
    scope:example_formation = {
    country_military_unit_type_fraction = {
    target = unit_type:key
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_can_have_mass_migration_to(arg):
    """
    Checks if the scoped country can have mass migration to target country
    can_have_mass_migration_to = c:countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_definition_has_culture(arg):
    """
    Checks if a culture is one of the cultures of the country definition
    country_definition_has_culture = <culture>Traits: culture scope
    **Supported Scopes**: country_definition
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_building_group_levels(arg):
    """
    Checks the sum of building levels for a building group in a country
    country_has_building_group_levels = {
    type = bg_heavy_industry
    value >= 100 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_building_levels(arg):
    """
    Checks the sum of building levels for a country
    country_has_building_levels >= 10 Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_building_type_levels(arg):
    """
    Checks the sum of building levels for a building type in a country
    country_has_building_type_levels = {
    target = bt:building_barracks
    value  >= 100Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_local_shortage(arg):
    """
    Whether the scoped market goods are in shortage in the target country
    country_has_local_shortage = scope:example_countryTraits: country scope
    **Supported Scopes**: market_goods
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_primary_culture(arg):
    """
    Checks if a culture is one of the primary cultures in the country
    country_has_primary_culture = <culture>Traits: culture scope
    **Supported Scopes**: country
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_has_state_religion(arg):
    """
    Checks if a religion is the state religion in the country
    country_has_accepted_religion = <religion>Traits: religion scope
    **Supported Scopes**: country
    **Supported Targets**: religion"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_navy_unit_type_fraction(arg):
    """
    Checks that a country has a certain percentage of a specific navy unit type
    scope:example_formation = {
    country_navy_unit_type_fraction = {
    target = unit_type:key
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_or_subject_owns_entire_state_region(arg):
    """
    Checks whether the scoped country or any of its subjects owns the entire specified state region
    country_or_subject_owns_entire_state_region = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_pm_usage(arg):
    """
    Checks how the ratio of Combat Units (of the same type) on the scoped Country with the specified Production Method compares to the value
    country_pm_usage = { target = X production_method = Y value <comparator> Z}
    where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_rank(arg):
    """
    Compares a Country's Power Ranking
    country_rank < rank_value:major_powerTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_tier(arg):
    """
    Compare tier of country tag
    country_tier = x
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def country_turmoil(arg):
    """
    Compares the country's population weighted turmoil
    country_turmoil > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_accepted(arg):
    """
    Checks if pop's culture is accepted
    culture_accepted = boolTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_can_have_mass_migration_to(arg):
    """
    Checks if the scoped culture can have mass migration to target country
    can_have_mass_migration_to = c:countryTraits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_is_discriminated_in(arg):
    """
    Checks if a culture is discriminated against within the scope country
    culture_is_discriminated_in = c:USATraits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_percent_country(arg):
    """
    Checks that a country's population has a certain percentage of a specific culture
    scope:example_country = {
    culture_percent_country = {
    target = cu:dixie
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_percent_state(arg):
    """
    Checks that a state's population has a certain percentage of a specific culture
    scope:example_state = {
    culture_percent_state = {
    target = cu:dixie
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def culture_secession_progress(arg):
    """
    Checks the culture's progress percentage towards secession in a country. 0 if no secession movement is active for the culture.
    culture_secession_progress = { target = scope:example_country value > 0.5 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def current_manpower(arg):
    """
    Compares the current manpower of a battle side
    manpower > 10000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: battle_side"""
    return default(inspect.stack()[0][3], arg)
    
    
def current_tooltip_depth(arg):
    """
    Returns the number of tooltips currently open on screenAn interface trigger, can only be used in specific places
    Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def custom_description(arg):
    """
    Wraps triggers that get a custom description instead of the auto-generated one
    custom_description = {
    text = <trigger_localization_key>
    subject = <optional subject scope> #    return default(inspect.stack()[0][3], arg)
    
    
defaults to current scope
    object = <optional object scope>
    value = <optional script value>
    ... triggers ...
    }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def custom_tooltip(arg):
    """
    Replaces the tooltips for the enclosed triggers with a custom text
    custom_tooltip = {
    text = <text>
    subject = <scope> (optional)
    <trigger>
    }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def day_value(arg):
    """
    Day valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def daynight_value(arg):
    """
    DayNight valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def debug_log(arg):
    """
    Log whether the parent trigger succeeded or failed
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def debug_log_details(arg):
    """
    Log whether the parent trigger succeeded or failed. Log which children succeeded or failed
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def devastation(arg):
    """
    Compares the devastation of a given state
    devastation > 5Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def diplomatic_play_pm_usage(arg):
    """
    Checks how the ratio of Combat Units (of the same type) on the scoped Diplomatic Play, on the target country's side, with the specified Production Method compares to the value
    diplomatic_play_pm_usage = { target = X production_method = Y value <comparator> Z}
    where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def earnings(arg):
    """
    Compare a building's current annual earnings per employee
    earnings >= 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def election_momentum(arg):
    """
    Compare election momentum of the scoped party against a value
    election_momentum = 0.75Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def empty_agitator_slots(arg):
    """
    Checks number of empty agitator slots in a country
    empty_agitator_slots >= 1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enacting_any_law(arg):
    """
    Checks if you're enacting any law.
    enacting_any_law = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enactment_chance(arg):
    """
    Compares the current enactment chance in scope country (including values from enactment modifier)Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enactment_chance_without_enactment_modifier(arg):
    """
    Compares the current enactment chance in scope country but excludes values from enactment modifierTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enactment_phase(arg):
    """
    Compares the current law enactment phase in scope country.Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enactment_setback_count(arg):
    """
    Compares the current enactment setback count in scope country.Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enemy_contested_wargoals(arg):
    """
    Determines the fraction of wargoals that enemies in the war are currently contesting
    enemy_contested_wargoals = { target = scope:war value > 0.4 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def enemy_occupation(arg):
    """
    Determines the (weighted) enemy occupation score of a country
    enemy_occupation > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def error_check(arg):
    """
    Checks an error in code that specifically uses the CErrorTable::CheckTrigger path, in general avoid this and just use normal script
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def escalation(arg):
    """
    Checks whether escalation has passed a certain threshold
    escalation > -58Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def exists(arg):
    """
    Checks whether the specified scope target exists (check for not being the null object)
    exists = from.owner.var:cool_var.mother
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def expanding_institution(arg):
    """
    Checks if the institution is expanding
    expanding_institution = <scope/key>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def experience_level(arg):
    """
    Compares the character experience level
    experience_level > 1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def flotilla_manpower(arg):
    """
    Compares the current total manpower of a country's Flotillas
    flotilla_manpower > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def formation_army_unit_type_fraction(arg):
    """
    Checks that a formation has a certain percentage of a specific army unit type
    scope:example_formation = {
    country_military_unit_type_fraction = {
    target = unit_type:key
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def formation_navy_unit_type_fraction(arg):
    """
    Checks that a formation has a certain percentage of a specific navy unit type
    scope:example_formation = {
    formation_navy_unit_type_fraction = {
    target = unit_type:key
    value >= 0.2
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def free_arable_land(arg):
    """
    Check free arable land in state
    free_arable_land > 0Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def front_side_pm_usage(arg):
    """
    Checks how the ratio of Combat Units on the scoped Front, on the target country's side, with the specified Production Method compares to the value
    front_side_pm_usage = { target = X production_method = Y value <comparator> Z}
    where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: front"""
    return default(inspect.stack()[0][3], arg)
    
    
def game_date(arg):
    """
    Compare to current game date
    current_game_date = 1837.1.1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def global_country_ranking(arg):
    """
    Compares a Country's Power Ranking (position)
    global_country_ranking > 42Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def global_population(arg):
    """
    Compares the global population
    global_population > 2000000000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def global_variable_list_size(arg):
    """
    Checks the size of a variable list
    variable_list_size = { name = X target >= Y }
    Where X is the name of the variable
    Where Y is a script value or number
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def gold_reserves(arg):
    """
    Does the country have the required gold reserves
    gold_reserves > 500Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def gold_reserves_limit(arg):
    """
    Compares the country's gold reserves limit
    gold_reserves > gold_reserves_limitTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def government_legitimacy(arg):
    """
    Compare LegitimacyTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def government_transfer_of_power(arg):
    """
    Checks country's government's transfer of power
    government_transfer_of_power = keyTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def government_wage_level(arg):
    """
    Compares the government wage level of scoped country
    government_wage_level = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def government_wage_level_value(arg):
    """
    Compares the government wage level value of scoped country
    government_wage_level_value = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_active_building(arg):
    """
    True if a state has an active building type
    has_active_building = building
    **Supported Scopes**: market, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_active_peace_deal(arg):
    """
    True if the country is in a war where there is a proposed peace deal
    has_active_peace_deal = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_active_production_method(arg):
    """
    Checks if a scoped building has the specified production method active
    has_active_production_method = key
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_any_secessionists_broken_out(arg):
    """
    Check if the country has secessionists broken outTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_any_secessionists_growing(arg):
    """
    Check if the country has any secessionists growingTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_any_secessionists_possible(arg):
    """
    Check if the country has any new secessionists possibleTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_assimilating_pops(arg):
    """
    Check if a state has any pops currently in the process of assimilating.Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_attitude(arg):
    """
    Checks if scoped country has a particular attitude towards another country
    has_attitude = { who = X attitude = Y }
    Where X = country and Y = attitude type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_battle_condition(arg):
    """
    True if the battle side currently has a condition with the given key
    has_battle_condition = battle_condition_key
    **Supported Scopes**: battle_side"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_building(arg):
    """
    True if a state/market/state region/country has a building type
    has_building = building
    **Supported Scopes**: country, market, state, state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_claim(arg):
    """
    Checks if country in scope has a claim on state/state region
    has_claim = <scope>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_claim_by(arg):
    """
    Checks if a state is claimed by a country
    any_state = {
    owner = root
    has_claim_by = c:MEX
    }Traits: country scope
    **Supported Scopes**: state
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_commander_order(arg):
    """
    Checks whether the scoped character is following the given order
    has_order = order type key/order type scope
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_company(arg):
    """
    Checks if a company of the specified type exists in scope country
    has_company = company_type:company_rheinmetallTraits: company_type scope
    **Supported Scopes**: country
    **Supported Targets**: company_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_completed_subgoal(arg):
    """
    Checks if the scoped country has completed a certain subgoal
    has_completed_subgoal = subgoal_key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_consumption_tax(arg):
    """
    Checks if the country is taxing the target good.
    c:FRA = { has_consumption_tax = g:grain }Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_converting_pops(arg):
    """
    Check if a state has any pops currently in the process of converting.Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_convoys_being_sunk(arg):
    """
    Check if the country has convoys being sunk through convoy raidingTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_cosmetic_dlc(arg):
    """
    Does the client have this cosmetic DLCAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_cultural_obsession(arg):
    """
    Checks if a culture has a certain goods as obsession
    has_cultural_obsession = <goods key>
    **Supported Scopes**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_culture(arg):
    """
    Checks characters culture
    has_culture = culture scope or character scope
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_culture_graphics(arg):
    """
    Checks if a culture has a certain culture_graphics
    has_culture_graphics = <culture graphics key>
    **Supported Scopes**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_decreasing_interests(arg):
    """
    Checks if the country has decreasing interest levelsTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_decree(arg):
    """
    Checks if scope state has a particular type of decree
    has_decree = <key>
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_diplomatic_pact(arg):
    """
    Checks if two countries have an active diplomatic pact of type
    has_diplomatic_pact = { who = X type = Y is_initiator = yes/no }
    Where X = country and Y = diplomatic action type, is_initiator is optional parameter that checks to see if scope country is the original initiator/target of the pact
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_diplomatic_play(arg):
    """
    Check if strategic region has a diplomatic play or notTraits: yes/no
    **Supported Scopes**: strategic_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_diplomatic_relevance(arg):
    """
    Checks if target country is diplomatically relevant for scope country
    has_diplomatic_relevance = <scope>Traits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_diplomats_expelled(arg):
    """
    Checks if country in scope has recently expelled diplomats of event target
    has_diplomats_expelled = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_discrimination_trait(arg):
    """
    Checks if scoped culture or religion has the given discrimination trait
    has_trait = trait
    **Supported Scopes**: culture, religion"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_dlc_feature(arg):
    """
    Does the host have DLC that enables this particular feature
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_employee_slots_filled(arg):
    """
    Checks whether the amount of employees of a certain poptype are above or below a given percentage of the total amount the building can currently hire. I.e. if a building is at 80% (given as 0.8) of its current hiring capacity for Shopkeepers, for example.
    has_employee_slots_filled = { pop_type = X percent = Y }
    Where X is a pop type and Y is a fixed point
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_export_priority_tariffs(arg):
    """
    Checks if scoped country has Import Prioritized tariffs for a good
    has_export_priority_tariffs = <key/scope>Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_failed_hires(arg):
    """
    Checks if a building failed to hire someone last week
    has_failed_hires = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_free_government_reform(arg):
    """
    Check if the country has a free (of radicals) government reform
    has_free_government_reform = <yes/no>Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_game_rule(arg):
    """
    Is the given game rule setting enabled?
    has_game_rule = faster_conversion
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_game_started(arg):
    """
    True if game has started
    has_game_started = boolTraits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_gameplay_dlc(arg):
    """
    Does the host have this gameplay DLC
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_global_highest_gdp(arg):
    """
    Checks if the scoped country has the highest GDP
    has_global_highest_gdp = yes/noTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_global_highest_innovation(arg):
    """
    Checks if the scoped country has the highest weekly innovation
    has_global_highest_innovation = yes/noTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_global_variable(arg):
    """
    Checks whether the current scope has the specified variable set
    has_variable = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_global_variable_list(arg):
    """
    Checks whether the current scope has the specified variable list set
    has_variable_list = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_government_clout(arg):
    """
    Does the country's government have the necessary total CloutTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_government_type(arg):
    """
    Is the country's government type as specified
    has_government_type = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_healthy_economy(arg):
    """
    Check if the country has a healthy economyTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_high_attrition(arg):
    """
    Checks if a Military Formation's attrition risk is higher than the base value for their type
    has_high_attrition = boolTraits: yes/no
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_homeland(arg):
    """
    Checks if scoped culture has a homeland in target state or state region
    has_homeland = state/state region
    **Supported Scopes**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_ideology(arg):
    """
    Check if scoped object has ideology
    **Supported Scopes**: character, interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_import_priority_tariffs(arg):
    """
    Checks if scoped country has Import Prioritized tariffs for a good
    has_import_priority_tariffs = <key/scope>Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_institution(arg):
    """
    Checks if scope country has a particular type of institution
    has_institution = <scope/key>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_insurrectionary_interest_groups(arg):
    """
    Check if the country has Interest Groups that are insurrectionaryTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_interest_marker_in_region(arg):
    """
    True if scope country has an interest marker in target region
    has_interest_marker_in_region = region scope/tag
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_journal_entry(arg):
    """
    Check if the country has at least one active journal entry of the specified type
    has_journal_entry = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_label(arg):
    """
    Check if the scope object has the specified label
    has_label = label_key
    **Supported Scopes**: province"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_law(arg):
    """
    Checks if a country has a certain Law activeTraits: law_type scope
    **Supported Scopes**: country
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_local_variable(arg):
    """
    Checks whether the current scope has the specified variable set
    has_variable = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_local_variable_list(arg):
    """
    Checks whether the current scope has the specified variable list set
    has_variable_list = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_map_interaction(arg):
    """
    Checks if the map interaction type is active
    has_map_interaction = keyAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_map_interaction_diplomatic_action(arg):
    """
    Checks if our current map interaction is a specific diplomatic action
    has_map_interaction_diplomatic_action = <key>An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_map_interaction_export_goods(arg):
    """
    Checks if the specified lens option is to export the specified goods
    has_selected_export_option_for_goods = <scope>An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_map_interaction_import_goods(arg):
    """
    Checks if the specified lens option is to import the specified goods
    has_selected_import_option_for_goods = <scope>An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_military_formation(arg):
    """
    Checks if character has a Military Formation
    has_military_formation = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_mobilization_option(arg):
    """
    Checks that a formation has a specific mobilization option
    has_mobilization_option = mobilization_option:keyTraits: mobilization_option scope
    **Supported Scopes**: military_formation
    **Supported Targets**: mobilization_option"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_mobilizing_unit(arg):
    """
    Checks if any Building in a scoped State maintains any Combat Units that are currently mobilizing
    has_mobilizing_unit = boolTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_modifier(arg):
    """
    Check if a supported scope has a certain timed modifier
    Supported scopes: Country, Character, State, Building, InterestGroup, PoliticalMovement, Institution, Front
    has_modifier = <key>
    **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_no_priority_tariffs(arg):
    """
    Checks if scoped country has Unprioritized tariffs for a good
    has_no_priority_tariffs = <key/scope>Traits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_objective(arg):
    """
    Checks if the scoped country has a certain objective type
    has_objective = objective_type_key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_ongoing_assimilation(arg):
    """
    Checks if the scoped pop has ongoing cultural assimilation
    has_ongoing_assimilation = yesTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_ongoing_conversion(arg):
    """
    Checks if the scoped pop has ongoing religious conversion
    has_ongoing_conversion = yesTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_overlapping_interests(arg):
    """
    Checks if country in scope has an overlapping interest marker with any of target country's interests
    has_overlapping_interests = <scope>Traits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_party(arg):
    """
    True if IG scope has a party
    has_party = boolTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_party_member(arg):
    """
    Checks if the target interest group is a member of scope party
    has_party_member = <ig>Traits: interest_group scope
    **Supported Scopes**: party
    **Supported Targets**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_play_goal(arg):
    """
    Checks if diplomatic play has a certain war goal type
    has_play_goal = return_state
    **Supported Scopes**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_political_movement(arg):
    """
    Checks if a political movement for the specified law exists in scope country
    can_have_political_movement = law_type:law_landed_votingTraits: law_type scope
    **Supported Scopes**: country
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_pop_culture(arg):
    """
    Checks if pop has specific culture
    has_pop_culture = culture
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_pop_religion(arg):
    """
    Checks if pop has specific religion
    has_religion = religion
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_port(arg):
    """
    Check if state has at least one port
    has_port = yes/noTraits: yes/no
    **Supported Scopes**: country, market, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_possible_decisions(arg):
    """
    Check if a country has any possible Decisions
    has_possible_decisions = yesTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_potential_resource(arg):
    """
    Checks if the specificed building group is allowed in the scoped state. Used to check if a state can potentially produce a resource
    has_potential_resource = bg_rubber_plantations
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_potential_to_form_country(arg):
    """
    Check if the target country could ever be able to form a nation
    has_potential_to_form_country = <tag>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_reached_end_date(arg):
    """
    True if the end date (N    return default(inspect.stack()[0][3], arg)
    
    
defines::NGame::END_DATE) has been reached
    has_reached_end_date = yesTraits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_religion(arg):
    """
    Checks characters religion
    has_religion = religion/character scope
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_researchable_technology(arg):
    """
    Check if the country has any researchable technology left.Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_revolution(arg):
    """
    Check if the country has revolutionary uprisingTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_revolution_over_law_type(arg):
    """
    Checks if a country is having a revolution over a particular law type
    has_revolution_over_law_type = law_type:law_autocracyTraits: law_type scope
    **Supported Scopes**: country
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_role(arg):
    """
    Checks if character has the specified role
    has_role = role
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_ruling_interest_group(arg):
    """
    Does the country's government include the named IG
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_ruling_interest_group_count(arg):
    """
    Does the country's government consist of the specified number of IGsTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_secret_goal(arg):
    """
    Checks if scoped country has a particular secret goal towards another country
    has_secret_goal = { who = X secret_goal = Y }
    Where X = country and Y = secret_goal type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_state_in_state_region(arg):
    """
    Check if country has a state in the state region
    has_state_in_state_region = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_state_religion(arg):
    """
    Check if the Pop has the state religionTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_state_trait(arg):
    """
    Checks if scoped state has a certain trait
    has_state_trait = key
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_strategic_adjacency(arg):
    """
    Checks if country in scope has a strategic adjacency (direct/coastal/wargoal adjacency) to target state/country
    has_strategic_adjacency = <scope>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_strategic_land_adjacency(arg):
    """
    Checks if country in scope has a strategic adjacency (direct land border or wargoal adjacency only) to target state/country
    has_strategic_adjacency = <scope>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_strategy(arg):
    """
    Checks if country in scope has a particular AI strategy
    has_strategy = <key>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_subject_relation_with(arg):
    """
    Checks if country in scope is subject or overlord of event target
    has_subject_relation_with = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_sufficient_construction_capacity_for_investment(arg):
    """
    Check if country has enough construction capacity to be spending all of its incoming investment pool funds.Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_technology_progress(arg):
    """
    Does the country have the required progress for an technology
    has_technology_progress = { technology = X progress = Y }
    Where X is an technology and Y is a fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_technology_researched(arg):
    """
    True if a country has researched an technology
    has_technology_researched = <scope/key>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_template(arg):
    """
    Checks if character was made from the specified template
    has_template = template_key
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_terrain(arg):
    """
    Check if the province has the specified terrain type
    has_terrain = terrain_key
    **Supported Scopes**: province"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_trait(arg):
    """
    Checks if character has specific trait
    has_trait = trait
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_treaty_port_in_country(arg):
    """
    Checks if the scoped country has a treaty port in target country
    c:POR = { has_treaty_port_in_country = c:CHI }Traits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_truce_with(arg):
    """
    Check if a country has a truce with a different target country
    has_truce_with = c:GBRTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_unification_candidate(arg):
    """
    Check if there is at least one unification candidate for country tag
    has_country_unification_candidate = GER
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_unit_type(arg):
    """
    Checks if a Combat Unit is of the specified type
    has_unit_type = unit_type:keyTraits: combat_unit_type scope
    **Supported Scopes**: new_combat_unit
    **Supported Targets**: combat_unit_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_variable(arg):
    """
    Checks whether the current scope has the specified variable set
    has_variable = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_variable_list(arg):
    """
    Checks whether the current scope has the specified variable list set
    has_variable_list = name
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_war_exhaustion(arg):
    """
    Checks the war exhaustion of the target country in the scoped war
    has_war_exhaustion = { target = c:GBR value > 50 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_war_goal(arg):
    """
    Checks if war has a certain war goal type
    has_war_goal = return_state
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_war_support(arg):
    """
    Checks the war support of the target country in the scoped war
    has_war_support = { target = c:GBR value > 50 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_war_with(arg):
    """
    Checks if country in scope is at war with event target
    has_war_with = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def has_wasted_construction(arg):
    """
    Check if country is wasting any of its produced construction.Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def hidden_trigger(arg):
    """
    AndTrigger that doesn't generate tooltips for contents within
    hidden_trigger = {}
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def highest_secession_progress(arg):
    """
    Compares the highest secession progress of any secession movement in a given country
    highest_secession_progress > 0.7Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def ig_approval(arg):
    """
    Compare to scoped interest group approval
    Usages: ig_approval > 2, ig_approval < happyTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def ig_clout(arg):
    """
    Compare to scoped interest group's clout
    ig_clout >= 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def ig_government_power_share(arg):
    """
    Compare to scoped interest group's political strength divided by total government political strength
    ig_government_power_share >= 0.5Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def ig_state_pol_strength_share(arg):
    """
    True if IG in scope has scripted political strength in state
    ig_state_pol_strength_share = {
    target = scope:target_ig
    value = 0.3
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def in_default(arg):
    """
    Check if the country is currently in default
    Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def in_election_campaign(arg):
    """
    Check if the country is in election campaign period
    in_election_campaign = <yes/no>Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def incorporation_progress(arg):
    """
    Check incorporation progress in state
    incorporation_progress > 0.25Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def influence(arg):
    """
    Compares the available influence of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def infrastructure(arg):
    """
    Compares the infrastructure value of a given state
    infrastructure > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state, state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def infrastructure_usage(arg):
    """
    Compares the infrastructure usage value of a given state
    infrastructure_usage > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state, state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def initiator_is(arg):
    """
    Checks who the initiator of a diplomatic play is
    initiator_is = countryTraits: country scope
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def institution_investment_level(arg):
    """
    Compares the level of investment in an institution
    institution_investment_level = { institution = <key> value = <comparator value> }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def interest_group_population(arg):
    """
    Compares population number in an interest group
    interest_group_population > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def interest_group_population_percentage(arg):
    """
    Compares percentage of population in an interest group
    interest_group_population_percentage > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def interest_group_supports_political_movement(arg):
    """
    Checks whether the scoped interest group supports a political movement
    interest_group_supports_political_movement = yes/noTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def investment_pool(arg):
    """
    Does the country have this amount of money saved in its investment pool
    investment_pool > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def investment_pool_gross_income(arg):
    """
    Does the country have this amount of gross income (income before expenses) for its investment pool
    investment_pool_gross_income > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def investment_pool_net_income(arg):
    """
    Does the country have this amount of net income (income after expenses) for its investment pool
    investment_pool_net_income > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_active(arg):
    """
    Checks if a naval invasion is currently active (started or ongoing)
    is_active = boolTraits: yes/no
    **Supported Scopes**: color"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_adjacent_to_country(arg):
    """
    Checks if country in scope is adjacent to a target country
    is_adjacent_to_country = <scope>Traits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_adjacent_to_state(arg):
    """
    Checks if country in scope is adjacent to a target state
    is_adjacent_to_state = <scope>Traits: state scope
    **Supported Scopes**: country
    **Supported Targets**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_advancing_on_front(arg):
    """
    Checks if a commander is advancing on a front
    is_advancing_on_front = frontTraits: front scope
    **Supported Scopes**: character
    **Supported Targets**: front"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_ai(arg):
    """
    True if country scope is controlled by an AI
    is_ai = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_army(arg):
    """
    Checks if a military formation is Army
    is_army = boolTraits: yes/no
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_at_war(arg):
    """
    Check if the country is at warTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_attacker_in_battle(arg):
    """
    Checks if a Commander is attacker in a battle
    is_attacker_in_battle = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_banning_goods(arg):
    """
    Check if a country is banning a good
    is_banning_goods = <goods key/scope>
    
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_being_bolstered(arg):
    """
    Check if scoped ig is being bolstered
    is_being_bolstered = <yes>/<no>Traits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_being_suppressed(arg):
    """
    Check if scoped ig is being suppressed
    is_being_suppressed = <yes>/<no>Traits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_buildable(arg):
    """
    Check if a building is buildable = yes (    return default(inspect.stack()[0][3], arg)
    
    
default)
    is_buildable = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_building_group(arg):
    """
    True if scope is a building of given group
    building_group = building
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_building_type(arg):
    """
    True if scope is a building of given type
    is_building_type = building
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_building_type_expanded(arg):
    """
    Checks if the CProductionMethodsPanelEntry for a particular CBuildingType is expanded
    is_building_type_expanded = <scope/key>An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_busy(arg):
    """
    Check if character is busy
    is_busy = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_capital(arg):
    """
    Check if state is the capital of the owner = boolTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_character_alive(arg):
    """
    Checks if the scoped character is alive
    is_character_alive = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_civil_war_type(arg):
    """
    Check if the scoped civil war is of a specific type
    is_civil_war_type = revolution / secession
    **Supported Scopes**: civil_war"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_coastal(arg):
    """
    Check if state borders a (non-impassable) sea region
    is_coastal = yes/noTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_construction_paused(arg):
    """
    Check if construction in a state is paused.Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_consumed_by_government_buildings(arg):
    """
    Check if the market goods is instrumental in running the bureaucratic machineTraits: yes/no
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_consumed_by_military_buildings(arg):
    """
    Check if the goods is instrumental in running the war machineTraits: yes/no
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_country_alive(arg):
    """
    Checks if the scoped country is alive, i.e. if it has at least one state on the map and can be interacted with
    is_country_alive = yes/noTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_country_type(arg):
    """
    Checks the countrys type
    is_country_type = country type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_defender_in_battle(arg):
    """
    Checks if a Commander is defender in a battle
    is_defender_in_battle = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_action_type(arg):
    """
    Checks diplomatic pact is of a certain action type
    is_diplomatic_action_type = diplomatic action type
    **Supported Scopes**: diplomatic_pact"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_pact_in_danger(arg):
    """
    Checks if diplomatic pact is in danger of breaking
    is_diplomatic_pact_in_danger = yesTraits: yes/no
    **Supported Scopes**: diplomatic_pact"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_ally_of(arg):
    """
    Checks if country in scope is in a diplomatic play together with event target
    is_diplomatic_play_ally_of = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_committed_participant(arg):
    """
    True if country is a committed participant of any diplomatic play
    is_diplomatic_play_participant = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_enemy_of(arg):
    """
    Checks if country in scope is in a diplomatic play against event target
    is_diplomatic_play_enemy_of = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_initiator(arg):
    """
    True if country is the initiator of any diplomatic play
    is_diplomatic_play_initiator = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_involved_with(arg):
    """
    Checks if country in scope is involved in the same diplomatic play as event target
    is_diplomatic_play_involved_with = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_participant_with(arg):
    """
    Checks if country in scope is a committed participant in the same diplomatic play as event target
    is_diplomatic_play_participant_with = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_target(arg):
    """
    True if country is the target of any diplomatic play
    is_diplomatic_play_target = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_type(arg):
    """
    Checks diplomatic play is of a certain type
    is_diplomatic_play_type = play type
    **Supported Scopes**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_diplomatic_play_undecided_participant(arg):
    """
    True if country is a undecided participant of any diplomatic play
    is_diplomatic_play_participant = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_direct_subject_of(arg):
    """
    Checks if country in scope is a direct subject (not subject-of-subject) of event target
    is_subject_of = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_employed(arg):
    """
    Check if the pop is employedTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_enacting_law(arg):
    """
    Checks if the scoped country is enacting a specific law type.
    is_enacting_law = law_type:law_conscriptionTraits: law_type scope
    **Supported Scopes**: country
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_expanding_institution(arg):
    """
    Are you expanding an institution
    is_expanding_institution = <yes>/<no>Traits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_female(arg):
    """
    Check if character is female
    is_female = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_fleet(arg):
    """
    Checks if a military formation is Fleet
    is_fleet = boolTraits: yes/no
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_forced_pact(arg):
    """
    Check if a diplomatic pact has a forced duration due to reasons such as a sway or obligationTraits: yes/no
    **Supported Scopes**: diplomatic_pact"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_fully_mobilized(arg):
    """
    Checks if the Military Formation is fully mobilized
    is_fully_mobilized = boolTraits: yes/no
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_game_paused(arg):
    """
    Checks if the game is paused
    is_game_paused = yes/noAn interface trigger, can only be used in specific places
    Traits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_gamestate_tutorial_active(arg):
    """
    Is the gamestate tutorial active? See save_progress_in_gamestate in tutorial_lesson_chains documentation.An interface trigger, can only be used in specific places
    Traits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_goal_complete(arg):
    """
    Check if the journal entry's goal has been met
    is_goal_complete = yes/noTraits: yes/no
    **Supported Scopes**: journalentry"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_government_funded(arg):
    """
    Check if a building is is_government_funded
    is_government_funded = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_heir(arg):
    """
    Checks whether the scoped character is an heir
    is_heir = yes / noTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_historical(arg):
    """
    Check if character is historical
    is_historical = yes/noTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_home_country_for(arg):
    """
    Checks if a country is the home country for target countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_homeland(arg):
    """
    Checks if scoped state region is a homeland of target culture
    is_homeland = culture scope/name
    **Supported Scopes**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_homeland_of_country_cultures(arg):
    """
    Checks if state is homeland of any of the target country's primary cultures
    is_homeland_of_country_cultures = <country>Traits: country scope
    **Supported Scopes**: state
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_immune_to_revolutions(arg):
    """
    Checks if the country has been set to be immune to revolutions via set_immune_to_revolutions
    Warning: This does not check if the country is naturally immune to revolutions due to for example being a revolutionary country itself, only for the effects of set_immune_to_revolutions.
    is_immune_to_revolutions = yes/noTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_battle(arg):
    """
    Checks if a Commander is engaged in battle
    is_in_battle = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_customs_union(arg):
    """
    Check if the country is part of a customs unionTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_exile_pool(arg):
    """
    Checks whether the scoped character is in the exile pool
    is_in_exile_pool = yes/noTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_government(arg):
    """
    True if IG scope is in the government
    is_in_government = boolTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_list(arg):
    """
    Checks if a target in in a list
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_revolt(arg):
    """
    Check if a state has any chance to split off into a revolutionary or seceding country
    is_in_revolt = yes/no.Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_void(arg):
    """
    Check if character is in the void
    is_in_void = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_in_war_together(arg):
    """
    Checks if country in scope is in war on the same side as event target
    is_in_war_together = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_incorporated(arg):
    """
    Check if state is incorporated = boolTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_insurrectionary(arg):
    """
    True if IG scope is contributing to a brewing revolution
    is_insurrectionary = boolTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_interest_active(arg):
    """
    Is the interest marker active
    is_interest_active = yes/noTraits: yes/no
    **Supported Scopes**: interest_marker"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_interest_group_type(arg):
    """
    Checks if Interest Group is of a certain type
    Can also be used on characters directly
    is_interest_group_type = x
    **Supported Scopes**: character, interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_isolated_from_market(arg):
    """
    Check if a state is isolated from its marketTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_junior_in_customs_union(arg):
    """
    True if country is a junior country in a customs custom
    is_junior_in_customs_union = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_land_theater(arg):
    """
    Checks if a theater is a land theater
    is_land_theater = boolTraits: yes/no
    **Supported Scopes**: theater"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_largest_state_in_region(arg):
    """
    Check if state is the largest in the state region = boolTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_lens_open(arg):
    """
    Checks if a certain lens is open, specified as a lens key. Specify an optional named tab to check if this tab is open.
    is_lens_open = { lens = lens_key tab_name = tab_key }An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_local_player(arg):
    """
    True if country scope is a player
    is_local_player = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_losing_power_rank(arg):
    """
    Check if the country is in the process of dropping in power rankingTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_marginal(arg):
    """
    True if IG scope is marginal
    is_marginal = boolTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_mass_migration_origin(arg):
    """
    Checks if the scoped country is the origin of mass migration
    is_mass_migration_origin = yesTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_mass_migration_origin_of_culture(arg):
    """
    Checks if the scoped country origin of mass migration of specific culture
    is_mass_migration_origin_of_culture = cu:example_cultureTraits: culture scope
    **Supported Scopes**: country
    **Supported Targets**: culture"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_mass_migration_target(arg):
    """
    Mass migration target is state.
    any_state = { limit = { owner = ROOT is_mass_migration_target = yes } }Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_member_of_party(arg):
    """
    Checks if Interest Group is a member of target party
    is_member_of_party = <party>Traits: party scope
    **Supported Scopes**: interest_group
    **Supported Targets**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_mobilized(arg):
    """
    Checks if the military formation is mobilized
    is_mobilized = boolTraits: yes/no
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_monarch(arg):
    """
    Checks if character is a monarch of a country with hereditary succession
    is_monarch = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_naval_invasion_stalled_due_to_orders(arg):
    """
    Checks if a naval invasion is stalled due to wrong admiral orders
    is_naval_invasion_stalled = boolTraits: yes/no
    **Supported Scopes**: color"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_objective_completed(arg):
    """
    Is the objective completed for the country in scope?
    is_objective_completed = yesTraits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_on_front(arg):
    """
    Checks if a character or military formation has been assigned to a Front and has arrived there
    is_on_front = yes/noTraits: yes/no
    **Supported Scopes**: character, military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_owed_obligation_by(arg):
    """
    Checks if the scoped country is owed a obligation by the target country
    is_owed_obligation_by = c:FRATraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_panel_open(arg):
    """
    Checks if a certain infopanel is open, specified as an event target (target) or as a string (panel_name). Specify an optional named tab (tab_name) to check if this tab is open.
    is_panel_open = { target = <scope> OR panel_name = panel_name tab_name = tab_name }An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_party(arg):
    """
    Checks if the target party is same as scoped party. Will only work on exact same party object, meaning you can't compare across countries.
    is_party = <party>Traits: party scope
    **Supported Scopes**: party
    **Supported Targets**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_party_type(arg):
    """
    Checks if the scoped party's type is the specified one
    is_party_type = party_type_database_key
    **Supported Scopes**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_player(arg):
    """
    True if country scope is a player
    is_player = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_political_movement_type(arg):
    """
    Check if a political movement is a particular type
    is_political_movement_type = movement_to_enact
    
    **Supported Scopes**: political_movement"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_pop_type(arg):
    """
    Checks if pop is of specified type
    is_pop_type = poptype
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_popup_open(arg):
    """
    Checks if the specified popup panel is open
    is_popup_open = popupAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_powerful(arg):
    """
    True if IG scope is influential
    is_powerful = boolTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_primary_culture_of(arg):
    """
    Checks if culture is any of a country's primary cultures
    is_primary_culture_of = <country>Traits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_production_method_active(arg):
    """
    Checks if the building of a particular type in scoped state has the specified production method active
    is_production_method_active = { building_type = <key> production_method = <key> }
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_progressing(arg):
    """
    Check if the journal entry is progressing
    is_progressing = yes/noTraits: yes/no
    **Supported Scopes**: journalentry"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_province_land(arg):
    """
    Check if the province is on landTraits: yes/no
    **Supported Scopes**: province"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_repairing(arg):
    """
    Checks if an Admiral is unavailable and repairing after loosing a naval battle
    is_repairing = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_researching_technology(arg):
    """
    Check if the country is actively researching a tech
    is_researching_technology = <scope/key/any>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_researching_technology_category(arg):
    """
    Check if the country is actively researching a tech category
    is_researching_technology_category = <key/any>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_revolutionary(arg):
    """
    Check if the country is revolutionaryTraits: yes/no
    **Supported Scopes**: country, interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_revolutionary_movement(arg):
    """
    Check whether the scoped political movement is causing a brewing revolution in the country
    is_revolutionary_movement = yes/noTraits: yes/no
    **Supported Scopes**: political_movement"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_rightclick_menu_open(arg):
    """
    Checks if the specified rightclick menu is open
    is_rightclick_menu_open = <menu_key>An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_ruler(arg):
    """
    Checks if character is a ruler/head of state of a country
    is_ruler = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_same_interest_group_type(arg):
    """
    Checks if Interest Group is of the same IG type as target
    is_interest_group_type = scope:neighbor_leading_igTraits: interest_group scope
    **Supported Scopes**: interest_group
    **Supported Targets**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_same_law_group_as(arg):
    """
    Checks if scope law type is in the same group as the target law type scope
    is_same_law_group_as = <law type scope>Traits: law_type scope
    **Supported Scopes**: law_type
    **Supported Targets**: law_type"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_same_party_type(arg):
    """
    Checks if Party is of the same party type as target
    is_same_party_type_as = scope:neighboring_partyTraits: party scope
    **Supported Scopes**: party
    **Supported Targets**: party"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_sea_adjacent(arg):
    """
    Check if state borders a sea region (regular or impassable)
    is_sea_adjacent = yes/noTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_secessionist(arg):
    """
    Check if the country is secessionistTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_set(arg):
    """
    Checks whether the specified scope target has been set (includes being the null object)
    is_set = from.owner.var:cool_var.mother
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_slave_state(arg):
    """
    Check if a state employs or has the potential to employ slaves.Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_split_state(arg):
    """
    Checks if the scoped state is a split state.
    scope:example_state = { is_split_state = yes }Traits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_state_region_land(arg):
    """
    Check if the state region is on landTraits: yes/no
    **Supported Scopes**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_state_religion(arg):
    """
    Checks if the religion is the state religion in a country
    is_accepted_religion = <country>Traits: country scope
    **Supported Scopes**: religion
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_strategic_objective(arg):
    """
    Checks if the scoped State is a Strategic Objective of a Country
    is_strategic_objective = <country>Traits: country scope
    **Supported Scopes**: state
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_strongest_ig_in_government(arg):
    """
    Checks whether the scoped interest group has the most clout out of all interest groups in government
    is_strongest_ig_in_government = yes/noTraits: yes/no
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_subject(arg):
    """
    True if country is a subject
    is_subject = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_subject_of(arg):
    """
    Checks if country in scope is subject (or subject-of-subject) of event target
    is_subject_of = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_subject_type(arg):
    """
    Checks the country's subject type
    is_subject_type = subject type
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_subsidized(arg):
    """
    Check if a building is being subsidized
    is_subsidized = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_subsistence_building(arg):
    """
    Check if a building is a subsistence building
    is_subsistence_building = yes/noTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_supporting_unification_candidate(arg):
    """
    Check if scope country is supporting a unification candidate for a specific country formation
    is_supporting_unification_candidate = { who = c:PRU country_formation = GER }
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_target_in_global_variable_list(arg):
    """
    Checks if a target is in a variable list
    is_target_in_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_target_in_local_variable_list(arg):
    """
    Checks if a target is in a variable list
    is_target_in_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_target_in_variable_list(arg):
    """
    Checks if a target is in a variable list
    is_target_in_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_target_of_wargoal(arg):
    """
    Checks if state is target of any wargoal in wars involving a specific country
    has_war_goal = <country>Traits: country scope
    **Supported Scopes**: state
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_taxing_goods(arg):
    """
    Check if a country is taxing a good
    has_embargo = <goods key/scope>
    
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_trade_route_active(arg):
    """
    Checks if the scoped trade route is active
    is_trade_route_active = yes/noTraits: yes/no
    **Supported Scopes**: trade_route"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_trade_route_productive(arg):
    """
    Checks if the scoped trade route is productive
    is_trade_route_productive = yes/noTraits: yes/no
    **Supported Scopes**: trade_route"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tradeable(arg):
    """
    Check if a goods or market goods is tradeable
    is_tradeable = yes/noTraits: yes/no
    **Supported Scopes**: goods, market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_traveling(arg):
    """
    Checks if the commander is traveling
    is_traveling = boolTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_treaty_port(arg):
    """
    Checks if the scoped state is a treaty port
    is_treaty_port = yes/noTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tutorial_active(arg):
    """
    Is the tutorial active?An interface trigger, can only be used in specific places
    Traits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tutorial_lesson_active(arg):
    """
    Is this the current tutorial lesson?
    is_tutorial_lesson_active = reactive_advice_successionAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tutorial_lesson_chain_completed(arg):
    """
    Has the tutorial lesson chain with the specified key been finished?An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tutorial_lesson_completed(arg):
    """
    has the tutorial lesson with the specified name been finished?An interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_tutorial_lesson_step_completed(arg):
    """
    Has the tutorial lesson step been finished?
    is_tutorial_lesson_step_completed = lesson_key:step_keyAn interface trigger, can only be used in specific places
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_under_colonization(arg):
    """
    Check if state is under colonization
    is_under_colonization = yes/noTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_under_construction(arg):
    """
    Checks if building is under construction
    is_under_construction = boolTraits: yes/no
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_unification_candidate(arg):
    """
    Check if scope country is a unification candidate for country tag
    has_country_unification_candidate = GER
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_violating_sovereignty_of(arg):
    """
    Check if the scoped country is violating the sovereignty of a target country
    is_violating_sovereignty_of = c:GBRTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_vulnerable_front(arg):
    """
    Whether the scoped Front doesn't have any Battalions nor Generals on target side, and the enemy has at least one General.
    is_vulnerable_front = scope:example_countryTraits: country scope
    **Supported Scopes**: front
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_war(arg):
    """
    True if the diplomatic play has escalated into war
    is_war = boolTraits: yes/no
    **Supported Scopes**: diplomatic_play"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_war_participant(arg):
    """
    Check if the target country is participant in a warTraits: country scope
    **Supported Scopes**: war
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def is_warleader(arg):
    """
    Check if country is warleader in warTraits: country scope
    **Supported Scopes**: war
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def isolated_states(arg):
    """
    Compare number of Isolated StatesTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def law_approved_by(arg):
    """
    Checks whether the scoped law is approved by an interest group
    law_approved_by = ig_rural_folk
    **Supported Scopes**: law"""
    return default(inspect.stack()[0][3], arg)
    
    
def law_stance(arg):
    """
    Compares the stance of the scoped character or interest group about the specified law
    **Supported Scopes**: character, interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def leading_producer_of(arg):
    """
    Checks if country is producing the most of a certain good
    leading_producer_of = g:luxury_clothesTraits: goods scope
    **Supported Scopes**: country
    **Supported Targets**: goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def leads_customs_union(arg):
    """
    Check if any other country is part of this country's customs union
    leads_customs_union = boolTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def list_size(arg):
    """
    Checks the size of a list
    list_size = { name = X value >= Y }
    Where X is the name of the list
    Where Y is a script valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def literacy_rate(arg):
    """
    Checks if a pop, state or country has a certain amount of literacy
    literacy = valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country, pop, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def local_variable_list_size(arg):
    """
    Checks the size of a variable list
    variable_list_size = { name = X target >= Y }
    Where X is the name of the variable
    Where Y is a script value or number
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def loyalist_fraction(arg):
    """
    Compares loyalist fraction in pops in state or country, all parameters except value are optional
    loyalist_fraction = { value = x pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def loyalty(arg):
    """
    Compares the loyalty in a given state, i.e. the fraction of Loyalists
    loyalty > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_access(arg):
    """
    Checks the market access of the scoped state
    market_access > 0.8Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_buy_orders(arg):
    """
    Checks if market goods has the specified number of buy orders
    market_goods_buy_orders < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_cheaper(arg):
    """
    Checks if market goods is at least the specified percentage cheaper than base price
    market_goods_cheaper > X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_consumption(arg):
    """
    Checks if market goods has the specified number of total consumption
    market_goods_consumption < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_delta(arg):
    """
    Checks if market has the specified goods delta (production + imports) - (consumption + exports)
    market_goods_delta < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_exports(arg):
    """
    Checks if market goods has the specified number of exports
    market_goods_exports < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_has_goods_shortage(arg):
    """
    Check if market goods has a shortage in the market
    market_goods_has_goods_shortage = yes/noTraits: yes/no
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_imports(arg):
    """
    Checks if market goods has the specified number of imports
    market_goods_imports < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_pricier(arg):
    """
    Checks if market goods is at least the specified percentage more expensive than base price
    market_goods_pricier > X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_production(arg):
    """
    Checks if market goods has the specified number of total production
    market_goods_production < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_sell_orders(arg):
    """
    Checks if market goods has the specified number of sell orders
    market_goods_sell_orders < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_goods_shortage_ratio(arg):
    """
    Compares the shortage ratio of a market goods in its market
    market_goods_shortage_ratio > 0.33Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: market_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def market_has_goods_shortage(arg):
    """
    Check if market has a shortage on any of its building inputs
    market_has_goods_shortage = yes/noTraits: yes/no
    **Supported Scopes**: market"""
    return default(inspect.stack()[0][3], arg)
    
    
def max_num_declared_interests(arg):
    """
    Compares the maximum number of declared interests of scoped country
    max_num_declared_interests = <value>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def max_organization(arg):
    """
    Compares the effective maximum Organization of the Military Formation in scope
    max_organization <     return default(inspect.stack()[0][3], arg)
    
    
define:NMilitary|MILITARY_FORMATION_ORGANIZATION_MAXTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def military_wage_level(arg):
    """
    Compares the military wage level of scoped country
    military_wage_level = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def military_wage_level_value(arg):
    """
    Compares the military wage level value of scoped country
    military_wage_level_value = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def month(arg):
    """
    Compare to current game date month (Jan: 0, Dec: 11)
    month > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def most_powerful_strata(arg):
    """
    Compares an interest groups most powerful strata
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def most_prominent_revolting_interest_group(arg):
    """
    Checks if the most prominent revolting interest group in the scoped state has the given interest group type. Evaluates false if the scoped state is not in revolt.
    most_prominent_revolting_interest_group = ig_landowners
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def nand(arg):
    """
    a negated AND trigger
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def naval_power_projection(arg):
    """
    Compares a Country's naval_power_projection
    scope:example_country = { naval_power_projection < root.naval_power_projectionTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def navy_reserves(arg):
    """
    Compare the amount of Navy ReservesTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def night_value(arg):
    """
    Night valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def nor(arg):
    """
    a negated OR trigger
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def Not(arg):
    """
    negates content of trigger
    **Supported Scopes**: none/all"""
    return default("not", arg)
    
    
def num_casualties(arg):
    """
    Checks the number of total casualties in the scoped war
    num_casualties >= 5000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_country_casualties(arg):
    """
    Checks the number of casualties for the target country in the scoped war
    num_country_casualties = { target = country value < 5000 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_country_dead(arg):
    """
    Checks the number of dead for the target country in the scoped war
    num_country_dead = { target = country value < 5000 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_country_wounded(arg):
    """
    Checks the number of wounded for the target country in the scoped war
    num_country_wounded = { target = country value < 5000 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_dead(arg):
    """
    Checks the number of total dead in the scoped war
    num_dead >= 5000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_declared_interests(arg):
    """
    Compares the number of declared interests of scoped country
    num_declared_interests = <value>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_mobilized_units_in_theater(arg):
    """
    Determines the number of mobilized units belonging to the scoped theater's owner or their allies, in fronts intersecting the scoped theater
    num_mobilized_units_in_theater > 25Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: theater"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_provinces_in_theater(arg):
    """
    Determines the number provinces in the scoped theater
    num_provinces_in_theater > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: theater"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_taxed_goods(arg):
    """
    Compares the number of consumption taxed goods of scoped country
    num_taxed_goods = <value>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def num_wounded(arg):
    """
    Checks the number of total wounded in the scoped war
    num_wounded >= 5000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def number_of_possible_decisions(arg):
    """
    The number of possible Descision a Country can take
    umber_of_possible_decisions > 0Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def occupancy(arg):
    """
    Evaluates a building's current occupancy
    occupancy < 0.25Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def Or(arg):
    """
    at least one entry inside trigger must be true
    **Supported Scopes**: none/all"""
    return default("or", arg)
    
    
def organization(arg):
    """
    Compares the Organization of the Military Formation in scope
    organization <=     return default(inspect.stack()[0][3], arg)
    
    
define:NMilitary|MILITARY_FORMATION_ORGANIZATION_MINTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: military_formation"""
    return default(inspect.stack()[0][3], arg)
    
    
def owes_obligation_to(arg):
    """
    Checks if country in scope owes a obligation to event target
    owes_obligation_to = countryTraits: country scope
    **Supported Scopes**: country
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def owns_entire_state_region(arg):
    """
    Check if country owns entire region
    owns_entire_state_region = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def owns_treaty_port_in(arg):
    """
    Does country own the treaty port in assigned state region
    owns_treaty_port_in = key
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def political_movement_radicalism(arg):
    """
    Compare radicalism of political movement
    political_movement_radicalism > 50Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: political_movement"""
    return default(inspect.stack()[0][3], arg)
    
    
def political_movement_support(arg):
    """
    Compare support of political movement
    political_movement_support > 50Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: political_movement"""
    return default(inspect.stack()[0][3], arg)
    
    
def pollution_amount(arg):
    """
    Compare state region pollutionTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def pollution_generation(arg):
    """
    Compare total pollution generation across all buildings in the stateTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_employment_building(arg):
    """
    Checks if pop is working in a specific building type
    pop_employment_building = building
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_employment_building_group(arg):
    """
    Checks if pop is working in a specific building type
    pop_employment_building = building
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_has_primary_culture(arg):
    """
    Checks if pop's culture is primary
    pop_has_primary_culture = boolTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_is_discriminated(arg):
    """
    Checks if pop is discriminated against
    pop_is_discriminated = boolTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_loyalist_fraction(arg):
    """
    Compares the number of Radicals in a pop to its total size
    pop_loyalty_fraction < 0.5Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_neutral_fraction(arg):
    """
    Compares the number of Neutrals (not Radical, not Loyalist) in a pop to its total size
    pop_neutral_fraction > 0.95Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_radical_fraction(arg):
    """
    Compares the number of Radicals in a pop to its total size
    pop_radical_fraction > 0.25Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_type_percent_country(arg):
    """
    Checks whether the scoped country has <percent> of its population belonging to the specified pop type
    scope:example_country = {
    pop_type_percent_country = {
        pop_type = <pop_type>
        percent <compare operator (<,>,= and so on)> <percent>
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def pop_type_percent_state(arg):
    """
    Checks that a state's population has a certain percentage of a specific pop type
    scope:example_state = {
    pop_type_percent_state = {
    target = pop_type:laborer
    value <= 0.8
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def prefers_law(arg):
    """
    Checks if the scoped interest group prefers the specified law to the comparison law
    **Supported Scopes**: interest_group"""
    return default(inspect.stack()[0][3], arg)
    
    
def prestige(arg):
    """
    Compare prestigeTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def produced_authority(arg):
    """
    Compares the produced authority of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def produced_bureaucracy(arg):
    """
    Compares the produced bureaucracy of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def produced_influence(arg):
    """
    Compares the produced influence of the scoped countryTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def quality_of_life(arg):
    """
    Compares the quality of life of the given pop
    quality_of_life > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def radical_fraction(arg):
    """
    Compares radical fraction in pops in state or country, all parameters except value are optional
    radical_fraction = { value = x pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country, state"""
    return default(inspect.stack()[0][3], arg)
    
    
def relative_infrastructure(arg):
    """
    Compares the infrastructure to infrastructure usage of a state
    relative_infrastructure > 1.1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def religion_accepted(arg):
    """
    Checks if pop's religion is accepted
    religion_accepted = boolTraits: yes/no
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def religion_percent_country(arg):
    """
    Checks that a country's population has a certain percentage of a specific religion
    scope:example_country = {
    religion_percent_country = {
    target = rel:catholic
    value <= 0.8
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def religion_percent_state(arg):
    """
    Checks that a state's population has a certain percentage of a specific religion
    scope:example_state = {
    religion_percent_state = {
    target = rel:catholic
    value <= 0.8
    }
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def remaining_undepleted(arg):
    """
    Check remaining amount of resource, like gold mines in a state
    remaining_undepleted = {
    type = bg_gold_mining
    amount > 1
    }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_region"""
    return default(inspect.stack()[0][3], arg)
    
    
def ruler_can_have_command(arg):
    """
    Checks if the country's government type allows its ruler to have command
    ruler_can_have_command = yes/noTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def save_temporary_scope_as(arg):
    """
    Saves a temporary target for use during the trigger execution
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def save_temporary_scope_value_as(arg):
    """
    Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect
    save_temporary_scope_value_as = { name = <string> value = x }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def scaled_debt(arg):
    """
    Compare value to a country's debt relative to debt ceiling
    scaled_debt = valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def scaled_gold_reserves(arg):
    """
    Compare value to a country's gold reserves relative to reserves limit
    scaled_gold_reserves = valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_heritage_and_other_trait_with_any_primary_culture(arg):
    """
    Checks if culture shares any trait marked as 'heritage' and other 'non-heritage' trait with any of a country's primary cultures
    shares_heritage_and_other_trait_with_any_primary_culture = <country>Traits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_heritage_trait_with_any_primary_culture(arg):
    """
    Checks if culture shares any trait marked as 'heritage' with any of a country's primary cultures
    shares_heritage_trait_with_any_primary_culture = <country>Traits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_heritage_trait_with_state_religion(arg):
    """
    Checks if the religion shares any trait marked as 'religion_group' with a country's religion
    shares_heritage_trait_with_state_religion = <country>Traits: country scope
    **Supported Scopes**: religion
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_non_heritage_trait_with_any_primary_culture(arg):
    """
    Checks if culture shares any trait *other than* one marked as 'heritage' with any of a country's primary cultures
    shares_non_heritage_trait_with_any_primary_culture = <country>Traits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_trait_with_any_primary_culture(arg):
    """
    Checks if the culture shares any trait with any of a country's primary cultures
    shares_trait_with_any_primary_culture = <country>Traits: country scope
    **Supported Scopes**: culture
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def shares_trait_with_state_religion(arg):
    """
    Checks if the religion shares any trait with a country's state religion
    shares_trait_with_state_religion = <country>Traits: country scope
    **Supported Scopes**: religion
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def should_set_wargoal(arg):
    """
    Check if the country is lacking a primary wargoal in any diplomatic play it is part ofTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def should_show_nudity(arg):
    """
    can nudity be shown?
    should_show_nudity = yes/noAn interface trigger, can only be used in specific places
    Traits: yes/no
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def shrinking_institution(arg):
    """
    Checks if the institution is shrinking
    expanding_institution = <scope/key>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def size_weighted_lost_battles_fraction(arg):
    """
    Determines the fraction of battles the target country has lost in the target war, weighted by manpower size of all battles in the war
    size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 }
    add = "size_weighted_lost_battles_fraction(scope:war)"Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def standard_of_living(arg):
    """
    Compares the standard of living of a given pop
    standard_of_living > 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def starting_manpower(arg):
    """
    Compares the starting manpower of a battle side
    starting_manpower > 25000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: battle_side"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_cheaper(arg):
    """
    Checks if state goods is at least the specified percentage cheaper than base price
    state_goods_cheaper > X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_consumption(arg):
    """
    Checks if state goods has the specified number of total consumption
    state_goods_consumption < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_delta(arg):
    """
    Checks if state has the specified goods delta (production - consumption)
    state_goods_delta < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_has_local_goods_shortage(arg):
    """
    Check if state goods has a shortage in a state, but NOT in the whole market
    state_goods_has_local_goods_shortage = yes/noTraits: yes/no
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_pricier(arg):
    """
    Checks if state goods is at least the specified percentage more expensive than base price
    state_goods_pricier > X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_goods_production(arg):
    """
    Checks if state goods has the specified number of total production
    state_goods_production < X
    Where X = fixed pointTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: state_goods"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_has_building_group_levels(arg):
    """
    Checks the sum of building levels for a building group in a state
    state_has_building_group_levels = {
    type = bg_heavy_industry
    value >= 100 }Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_has_building_levels(arg):
    """
    Checks the sum of building levels for a state
    state_has_building_levels >= 10Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_has_building_type_levels(arg):
    """
    Checks the sum of building levels for a building type in a state
    state_has_building_type_levels = {
    target = bt:building_barracks
    value >= 100Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_has_goods_shortage(arg):
    """
    Check if state has a shortage on any of its building inputs
    state_has_goods_shortage = yes/noTraits: yes/no
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_population(arg):
    """
    Checks the total population of the scoped state
    state_population <= 250000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def state_unemployment_rate(arg):
    """
    Checks the unemployment rate (percentage) in the scoped state
    state_unemployment_rate > 0.1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def strata(arg):
    """
    Checks the strata of the scoped pop
    strata >= rich/middle/poorTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def supply_network_strength(arg):
    """
    Compares the country's supply network strength (can exceed 1)
    supply_network_strength > 1.1Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def switch(arg):
    """
    Switch on a trigger for the evaluation of another trigger with an optional fallback trigger.
    switch = {
    trigger = simple_assign_trigger
    case_1 = { <triggers> }
    case_2 = { <triggers> }
    case_n = { <triggers> }
    fallback = { <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def taking_loans(arg):
    """
    Check if the country is currently running a weekly     return default(inspect.stack()[0][3], arg)
    
    
deficit and taking loans to compensateTraits: yes/no
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def target_is(arg):
    """
    Checks who the target of a diplomatic play is
    target_is = countryTraits: country scope
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def tax_capacity(arg):
    """
    Checks the taxation capacity of the scoped state
    tax_capacity > 50Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def tax_capacity_usage(arg):
    """
    Checks the taxation capacity usage of the scoped state
    tax_capacity_usage > 50Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def tax_level(arg):
    """
    Compares the overall tax level of scoped country
    tax_level = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def tax_level_value(arg):
    """
    Compares the overall tax level integer value of scoped country
    income_tax_level_value = <level>Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_manpower(arg):
    """
    Compares the current total manpower of a country's combat units
    total_manpower > 25000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_population(arg):
    """
    Compares the total population of a given country
    total_population > 100000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_population_including_subjects(arg):
    """
    Compares the total population in the scope country and its subjects
    total_population_including_subjects > 40000000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_population_including_subjects_share(arg):
    """
    Compares the total population in the scope country and its subjects' share of the global population
    total_population_including_subjects_share > 0.4Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_population_share(arg):
    """
    Compares the total population of a given country's share of the global population
    total_population_share > 0.02Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def total_urbanization(arg):
    """
    Compares the total urbanization of a given state/ntotal_urbanization > 5Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def trade_route_needs_convoys_to_grow(arg):
    """
    Checks if the scoped trade route needs more convoys to be able to grow
    trade_route_needs_convoys_to_grow = yes/noTraits: yes/no
    **Supported Scopes**: trade_route"""
    return default(inspect.stack()[0][3], arg)
    
    
def trait_value(arg):
    """
    Compares the character's total trait value
    trait_value < experience_levelTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def trigger_else(arg):
    """
    Evaluates the triggers if the display_triggers of preceding 'trigger_if' or 'trigger_else_if' is not mettrigger_if = { limit = { <display_triggers> } <triggers> }
    trigger_else = { <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def trigger_else_if(arg):
    """
    Evaluates the enclosed triggers if the display_triggers of the preceding `trigger_if` or `trigger_else_if` is not met and its own display_trigger of the limit is mettrigger_if = { limit = { <display_triggers> } <triggers> }
    trigger_else_if = { limit = { <display_triggers> } <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def trigger_if(arg):
    """
    Evaluates the triggers if the display_triggers of the limit are met
    trigger_if = { limit = { <display_triggers> } <triggers> }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def turmoil(arg):
    """
    Compares the turmoil in a given state, i.e. the fraction of Radicals
    turmoil > 0.2Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: state"""
    return default(inspect.stack()[0][3], arg)
    
    
def variable_list_size(arg):
    """
    Checks the size of a variable list
    variable_list_size = { name = X target >= Y }
    Where X is the name of the variable
    Where Y is a script value or number
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def war_has_active_peace_deal(arg):
    """
    True if the war has a proposed peace deal
    war_has_active_peace_deal = boolTraits: yes/no
    **Supported Scopes**: war"""
    return default(inspect.stack()[0][3], arg)
    
    
def was_exiled(arg):
    """
    Checks whether the scoped character was exiled
    was_exiled = yes/noTraits: yes/no
    **Supported Scopes**: character"""
    return default(inspect.stack()[0][3], arg)
    
    
def was_formed_from(arg):
    """
    Check if a formed country previously had a specific     return default(inspect.stack()[0][3], arg)
    
    
definition
    was_formed_from = <tag>
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def wealth(arg):
    """
    Checks if a pop has a certain amount of wealth
    wealth = valueTraits: <, <=, =, !=, >, >=
    **Supported Scopes**: pop"""
    return default(inspect.stack()[0][3], arg)
    
    
def weekly_net_fixed_income(arg):
    """
    Does the country have this amount of weekly income after fixed expenses
    weekly_net_income > 1000Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: country"""
    return default(inspect.stack()[0][3], arg)
    
    
def weekly_profit(arg):
    """
    Checks whether the profits the building has made this week are above or below a given value
    weekly_profit >= 20.0Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: building"""
    return default(inspect.stack()[0][3], arg)
    
    
def weighted_calc_true_if(arg):
    """
    Returns true if the sum of weights of fulfilled sub-triggers amount to the specified sum
    weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } }
    **Supported Scopes**: none/all"""
    return default(inspect.stack()[0][3], arg)
    
    
def year(arg):
    """
    Compares the current year of the game
    year > 1850Traits: <, <=, =, !=, >, >=
    **Supported Scopes**: none/all
    
    
    
