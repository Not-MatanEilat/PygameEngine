from abc import ABC, abstractmethod
from typing import Callable, List, Optional

import pygame

from engine.component.transform_component.position import Position
from engine.component.transform_component.transform_component import TransformComponent
from engine.mouse.mouse_manager import MouseManager

OnClickCallable = Callable[[], None]


class OnClickListener(ABC):

    @abstractmethod
    def set_on_click_listener(self, on_click_callable: OnClickCallable) -> None:
        ...


def is_clicked(events: List[pygame.event.Event]) -> bool:
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            return True

    return False


def observe(on_click: OnClickCallable, observed_transform: TransformComponent, events: List[pygame.event.Event]) -> None:
    if not is_clicked(events):
        return

    mouse_position = MouseManager.get_mouse_position()

    if observed_transform.collide_point(Position(mouse_position.x, mouse_position.y)):
        on_click()
