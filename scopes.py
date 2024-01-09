from enum import Enum
from helpers import eq, br

from effect.country import CountryEffect
from effect.culture import CultureEffect
from effect.state import StateEffect
from effect.region import RegionEffect
from effect.pop import PopEffect
from effect.ig import IGEffect
from effect.party import PartyEffect
from effect.dip_play import DipPlayEffect
from parsing.generated.country import Country
from parsing.generated.interest_group import Interest_group
from parsing.generated.religion import Religion
from parsing.generated.building import Building
from parsing.generated.culture import Culture
from parsing.generated.party import Party
from parsing.generated.state_region import State_region
from parsing.generated.market_goods import Market_goods


class Scope:
    """ Currently unfinished in terms of verification and exhaustiveness """

    def __init__(self, key, item, *effects):
        self.prev = "root"
        if isinstance(key, Enum):
            self.id = key.name
        else:
            self.id = key
        self.item = item
        self.content = ""
        for effect in effects:
            self.content += str(effect) + "\n"

    def __str__(self):
        return eq(self.id + ":" + self.item, br(self.content))

    def type(self):
        return "undef"


class EffectScope(Scope):
    def type(self):
        return "effect_all"


class TriggerScope(Scope):
    def type(self):
        return "trigger_all"


# Effect scopes


class CountrySE(EffectScope):
    def __init__(self, country_tag: Country, *effects: CountryEffect):
        super().__init__("c", country_tag, effects)

    def type(self):
        return "country"


class MarketGoodSE(EffectScope):
    def __init__(self, good: Market_goods, *effects):
        super().__init__("mg", good, effects)

    def type(self):
        return "market_goods"


class StateSE(EffectScope):
    def __init__(self, state_tag, *effects: StateEffect):
        super().__init__("s", state_tag, effects)

    def type(self):
        return "state"


class CultureSE(EffectScope):
    def __init__(self, culture: Culture, *effects: CultureEffect):
        super().__init__("cu", culture, effects)

    def type(self):
        return "culture"


class RegionSE(EffectScope):
    def __init__(self, state_region: State_region, *effects: RegionEffect):
        super().__init__("sr", state_region, effects)

    def type(self):
        return "state_region"


class PopSE(EffectScope):
    def __init__(self, pop, *effects: PopEffect):
        super().__init__("pop", pop, effects)

    def type(self):
        return "pop"


class IGSE(EffectScope):
    def __init__(self, ig: Interest_group, *effects: IGEffect):
        super().__init__("ig", ig, effects)

    def type(self):
        return "interest_group"


class PartySE(EffectScope):
    def __init__(self, party: Party, *effects: PartyEffect):
        super().__init__("py", party, effects)

    def type(self):
        return "party"


class DipPlaySE(EffectScope):
    def __init__(self, party: Party, *effects: DipPlayEffect):
        super().__init__("dp", party, effects)

    def type(self):
        return "diplomatic_play"


# Trigger scopes


global current_scope # TODO: used in future to sanity-check stuff
