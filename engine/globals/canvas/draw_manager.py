import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.transform_component.transform import Transform


class DrawManager:
    def __init__(self, canvas_surface: Surface):
        self._canvas_surface = canvas_surface

    def fill(self, color: Color) -> None:
        self._canvas_surface.fill(color)

    def draw_surface(self, surface: Surface, transform: Transform) -> None:
        self._canvas_surface.blit(surface, (transform.position.x, transform.position.y))

    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        pygame.draw.rect(self._canvas_surface,
                         color,
                    (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y))

    def draw_rectangle_border(self, transform: Transform, color: Color, border_thickness) -> None:
        pygame.draw.rect(self._canvas_surface,
                         color,
                         (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y),
                         border_thickness)
