from typing import Tuple

import pygame

from engine.colors import BLACK
from engine.ui.text.dynamic_font import DynamicFont
from engine.ui.text.text import Text

DEFAULT_FONT_NAME = 'Comic Sans MS'

DEFAULT_TEXT = "<place holder>"

DEFAULT_COLOR = BLACK

DEFAULT_SIZE = 30


class TextBuilder:
    def __init__(self, rect: pygame.Rect):
        self._rect = rect
        self._text = DEFAULT_TEXT
        self._color = DEFAULT_COLOR
        self._size = DEFAULT_SIZE
        self._font_name = DEFAULT_FONT_NAME

    def set_text(self, text: str) -> 'TextBuilder':
        self._text = text
        return self

    def set_color(self, color: Tuple) -> 'TextBuilder':
        self._color = color
        return self

    def set_size(self, size: float) -> 'TextBuilder':
        self._size = size
        return self

    def set_font_name(self, font: str) -> 'TextBuilder':
        self._font_name = font
        return self

    def create_text(self) -> Text:
        return Text(
            text=self._text,
            rect=self._rect,
            font=DynamicFont(
                font_name=self._font_name,
                size=self._size
            ),
            color=self._color
        )
