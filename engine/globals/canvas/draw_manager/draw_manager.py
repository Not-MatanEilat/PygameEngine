import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.normal_components.transform_component.scale import Scale
from engine.component.normal_components.transform_component.transform import Transform
from engine.globals.canvas.canvas_relative_transformer import CanvasRelativeTransformer
from engine.globals.canvas.draw_manager.drawables.image import Image
from engine.globals.canvas.draw_manager.drawables.text import Text


class DrawManager:
    def __init__(self, canvas_surface: Surface):
        self._canvas_surface = canvas_surface
        self._canvas_relative_transformer = CanvasRelativeTransformer(
            canvas_scale=Scale(canvas_surface.get_width(), canvas_surface.get_height()))

    def fill(self, color: Color) -> None:
        self._canvas_surface.fill(color)

    def draw_image(self, image: Image, transform: Transform) -> None:
        new_transform = self._canvas_relative_transformer.create_transform_relative_to_canvas(transform)
        self._canvas_surface.blit(
            source=image.pygame_image,
            dest=(new_transform.position.x, new_transform.position.y))

    def draw_text(self, text: Text, transform: Transform):
        new_transform = self._canvas_relative_transformer.create_transform_relative_to_canvas(transform)
        self._canvas_surface.blit(
            source=text.get_text_surface(),
            dest=(new_transform.position.x, new_transform.position.y)
        )

    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        new_transform = self._canvas_relative_transformer.create_transform_relative_to_canvas(transform)
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(new_transform.position.x, new_transform.position.y, new_transform.scale.x, new_transform.scale.y))

    def draw_rectangle_border(self, transform: Transform, color: Color, border_thickness) -> None:
        new_transform = self._canvas_relative_transformer.create_transform_relative_to_canvas(transform)
        pygame.draw.rect(surface=self._canvas_surface,
                         color=color,
                         rect=(new_transform.position.x, new_transform.position.y, new_transform.scale.x, new_transform.scale.y),
                         width=border_thickness)

    def get_canvas_scale(self) -> Scale:
        return Scale(self._canvas_surface.get_width(), self._canvas_surface.get_height())

    def get_canvas_relative_transformer(self) -> CanvasRelativeTransformer:
        return self._canvas_relative_transformer
