from typing import List

import pygame.event
from pygame import Surface

from engine.colors import Color
from engine.sprite.position import Position
from engine.sprite.sprite import Sprite
from engine.ui.shapes.triangle import Triangle, to_triangle_points, get_middle
from engine.ui.view import View


class TriangleSurface(View, Sprite):
    def __init__(self, triangle: Triangle, color: Color):
        self._triangle = triangle
        self._color = color

    def draw(self, screen: Surface) -> None:
        pygame.draw.polygon(screen, self._color, to_triangle_points(self._triangle))

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        pass

    def get_position(self) -> Position:
        return get_middle(self._triangle)