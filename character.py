from typing import List
from helpers import br, eq, add_if_defined
from scriptbase import getlocalscriptfile


class Character:
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
    def __init__(self,
                 first_name: str = "",
                 last_name: str = "",
                 culture: str = "",
                 religion: str = "",
                 female: bool = False,
                 noble: bool = False,
                 ruler: bool = False,
                 heir: bool = False,
                 historical: bool = False,
                 ig_leader: bool = False,
                 birth_date: str = "1920.1.1",
                 ideology: str = "",
                 interest_group: str = "",
                 template: str = "",
                 traits: List[str] = [],
                 save_scope_as: str = "",
                 trait_generation: str = "",
                 hq: str = ""):
        # register this somewhere or something
        self.content = ""

        for pair in zip([first_name, last_name, culture, religion, female, noble, ruler, heir, historical, ig_leader,
                         birth_date, ideology, interest_group, template, save_scope_as, hq],
                        "first_name, last_name, culture, religion, female, noble, ruler, heir, historical, ig_leader, "
                        "birth_date, ideology, interest_group, template, save_scope_as, hq".split(", ")):
            self.content += add_if_defined(pair[1], pair[0])

        if traits:
            traits_content = ""
            for item in traits:
                traits_content += item + "\n"
            self.content += eq("traits", br(traits_content))
        if trait_generation:
            self.content += eq("trait_generation", br(trait_generation))

        getlocalscriptfile().export(str(self))

    def __str__(self):
        return eq("create_character", br(self.content))
