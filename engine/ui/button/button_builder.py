import pygame

from engine.colors import RED, Color
from engine.ui.button.button import Button

from engine.ui.text.text_component_builder import TextComponentBuilder

DEFAULT_BACKGROUND_COLOR = RED


class ButtonBuilder:
    def __init__(self, rect: pygame.Rect):
        self._rect = rect
        self._text = TextComponentBuilder(rect).create_text()

        self._background_color = DEFAULT_BACKGROUND_COLOR

    def set_background_color(self, background_color: Color) -> 'ButtonBuilder':
        self._background_color = background_color
        return self

    def create_button(self) -> Button:
        return Button(
            rect=self._rect,
            text=self._text,
            background_color=self._background_color
        )
