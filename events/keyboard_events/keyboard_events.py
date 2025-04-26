from typing import Dict

from events.keyboard_events.key import Key
from events.keyboard_events.key_properties import KeyProperties


class KeyboardEvents:
    def __init__(self, keys_properties: Dict[Key, KeyProperties]):
        self._keys_properties = keys_properties

    def is_pressed(self, key: Key) -> bool:
        return self._keys_properties[key].is_pressed

    def is_hold(self, key: Key) -> bool:
        return self._keys_properties[key].is_hold

    def is_down(self, key: Key) -> bool:
        return self._keys_properties[key].is_down

    def is_released(self, key: Key) -> bool:
        return self._keys_properties[key].is_released

    def get_key(self, key: Key) -> KeyProperties:
        return self._keys_properties[key]
