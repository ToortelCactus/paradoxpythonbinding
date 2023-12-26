from helpers import eq, br
from enum import Enum
import effects as ef
from scriptbase import getlocalscriptfile

defs = ["type", "placement", "title", "desc", "flavor", "icon", "duration",
        "immediate", "trigger", "event_image", "on_created_soundeffect",
        "on_opened_soundeffect", "cancellation_trigger"]


class EventType(Enum):
    country_event = 1
    character_event = 2
    state_event = 3


def empty_data():
    data = {}
    for d in defs:
        data.setdefault(d, None)
    return data


class Event:
    def __init__(self, name: str,
                 event_type: EventType,
                 effects: list,
                 trigger,
                 icon_path: str,
                 duration: int,
                 event_img_path: str,
                 created_sfx_path: str,
                 options: list,
                 placement: str = "root",
                 opened_sfx_path: str = None,
                 desc_file: str = None):
        # register this somewhere or something
        self.name = name
        self.data = empty_data()
        if desc_file:
            self.description(desc_file)
        else:
            self.description(self.name)

        self.type(event_type)
        self.immediate(effects)
        self.trigger(trigger)
        self.icon(icon_path)
        self.duration(duration)
        self.event_image(event_img_path)
        self.on_created_soundeffect(created_sfx_path)
        self.on_opened_soundeffect(opened_sfx_path)
        self.options(options)

        getlocalscriptfile().export(str(self))

    def type(self, ty: EventType):
        self.data["type"] = ty.name
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
        contents = ""
        for effect in effects:
            contents += "\t" + effect + "\n"

        self.data["immediate"] = contents
        return self

    def trigger(self, conditional):
        # TODO
        self.data["trigger"] = conditional
        return self

    def cancellation_trigger(self, conditional):
        self.data["cancellation_trigger"] = conditional
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

        self.data["event_image"] = content
        return self

    def on_created_soundeffect(self, path):
        self.data["on_created_soundeffect"] = '"' + path + '"'
        return self

    def on_opened_soundeffect(self, path):
        if path:
            self.data["on_opened_soundeffect"] = '"' + path + '"'
        return self

    def options(self, options: list):
        # TODO
        return self

    def __str__(self):
        content = ""
        for item in list(self.data.items()):
            if item[1]:
                content += eq(item[0], br(item[1], 1)) + "\n"
        return eq(self.name, br(content))


