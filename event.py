from helpers import eq, br
from enum import Enum
import effects as ef

defs = ["type", "placement", "title", "desc", "flavor", "icon", "duration",
        "immediate", "trigger", "event_image", "on_created_soundeffect",
        "on_opened_soundeffect"]


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
    def __init__(self, name):
        # register this somewhere or something
        self.name = name
        self.data = empty_data()
        self.description(self.name)

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

    def icon(self, path):
        self.data["icon"] = '"' + path + '"'
        return self

    def duration(self, num: int):
        self.data["duration"] = str(num)
        return self

    def event_image(self, path):
        content = '"' + path + '"'
        if path[-1] == "2":
            content = eq("video", br(content))
        else:
            content = eq("texture", br(content))

        self.data["event_image"] = content
        return self

    def on_created_soundeffect(self, path):
        self.data["event_image"] = '"' + path + '"'
        return self

    def on_opened_soundeffect(self, path):
        self.data["event_image"] = '"' + path + '"'
        return self

    def options(self, options: list):
        # TODO
        return self

    def __str__(self):
        content = ""
        for item in list(self.data.items()):
            content += eq(item[0], br(item[1])) + "\n"
        return eq(self.name, br(content))

