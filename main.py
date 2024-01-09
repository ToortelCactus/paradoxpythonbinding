from event import CountryEvent, Option
from character import Character
from modifier import Modifier as Mod
from scriptbase import EventFile, HistoryFile, ModifierFile
from effect.effects import E
from effect.country import CE
import triggers as c
from parsing.generated.modifier_type import Modifier_type as mf
from parsing.generated.modifier import Modifier

# example event file named "csr_events" with 2 events:

EventFile("csr_events", "europe")

CountryEvent(name="exampl",
             immediate=[CE.add_treasury("50.0")],
             trigger=[],
             icon_path="gfx/interface/icons/event_icons/event_protest.dds",
             duration=3,
             event_img_path="southamerica_aristocrats.vk2",
             created_sfx_path="event:/SFX/UI/Alerts/event_appear",
             options=[
                 Option(
                     [CE.change_infamy("-150")],
                     is_highlighted=True
                 ),
                 Option(
                     [CE.change_tag("BRZ")]  # You are going to Brazil
                 )
             ]

             )

CountryEvent(name="exampl2",
             immediate=[],
             trigger=[
                 c.exists("c:BRZ"),
                 c.year_after("1900"),
                 c.Not(["this = c:BRZ"])
             ],
             icon_path="gfx/interface/icons/event_icons/event_protest.dds",
             duration=3,
             event_img_path="southamerica_aristocrats.vk2",
             created_sfx_path="event:/SFX/UI/Alerts/event_appear",
             opened_sfx_path="event:/SFX/Events/unspecific/leader_speaking_to_a_group_of_people",
             options=[
                 Option(
                     [CE.change_tag("BRZ")],  # *You are going to Brazil*
                     is_highlighted=True
                 ),
                 Option(
                     [CE.change_tag("BRZ"),
                      CE.call_election(6)]  # You are going to Brazil and have an election
                 ),
                 Option(
                     [CE.change_tag("BRZ")]  # You are going to Brazil
                 ),
                 Option(
                     [CE.change_tag("BRZ"), E.add_modifier(Modifier.declared_bankruptcy, 6)]  # You are going to Brazil
                 )
             ]

             )

# example of history characters in common/history
HistoryFile(HistoryFile.Category.characters, "cng - congo")

Character(
    first_name="Ogutu",
    last_name="M'beke",
    historical=True,
    traits=["career_media_personality",
            "humorous"]  # add ADHD trait when it releases
)

# Modifiers example
ModifierFile("notmodifiers")

protest_icon = "gfx/interface/icons/event_icons/event_protest.dds"

Mod(
    "shrimple_country_modifier",
    protest_icon,
    [
        (mf.interest_group_ig_urbanists_approval_add, "1"),
        (mf.interest_group_ig_bureaucrats_approval_add, "2.5")
    ]
)