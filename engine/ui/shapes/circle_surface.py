from typing import List

import pygame.event
from pygame import Surface

from engine.colors import Color
from engine.sprite.position import Position
from engine.sprite.sprite import Sprite
from engine.ui.shapes.circle import Circle
from engine.ui.view import View


class CircleSurface(View, Sprite):
    def __init__(self, circle: Circle, color: Color):
        self._circle = circle
        self._color = color

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, self._color, (self._circle.center_x, self._circle.center_y), self._circle.radius)

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        pass

    def get_position(self) -> Position:
        return Position(self._circle.center_x, self._circle.center_y)