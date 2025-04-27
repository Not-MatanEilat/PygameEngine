
import pygame

from engine.colors import BLACK, Color
from engine.component.ui_components.text_component.dynamic_font import DynamicFont
from engine.component.ui_components.text_component.text import Text
from engine.component.ui_components.text_component.text_component import TextComponent

DEFAULT_ANTI_ALIAS = False

DEFAULT_FONT_NAME = 'Comic Sans MS'

DEFAULT_TEXT = "<place holder>"

DEFAULT_COLOR = BLACK

DEFAULT_SIZE = 30


class TextBuilder:
    def __init__(self):
        self._text = DEFAULT_TEXT
        self._color = DEFAULT_COLOR
        self._size = DEFAULT_SIZE
        self._font_name = DEFAULT_FONT_NAME
        self._anti_alias = DEFAULT_ANTI_ALIAS

    def set_text(self, text: str) -> 'TextBuilder':
        self._text = text
        return self

    def set_color(self, color: Color) -> 'TextBuilder':
        self._color = color
        return self

    def set_size(self, size: float) -> 'TextBuilder':
        self._size = size
        return self

    def set_font_name(self, font: str) -> 'TextBuilder':
        self._font_name = font
        return self

    def set_anti_alias(self, anti_alias: bool) -> 'TextBuilder':
        self._anti_alias = anti_alias
        return self

    def create_text(self) -> Text:
        dynamic_font = DynamicFont(
                font_name=self._font_name,
                size=self._size,
            )

        return Text(
            string=self._text,
            font=dynamic_font,
            text_surface=dynamic_font.get_font().render(
                text=self._text,
                antialias=self._anti_alias,
                color=self._color),
            color=self._color,
            anti_alias=self._anti_alias
        )
