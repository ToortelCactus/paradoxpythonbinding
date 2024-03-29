from typing import List, Tuple
from transferendum_in_pythonis.helpers import eq, default_list
from transferendum_in_pythonis.scriptbase import getlocalscriptfile
from transferendum_in_pythonis.parsing.generated.modifier_type import Modifier_type


class NewModifier:
    """
    Creates a modifier
    name - modifiers internal name
    icon - path to icon
    modifier_types - pairs of modifier type and value in string:
        [(Modifier_type.bank_credibility, "4.1")]

    """
    def __init__(self,
                 name: str,
                 icon: str,
                 modifier_types: List[Tuple[Modifier_type, str]]
                 ):
        # register this somewhere or something
        self.name = name
        self.content = [eq("icon", icon)]
        for mt, val in modifier_types:
            self.content.append(eq(mt.name, val))

        getlocalscriptfile().export(str(self))

    def __str__(self):
        return default_list(self.name, self.content)
