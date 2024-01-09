from typing import List, Tuple
from helpers import eq, default_list
from scriptbase import getlocalscriptfile


class Journal:
    """
    Creates a journal entry
    name - internal name
    icon - path to icon

    NOT IMPLEMENTED

    """
    def __init__(self,
                 name: str,
                 icon: str,
                 is_shown_when_inactive: list, # trigger type
                 possible: list, # trigger type
                 complete: list, #trigger type
                 status_desc: list, # effect?
                 on_monthly_pulse: list, # effect
                 on_yearly_pulse: list, #effect
                 on_complete: list, # effect
                 fail: list, # trigger
                 weight: int,
                 transferable: str, #yes/no
                 progressbar: str,  #yes/no
                 should_be_pinned_by_default: str  #yes/no
                 ):
        # register this somewhere or something
        self.name = name
        self.content = [eq("icon", icon)]


        getlocalscriptfile().export(str(self))

    def __str__(self):
        return default_list(self.name, self.content)
