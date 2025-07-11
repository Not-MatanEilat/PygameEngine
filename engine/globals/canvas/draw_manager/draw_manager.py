import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.transform_component.transform import Transform
from engine.globals.canvas.draw_manager.drawables.image import Image
from engine.globals.canvas.draw_manager.drawables.text import Text


class DrawManager:
    def __init__(self, canvas_surface: Surface):
        self._canvas_surface = canvas_surface

    def fill(self, color: Color) -> None:
        self._canvas_surface.fill(color)

    def draw_image(self, image: Image, transform: Transform) -> None:
        self._canvas_surface.blit(
            source=image.pygame_image,
            dest=(transform.position.x, transform.position.y))

    def draw_text(self, text: Text, transform: Transform):
        self._canvas_surface.blit(
            source=text.get_text_surface(),
            dest=(transform.position.x, transform.position.y)
        )

    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(transform.position.x, transform.position.y, transform.scale.x, transform.scale.y))

    def draw_rectangle_border(self, transform: Transform, color: Color, border_thickness) -> None:
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(transform.position.x, transform.position.y, transform.scale.x, transform.scale.y),
                         width=border_thickness)

