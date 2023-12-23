import helpers


def abandon_revolution(arg):
    """
    Removes interest group from revolution
    abandon_revolution = yes/no
    **Supported Scopes**: interest_group
    """


def activate_building(arg):
    """

    Activate a building in a state
    activate_building = { building = building_key }
    **Supported Scopes**: state
    """


def activate_law(arg):
    """

    Activates a law for a country
    **Supported Scopes**: country
    **Supported Targets**: law_type
    """


def activate_production_method(arg):
    """

    Activates the named production method for buildings of a certain type in country/state
    **Supported Scopes**: country, state
    """


def add_arable_land(arg):
    """

    Add/remove arable land from a state region
    **Supported Scopes**: state_region
    """


def add_banned_goods(arg):
    """

    Adds a total ban of a good to a country
    add_banned_goods = <goods key/scope>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def add_change_relations_progress(arg):
    """

    Add progress towards changing relations between two countries
    add_change_relations_progress = {
        tcountry = country scope/tag
        value = amount
    }
    **Supported Scopes**: country
    """


def add_character_role(arg):
    """

    Adds a new role to a character
    add_character_role = general
    **Supported Scopes**: character
    """


def add_civil_war_progress(arg):
    """

    Adds the specified number of percentage points to a civil war progress (range is [0, 1], 0.1 means 10 percentage points)
    add_civil_war_progress = 0.1 / -0.1
    **Supported Scopes**: civil_war
    """


def add_claim(arg):
    """

    Adds scoped state region as a claim for target country
    add_claim = scope/country
    **Supported Scopes**: state_region
    **Supported Targets**: country
    """


def add_commander_rank(arg):
    """

    Promotes/demotes a character a given amount of military ranks
    **Supported Scopes**: character
    """


def add_company(arg):
    """

    Adds company type to a country's companies
    add_company = company_type:key
    **Supported Scopes**: country
    **Supported Targets**: company_type
    """


def add_cultural_obsession(arg):
    """

    Adds a new obsession to the culture in scope
    add_cultural_obsession = X
    Where X is a goods
    **Supported Scopes**: culture
    """


def add_culture_standard_of_living_modifier(arg):
    """

    Apply a standard of living modifier in the scoped state for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier.
    **Supported Scopes**: state
    """


def add_declared_interest(arg):
    """

    Will create a declared interest in the target strategic region
    c:FRA = { add_declared_interest = region_nile_basin }
    **Supported Scopes**: country
    """


def add_devastation(arg):
    """

    Add/remove devastation from a state region
    **Supported Scopes**: state_region
    """


def add_diplomatic_play_war_support(arg):
    """

    Adds war support to the target country in the scoped diplomatic play. The amount will appear under the 'situations' header in tooltips
    add_diplomatic_play_war_support = { target = country value = value }
    **Supported Scopes**: diplomatic_play
    """


def add_enactment_modifier(arg):
    """

    Adds an enactment-related timed modifier effect to object in scope
    **Supported Scopes**: country
    """


def add_enactment_phase(arg):
    """

    Changes the current law enactment phase in scope country by an added amount. The result will be clamped between 0 and NPolitics::LAW_ENACTMENT_MAX_PHASES. The enacting law will pass if the resulting value equals NPolitics::LAW_ENACTMENT_MAX_PHASES.
    **Supported Scopes**: country
    """


def add_enactment_setback(arg):
    """

    Changes the current law enactment setback count in scope country by an added amount. The result will be clamped between 0 and NPolitics::LAW_ENACTMENT_MAX_SETBACKS. The law enactment will fail if the resulting value equals NPolitics::LAW_ENACTMENT_MAX_SETBACKS.
    **Supported Scopes**: country
    """


def add_era_researched(arg):
    """

    Add specified era as researched in a country scope
    add_era_researched = era
    **Supported Scopes**: country
    """


def add_escalation(arg):
    """

    Add escalation to a diplomatic play
    add_escalation = integer
    **Supported Scopes**: diplomatic_play
    """


def add_experience(arg):
    """

    Adds an amount of experience to a commander
    add_experience = 0.2
    **Supported Scopes**: character
    """


def add_homeland(arg):
    """

    Adds scoped state region as Homeland for target culture
     add_homeland = cu:culture
    **Supported Scopes**: state_region
    **Supported Targets**: culture
    """


def add_ideology(arg):
    """

    Adds an ideology to scoped interest group
    add_ideology = x
    **Supported Scopes**: interest_group
    """


def add_ig_to_party(arg):
    """

    Adds target interest group to scope party
    py:py_key = {
        add_ig_to_party = ig:ig_key
    }
    **Supported Scopes**: party
    **Supported Targets**: interest_group
    """


def add_initiator_backers(arg):
    """

    Add a tag/scope country to the initiator side of a diplomatic play
    add_initiator_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """


def add_investment_pool(arg):
    """

    Directly adds money to the investment pool
    add_investment_pool = 50
    **Supported Scopes**: country
    """


def add_journal_entry(arg):
    """

    Adds a journal entry to a scoped country's journal, with optional saved scope target
    add_journal_entry = { type = <key> target = <scope> }
    **Supported Scopes**: none/all
    """


def add_law_progress(arg):
    """

    Adds x% progress to the current checkpoint of the law being passed (range is [0, 1], 0.1 means 10 percentage points)
    add_law_progress = 0.1 / -0.1
    **Supported Scopes**: country
    """


def add_loyalists(arg):
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


def add_loyalists_in_state(arg):
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


def add_modifier(arg):
    """

    Adds a timed modifier effect to object in scope
    **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
    """


def add_momentum(arg):
    """

    Adds momentum to a Party during a campaign perioddd_momentum = value
    **Supported Scopes**: party
    """


def add_morale(arg):
    """

    Adds the specified amount of Morale to the Combat Unit in scope
    add_morale = -0.2
    **Supported Scopes**: new_combat_unit
    """


def add_organization(arg):
    """

    Adds the specified amount of Organization to the Military Formation in scope
    add_organization = -10
    **Supported Scopes**: military_formation
    """


def add_pollution(arg):
    """

    Increase/decrease pollution level in a scoped state region
    add_pollution = 10
    **Supported Scopes**: state_region
    """


def add_pop_wealth(arg):
    """

    Adds the wealth of the pop
    add_pop_wealth = { wealth_distribution = {...} update_loyalties = true/false }
    Where the distribution adding to wealth of the pop
    **Supported Scopes**: pop
    """


def add_primary_culture(arg):
    """

    Adds a culture to the primary cultures of a country
    add_primary_culture = X
    Where X is a culture scope
    **Supported Scopes**: country
    **Supported Targets**: culture
    """


def add_radicals(arg):
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


def add_radicals_in_state(arg):
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


def add_random_trait(arg):
    """

    Adds a random qualifying Trait of the specified category
    add_random_trait = personality / skill / condition
    **Supported Scopes**: character
    """


def add_religion_standard_of_living_modifier(arg):
    """

    Apply a standard of living modifier in the scoped state for the given religion. Other than the required religion argument, this effect has the same syntax as add_modifier.
    **Supported Scopes**: state
    """


def add_ruling_interest_group(arg):
    """

    Adds interest group to government
    add_ruling_interest_group = yes/no
    **Supported Scopes**: interest_group
    """


def add_state_trait(arg):
    """

    add state trait in a scoped state region
    add_state_trait = <state_trait_name>
    **Supported Scopes**: state_region
    """


def add_target_backers(arg):
    """

    Add a tag/scope country to the target side of a diplomatic play
    add_target_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """


def add_taxed_goods(arg):
    """

    Adds consumption taxes on a good to a country
    add_taxed_goods = <goods key/scope>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def add_technology_progress(arg):
    """

    Add technology progress
    add_technology_progress = { progress = X technology = Y }
    Where X is a fixed point and Y is an technology
    **Supported Scopes**: country
    """


