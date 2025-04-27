from pathlib import Path

import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.base_component import BaseComponent
from engine.component.transform_component.transform_component import TransformComponent
from engine.component.ui_components.text_component.dynamic_font import DynamicFont
from engine.component.ui_components.text_component.text import Text
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager


class TextComponent(BaseComponent):
    def __init__(self, text: Text):
        super().__init__()
        self._text = text

        self.transform_component: TransformComponent = None

    def on_tick(self, event_tick: EventTick) -> None:
        GlobalManager.get_instance().get_canvas_manager().draw_surface(self._text.get_text_surface(), self.transform_component.transform)

    def start(self) -> None:
        self.transform_component = self.get_component(TransformComponent)

    def set_text(self, text: str) -> None:
        self._text.set_string(text)

    def get_text(self) -> str:
        return self._text.get_string()

    def set_font(self, font: pygame.Font, size: int) -> None:
        self._text.set_font(font, size)

    def get_font(self) -> DynamicFont:
        return self._text.get_font()

    def set_color(self, color: Color) -> None:
        self._text.set_color(color)

    def get_color(self) -> Color:
        return self._text.get_color()

    def set_size(self, size: int) -> None:
        self._text.set_size(size)

    def set_font_by_name(self, font_name: str) -> None:
        self._text.set_font_by_name(font_name)
