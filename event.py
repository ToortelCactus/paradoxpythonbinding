from helpers import eq, br, list_to_text
from enum import Enum
from scriptbase import getlocalscriptfile
from options import Option
from string import ascii_lowercase
from effect.country import CountryEffect
from effect.state import StateEffect

from typing import List

defs = ["type", "placement", "title", "desc", "flavor", "icon", "duration",
        "on_created_soundeffect", "on_opened_soundeffect"]

defsBr = ["immediate", "trigger", "cancellation_trigger", "event_image"]


class EventType(Enum):
    country_event = 1
    character_event = 2
    state_event = 3


def empty_data():
    data = {}
    for d in defs:
        data.setdefault(d, None)
    return data


def empty_brdata():
    data = {}
    for d in defsBr:
        data.setdefault(d, None)
    return data


class Event:
    """
    Creates event
    """

    def __init__(self, name: str,
                 event_type: EventType,
                 effects: list,
                 trigger: list,
                 icon_path: str,
                 duration: int,
                 event_img_path: str,
                 created_sfx_path: str,
                 options: list,
                 cancel_trigger=None,
                 placement: str = "root",
                 opened_sfx_path: str = None,
                 desc_file: str = None):
        # register this somewhere or something
        self.name = name
        self.data = empty_data()
        self.brdata = empty_brdata()
        self.option_data = []
        if desc_file:
            self.description(desc_file)
        else:
            self.description(self.name)

        self.type(event_type)
        self.placement(placement)
        self.immediate(effects)
        self.trigger(trigger)
        self.cancellation_trigger(cancel_trigger)
        self.icon(icon_path)
        self.duration(duration)
        self.event_image(event_img_path)
        self.on_created_soundeffect(created_sfx_path)
        self.on_opened_soundeffect(opened_sfx_path)
        self.options(options)
        self.addendum = ""

        getlocalscriptfile().export(str(self))

    def type(self, ty: EventType):
        self.data["type"] = ty.name
        return self

    def placement(self, scope):
        self.data["placement"] = scope
        return self

    def description(self, filename):
        """
        This includes title and flavor.
        Using this overwrites default
        """
        self.data["title"] = filename + ".t"
        self.data["desc"] = filename + ".desc"
        self.data["flavor"] = filename + ".f"
        return self

    def immediate(self, effects: list):
        self.brdata["immediate"] = list_to_text(effects)
        return self

    def trigger(self, conditionals: list):
        if conditionals:
            self.brdata["trigger"] = list_to_text(conditionals)
        return self

    def cancellation_trigger(self, conditional):
        self.brdata["cancellation_trigger"] = conditional
        return self

    def icon(self, path):
        self.data["icon"] = '"' + path + '"'
        return self

    def duration(self, num: int):
        self.data["duration"] = str(num)
        return self

    def event_image(self, path):
        content = '"' + path + '"'
        if path[-1] == "2":
            content = eq("video", br(content, 2))
        else:
            content = eq("texture", br(content, 2))

        self.brdata["event_image"] = content
        return self

    def on_created_soundeffect(self, path):
        self.data["on_created_soundeffect"] = '"' + path + '"'
        return self

    def on_opened_soundeffect(self, path):
        if path:
            self.data["on_opened_soundeffect"] = '"' + path + '"'
        return self

    def options(self, options: List[Option]):
        self.option_data = options
        for opt, letter in zip(self.option_data, ascii_lowercase[:len(options)]):
            opt.name = self.name + "." + letter
        return self

    def add_text(self, text: str):
        """ When no other function can do the job, use this and write it in text (!danger! no validation) """
        self.addendum = text
        return self

    def __str__(self):
        content = ""

        # non-bracketed items
        for item in list(self.data.items()):
            if item[1]:
                content += eq(item[0], item[1]) + "\n"

        # bracketed items
        for item in list(self.brdata.items()):
            if item[1]:
                content += eq(item[0], br(item[1], 1)) + "\n"

        # options
        for option in self.option_data:
            content += eq("option", br(str(option), 1)) + "\n"

        content += self.addendum
        return eq(self.name, br(content))


class CountryEvent(Event):
    """
    Creates country event
    """

    def __init__(self, name: str,
                 immediate: List[CountryEffect],
                 trigger: list,
                 icon_path: str,
                 duration: int,
                 event_img_path: str,
                 created_sfx_path: str,
                 options: list,
                 cancel_trigger=None,
                 placement: str = "root",
                 opened_sfx_path: str = None,
                 desc_file: str = None):
        super().__init__(name,
                         EventType.country_event,
                         immediate,
                         trigger,
                         icon_path,
                         duration,
                         event_img_path,
                         created_sfx_path,
                         options,
                         cancel_trigger,
                         placement,
                         opened_sfx_path,
                         desc_file)


class CharacterEvent(Event):
    """
    Creates character event
    """
    def __init__(self, name: str, immediate: list, trigger: list, icon_path: str, duration: int, event_img_path: str,
                 created_sfx_path: str, options: list, cancel_trigger=None,
                 placement: str = "root", opened_sfx_path: str = None, desc_file: str = None):
        super().__init__(name,
                         EventType.character_event,
                         immediate,
                         trigger,
                         icon_path,
                         duration,
                         event_img_path,
                         created_sfx_path,
                         options,
                         cancel_trigger,
                         placement,
                         opened_sfx_path,
                         desc_file)


class StateEvent(Event):
    """
    Creates state event
    """
    def __init__(self, name: str,
                 immediate: List[StateEffect],
                 trigger: list,
                 icon_path: str,
                 duration: int,
                 event_img_path: str,
                 created_sfx_path: str,
                 options: list,
                 cancel_trigger=None,
                 placement: str = "root",
                 opened_sfx_path: str = None,
                 desc_file: str = None):
        super().__init__(name,
                         EventType.state_event,
                         immediate,
                         trigger,
                         icon_path,
                         duration,
                         event_img_path,
                         created_sfx_path,
                         options,
                         cancel_trigger,
                         placement,
                         opened_sfx_path,
                         desc_file)
