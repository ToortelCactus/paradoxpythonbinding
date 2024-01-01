from helpers import eq, br, list_to_text


class Option:
    def __init__(self, effects: list = [], trigger: str = None, is_default: bool = False, is_highlighted: bool = False):
        self.name = ""
        self.highlight = is_highlighted
        self.default = is_default
        self.effects = effects
        self.trigger = self.conditional(trigger)
        self.addendum = ""

    def conditional(self, conditional):
        if conditional:
            return eq("trigger", br(conditional, 2)) + "\n"
        return None

    def add_text(self, text: str):
        """ When no other function can do the job, use this and write it in text (!danger! no validation) """
        self.addendum = text
        return self

    def __str__(self):
        content = eq("name", self.name) + "\n"
        if self.highlight:
            content += eq("highlighted_option", "yes") + "\n"
        if self.default:
            content += eq("default_option", "yes") + "\n"

        if self.trigger:
            content += eq("trigger", br(self.trigger, 2)) + "\n"

        # effect items
        content += list_to_text(self.effects)

        content += self.addendum
        return content

