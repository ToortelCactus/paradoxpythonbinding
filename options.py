from helpers import eq, br, effects_to_script


class Option:
    def __init__(self, effects: list = [], trigger: str = None, is_default: bool = False, is_highlighted: bool = False):
        self.name = ""
        self.highlight = is_highlighted
        self.default = is_default
        self.effects = effects
        self.trigger = self.conditional(trigger)

    def conditional(self, conditional):
        if conditional:
            return eq("trigger", br(conditional, 2)) + "\n"
        return None

    def __str__(self):
        content = eq("name", self.name) + "\n"
        if self.highlight:
            content += eq("highlighted_option", "yes") + "\n"
        if self.default:
            content += eq("default_option", "yes") + "\n"

        if self.trigger:
            content += eq("trigger", br(self.trigger, 2)) + "\n"

        # effect items
        content += effects_to_script(self.effects)

        return content

