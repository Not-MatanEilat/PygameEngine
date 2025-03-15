from abc import ABC, abstractmethod
from typing import Callable, List

import pygame


class OnClickListener(ABC):

    @abstractmethod
    def set_on_click_listener(self, func: Callable[[], None]) -> None:
        raise NotImplementedError()


def is_clicked(events: List[pygame.event.Event]) -> bool:
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            return True

    return False


def observe(on_click: Callable[[], None], observed_rect: pygame.Rect, events: List[pygame.event.Event]) -> None:
    if not is_clicked(events):
        return

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if observed_rect.collidepoint(mouse_x, mouse_y):
        on_click()
