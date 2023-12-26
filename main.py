from event import *
from scriptbase import ScriptFile

ScriptFile("csr_events")

Event(name="prevrat",
      event_type=EventType.country_event,
      effects=[],
      trigger=None,
      icon_path="gfx/interface/icons/event_icons/event_protest.dds",
      duration=3,
      event_img_path="southamerica_aristocrats.vk2",
      created_sfx_path="event:/SFX/UI/Alerts/event_appear",
      options=[])