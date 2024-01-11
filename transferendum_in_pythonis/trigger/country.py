from transferendum_in_pythonis.common import *
from .triggers import Trigger

# from scopes import RegionSE
# from scopes import CountrySE

from transferendum_in_pythonis.parsing.generated.dip_play import Dip_play
from transferendum_in_pythonis.parsing.generated.dip_action import Dip_action
from transferendum_in_pythonis.parsing.generated.state_region import State_region
from transferendum_in_pythonis.parsing.generated.country import Country
from transferendum_in_pythonis.parsing.generated.gov_type import Gov_type


class Level(Enum):
    very_low = 1
    low = 2
    medium = 3
    high = 4
    very_high = 5


class CountryTrigger(Trigger):
    """ Wrapper around effect functions """

    def __init__(self, content: str):
        super().__init__(content)


def default(arg1, arg2):
    return CountryTrigger(de(arg1, arg2))


class CT:
    @staticmethod
    def additional_war_exhaustion(arg):
        """
        Compares the additional war exhaustion the scoped country has accumulated from scripted events in the target diplomatic play
        additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 }Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def aggressive_diplomatic_plays_permitted(arg):
        """
        True if country is independent or permitted to start their own Diplomatic Plays
        aggressive_diplomatic_plays_permitted = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_active_party(arg):
        """
        Iterate through all active political parties in a country
        any_active_party = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: party"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_civil_war(arg):
        """
        Iterate through all civil wars related to the scoped country
        any_civil_war = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: civil_war"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_cobelligerent_in_diplo_play(arg):
        """
        Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
        any_cobelligerent_in_diplo_play = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_cobelligerent_in_war(arg):
        """
        Iterate through all co-belligerents of scope country in all wars
        any_cobelligerent_in_war = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_company(arg):
        """
        Iterate through all companies in a country
        any_company = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: company"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_enemy_in_diplo_play(arg):
        """
        Iterate through all enemies of scope country in all diplomatic plays (includes wars)
        any_enemy_in_diplo_play = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_enemy_in_war(arg):
        """
        Iterate through all enemies of scope country in all wars
        any_enemy_in_war = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_interest_group(arg):
        """
        Iterate through all interest groups in a country
        any_interest_group = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: interest_group"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_law(arg):
        """
        Iterate through all laws in a country
        any_law = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: law"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_military_formation(arg):
        """
        Iterate through all military formations currently present at input scope
        Supported scopes: country, front, hq
        any_military_formation = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country, front, hq
        **Supported Targets**: military_formation"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_neighbouring_state(arg):
        """
        Iterate through all states neighbouring a state region
        any_neighbouring_state = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country, state, state_region, strategic_region
        **Supported Targets**: state"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_overlord_or_above(arg):
        """
        Any country above current in hierarchy
        any_overlord_or_above = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_political_movement(arg):
        """
        Iterate through all political movements in a country
        any_political_movement = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: political_movement"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_potential_party(arg):
        """
        Iterate through all potential political parties in a country
        any_potential_party = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: party"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_primary_culture(arg):
        """
        Primary cultures of the scoped country or country definition
        any_primary_culture = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country, country_definition, state
        **Supported Targets**: culture"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_rival_country(arg):
        """
        Any country that is rival to the country in a scope
        any_rival_country = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_ally(arg):
        """
        Iterate through all allies to a: country
        any_scope_ally = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_diplomatic_pact(arg):
        """
        Any diplomatic pact of the country in a scope
        any_scope_diplomatic_pact = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: diplomatic_pact"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_held_interest_marker(arg):
        """
        Iterate through all interest markers held by a country
        any_scope_held_interest_marker = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: interest_marker"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_theater(arg):
        """
        Iterate through all theaters in a: country
        any_scope_theater = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: theater"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_violate_sovereignty_interested_parties(arg):
        """
        Iterate through all countries that would be interested if country in scope has their sovereignty violated
        any_scope_violate_sovereignty_interested_parties = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_violate_sovereignty_wars(arg):
        """
        Iterate through all relevant wars if target country had their sovereignty violated by scoped country
        any_scope_violate_sovereignty_wars = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: war"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_scope_war(arg):
        """
        Iterate through all wars related to the scope
        any_scope_war = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: war"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def any_subject_or_below(arg):
        """
        Any country below current in hierarchy
        any_subject_or_below = { <count=num/all> / <percent=fixed_point> <triggers> }
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def arable_land_country(arg):
        """
        Compare arable land in *all* states
        arable_land_country > 10Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def army_reserves(arg):
        """
        Compare the amount of Army ReservesTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def authority(arg):
        """
        Compares the available authority of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def average_country_infrastructure(arg):
        """
        Check average infrastructure in all states owned by scope country
        average_country_infrastructure = 3Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def average_incorporated_country_infrastructure(arg):
        """
        Check average infrastructure in incorporated states owned by the scope country
        average_incorporated_country_infrastructure = 3Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def battalion_manpower(arg):
        """
        Compares the current total manpower of a country's Battalions
        battalion_manpower > 15000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def bureaucracy(arg):
        """
        Compares the available bureaucracy of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_afford_diplomatic_action(arg):
        """
        Checks if the country in scope can afford the Influence for the specified diplomatic action (pact or ongoing)
        can_afford_diplomatic_action = { target = X type = Y }
        Where X = country and Y = diplomatic action type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_establish_any_export_route(arg):
        """
        Check if a country can establish any export routes
        can_establish_any_export_route = <goods key/scope>
        Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_establish_any_import_route(arg):
        """
        Check if a country can establish any import routes
        can_establish_any_import_route = <goods key/scope>
        Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_establish_company(arg):
        """
        Check if the country can establish a new companyTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_form_nation(arg):
        """
        Check if the target country is able to potentially form a nation
        can_form_nation = <tag>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_have_as_subject(arg):
        """
        Checks if a country can have another country as a particular type of subject
        can_have_as_subject = { who = X type = Y }
        Where X = country and Y = subject type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_have_political_movement(arg):
        """
        Checks if a political movement for the specified law can arise in scope country
        can_have_political_movement = law_type:law_landed_votingTraits: law_type scope
        **Supported Scopes**: country
        **Supported Targets**: law_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_have_subjects(arg):
        """
        Check if the country is able to have subjects of it sownTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_research(arg):
        """
        True if a country can research an technology
        can_research = technology
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def can_take_on_scaled_debt(arg):
        """
        Checks if scoped country can take on a certain amount of scaled debt from another country
        can_take_on_scaled_debt = { who = X value = Y }
        Where X = country and Y = decimal value
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_duration(arg):
        """
        Compares the maximum of all the very roughly approximated weeks remaining to finish the constructions in any queue: construction_queue_duration < 52Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_government_duration(arg):
        """
        Compares the very roughly approximated weeks remaining to finish the constructions in the government queue: construction_queue_government_duration < 52Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_num_queued_government_levels(arg):
        """
        Compares the number of government constructed building levels in the construction queueTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_num_queued_levels(arg):
        """
        Compares the number of building levels in the construction queueTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_num_queued_private_levels(arg):
        """
        Compares the number of privately constructed building levels in the construction queueTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def construction_queue_private_duration(arg):
        """
        Compares the very roughly approximated weeks remaining to finish the constructions in the private queue: construction_queue_private_duration < 52Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def country_can_have_mass_migration_to(arg):
        """
        Checks if the scoped country can have mass migration to target country
        can_have_mass_migration_to = c:countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_has_building_group_levels(arg):
        """
        Checks the sum of building levels for a building group in a country
        country_has_building_group_levels = {
        type = bg_heavy_industry
        value >= 100 }Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_has_building_levels(arg):
        """
        Checks the sum of building levels for a country
        country_has_building_levels >= 10 Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_has_building_type_levels(arg):
        """
        Checks the sum of building levels for a building type in a country
        country_has_building_type_levels = {
        target = bt:building_barracks
        value  >= 100Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_has_primary_culture(arg):
        """
        Checks if a culture is one of the primary cultures in the country
        country_has_primary_culture = <culture>Traits: culture scope
        **Supported Scopes**: country
        **Supported Targets**: culture"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_has_state_religion(arg):
        """
        Checks if a religion is the state religion in the country
        country_has_accepted_religion = <religion>Traits: religion scope
        **Supported Scopes**: country
        **Supported Targets**: religion"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def country_or_subject_owns_entire_state_region(arg):
        """
        Checks whether the scoped country or any of its subjects owns the entire specified state region
        country_or_subject_owns_entire_state_region = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_pm_usage(arg):
        """
        Checks how the ratio of Combat Units (of the same type) on the scoped Country with the specified Production Method compares to the value
        country_pm_usage = { target = X production_method = Y value <comparator> Z}
        where X = country scope and Y = production method key and Z = value to compare toTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_rank(arg):
        """
        Compares a Country's Power Ranking
        country_rank < rank_value:major_powerTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_tier(arg):
        """
        Compare tier of country tag
        country_tier = x
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def country_turmoil(arg):
        """
        Compares the country's population weighted turmoil
        country_turmoil > 0.2Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def empty_agitator_slots(arg):
        """
        Checks number of empty agitator slots in a country
        empty_agitator_slots >= 1Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enacting_any_law(arg):
        """
        Checks if you're enacting any law.
        enacting_any_law = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enactment_chance(arg):
        """
        Compares the current enactment chance in scope country (including values from enactment modifier)Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enactment_chance_without_enactment_modifier(arg):
        """
        Compares the current enactment chance in scope country but excludes values from enactment modifierTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enactment_phase(arg):
        """
        Compares the current law enactment phase in scope country.Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enactment_setback_count(arg):
        """
        Compares the current enactment setback count in scope country.Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enemy_contested_wargoals(arg):
        """
        Determines the fraction of wargoals that enemies in the war are currently contesting
        enemy_contested_wargoals = { target = scope:war value > 0.4 }Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def enemy_occupation(arg):
        """
        Determines the (weighted) enemy occupation score of a country
        enemy_occupation > 0.2Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def expanding_institution(arg):
        """
        Checks if the institution is expanding
        expanding_institution = <scope/key>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def flotilla_manpower(arg):
        """
        Compares the current total manpower of a country's Flotillas
        flotilla_manpower > 1000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def global_country_ranking(arg):
        """
        Compares a Country's Power Ranking (position)
        global_country_ranking > 42Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def gold_reserves(arg):
        """
        Does the country have the required gold reserves
        gold_reserves > 500Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def gold_reserves_limit(arg):
        """
        Compares the country's gold reserves limit
        gold_reserves > gold_reserves_limitTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def government_legitimacy(arg):
        """
        Compare LegitimacyTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def government_transfer_of_power(arg):
        """
        Checks country's government's transfer of power
        government_transfer_of_power = keyTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def government_wage_level(arg):
        """
        Compares the government wage level of scoped country
        government_wage_level = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def government_wage_level_value(arg):
        """
        Compares the government wage level value of scoped country
        government_wage_level_value = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_active_peace_deal(arg):
        """
        True if the country is in a war where there is a proposed peace deal
        has_active_peace_deal = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_any_secessionists_broken_out(arg):
        """
        Check if the country has secessionists broken outTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_any_secessionists_growing(arg):
        """
        Check if the country has any secessionists growingTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_any_secessionists_possible(arg):
        """
        Check if the country has any new secessionists possibleTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_attitude(arg):
        """
        Checks if scoped country has a particular attitude towards another country
        has_attitude = { who = X attitude = Y }
        Where X = country and Y = attitude type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_claim(arg):
        """
        Checks if country in scope has a claim on state/state region
        has_claim = <scope>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_company(arg):
        """
        Checks if a company of the specified type exists in scope country
        has_company = company_type:company_rheinmetallTraits: company_type scope
        **Supported Scopes**: country
        **Supported Targets**: company_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_completed_subgoal(arg):
        """
        Checks if the scoped country has completed a certain subgoal
        has_completed_subgoal = subgoal_key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_consumption_tax(arg):
        """
        Checks if the country is taxing the target good.
        c:FRA = { has_consumption_tax = g:grain }Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_convoys_being_sunk(arg):
        """
        Check if the country has convoys being sunk through convoy raidingTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_decreasing_interests(arg):
        """
        Checks if the country has decreasing interest levelsTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_diplomatic_pact(arg):
        """
        Checks if two countries have an active diplomatic pact of type
        has_diplomatic_pact = { who = X type = Y is_initiator = yes/no }
        Where X = country and Y = diplomatic action type, is_initiator is optional parameter that checks to see if scope country is the original initiator/target of the pact
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_diplomatic_relevance(arg):
        """
        Checks if target country is diplomatically relevant for scope country
        has_diplomatic_relevance = <scope>Traits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_diplomats_expelled(arg):
        """
        Checks if country in scope has recently expelled diplomats of event target
        has_diplomats_expelled = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_export_priority_tariffs(arg):
        """
        Checks if scoped country has Import Prioritized tariffs for a good
        has_export_priority_tariffs = <key/scope>Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_free_government_reform(arg):
        """
        Check if the country has a free (of radicals) government reform
        has_free_government_reform = <yes/no>Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_global_highest_gdp(arg):
        """
        Checks if the scoped country has the highest GDP
        has_global_highest_gdp = yes/noTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_global_highest_innovation(arg):
        """
        Checks if the scoped country has the highest weekly innovation
        has_global_highest_innovation = yes/noTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_government_clout(arg):
        """
        Does the country's government have the necessary total CloutTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_government_type(gt: Gov_type):
        """
        Is the country's government type as specified
        has_government_type = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], gt.name)

    @staticmethod
    def has_healthy_economy(arg):
        """
        Check if the country has a healthy economyTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_import_priority_tariffs(arg):
        """
        Checks if scoped country has Import Prioritized tariffs for a good
        has_import_priority_tariffs = <key/scope>Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_institution(arg):
        """
        Checks if scope country has a particular type of institution
        has_institution = <scope/key>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_insurrectionary_interest_groups(arg):
        """
        Check if the country has Interest Groups that are insurrectionaryTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_interest_marker_in_region(arg):
        """
        True if scope country has an interest marker in target region
        has_interest_marker_in_region = region scope/tag
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_journal_entry(arg):
        """
        Check if the country has at least one active journal entry of the specified type
        has_journal_entry = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_law(arg):
        """
        Checks if a country has a certain Law activeTraits: law_type scope
        **Supported Scopes**: country
        **Supported Targets**: law_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_modifier(arg):
        """
        Check if a supported scope has a certain timed modifier
        Supported scopes: Country, Character, State, Building, InterestGroup, PoliticalMovement, Institution, Front
        has_modifier = <key>
        **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_no_priority_tariffs(arg):
        """
        Checks if scoped country has Unprioritized tariffs for a good
        has_no_priority_tariffs = <key/scope>Traits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_objective(arg):
        """
        Checks if the scoped country has a certain objective type
        has_objective = objective_type_key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_overlapping_interests(arg):
        """
        Checks if country in scope has an overlapping interest marker with any of target country's interests
        has_overlapping_interests = <scope>Traits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_political_movement(arg):
        """
        Checks if a political movement for the specified law exists in scope country
        can_have_political_movement = law_type:law_landed_votingTraits: law_type scope
        **Supported Scopes**: country
        **Supported Targets**: law_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_possible_decisions(arg):
        """
        Check if a country has any possible Decisions
        has_possible_decisions = yesTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_potential_to_form_country(arg):
        """
        Check if the target country could ever be able to form a nation
        has_potential_to_form_country = <tag>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_researchable_technology(arg):
        """
        Check if the country has any researchable technology left.Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_revolution(arg):
        """
        Check if the country has revolutionary uprisingTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_revolution_over_law_type(arg):
        """
        Checks if a country is having a revolution over a particular law type
        has_revolution_over_law_type = law_type:law_autocracyTraits: law_type scope
        **Supported Scopes**: country
        **Supported Targets**: law_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_ruling_interest_group(arg):
        """
        Does the country's government include the named IG
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_ruling_interest_group_count(arg):
        """
        Does the country's government consist of the specified number of IGsTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_secret_goal(arg):
        """
        Checks if scoped country has a particular secret goal towards another country
        has_secret_goal = { who = X secret_goal = Y }
        Where X = country and Y = secret_goal type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_state_in_state_region(arg):
        """
        Check if country has a state in the state region
        has_state_in_state_region = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_strategic_adjacency(arg):
        """
        Checks if country in scope has a strategic adjacency (direct/coastal/wargoal adjacency) to target state/country
        has_strategic_adjacency = <scope>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_strategic_land_adjacency(arg):
        """
        Checks if country in scope has a strategic adjacency (direct land border or wargoal adjacency only) to target state/country
        has_strategic_adjacency = <scope>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_strategy(arg):
        """
        Checks if country in scope has a particular AI strategy
        has_strategy = <key>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_subject_relation_with(arg):
        """
        Checks if country in scope is subject or overlord of event target
        has_subject_relation_with = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_sufficient_construction_capacity_for_investment(arg):
        """
        Check if country has enough construction capacity to be spending all of its incoming investment pool funds.Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_technology_progress(arg):
        """
        Does the country have the required progress for an technology
        has_technology_progress = { technology = X progress = Y }
        Where X is an technology and Y is a fixed pointTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_technology_researched(arg):
        """
        True if a country has researched an technology
        has_technology_researched = <scope/key>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_treaty_port_in_country(arg):
        """
        Checks if the scoped country has a treaty port in target country
        c:POR = { has_treaty_port_in_country = c:CHI }Traits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_truce_with(arg):
        """
        Check if a country has a truce with a different target country
        has_truce_with = c:GBRTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_war_with(arg):
        """
        Checks if country in scope is at war with event target
        has_war_with = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def has_wasted_construction(arg):
        """
        Check if country is wasting any of its produced construction.Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def highest_secession_progress(arg):
        """
        Compares the highest secession progress of any secession movement in a given country
        highest_secession_progress > 0.7Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def in_default(arg):
        """
        Check if the country is currently in default
        Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def in_election_campaign(arg):
        """
        Check if the country is in election campaign period
        in_election_campaign = <yes/no>Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def influence(arg):
        """
        Compares the available influence of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def initiator_is(arg):
        """
        Checks who the initiator of a diplomatic play is
        initiator_is = countryTraits: country scope
        **Supported Scopes**: diplomatic_play
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def institution_investment_level(arg):
        """
        Compares the level of investment in an institution
        institution_investment_level = { institution = <key> value = <comparator value> }Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def investment_pool(arg):
        """
        Does the country have this amount of money saved in its investment pool
        investment_pool > 1000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def investment_pool_gross_income(arg):
        """
        Does the country have this amount of gross income (income before expenses) for its investment pool
        investment_pool_gross_income > 1000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def investment_pool_net_income(arg):
        """
        Does the country have this amount of net income (income after expenses) for its investment pool
        investment_pool_net_income > 1000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_adjacent_to_country(arg):
        """
        Checks if country in scope is adjacent to a target country
        is_adjacent_to_country = <scope>Traits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_adjacent_to_state(arg):
        """
        Checks if country in scope is adjacent to a target state
        is_adjacent_to_state = <scope>Traits: state scope
        **Supported Scopes**: country
        **Supported Targets**: state"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_ai(arg):
        """
        True if country scope is controlled by an AI
        is_ai = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_at_war(arg):
        """
        Check if the country is at warTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_banning_goods(arg):
        """
        Check if a country is banning a good
        is_banning_goods = <goods key/scope>
    
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_construction_paused(arg):
        """
        Check if construction in a state is paused.Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_country_alive(arg):
        """
        Checks if the scoped country is alive, i.e. if it has at least one state on the map and can be interacted with
        is_country_alive = yes/noTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_country_type(arg):
        """
        Checks the countrys type
        is_country_type = country type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_ally_of(arg):
        """
        Checks if country in scope is in a diplomatic play together with event target
        is_diplomatic_play_ally_of = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_committed_participant(arg):
        """
        True if country is a committed participant of any diplomatic play
        is_diplomatic_play_participant = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_enemy_of(arg):
        """
        Checks if country in scope is in a diplomatic play against event target
        is_diplomatic_play_enemy_of = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_initiator(arg):
        """
        True if country is the initiator of any diplomatic play
        is_diplomatic_play_initiator = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_involved_with(arg):
        """
        Checks if country in scope is involved in the same diplomatic play as event target
        is_diplomatic_play_involved_with = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_participant_with(arg):
        """
        Checks if country in scope is a committed participant in the same diplomatic play as event target
        is_diplomatic_play_participant_with = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_target(arg):
        """
        True if country is the target of any diplomatic play
        is_diplomatic_play_target = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_diplomatic_play_undecided_participant(arg):
        """
        True if country is a undecided participant of any diplomatic play
        is_diplomatic_play_participant = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_direct_subject_of(arg):
        """
        Checks if country in scope is a direct subject (not subject-of-subject) of event target
        is_subject_of = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_enacting_law(arg):
        """
        Checks if the scoped country is enacting a specific law type.
        is_enacting_law = law_type:law_conscriptionTraits: law_type scope
        **Supported Scopes**: country
        **Supported Targets**: law_type"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_expanding_institution(arg):
        """
        Are you expanding an institution
        is_expanding_institution = <yes>/<no>Traits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_home_country_for(arg):
        """
        Checks if a country is the home country for target countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_immune_to_revolutions(arg):
        """
        Checks if the country has been set to be immune to revolutions via set_immune_to_revolutions
        Warning: This does not check if the country is naturally immune to revolutions due to for example being a revolutionary country itself, only for the effects of set_immune_to_revolutions.
        is_immune_to_revolutions = yes/noTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_in_customs_union(arg):
        """
        Check if the country is part of a customs unionTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_in_war_together(arg):
        """
        Checks if country in scope is in war on the same side as event target
        is_in_war_together = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_junior_in_customs_union(arg):
        """
        True if country is a junior country in a customs custom
        is_junior_in_customs_union = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_local_player(arg):
        """
        True if country scope is a player
        is_local_player = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_losing_power_rank(arg):
        """
        Check if the country is in the process of dropping in power rankingTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_mass_migration_origin(arg):
        """
        Checks if the scoped country is the origin of mass migration
        is_mass_migration_origin = yesTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_mass_migration_origin_of_culture(arg):
        """
        Checks if the scoped country origin of mass migration of specific culture
        is_mass_migration_origin_of_culture = cu:example_cultureTraits: culture scope
        **Supported Scopes**: country
        **Supported Targets**: culture"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_owed_obligation_by(arg):
        """
        Checks if the scoped country is owed a obligation by the target country
        is_owed_obligation_by = c:FRATraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_player(arg):
        """
        True if country scope is a player
        is_player = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_researching_technology(arg):
        """
        Check if the country is actively researching a tech
        is_researching_technology = <scope/key/any>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_researching_technology_category(arg):
        """
        Check if the country is actively researching a tech category
        is_researching_technology_category = <key/any>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_secessionist(arg):
        """
        Check if the country is secessionistTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_subject(arg):
        """
        True if country is a subject
        is_subject = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_subject_of(arg):
        """
        Checks if country in scope is subject (or subject-of-subject) of event target
        is_subject_of = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_subject_type(arg):
        """
        Checks the country's subject type
        is_subject_type = subject type
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_supporting_unification_candidate(arg):
        """
        Check if scope country is supporting a unification candidate for a specific country formation
        is_supporting_unification_candidate = { who = c:PRU country_formation = GER }
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_taxing_goods(arg):
        """
        Check if a country is taxing a good
        has_embargo = <goods key/scope>
    
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_unification_candidate(arg):
        """
        Check if scope country is a unification candidate for country tag
        has_country_unification_candidate = GER
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def is_violating_sovereignty_of(arg):
        """
        Check if the scoped country is violating the sovereignty of a target country
        is_violating_sovereignty_of = c:GBRTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def isolated_states(arg):
        """
        Compare number of Isolated StatesTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def leading_producer_of(arg):
        """
        Checks if country is producing the most of a certain good
        leading_producer_of = g:luxury_clothesTraits: goods scope
        **Supported Scopes**: country
        **Supported Targets**: goods"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def leads_customs_union(arg):
        """
        Check if any other country is part of this country's customs union
        leads_customs_union = boolTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def military_wage_level(arg):
        """
        Compares the military wage level of scoped country
        military_wage_level = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def military_wage_level_value(arg):
        """
        Compares the military wage level value of scoped country
        military_wage_level_value = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def max_num_declared_interests(arg):
        """
        Compares the maximum number of declared interests of scoped country
        max_num_declared_interests = <value>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def naval_power_projection(arg):
        """
        Compares a Country's naval_power_projection
        scope:example_country = { naval_power_projection < root.naval_power_projectionTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def navy_reserves(arg):
        """
        Compare the amount of Navy ReservesTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def num_declared_interests(arg):
        """
        Compares the number of declared interests of scoped country
        num_declared_interests = <value>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def num_taxed_goods(arg):
        """
        Compares the number of consumption taxed goods of scoped country
        num_taxed_goods = <value>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def number_of_possible_decisions(arg):
        """
        The number of possible Descision a Country can take
        umber_of_possible_decisions > 0Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def owes_obligation_to(arg):
        """
        Checks if country in scope owes a obligation to event target
        owes_obligation_to = countryTraits: country scope
        **Supported Scopes**: country
        **Supported Targets**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def owns_entire_state_region(arg):
        """
        Check if country owns entire region
        owns_entire_state_region = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def owns_treaty_port_in(arg):
        """
        Does country own the treaty port in assigned state region
        owns_treaty_port_in = key
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def prestige(arg):
        """
        Compare prestigeTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def produced_authority(arg):
        """
        Compares the produced authority of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def produced_bureaucracy(arg):
        """
        Compares the produced bureaucracy of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def produced_influence(arg):
        """
        Compares the produced influence of the scoped countryTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
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

    @staticmethod
    def ruler_can_have_command(arg):
        """
        Checks if the country's government type allows its ruler to have command
        ruler_can_have_command = yes/noTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def scaled_debt(arg):
        """
        Compare value to a country's debt relative to debt ceiling
        scaled_debt = valueTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def scaled_gold_reserves(arg):
        """
        Compare value to a country's gold reserves relative to reserves limit
        scaled_gold_reserves = valueTraits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def should_set_wargoal(arg):
        """
        Check if the country is lacking a primary wargoal in any diplomatic play it is part ofTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def shrinking_institution(arg):
        """
        Checks if the institution is shrinking
        expanding_institution = <scope/key>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def size_weighted_lost_battles_fraction(arg):
        """
        Determines the fraction of battles the target country has lost in the target war, weighted by manpower size of all battles in the war
        size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 }
        add = "size_weighted_lost_battles_fraction(scope:war)"Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def supply_network_strength(arg):
        """
        Compares the country's supply network strength (can exceed 1)
        supply_network_strength > 1.1Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def taking_loans(arg):
        """
        Check if the country is currently running a weekly deficit and taking loans to compensateTraits: yes/no
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def tax_level(arg):
        """
        Compares the overall tax level of scoped country
        tax_level = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def tax_level_value(arg):
        """
        Compares the overall tax level integer value of scoped country
        income_tax_level_value = <level>Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def total_manpower(arg):
        """
        Compares the current total manpower of a country's combat units
        total_manpower > 25000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def total_population(arg):
        """
        Compares the total population of a given country
        total_population > 100000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def total_population_including_subjects(arg):
        """
        Compares the total population in the scope country and its subjects
        total_population_including_subjects > 40000000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def total_population_including_subjects_share(arg):
        """
        Compares the total population in the scope country and its subjects' share of the global population
        total_population_including_subjects_share > 0.4Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def total_population_share(arg):
        """
        Compares the total population of a given country's share of the global population
        total_population_share > 0.02Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def was_formed_from(arg):
        """
        Check if a formed country previously had a specific definition
        was_formed_from = <tag>
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)

    @staticmethod
    def weekly_net_fixed_income(arg):
        """
        Does the country have this amount of weekly income after fixed expenses
        weekly_net_income > 1000Traits: <, <=, =, !=, >, >=
        **Supported Scopes**: country"""
        return default(inspect.stack()[0][3], arg)
