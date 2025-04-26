from typing import Dict, Callable, List

from collections import defaultdict

from engine.colors import Color
from engine.component.image_renderer_component.image import Image
from engine.component.transform_component.transform import Transform
from engine.globals.canvas.canvas_wrapper.base_canvas_wrapper import BaseCanvasWrapper


class CanvasManager:
    def __init__(self, canvas_wrapper: BaseCanvasWrapper, default_background_color: Color):
        self._canvas_wrapper = canvas_wrapper
        self._default_background_color = default_background_color
        self._draw_calls: Dict[int, List[Callable]] = defaultdict(list)

    def draw_image(self, image: Image, transform: Transform, layer=0) -> None:
        self._draw_calls[layer].append(
            lambda: self._canvas_wrapper.draw_image(image, transform))

    def draw_rectangle(self, transform: Transform, color: Color, layer=0) -> None:
        self._draw_calls[layer].append(
            lambda: self._canvas_wrapper.draw_rectangle(transform, color))

    def on_tick(self) -> None:
        self._canvas_wrapper.fill(self._default_background_color)

        for layer in sorted(self._draw_calls.keys()):
            for draw_call in self._draw_calls[layer]:
                draw_call()

        self._draw_calls.clear()

