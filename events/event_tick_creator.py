from typing import List, Dict

import pygame.event
from pygame.key import ScancodeWrapper

from engine.component.transform_component.position import Position
from events.event_tick import EventTick
from events.keyboard_events.key import Key
from events.keyboard_events.key_properties import KeyProperties
from events.keyboard_events.keyboard_events import KeyboardEvents
from events.mouse_events.click_properties import ClickProperties
from events.mouse_events.mouse_events import MouseEvents


class EventTickCreator:

    @staticmethod
    def create_event_tick(events: List[pygame.event.Event], last_event_tick: EventTick) -> EventTick:
        return EventTick(
            mouse_events=create_mouse_events(last_event_tick),
            keyboard_events=create_keyboard_events(last_event_tick),
            is_quit=check_quit(events)
        )

    @staticmethod
    def create_empty_event_tick() -> EventTick:
        """
        In order to calculate an event tick, we need the last tick, but in order to do that
        we need any event tick to start off with
        so this function returns an event tick with values as if nothing happened in that tick
        """
        return EventTick(
            mouse_events=MouseEvents(
                left_click=ClickProperties(
                    is_clicked=False,
                    is_hold=False,
                    is_down=False,
                    is_released=False
                ),
                right_click=ClickProperties(
                    is_clicked=False,
                    is_hold=False,
                    is_down=False,
                    is_released=False
                ),
                middle_click=ClickProperties(
                    is_clicked=False,
                    is_hold=False,
                    is_down=False,
                    is_released=False
                ),
                position=Position(
                    x=0,
                    y=0
                )
            ),
            keyboard_events=KeyboardEvents(
                keys_properties={Key(keycode): KeyProperties(
                    is_pressed=False,
                    is_hold=False,
                    is_down=False,
                    is_released=False
                ) for keycode in Key}
            ),
            is_quit=False
        )


def create_keyboard_events(last_event_tick: EventTick) -> KeyboardEvents:
    keys_pressed = pygame.key.get_just_pressed()
    keys_pressed_wrapper_dict: Dict[Key, KeyProperties] = {}
    for keycode in Key:
        current_key_properties = last_event_tick.keyboard_events.get_key(Key(keycode))

        is_key_currently_pressed = keys_pressed[keycode.value]

        keys_pressed_wrapper_dict[Key(keycode)] = KeyProperties(
            is_pressed=is_pressed(is_key_currently_pressed, current_key_properties),
            is_hold=is_key_hold(is_key_currently_pressed, current_key_properties),
            is_down=is_key_hold(is_key_currently_pressed, current_key_properties) or is_pressed(is_key_currently_pressed, current_key_properties),
            is_released=is_key_released(is_key_currently_pressed, current_key_properties)
        )

    return KeyboardEvents(
        keys_properties=keys_pressed_wrapper_dict
    )

def create_mouse_events(last_event_tick: EventTick) -> MouseEvents:
    left_click, middle_click, right_click = pygame.mouse.get_pressed()
    return MouseEvents(
        left_click=create_click_properties(left_click, last_event_tick.mouse_events.left_click),
        right_click=create_click_properties(right_click, last_event_tick.mouse_events.right_click),
        middle_click=create_click_properties(middle_click, last_event_tick.mouse_events.middle_click),
        position=get_mouse_position()
    )

def get_mouse_position() -> Position:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return Position(mouse_x, mouse_y)


def create_click_properties(is_click_down: bool, last_tick_click_properties: ClickProperties) -> ClickProperties:
    return ClickProperties(
        is_clicked=is_clicked(is_click_down, last_tick_click_properties),
        is_hold=is_click_hold(is_click_down, last_tick_click_properties),
        is_down=is_click_hold(is_click_down, last_tick_click_properties) or is_clicked(is_click_down, last_tick_click_properties),
        is_released=is_click_released(is_click_down, last_tick_click_properties)
    )

def is_clicked(is_currently_down: bool, last_tick_click_properties: ClickProperties) -> bool:
    return not last_tick_click_properties.is_down and is_currently_down

def is_click_hold(is_currently_down: bool, last_tick_click_properties: ClickProperties) -> bool:
    return is_currently_down and last_tick_click_properties.is_down

def is_click_released(is_currently_down: bool, last_tick_click_properties: ClickProperties) -> bool:
    return not is_currently_down and last_tick_click_properties.is_down

def is_pressed(is_currently_down: bool, last_tick_key_properties: KeyProperties) -> bool:
    return last_tick_key_properties.is_down and is_currently_down

def is_key_hold(is_currently_down: bool, last_tick_key_properties: KeyProperties) -> bool:
    return is_currently_down and last_tick_key_properties.is_down

def is_key_released(is_currently_down: bool, last_tick_key_properties: KeyProperties) -> bool:
    return not is_currently_down and last_tick_key_properties.is_down

def check_quit(events: List[pygame.event.Event]) -> bool:
    return any(event.type == pygame.QUIT for event in events)

def is_event_active(events: List[pygame.event.Event], event_to_check: int) -> bool:
    for event in events:
        if event.type == event_to_check:
            return True

    return False
