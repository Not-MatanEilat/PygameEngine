from typing import List, Optional, Callable

import pygame

from engine.component.base_component import BaseComponent
from engine.component.transform_component.transform_component import TransformComponent
from engine.ui.on_click_listener import observe
from events.event_tick import EventTick

OnClickCallable = Callable[[], None]

class ClickListenerComponent(BaseComponent):
    def __init__(self, on_click: OnClickCallable):
        super().__init__()

        self._on_click: OnClickCallable = on_click

        self._transform_component: TransformComponent = None


    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self, event_tick: EventTick) -> None:
        if event_tick.mouse_events.left_click.is_clicked:
            if self._transform_component.collide_point(event_tick.mouse_events.position):
                self._on_click()

    def set_on_click_listener(self, on_click_callable: OnClickCallable) -> None:
        self._on_click = on_click_callable
