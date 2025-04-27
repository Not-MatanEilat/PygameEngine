from engine.events.keyboard_events.keyboard_events import KeyboardEvents
from engine.events.mouse_events.mouse_events import MouseEvents

from dataclasses import dataclass


@dataclass
class EventTick:
    mouse_events: MouseEvents
    keyboard_events: KeyboardEvents
    is_quit: bool
