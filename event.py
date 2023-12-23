from helpers import eq, br

defs = ["type", "placement", "title", "desc", "flavor", "icon",
        "immediate", "trigger", "event_image", "on_created_soundeffect",
        "on_opened_soundeffect"]


def empty_data():
    data = {}
    for d in defs:
        data.setdefault(d, None)
    return data


class Event:
    def __init__(self):
        # register this somewhere or something

        self.data = empty_data()
        pass

    def immediate(self, effects: list):
        contents = ""
        for effect in effects:
            contents += "\t" + effect
        return self
