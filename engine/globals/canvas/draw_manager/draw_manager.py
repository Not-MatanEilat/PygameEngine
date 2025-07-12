import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.transform_component.position import Position
from engine.component.transform_component.scale import Scale
from engine.component.transform_component.transform import Transform
from engine.globals.canvas.draw_manager.drawables.image import Image
from engine.globals.canvas.draw_manager.drawables.text import Text


class DrawManager:
    def __init__(self, canvas_surface: Surface):
        self._canvas_surface = canvas_surface

    def fill(self, color: Color) -> None:
        self._canvas_surface.fill(color)

    def draw_image(self, image: Image, transform: Transform) -> None:
        new_transform = create_transform_relative_to_canvas_size(transform, self._canvas_surface)
        self._canvas_surface.blit(
            source=image.pygame_image,
            dest=(new_transform.position.x, new_transform.position.y))

    def draw_text(self, text: Text, transform: Transform):
        new_transform = create_transform_relative_to_canvas_size(transform, self._canvas_surface)
        self._canvas_surface.blit(
            source=text.get_text_surface(),
            dest=(new_transform.position.x, new_transform.position.y)
        )

    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        new_transform = create_transform_relative_to_canvas_size(transform, self._canvas_surface)
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(new_transform.position.x, new_transform.position.y, new_transform.scale.x, new_transform.scale.y))

    def draw_rectangle_border(self, transform: Transform, color: Color, border_thickness) -> None:
        new_transform = create_transform_relative_to_canvas_size(transform, self._canvas_surface)
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(new_transform.position.x, new_transform.position.y, new_transform.scale.x, new_transform.scale.y),
                         width=border_thickness)

RELATIVE_CANVAS_MULTIPLIER_SIZE = 0.0005

def create_transform_relative_to_canvas_size(old_transform: Transform, canvas_surface: Surface) -> Transform:
    x_position = RELATIVE_CANVAS_MULTIPLIER_SIZE * old_transform.position.x * canvas_surface.get_width()
    y_position = RELATIVE_CANVAS_MULTIPLIER_SIZE * old_transform.position.y * canvas_surface.get_height()
    x_scale = RELATIVE_CANVAS_MULTIPLIER_SIZE * old_transform.scale.x * canvas_surface.get_width()
    y_scale = RELATIVE_CANVAS_MULTIPLIER_SIZE * old_transform.scale.y * canvas_surface.get_height()
    return Transform(position=Position(x_position, y_position),
                     rotation=old_transform.rotation,
                     scale=Scale(x_scale, y_scale))

