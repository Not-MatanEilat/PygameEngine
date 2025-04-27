from dataclasses import dataclass

@dataclass
class KeyProperties:
    is_pressed: bool
    is_hold: bool
    is_down: bool
    is_released: bool