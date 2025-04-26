from dataclasses import dataclass

from engine.component.transform_component.position import Position
from events.mouse_events.click_properties import ClickProperties


@dataclass
class MouseEvents:
    left_click: ClickProperties
    right_click: ClickProperties
    middle_click: ClickProperties
    position: Position