def add_technology_researched(arg):
    """

    Research the specified technology in a country scope
    add_technology_researched = technology
    **Supported Scopes**: country
    """


def add_to_global_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def add_to_list(arg):
    """

    Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the (unbroken) event chain
    add_to_list = <string> NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent
    **Supported Scopes**: none/all
    """


def add_to_local_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def add_to_temporary_list(arg):
    """

    Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the same effect
    add_to_temporary_list = <string> NOTE, if adding a temporary target to a permanent list, the list will stay permanent
    **Supported Scopes**: none/all
    """


def add_to_variable_list(arg):
    """

    Adds the event target to a variable list
    add_to_variable_list = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def add_trait(arg):
    """

    Add a trait to a Character
    add_trait = trait
    **Supported Scopes**: character
    """


def add_treasury(arg):
    """

    Add/remove money from a country
    add_treasury = fixed point
    **Supported Scopes**: country
    """


def add_war_exhaustion(arg):
    """

    Adds war exhaustion to the target country in the scoped war. The amount will appear under the 'situations' header in tooltips
    add_war_exhaustion = { target = country value = value }
    **Supported Scopes**: war
    """


def add_war_goal(arg):
    """

    Adds a war goal to a DP. Same data read in as add_war_goal in create_diplomatic_play
    random_diplomatic_play = { add_war_goal = { holder = initiator type = secession primary_demand = yes }
    **Supported Scopes**: diplomatic_play
    """


def add_war_war_support(arg):
    """

    Adds war support to the target country in the scoped war. The amount will appear under the 'situations' header in tooltips
    add_war_war_support = { target = country value = value }
    **Supported Scopes**: war
    """


def annex(arg):
    """

    Annexes a country
    annex = scope
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def annex_as_civil_war(arg):
    """

    Annexes a country with all the inheritance effects of a victorious side in a civil war
    annex_as_civil_war = scope
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def annex_with_incorporation(arg):
    """

    Annexes a country, inheriting incorporation of their states
    annex_with_incorporation = scope
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def assert_if(arg):
    """

    Conditionally cause an assert during run time
    assert_if = { limit = { X } text = Y }, where X is a trigger and Y is an optional string
    **Supported Scopes**: none/all
    """


def assert_read(arg):
    """

    Conditionally cause an assert during read time
    assert_read = X, where X is yes or the string to be printed in the assert
    **Supported Scopes**: none/all
    """


def call_election(arg):
    """

    Sets the next election date for country in N months
    call_election = {
        months = 6
    }
    **Supported Scopes**: country
    """


def cancel_enactment(arg):
    """

    Stops enacting the country's currently enacting law
    cancel_enactment = yes
    **Supported Scopes**: country
    """


def change_character_culture(arg):
    """

    Changes the culture of the scoped character
    change_character_culture = cu:colombian
    **Supported Scopes**: character
    **Supported Targets**: culture
    """


def change_character_religion(arg):
    """

    Changes the religion of the scoped character
    change_character_religion = rel:protestant
    **Supported Scopes**: character
    **Supported Targets**: religion
    """


def change_global_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """


def change_infamy(arg):
    """

    Change infamy of scope country
    change_infamy = amount
    **Supported Scopes**: country
    """


def change_institution_investment_level(arg):
    """

    Add/remove the investment level for the institution
    change_institution_investment_level = {
        institution = institution_police
        investment = -1
    }
    **Supported Scopes**: country
    """


def change_local_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """


def change_pop_culture(arg):
    """

    Changes the culture of the scoped pop to a specified culture by a specified percentage
    change_pop_culture = { target = cu:spanish value = 0.33 }
    **Supported Scopes**: pop
    """


def change_pop_religion(arg):
    """

    Changes the religion of the scoped pop to a specified religion by a specified percentage
    change_pop_religion = { target = rel:catholic value = 0.5 }
    **Supported Scopes**: pop
    """


def change_poptype(arg):
    """

    Changes the type of the pop to the given type
    **Supported Scopes**: pop
    **Supported Targets**: pop_type
    """


def change_relations(arg):
    """

    Change relations between two countries
    change_relations = {
        tcountry = country scope/tag
        value = amount
    }
    **Supported Scopes**: country
    """


def change_subject_type(arg):
    """

    Will change the subject type of the country that is the current scope.
    change_subject_type = subject_type_dominion
    **Supported Scopes**: country
    """


def change_tag(arg):
    """

    Change the tag for the scoped country
    c:GBR = { change_tag = FRA }
    **Supported Scopes**: country
    """


def change_tension(arg):
    """

    Change tension between two countries
    change_tension = {
        tcountry = country scope/tag
        value = amount
    }
    **Supported Scopes**: country
    """


def change_variable(arg):
    """

    Changes the value or a numeric variable
    change_variable = { name = X operation = Y }
    Where X is the name of the numeric variable to modify
    Where the valid operations are add, subtract, multiply, divide, modulo, min and max
    Where Y is a fixed point value, script value or event target of a value type
    **Supported Scopes**: none/all
    """


def clamp_global_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """


def clamp_local_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """


def clamp_variable(arg):
    """

    Clamps a variable the specified max and min
    clamp_variable = { name = X max = Y min = Z }
    Where X is the name of the variable
    Where Y and Z are script values
    **Supported Scopes**: none/all
    """


def clear_debt(arg):
    """

    Clear country loans = bool
    **Supported Scopes**: country
    """


def clear_enactment_modifier(arg):
    """

    Clears the current law enactment modifier of scope country.
    **Supported Scopes**: country
    """


def clear_global_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """


def clear_local_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """


def clear_saved_scope(arg):
    """

    Clears a saved scope from the top scope
    save_scope_as = cool_scope -> clear_saved_scope = cool_scope
    **Supported Scopes**: none/all
    """


def clear_scaled_debt(arg):
    """

    Clears an amount of debt equal to the defined multiplier on target's max credit(arg):

    clear_scaled_debt = value
    **Supported Scopes**: country
    """


def clear_variable_list(arg):
    """

    Empties the list
    clear_variable_list = variable_name
    **Supported Scopes**: none/all
    """


def complete_objective_subgoal(arg):
    """

    Completes an objective subgoal
    complete_objective_subgoal = <key>
    **Supported Scopes**: country
    """


def convert_population(arg):
    """

    Changes X% of the different religion population to the specified religion.
    convert_population = { target = rel:catholic value = 0.5 }
    **Supported Scopes**: state
    """


def copy_laws(arg):
    """

    Copies the constitution of the target country scope
    Warning: This stops any current enactment.
    copy_laws = scope
    **Supported Scopes**: country
    **Supported Targets**: country
    """


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


def create_character(arg):
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


def create_diplomatic_pact(arg):
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


def create_diplomatic_play(arg):
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


def create_incident(arg):
    """

    Creates a diplomatic incident that generates infamy, with target country as the victim
    create_incident = {
        tcountry = country scope/tag
        value = infamy amount
    }
    **Supported Scopes**: country
    """


def create_mass_migration(arg):
    """

    Initiates mass migration of a specific culture from a origin country to a scoped state
    create_mass_migration = {
        origin = c:GBR
        culture = cu:english
    }
    **Supported Scopes**: state
    """


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


def create_pop(arg):
    """

    Creates a pop in the scoped state
    **Supported Scopes**: state
    """


def create_state(arg):
    """

    creates a state in a state region
    **Supported Scopes**: state_region
    """


def create_trade_route(arg):
    """

    Creates a new Trade Route
    trade_route = {
        goods = x
        level = x
        import = yes/no
        origin = state_region
        target = state_region
    }
    **Supported Scopes**: country
    """


def create_truce(arg):
    """

    Create a truce betweeen two countries
    create_truce = {
        tcountry = country scope/tag
        months = integer
    }
    **Supported Scopes**: country
    """


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


def custom_label(arg):
    """

    just a tooltip, the scope as object (for grouping, localization).
    custom_label = key; alternatively custom_label = { text = key subject = scope (optional) <hidden effects> }
    **Supported Scopes**: none/all
    """


def custom_tooltip(arg):
    """

    just a tooltip, the scope as subject (for grouping, localization).
    custom_tooltip = key; alternatively custom_tooltip = { text = key subject = scope (optional) <hidden effects> }
    **Supported Scopes**: none/all
    """


def deactivate_building(arg):
    """

    # Deactivate a building in a state
    deactivate_building = { building = building_key }
    **Supported Scopes**: state
    """


def deactivate_law(arg):
    """
    Deactivates a law for a country
    **Supported Scopes**: country
    **Supported Targets**: law_type
    """


def deactivate_parties(arg):
    """

    Deactivates parties in scoped country.
    deactivate_parties = yes
    **Supported Scopes**: country
    """


def debug_log(arg):
    """

    Log a string to the debug log when this effect executes, debug_log = message, the message can be a localization string with ROOT, SCOPE and PREV available
    **Supported Scopes**: none/all
    """


def debug_log_scopes(arg):
    """

    Log the current scope to the debug log when this effect executes
    debug_log_scopes = yes # log full scope info
    debug_log_scopes = no  # log only current scope
    **Supported Scopes**: none/all
    """


def deploy_to_front(arg):
    """

    Deploys the scope formation to the target front
    deploy_to_front = p:xFAFAFA.front
    **Supported Scopes**: military_formation
    **Supported Targets**: front
    """


def disband_party(arg):
    """

    Removes all interest groups from the party, causing it to disband
    disband_party = yes
    **Supported Scopes**: party
    """


def disinherit_character(arg):
    """

    Strips the scoped character of their heir status in whichever countries apply.
    scope:larry = { disinherit_character = yes }
    **Supported Scopes**: character
    """


def Else(arg):
    """

    Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met
    if = { limit = { <triggers> } <effects> }
    else = { <effects> }
    **Supported Scopes**: none/all
    """


def else_if(arg):
    """

    Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met, and its own limit is met
    if = { limit = { <triggers> } <effects> }
    else_if = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """


def end_play(arg):
    """

    End a diplomatic play
    end_play = bool
    **Supported Scopes**: diplomatic_play
    """


def end_truce(arg):
    """

    Ends a truce betweeen two countries
    end_truce = {
        tcountry = country scope/tag
        months = integer
    }
    **Supported Scopes**: country
    """


def every_active_party(arg):
    """

    Iterate through all active political parties in a country
    every_active_party = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """


def every_character(arg):
    """

    Iterate through all characters globally
    every_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def every_character_in_exile_pool(arg):
    """

    Iterate through characters in the exile pool
    every_character_in_exile_pool = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def every_character_in_void(arg):
    """

    Iterate through characters in the void
    every_character_in_void = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def every_civil_war(arg):
    """

    Iterate through all civil wars related to the scoped country
    every_civil_war = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: civil_war
    """


def every_cobelligerent_in_diplo_play(arg):
    """

    Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
    every_cobelligerent_in_diplo_play = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_cobelligerent_in_war(arg):
    """

    Iterate through all co-belligerents of scope country in all wars
    every_cobelligerent_in_war = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_combat_unit(arg):
    """

    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    every_combat_unit = { limit = { <triggers> } <effects> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit
    """


def every_company(arg):
    """

    Iterate through all companies in a country
    every_company = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: company
    """


def every_country(arg):
    """

    Iterate through all countries globally
    every_country = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: country
    """


def every_diplomatic_play(arg):
    """

    Iterate through all diplomatic plays globally
    every_diplomatic_play = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play
    """


def every_enemy_in_diplo_play(arg):
    """

    Iterate through all enemies of scope country in all diplomatic plays (includes wars)
    every_enemy_in_diplo_play = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_enemy_in_war(arg):
    """

    Iterate through all enemies of scope country in all wars
    every_enemy_in_war = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_in_global_list(arg):
    """

    Iterate through all items in global list. list = name or variable = name
    every_in_global_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """


def every_in_hierarchy(arg):
    """

    Any country in current hierarchy, including current
    every_in_hierarchy = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_in_list(arg):
    """

    Iterate through all items in list. list = name or variable = name
    every_in_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """


def every_in_local_list(arg):
    """

    Iterate through all items in local list. list = name or variable = name
    every_in_local_list = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """


def every_interest_group(arg):
    """

    Iterate through all interest groups in a country
    every_interest_group = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_group
    """


def every_law(arg):
    """

    Iterate through all laws in a country
    every_law = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: law
    """


def every_market(arg):
    """

    Iterate through all markets globally
    every_market = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: market
    """


def every_market_goods(arg):
    """

    Iterate through all active (market) goods in a market
    every_market_goods = { limit = { <triggers> } <effects> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods
    """


def every_member(arg):
    """

    Iterate through all interest group members of a party
    every_member = { limit = { <triggers> } <effects> }
    **Supported Scopes**: party
    **Supported Targets**: interest_group
    """


def every_military_formation(arg):
    """

    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    every_military_formation = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation
    """


def every_neighbouring_state(arg):
    """

    Iterate through all states neighbouring a state region
    every_neighbouring_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state
    """


def every_overlord_or_above(arg):
    """

    Any country above current in hierarchy
    every_overlord_or_above = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_participant(arg):
    """

    Any of two participants of the diplomatic pact in a scope
    every_participant = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country
    """


def every_political_movement(arg):
    """

    Iterate through all political movements in a country
    every_political_movement = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: political_movement
    """


def every_potential_party(arg):
    """

    Iterate through all potential political parties in a country
    every_potential_party = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """


def every_preferred_law(arg):
    """

    Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law
    every_preferred_law = { limit = { <triggers> } <effects> }
    **Supported Scopes**: interest_group
    **Supported Targets**: law
    """


def every_primary_culture(arg):
    """

    Primary cultures of the scoped country or country definition(arg):

    every_primary_culture = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, country_definition, state(arg):

    **Supported Targets**: culture
    """


def every_province(arg):
    """

    Iterate through all Provinces in the scoped State
    every_province = { limit = { <triggers> } <effects> }
    **Supported Scopes**: province
    **Supported Targets**: state
    """


def every_rival_country(arg):
    """

    Any country that is rival to the country in a scope
    every_rival_country = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_scope_admiral(arg):
    """

    Iterate through all admirals in a: country, interestgroup, or military formation
    every_scope_admiral = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def every_scope_ally(arg):
    """

    Iterate through all allies to a: country
    every_scope_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_scope_building(arg):
    """

    Iterate through all buildings in a: state, country
    every_scope_building = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: building
    """


def every_scope_character(arg):
    """

    Iterate through all characters in a: country, interestgroup, or front
    every_scope_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def every_scope_country(arg):
    """

    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    every_scope_country = { limit = { <triggers> } <effects> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country
    """


def every_scope_culture(arg):
    """

    Iterate through all cultures in the scope
    every_scope_culture = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture
    """


def every_scope_diplomatic_pact(arg):
    """

    Any diplomatic pact of the country in a scope
    every_scope_diplomatic_pact = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: diplomatic_pact
    """


def every_scope_front(arg):
    """

    Iterate through all Fronts related to the scoped War
    every_scope_front = { limit = { <triggers> } <effects> }
    **Supported Scopes**: war
    **Supported Targets**: front
    """


def every_scope_general(arg):
    """

    Iterate through all generals in a: country, interestgroup, front, or military formation
    every_scope_general = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def every_scope_held_interest_marker(arg):
    """

    Iterate through all interest markers held by a country
    every_scope_held_interest_marker = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_marker
    """


def every_scope_initiator_ally(arg):
    """

    Iterate through all allies to an initiator in a: diplomatic play
    every_scope_initiator_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def every_scope_interest_marker(arg):
    """

    Iterate through all interest markers in a: country, strategic region
    every_scope_interest_marker = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker
    """


def every_scope_play_involved(arg):
    """

    Iterate through all involved in a: diplomatic play
    every_scope_play_involved = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def every_scope_politician(arg):
    """

    Iterate through all politicians in a: country or interestgroup
    every_scope_politician = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def every_scope_pop(arg):
    """

    Iterate through all pops in a: country, state, interest group, culture
    every_scope_pop = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, culture, interest_group, state
    **Supported Targets**: pop
    """


def every_scope_state(arg):
    """

    Iterate through all states including provinces from a: country, state_region, theater, or front
    every_scope_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state
    """


def every_scope_target_ally(arg):
    """

    Iterate through all allies to a target in a: diplomatic play
    every_scope_target_ally = { limit = { <triggers> } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def every_scope_theater(arg):
    """

    Iterate through all theaters in a: country
    every_scope_theater = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: theater
    """


def every_scope_violate_sovereignty_interested_parties(arg):
    """

    Iterate through all countries that would be interested if country in scope has their sovereignty violated
    every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_scope_violate_sovereignty_wars(arg):
    """

    Iterate through all relevant wars if target country had their sovereignty violated by scoped country
    every_scope_violate_sovereignty_wars = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """


def every_scope_war(arg):
    """

    Iterate through all wars related to the scope
    every_scope_war = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """


def every_sea_node_adjacent_state(arg):
    """

    Iterate through all states that share a sea node with a state
    every_sea_node_adjacent_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: state
    **Supported Targets**: state
    """


def every_state(arg):
    """

    Iterate through all states globally
    every_state = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state
    """


def every_state_region(arg):
    """

    Iterate through all state regions
    every_state_region = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region
    """


def every_strategic_objective(arg):
    """

    Iterate through all Strategic Objective states from the scoped Country
    every_strategic_objective = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: state
    """


def every_subject_or_below(arg):
    """

    Any country below current in hierarchy
    every_subject_or_below = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def every_supporting_character(arg):
    """

    Iterate through all characters that support the scoped political movement
    every_supporting_character = { limit = { <triggers> } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character
    """


def every_supporting_interest_group(arg):
    """

    Iterate through all interest groups supporting a political movement
    every_supporting_interest_group = { limit = { <triggers> } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group
    """


def every_trade_route(arg):
    """

    Iterate through all trade routes in a: market, country, marketgoods
    every_trade_route = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route
    """


def every_valid_mass_migration_culture(arg):
    """

    Lists for cultures in the scoped country that are valid for mass migration
    every_valid_mass_migration_culture = { limit = { <triggers> } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: culture
    """


def exile_character(arg):
    """

    Exile a character to the exile pool
    exile_character = yes
    **Supported Scopes**: character
    """


def force_resource_depletion(arg):
    """

    Forces a resource depletion in state
    force_resource_depletion = bg_gold_mining
    **Supported Scopes**: state
    """


def force_resource_discovery(arg):
    """

    Forces a resource discovery in state
    force_resource_discovery = bg_gold_mining
    **Supported Scopes**: state
    """


def free_character_from_void(arg):
    """

    Frees a character from the void, if set to no character is deleted instead
    free_character_from_void = yes
    **Supported Scopes**: character
    """


def fully_mobilize_army(arg):
    """

    Fully mobilizes scope army
    fully_mobilize_army = yes
    **Supported Scopes**: military_formation
    """


def hidden_effect(arg):
    """

    Enclosed effects are not shown in tooltips
    hidden_effect = { <more effects> }
    **Supported Scopes**: none/all
    """


def If(arg):
    """

    Executes enclosed effects if limit criteria are met
    if = { limit = { <triggers> } <effects> }
    **Supported Scopes**: none/all
    """


def join_revolution(arg):
    """

    Adds interest group to ongoing revolution
    join_revolution = yes/no
    **Supported Scopes**: interest_group
    """


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


def kill_population(arg):
    """

    Kills a number of individuals in the population in the scoped country.

    All parameters except percent are optional. Pop type and strata cannot be used at the same time.kill_population = {
        value = <integer value>
        culture = <scope/cu:key>
        religion = <scope/rel:key>
        interest_group = <scope/ig:key>
        pop_type = <scope/pop_type:key>
        strata = <key>
    }
    **Supported Scopes**: country
    """


def kill_population_in_state(arg):
    """

    Kills a number of individuals in the population in the scoped state.

    All parameters except percent are optional. Pop type and strata cannot be used at the same time.kill_population = {
        value = <integer value>
        culture = <scope/cu:key>
        religion = <scope/rel:key>
        interest_group = <scope/ig:key>
        pop_type = <scope/pop_type:key>
        strata = <key>
    }
    **Supported Scopes**: state
    """


def kill_population_percent(arg):
    """

    Kills a percentage of the population in the scoped country.

    All parameters except percent are optional. Pop type and strata cannot be used at the same time.kill_population_percent = {
        percent = <decimal value>
        culture = <scope/cu:key>
        religion = <scope/rel:key>
        interest_group = <scope/ig:key>
        pop_type = <scope/pop_type:key>
        strata = <key>
    }
    **Supported Scopes**: country
    """


def kill_population_percent_in_state(arg):
    """

    Kills a percentage of the population in the scoped state.

    All parameters except percent are optional. Pop type and strata cannot be used at the same time.kill_population_percent = {
        percent = <decimal value>
        culture = <scope/cu:key>
        religion = <scope/rel:key>
        interest_group = <scope/ig:key>
        pop_type = <scope/pop_type:key>
        strata = <key>
    }
    **Supported Scopes**: state
    """


def lock_trade_route(arg):
    """

    Lock a trade route for a set amount of time, preventing it from being cancelled manually
    lock_trade_route = {
        years = 5
    }
    **Supported Scopes**: trade_route
    """


def make_independent(arg):
    """

    Makes a country independent.
    make_independent = bool
    **Supported Scopes**: country
    """


def mobilize_army(arg):
    """

    Mobilizes scope army
    mobilize_army = yes
    **Supported Scopes**: military_formation
    """


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


def place_character_in_void(arg):
    """

    Banishes a character to the void, duration is how long character is kept before being deleted
    place_character_in_void = months
    **Supported Scopes**: character
    """


def play_as(arg):
    """

    Change which country scoped country's player will play as
    play_as = <scope>
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def post_notification(arg):
    """

    Posts notification
    **Supported Scopes**: none/all
    """


def post_proposal(arg):
    """

    Posts proposal
    **Supported Scopes**: none/all
    """


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


def random_active_party(arg):
    """

    Iterate through all active political parties in a country
    random_active_party = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """


def random_character(arg):
    """

    Iterate through all characters globally
    random_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def random_character_in_exile_pool(arg):
    """

    Iterate through characters in the exile pool
    random_character_in_exile_pool = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def random_character_in_void(arg):
    """

    Iterate through characters in the void
    random_character_in_void = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: character
    """


def random_civil_war(arg):
    """

    Iterate through all civil wars related to the scoped country
    random_civil_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: civil_war
    """


def random_cobelligerent_in_diplo_play(arg):
    """

    Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars)
    random_cobelligerent_in_diplo_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_cobelligerent_in_war(arg):
    """

    Iterate through all co-belligerents of scope country in all wars
    random_cobelligerent_in_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_combat_unit(arg):
    """

    Iterate through all combat units of input scope
    Supported scopes: building, military formation, front, battle
    random_combat_unit = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: battle, building, front, hq, military_formation
    **Supported Targets**: new_combat_unit
    """


def random_company(arg):
    """

    Iterate through all companies in a country
    random_company = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: company
    """


def random_country(arg):
    """

    Iterate through all countries globally
    random_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: country
    """


def random_diplomatic_play(arg):
    """

    Iterate through all diplomatic plays globally
    random_diplomatic_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: diplomatic_play
    """


def random_enemy_in_diplo_play(arg):
    """

    Iterate through all enemies of scope country in all diplomatic plays (includes wars)
    random_enemy_in_diplo_play = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_enemy_in_war(arg):
    """

    Iterate through all enemies of scope country in all wars
    random_enemy_in_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_in_global_list(arg):
    """

    Iterate through all items in global list. list = name or variable = name
    random_in_global_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """


def random_in_hierarchy(arg):
    """

    Any country in current hierarchy, including current
    random_in_hierarchy = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_in_list(arg):
    """

    Iterate through all items in list. list = name or variable = name
    random_in_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """


def random_in_local_list(arg):
    """

    Iterate through all items in local list. list = name or variable = name
    random_in_local_list = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    """


def random_interest_group(arg):
    """

    Iterate through all interest groups in a country
    random_interest_group = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_group
    """


def random_law(arg):
    """

    Iterate through all laws in a country
    random_law = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: law
    """


def random_list(arg):
    """

    a random list effect
    random_list = { X1 = { trigger = { enables/disable this effect} modifier = Y1 effect1 } X2 = { trigger = { enables/disable this effect} modifier = Y2 effect2 } ... }
    Selects one effect from the list and fires it. The effects are weighted by numbers X1, X2... (the higher the number, the higher the chance of the effect being picked).
    The chances can be modified by optional value modifier lists Y1, Y2... (AKA MTTH constructs)
    **Supported Scopes**: none/all
    """


def random_log_scopes(arg):
    """

    Log the current scope to the random log when this effect executes.
    Only use temprorarily for debugging purposes as it can introduce localized strings into the random log.
    random_log_scopes = yes # log full scope info
    random_log_scopes = no  # log only current scope
    **Supported Scopes**: none/all
    """


def random_market(arg):
    """

    Iterate through all markets globally
    random_market = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: market
    """


def random_market_goods(arg):
    """

    Iterate through all active (market) goods in a market
    random_market_goods = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: market
    **Supported Targets**: market_goods
    """


def random_member(arg):
    """

    Iterate through all interest group members of a party
    random_member = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: party
    **Supported Targets**: interest_group
    """


def random_military_formation(arg):
    """

    Iterate through all military formations currently present at input scope
    Supported scopes: country, front, hq
    random_military_formation = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, hq
    **Supported Targets**: military_formation
    """


def random_neighbouring_state(arg):
    """

    Iterate through all states neighbouring a state region
    random_neighbouring_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state, state_region, strategic_region
    **Supported Targets**: state
    """


def random_overlord_or_above(arg):
    """

    Any country above current in hierarchy
    random_overlord_or_above = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_participant(arg):
    """

    Any of two participants of the diplomatic pact in a scope
    random_participant = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_pact
    **Supported Targets**: country
    """


def random_political_movement(arg):
    """

    Iterate through all political movements in a country
    random_political_movement = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: political_movement
    """


def random_potential_party(arg):
    """

    Iterate through all potential political parties in a country
    random_potential_party = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: party
    """


def random_preferred_law(arg):
    """

    Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law
    random_preferred_law = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: interest_group
    **Supported Targets**: law
    """


def random_primary_culture(arg):
    """

    Primary cultures of the scoped country or country definition(arg):

    random_primary_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, country_definition, state(arg):

    **Supported Targets**: culture
    """


def random_province(arg):
    """

    Iterate through all Provinces in the scoped State
    random_province = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: province
    **Supported Targets**: state
    """


def random_rival_country(arg):
    """

    Any country that is rival to the country in a scope
    random_rival_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_scope_admiral(arg):
    """

    Iterate through all admirals in a: country, interestgroup, or military formation
    random_scope_admiral = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def random_scope_ally(arg):
    """

    Iterate through all allies to a: country
    random_scope_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_scope_building(arg):
    """

    Iterate through all buildings in a: state, country
    random_scope_building = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: building
    """


def random_scope_character(arg):
    """

    Iterate through all characters in a: country, interestgroup, or front
    random_scope_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def random_scope_country(arg):
    """

    Iterate through all countries with a presence in the supported scope (currently: market, strategic region)
    random_scope_country = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: market, strategic_region
    **Supported Targets**: country
    """


def random_scope_culture(arg):
    """

    Iterate through all cultures in the scope
    random_scope_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, state
    **Supported Targets**: culture
    """


def random_scope_diplomatic_pact(arg):
    """

    Any diplomatic pact of the country in a scope
    random_scope_diplomatic_pact = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: diplomatic_pact
    """


def random_scope_front(arg):
    """

    Iterate through all Fronts related to the scoped War
    random_scope_front = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: war
    **Supported Targets**: front
    """


def random_scope_general(arg):
    """

    Iterate through all generals in a: country, interestgroup, front, or military formation
    random_scope_general = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def random_scope_held_interest_marker(arg):
    """

    Iterate through all interest markers held by a country
    random_scope_held_interest_marker = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: interest_marker
    """


def random_scope_initiator_ally(arg):
    """

    Iterate through all allies to an initiator in a: diplomatic play
    random_scope_initiator_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def random_scope_interest_marker(arg):
    """

    Iterate through all interest markers in a: country, strategic region
    random_scope_interest_marker = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, strategic_region
    **Supported Targets**: interest_marker
    """


def random_scope_play_involved(arg):
    """

    Iterate through all involved in a: diplomatic play
    random_scope_play_involved = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def random_scope_politician(arg):
    """

    Iterate through all politicians in a: country or interestgroup
    random_scope_politician = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, interest_group, military_formation
    **Supported Targets**: character
    """


def random_scope_pop(arg):
    """

    Iterate through all pops in a: country, state, interest group, culture
    random_scope_pop = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, culture, interest_group, state
    **Supported Targets**: pop
    """


def random_scope_state(arg):
    """

    Iterate through all states including provinces from a: country, state_region, theater, or front
    random_scope_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, front, state_region, strategic_region, theater
    **Supported Targets**: state
    """


def random_scope_target_ally(arg):
    """

    Iterate through all allies to a target in a: diplomatic play
    random_scope_target_ally = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def random_scope_theater(arg):
    """

    Iterate through all theaters in a: country
    random_scope_theater = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: theater
    """


def random_scope_violate_sovereignty_interested_parties(arg):
    """

    Iterate through all countries that would be interested if country in scope has their sovereignty violated
    random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_scope_violate_sovereignty_wars(arg):
    """

    Iterate through all relevant wars if target country had their sovereignty violated by scoped country
    random_scope_violate_sovereignty_wars = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """


def random_scope_war(arg):
    """

    Iterate through all wars related to the scope
    random_scope_war = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: war
    """


def random_sea_node_adjacent_state(arg):
    """

    Iterate through all states that share a sea node with a state
    random_sea_node_adjacent_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: state
    **Supported Targets**: state
    """


def random_state(arg):
    """

    Iterate through all states globally
    random_state = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state
    """


def random_state_region(arg):
    """

    Iterate through all state regions
    random_state_region = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: none/all
    **Supported Targets**: state_region
    """


def random_strategic_objective(arg):
    """

    Iterate through all Strategic Objective states from the scoped Country
    random_strategic_objective = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: state
    """


def random_subject_or_below(arg):
    """

    Any country below current in hierarchy
    random_subject_or_below = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: country
    """


def random_supporting_character(arg):
    """

    Iterate through all characters that support the scoped political movement
    random_supporting_character = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: character
    """


def random_supporting_interest_group(arg):
    """

    Iterate through all interest groups supporting a political movement
    random_supporting_interest_group = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: political_movement
    **Supported Targets**: interest_group
    """


def random_trade_route(arg):
    """

    Iterate through all trade routes in a: market, country, marketgoods
    random_trade_route = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country, market, market_goods
    **Supported Targets**: trade_route
    """


def random_valid_mass_migration_culture(arg):
    """

    Lists for cultures in the scoped country that are valid for mass migration
    random_valid_mass_migration_culture = { limit = { <triggers> } (optional) weight = { mtth } <effects> }
    **Supported Scopes**: country
    **Supported Targets**: culture
    """


def recalculate_pop_ig_support(arg):
    """

    Recalculates and updates a country's pop IG memberships = bool
    **Supported Scopes**: country
    """


def remove_active_objective_subgoal(arg):
    """

    Removes an active objective subgoal
    remove_active_objective_subgoal = <key>
    **Supported Scopes**: country
    """


def remove_as_interest_group_leader(arg):
    """

    Removes a character from position as interest group leader
    remove_as_interest_group_leader = yes
    **Supported Scopes**: character
    """


def remove_banned_goods(arg):
    """

    Removes a total ban of a good from a country
    remove_banned_goods = <goods key/scope>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def remove_building(arg):
    """

    Remove a building in the scope state
    remove_building = building_key
    **Supported Scopes**: state
    """


def remove_character_role(arg):
    """

    Removes an existing role from a character
    remove_character_role = general
    **Supported Scopes**: character
    """


def remove_claim(arg):
    """

    Removes scoped state region as a claim for target country
    add_claim = scope/country
    **Supported Scopes**: state_region
    **Supported Targets**: country
    """


def remove_company(arg):
    """

    Removes company type from a country's companies
    remove_company = company_type:key
    **Supported Scopes**: country
    **Supported Targets**: company_type
    """


def remove_cultural_obsession(arg):
    """

    Removes a new obsession to the culture in scope
    remove_cultural_obsession = X
    Where X is a goods
    **Supported Scopes**: culture
    """


def remove_diplomatic_pact(arg):
    """

    Removes a diplomatic pact between two countries, with scope country as initiator
    remove_diplomatic_pact = {
        country = country scope/tag
        type = diplomatic action type
    }
    **Supported Scopes**: country
    """


def remove_enactment_modifier(arg):
    """

    Removes an enactment-related timed modifier effect to object in scope
    **Supported Scopes**: country
    """


def remove_from_list(arg):
    """

    Removes the current scope from a named list remove_from_list = <string>
    **Supported Scopes**: none/all
    """


def remove_global_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """


def remove_homeland(arg):
    """

    Removes scoped state region as Homeland for target culture
    remove_homeland = cu:culture
    **Supported Scopes**: state_region
    **Supported Targets**: culture
    """


def remove_ideology(arg):
    """

    Removes an ideology from scoped interest group
    remove_ideology = x
    **Supported Scopes**: interest_group
    """


def remove_ig_from_party(arg):
    """

    Removes target interest group from scope party
    py:py_key = {
        remove_ig_from_party = ig:ig_key
    }
    **Supported Scopes**: party
    **Supported Targets**: interest_group
    """


def remove_initiator_backers(arg):
    """

    Remove a tag/scope country from the initiator side of a diplomatic play
    remove_initiator_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """


def remove_list_global_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def remove_list_local_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def remove_list_variable(arg):
    """

    Removes the target from a variable list
    remove_list_variable = { name = X target = Y }
    Where X is the name of the variable
    Where Y is an event target
    **Supported Scopes**: none/all
    """


def remove_local_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """


def remove_modifier(arg):
    """

    Removes a timed modifier effect to object in scope
    **Supported Scopes**: country, building, character, institution, interest_group, journalentry, political_movement, state
    """


def remove_primary_culture(arg):
    """

    Removes a culture from the primary cultures of a country
    remove_primary_culture = X
    Where X is a culture scope
    **Supported Scopes**: country
    **Supported Targets**: culture
    """


def remove_ruling_interest_group(arg):
    """

    Removes interest group in scope from government
    remove_ruling_interest_group = yes/no
    **Supported Scopes**: interest_group
    """


def remove_state_trait(arg):
    """

    remove state trait in a scoped state region
    remove_state_trait = <state_trait_name>
    **Supported Scopes**: state_region
    """


def remove_target_backers(arg):
    """

    Remove a tag/scope country to the target side of a diplomatic play
    remove_target_backers = { list of scopes/tags }
    **Supported Scopes**: diplomatic_play
    """


def remove_taxed_goods(arg):
    """

    Removes consumption taxes on a good from a country
    remove_taxed_goods = <goods key/scope>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def remove_trait(arg):
    """

    Remove a trait from a Character
    remove_trait = trait
    **Supported Scopes**: character
    """


def remove_variable(arg):
    """

    Removes a variable
    remove_variable = variable_name
    **Supported Scopes**: none/all
    """


def remove_war_goal(arg):
    """

    Removes a war goal from a DP.
    any_diplomatic_play = { limit = { has_war_goal = return_state } remove_war_goal = { who = initiator war_goal = return_state } }
    **Supported Scopes**: diplomatic_play
    """


def resolve_play_for(arg):
    """

    effect end diplo play for one side, with it gaining war goals
    resolve_play_for = initiator
    resolve_play_for = scope:custom_scoped_country
    **Supported Scopes**: diplomatic_play
    **Supported Targets**: country
    """


def round_global_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """


def round_local_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """


def round_variable(arg):
    """

    Rounds a variable to the nearest specified value
    round_variable = { name = X nearest = Y }
    Where X is the name of the variable
    Where Y is a script value
    **Supported Scopes**: none/all
    """


def save_scope_as(arg):
    """

    Saves the current scope as an arbitrarily-named target to be referenced later in the (unbroken) event chain
    save_scope_as = <string>
    **Supported Scopes**: none/all
    """


def save_scope_value_as(arg):
    """

    Saves a numerical or bool value as an arbitrarily-named target to be referenced later in the (unbroken) event chain
    save_scope_value_as = { name = <string> value = x }
    **Supported Scopes**: none/all
    """


def save_temporary_scope_as(arg):
    """

    Saves the current scope as an arbitrarily-named temporary target to be referenced later in the same effect
    save_temporary_scope_as = <string>
    **Supported Scopes**: none/all
    """


def save_temporary_scope_value_as(arg):
    """

    Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect
    save_temporary_scope_value_as = { name = <string> value = x }
    **Supported Scopes**: none/all
    """


def seize_investment_pool(arg):
    """

    Seize investment pool for the treasury and transfer all private construction queue elements to the government queue = bool
    **Supported Scopes**: country
    """


def set_as_interest_group_leader(arg):
    """

    Sets a character as interest group leader
    set_as_interest_group_leader = yes
    **Supported Scopes**: character
    """


def set_available_for_autonomous_investment(arg):
    """

    Sets a building type as available for autonomous investment in the current scoped State
    set_available_for_autonomous_investment = building type scope
    **Supported Scopes**: state
    **Supported Targets**: building_type
    """


def set_capital(arg):
    """

    Set capital state in a country scope
    set_capital = X
    Where X is a state region
    **Supported Scopes**: country
    """


def set_character_as_ruler(arg):
    """

    Set scoped character as ruler in their country.
    scope:larry = { set_character_as_ruler = yes }
    **Supported Scopes**: character
    """


def set_character_busy_and_immortal(arg):
    """

    Mark a character as busy and immortal or clear said mark
    set_character_busy = bool
    **Supported Scopes**: character
    """


def set_character_immortal(arg):
    """

    Set scoped character as immortal.
    scope:larry = { set_character_immortal = yes/no }
    **Supported Scopes**: character
    """


def set_commander_rank(arg):
    """

    Promotes/demotes a character to a given military rank value
    set_commander_rank = 3
    **Supported Scopes**: character
    """


def set_company_establishment_date(arg):
    """

    Sets the establishment date of scope company
    set_company_establishment_date = 1782.7.18
    **Supported Scopes**: company
    """


def set_country_type(arg):
    """

    Sets the type of country for a country, for history
    **Supported Scopes**: country
    """


def set_devastation(arg):
    """

    Set devastation to a state region
    **Supported Scopes**: state_region
    """


def set_diplomats_expelled(arg):
    """

    Set diplomats expelled = bool
    **Supported Scopes**: country
    **Supported Targets**: country
    """


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


def set_government_wage_level(arg):
    """

    Sets the government wage level of scoped country
    set_government_wage_level = very_low/low/medium/high/very_high
    **Supported Scopes**: country
    """


def set_home_country(arg):
    """

    Set a character's home country. This makes them start considering themselves as having been exiled, i.e. was_exiled starts evaluating to yes for them.
    set_home_country = c:FRA
    **Supported Scopes**: character
    **Supported Targets**: country
    """


def set_home_country_definition(arg):
    """

    Set a character's home country directly to a tag, you can use this to avoid making sure that the tag exists, this makes them an exile
    set_home_country_definition = cd:FRA(arg):

    **Supported Scopes**: character
    **Supported Targets**: country_definition(arg):

    """


def set_ideology(arg):
    """

    Changes scoped character's ideology
    set_ideology = x
    **Supported Scopes**: character
    **Supported Targets**: ideology
    """


def set_ig_bolstering(arg):
    """

    Starts/stops bolstering the interest group in scope
    set_ig_bolstering = yes/no
    **Supported Scopes**: interest_group
    """


def set_ig_suppression(arg):
    """

    Starts/stops suppressing the interest group in scope
    set_ig_suppression = yes/no
    **Supported Scopes**: interest_group
    """


def set_ig_trait(arg):
    """

    Adds a trait to the Interest Group, or replaces their current trait with the same approval level
    set_ig_trait = ig_trait:ig_trait_engines_of_progress
    **Supported Scopes**: interest_group
    **Supported Targets**: interest_group_trait
    """


def set_immune_to_revolutions(arg):
    """

    Makes a country immune to revolutions or removes such immunity.
    set_immune_to_revolutions = yes/no
    **Supported Scopes**: country
    """


def set_institution_investment_level(arg):
    """

    Sets the investment level for an institution
    set_institution_investment_level = { institution = <key> level = x }
    **Supported Scopes**: country
    """


def set_interest_group_name(arg):
    """

    Renames interest group to the specified loc key
    set_interest_group_name = x
    **Supported Scopes**: interest_group
    """


def set_key(arg):
    """

    Set name to a diplomatic play
    set_key = loc_key
    **Supported Scopes**: diplomatic_play
    """


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


def set_market_capital(arg):
    """

    Set market capital in a country scope
    set_market_capital = X
    Where X is a state region
    **Supported Scopes**: country
    """


def set_military_wage_level(arg):
    """

    Sets the military wage level of scoped country
    set_military_wage_level = very_low/low/medium/high/very_high
    **Supported Scopes**: country
    """


def set_mutual_secret_goal(arg):
    """

    Set mutual secret AI goal for scope country and target country
    set_mutual_secret_goal = {
        tcountry = country scope/tag
        secret_goal = secret goal type
    }
    **Supported Scopes**: country
    """


def set_next_election_date(arg):
    """

    Set next election date for country
    set_next_election_date = year.month.day
    **Supported Scopes**: country
    """


def set_owes_obligation_to(arg):
    """

    Set whether a country owes another a obligation
    set_owes_obligation = {
        country = country scope/tag
        setting = yes/no
    }
    **Supported Scopes**: country
    """


def set_owner_of_provinces(arg):
    """

    Gives a set of provinces in a state region to a specific country
    set_owner_of_provinces = { country = <scope> provinces = {} }
    **Supported Scopes**: state_region
    """


def set_pop_literacy(arg):
    """

    Sets the literacy of the pop
    set_pop_literacy = { literacy_rate = {...} }
    Where the ratio is a script value computing the percentage of (workforce) pops that will be literate
    **Supported Scopes**: pop
    """


def set_pop_qualifications(arg):
    """

    Sets the pop qualifications of the pop for the given type
    set_pop_qualifications = { pop_type = {} qualifications = {...} }
    Where the qualifications is a script value computing the percentage of (workforce) pops that will have the qualifications
    **Supported Scopes**: pop
    """


def set_pop_wealth(arg):
    """

    Sets the wealth of the pop
    set_pop_wealth = { wealth_distribution = {...} update_loyalties = true/false }
    Where wealth is a script values
    **Supported Scopes**: pop
    """


def set_relations(arg):
    """

    Set relations between two countries
    set_relations = {
        tcountry = country scope/tag
        value = amount
    }
    **Supported Scopes**: country
    """


def set_ruling_interest_groups(arg):
    """

    Creates a government for the country in scope from a set of interest groups
    set_ruling_interest_groups = { ig_tag1 ig_tag2 }
    **Supported Scopes**: country
    """


def set_ruling_party(arg):
    """

    Adds all interest groups in a party to government and removes all other interest groups from the government
    set_ruling_party = yes
    **Supported Scopes**: party
    """


def set_secret_goal(arg):
    """

    Set a secret AI goal for scope country towards another country
    set_secret_goal = {
        tcountry = country scope/tag
        secret_goal = secret goal type
    }
    **Supported Scopes**: country
    """


def set_state_owner(arg):
    """

    Set State Owner
    set_state_owner = scope
    **Supported Scopes**: state
    **Supported Targets**: country
    """


def set_state_religion(arg):
    """

    Changes the state religion of the country to the specified religion
    set_state_religion = X
    Where X is a religion scope
    **Supported Scopes**: country
    **Supported Targets**: religion
    """


def set_state_type(arg):
    """

    Sets a state to a certain type (incorporated, unincorporated, treaty_port)
    **Supported Scopes**: state
    """


def set_strategy(arg):
    """

    Set AI strategy for scope country
    set_strategy = <key>
    **Supported Scopes**: country
    """


def set_subsidized(arg):
    """

    Sets whether a building is subsidized
    set_subsidized = yes/no
    **Supported Scopes**: building
    """


def set_target_technology(arg):
    """

    Sets a (new) target technology scope for a journal entry
    set_target_technology = <scope>
    **Supported Scopes**: journalentry
    """


def set_tariffs_export_priority(arg):
    """

    Sets Export Prioritized tariffs for a good in scoped country
    set_tariffs_export_priority = <scope/key>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def set_tariffs_import_priority(arg):
    """

    Sets Import Prioritized tariffs for a good in scoped country
    set_tariffs_import_priority = <scope/key>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def set_tariffs_no_priority(arg):
    """

    Sets tariffs to have no import/export priority for a good in scoped country
    set_tariffs_no_priority = <scope/key>
    **Supported Scopes**: country
    **Supported Targets**: goods
    """


def set_tax_level(arg):
    """

    Sets the overall tax level of scoped country
    set_tax_level = very_low/low/medium/high/very_high
    **Supported Scopes**: country
    """


def set_tension(arg):
    """

    Set tension between two countries
    set_tension = {
        tcountry = country scope/tag
        value = amount
    }
    **Supported Scopes**: country
    """


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


def set_war(arg):
    """

    Set a diplomatic play to be a war
    set_war = bool
    **Supported Scopes**: diplomatic_play
    """


def show_as_tooltip(arg):
    """

    Enclosed effects are only shown in tooltips (but are not actually executed)
    show_as_tooltip = { <more effects> }
    **Supported Scopes**: none/all
    """


def start_building_construction(arg):
    """

    Start constructing a building in a scoped state as a government construction
    start_building_construction = building_barracks
    **Supported Scopes**: state
    """


def start_enactment(arg):
    """

    Starts enacting the specified law type for the country in scope
    start_enactment = law_type:law_multicultural
    **Supported Scopes**: country
    **Supported Targets**: law_type
    """


def start_privately_funded_building_construction(arg):
    """

    Start constructing a building in a scoped state as a private construction
    start_privately_funded_building_construction = building_barracks
    **Supported Scopes**: state
    """


def start_research_random_technology(arg):
    """

    Scoped country starts research of any random technology they can
    start_research_random_technology = yes
    **Supported Scopes**: country
    """


def start_tutorial_lesson(arg):
    """

    Starts the tutorial lesson with the given key. Does nothing if the tutorial is not running, the lesson is completed (or already running), or the lesson cannot be triggered (e.g. trigger fails)
    **Supported Scopes**: none/all
    """


def switch(arg):
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


def take_on_scaled_debt(arg):
    """

    Transfers an amount of debt equal to the defined multiplier on target's max credit(arg):

    take_on_scaled_debt = {
        who = <country>
        value = decimal value
    }
    **Supported Scopes**: country
    """


def teleport_to_front(arg):
    """

    Teleports the scope formation to the target front
    teleport_to_front = p:xFAFAFA.front
    **Supported Scopes**: military_formation
    **Supported Targets**: front
    """


def transfer_character(arg):
    """

    Transfers current scope character to target country
    transfer_character = country
    **Supported Scopes**: character
    **Supported Targets**: country
    """


def transfer_to_formation(arg):
    """

    Transfers scope character to target formation
    transfer_to_formation = scope:formation
    **Supported Scopes**: character
    **Supported Targets**: military_formation
    """


def trigger_event(arg):
    """

    Triggers an event for the current scope
    trigger_event = X
    trigger_event = { id = X days/weeks/months/years = Y }
    Where X is an event ID and Y is an integer to delay the event by
    **Supported Scopes**: none/all
    """


def unset_available_for_autonomous_investment(arg):
    """

    Sets a building type as unavailable for autonomous investment in the current scoped State
    unset_available_for_autonomous_investment = building type scope
    **Supported Scopes**: state
    **Supported Targets**: building_type
    """


def update_party_support(arg):
    """

    Updates party support in scoped country.
    update_party_support = yes
    **Supported Scopes**: country
    """


def validate_subsidies(arg):
    """

    Validates subsidies across a country's buildings.
    validate_subsidies = bool
    **Supported Scopes**: country
    """


def violate_sovereignty_join(arg):
    """

    Target joins scoped war
    violate_sovereignty_accept = <country>
    **Supported Scopes**: country
    """


def While(arg):
    """

    Repeats enclosed effects while limit criteria are met or until set iteration count is reached
    while = { limit = { <triggers> } <effects> }
     while = { count = 3 <effects> }
        default max of 1000.(arg):

    **Supported Scopes**: none/all
        """