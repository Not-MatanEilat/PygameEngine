from typing import Dict, Callable, List

from collections import defaultdict

from pygame import Surface

from engine.colors import Color
from engine.component.transform_component.transform import Transform
from engine.globals.canvas.draw_manager import DrawManager


class CanvasManager:
    def __init__(self, draw_manager: DrawManager, default_background_color: Color):
        self._draw_manager = draw_manager
        self._default_background_color = default_background_color
        self._draw_calls: Dict[int, List[Callable]] = defaultdict(list)

    def draw_surface(self, surface: Surface, transform: Transform, layer=0) -> None:
        self._draw_calls[layer].append(
            lambda: self._draw_manager.draw_surface(surface, transform))

    def draw_rectangle(self, transform: Transform, color: Color, layer=0) -> None:
        self._draw_calls[layer].append(
            lambda: self._draw_manager.draw_rectangle(transform, color))

    def draw_rectangle_border(self, transform: Transform, color: Color, border_thickness: int, layer=0) -> None:
        self._draw_calls[layer].append(
            lambda: self._draw_manager.draw_rectangle_border(transform, color, border_thickness))

    def on_tick(self) -> None:
        self._draw_manager.fill(self._default_background_color)

        for layer in sorted(self._draw_calls.keys(), reverse=True):
            for draw_call in self._draw_calls[layer]:
                draw_call()

        self._draw_calls.clear()

