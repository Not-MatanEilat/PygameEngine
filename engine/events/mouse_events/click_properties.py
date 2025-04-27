from dataclasses import dataclass

@dataclass
class ClickProperties:
    is_clicked: bool
    is_hold: bool
    is_released: bool
    is_down: bool