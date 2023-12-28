from event import Event, EventType, Option
from scriptbase import ScriptFile
import effects as ef
import conditional as c

# example event file named "csr_events" with 2 events:


ScriptFile("csr_events", "europe")

Event(name="exampl",
      event_type=EventType.country_event,
      effects=[],
      trigger=[],
      icon_path="gfx/interface/icons/event_icons/event_protest.dds",
      duration=3,
      event_img_path="southamerica_aristocrats.vk2",
      created_sfx_path="event:/SFX/UI/Alerts/event_appear",
      options=[
            Option(
                  [ef.change_infamy("-150")],
                  is_highlighted=True
            ),
            Option(
                  [ef.change_tag("BRZ")]  # You are going to Brazil
            )
      ]

      )

Event(name="exampl2",
      event_type=EventType.country_event,
      effects=[],
      trigger=[
            c.exists("c:BRZ"),
            c.year_since("1900"),
            c.Not("this = c:BRZ")
      ],
      icon_path="gfx/interface/icons/event_icons/event_protest.dds",
      duration=3,
      event_img_path="southamerica_aristocrats.vk2",
      created_sfx_path="event:/SFX/UI/Alerts/event_appear",
      opened_sfx_path="event:/SFX/Events/unspecific/leader_speaking_to_a_group_of_people",
      options=[
            Option(
                  [ef.change_tag("BRZ")],  # You are going to Brazil
                  is_highlighted=True
            ),
            Option(
                  [ef.change_tag("BRZ")]  # You are going to Brazil
            ),
            Option(
                  [ef.change_tag("BRZ")]  # You are going to Brazil
            ),
            Option(
                  [ef.change_tag("BRZ")]  # You are going to Brazil
            )
      ]

      )
