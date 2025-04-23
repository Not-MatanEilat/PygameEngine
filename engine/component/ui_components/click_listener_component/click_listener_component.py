from typing import List, Optional, Callable

import pygame

from engine.component.base_component import BaseComponent
from engine.component.transform_component.transform_component import TransformComponent
from engine.ui.on_click_listener import observe


OnClickCallable = Callable[[], None]

class ClickListenerComponent(BaseComponent):
    def __init__(self, on_click: OnClickCallable):
        super().__init__()

        self._on_click: OnClickCallable = on_click

        self._transform_component: TransformComponent = None


    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self) -> None:
        pass

    def set_on_click_listener(self, on_click_callable: OnClickCallable) -> None:
        self._on_click = on_click_callable

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        observe(self._on_click, self._transform_component, events)
