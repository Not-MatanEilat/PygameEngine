from pathlib import Path
from typing import List

import pygame

from engine.colors import Color
from engine.component.base_component import BaseComponent
from engine.component.image_renderer_component.image import Image
from engine.component.transform_component.transform_component import TransformComponent
from engine.component.ui_components.text_component.dynamic_font import DynamicFont
from engine.globals.global_manager import GlobalManager
from events.event_tick import EventTick


class TextComponent(BaseComponent):
    def __init__(self, text: str, font: DynamicFont, color: Color, anti_alias: bool):
        super().__init__()
        self._text = text

        self._font = font
        self._color = color
        self._anti_alias = anti_alias

        self._text_surface = font.get_font().render(text=text, antialias=anti_alias, color=color)

        self.transform_component: TransformComponent = None

    def on_tick(self, event_tick: EventTick) -> None:
        GlobalManager.get_instance().get_canvas_manager().draw_image(Image(path=Path("asdsa"), image_surface=self._text_surface), self.transform_component.transform)

    def start(self) -> None:
        self.transform_component = self.get_component(TransformComponent)

    def set_text(self, text: str) -> None:
        self._text_surface = self._font.get_font().render(text=text, antialias=self._anti_alias, color=self._color)
        self._text = text

    def get_text(self) -> str:
        return self._text

    def set_font(self, font: pygame.Font) -> None:
        self._text_surface = font.render(text=self._text, antialias=self._anti_alias, color=self._color)
        self._font = font

    def get_font(self) -> pygame.Font:
        return self._font.get_font()

    def set_color(self, color: Color) -> None:
        self._text_surface = self._font.get_font().render(text=self._text, antialias=self._anti_alias, color=color)
        self._color = color

    def get_color(self) -> Color:
        return self._color

    def set_size(self, size: int) -> None:
        self._font.set_size(size)

    def set_font_name(self, font_name: str) -> None:
        self._font.set_font_name(font_name)
