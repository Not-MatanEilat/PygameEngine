import pygame.draw
from pygame import Surface, Color

from engine.component.image_renderer_component.image import Image
from engine.component.transform_component.position import Position
from engine.component.transform_component.transform import Transform
from engine.globals.canvas.canvas_wrapper.base_canvas_wrapper import BaseCanvasWrapper


class PygameCanvasWrapper(BaseCanvasWrapper):
    def __init__(self, canvas_surface: Surface):
        self._canvas_surface = canvas_surface

    def fill(self, color: Color) -> None:
        self._canvas_surface.fill(color)

    def draw_image(self, image: Image, transform: Transform) -> None:
        self._canvas_surface.blit(image.image_surface, (transform.position.x, transform.position.y))

    def draw_rectangle(self, transform: Transform, color: Color) -> None:
        pygame.draw.rect(self._canvas_surface,
                         color,
                    (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y))
