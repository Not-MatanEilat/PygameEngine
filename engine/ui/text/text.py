from typing import Tuple, Callable, Optional, List

import pygame.font
from pygame import Surface, Rect

from engine.sprite.position import Position, to_position
from engine.sprite.sprite import Sprite
from engine.ui.on_click_listener import OnClickListener, observe
from engine.ui.text.dynamic_font import DynamicFont
from engine.ui.view import View


class Text(View, Sprite, OnClickListener):
    def __init__(self, text: str, rect: Rect, font: DynamicFont, color: Tuple, anti_alias: bool):
        self._text = text
        self._rect = rect

        self._font = font
        self._color = color
        self._anti_alias = anti_alias

        self._text_surface = font.get_font().render(text=text, antialias=anti_alias, color=color)

        self._on_click: Optional[Callable[[None], None]] = None

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        if self._on_click:
            observe(self._on_click, self._rect, events)

    def draw(self, screen: Surface) -> None:
        screen.blit(self._text_surface, self._rect)

    def get_position(self) -> Position:
        return to_position(self._rect)

    def set_on_click_listener(self, func: Callable[[], None]) -> None:
        self._on_click = func

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

    def set_color(self, color: Tuple) -> None:
        self._text_surface = self._font.get_font().render(text=self._text, antialias=self._anti_alias, color=color)
        self._color = color

    def get_color(self) -> Tuple:
        return self._color

    def set_size(self, size: int) -> None:
        self._font.set_size(size)

    def set_font_name(self, font_name: str) -> None:
        self._font.set_font_name(font_name)
