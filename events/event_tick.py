from events.keyboard_events.keyboard_events import KeyboardEvents
from events.mouse_events.mouse_events import MouseEvents

from dataclasses import dataclass


@dataclass
class EventTick:
    mouse_events: MouseEvents
    keyboard_events: KeyboardEvents
    is_quit: bool
