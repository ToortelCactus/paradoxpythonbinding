from typing import List
from transferendum_in_pythonis.helpers import eq, default_list
from transferendum_in_pythonis.scriptbase import getlocalscriptfile


class ChanceModifier:
    """ adds chance based on triggers """
    def __init__(self,
                 trigger: str,
                 add: int
                 ):
        self.content = default_list("modifier",
                                    [
                                        eq("trigger", trigger),
                                        eq("add", str(add))
                                    ])

    def __str__(self):
        return self.content


class Decision:
    """
    Creates a decision
    name - decision internal name
    is_shown - The requirements/to which countries the decision is shown
    possible - The requirements for the decision to be taken, trigger
    when_taken - basically "immediate", effects
    ai_chance_base - base AI chance (in percent, can be negative)
    ai_chance_modifiers - they add chance based on triggers

    """
    def __init__(self,
                 name: str,
                 is_shown: List[str],
                 possible: List[str],
                 when_taken: List[str],
                 ai_chance_base: int,
                 ai_chance_modifiers: List[ChanceModifier] = []
                 ):
        # register this somewhere or something
        self.content = [
            default_list("is_shown", is_shown),
            default_list("possible", possible),
            default_list("when_taken", when_taken),
            default_list("ai_chance", [eq("base", str(ai_chance_base))] + list(map(str, ai_chance_modifiers)))
        ]

        getlocalscriptfile().export(str(self))

    def __str__(self):
        return default_list("name", self.content)