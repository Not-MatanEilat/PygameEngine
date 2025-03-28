from typing import List, Tuple

import pygame.event
from pygame import Surface, Rect

from engine.sprite.position import Position, to_position
from engine.sprite.sprite import Sprite
from engine.ui.view import View


class RectangleSurface(View, Sprite):
    def __init__(self, rect: Rect, color: Tuple):
        self._rect = rect
        self._color = color

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self._color, self._rect)

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        pass

    def get_position(self) -> Position:
        return to_position(self._rect)
