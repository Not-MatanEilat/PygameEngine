from typing import Callable, List, Optional

import pygame.event
from pygame import Surface

from engine.colors import Color
from engine.sprite.position import Position, to_position
from engine.sprite.sprite import Sprite
from engine.ui.on_click_listener import OnClickListener, observe, OnClickCallable
from engine.ui.text.text import Text
from engine.ui.view import View


class Button(View, Sprite, OnClickListener):
    def __init__(self, rect: pygame.Rect, text: Text, background_color: Color):
        self._rect = rect
        self._text = text
        self._background_color = background_color

        self._on_click = Optional[OnClickCallable]

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self._background_color, self._rect)
        self._text.draw(screen)

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        if self._on_click:
            observe(self._on_click, self._rect, events)

    def get_position(self) -> Position:
        return to_position(self._rect)

    def set_on_click_listener(self, on_click_callable: OnClickCallable) -> None:
        self._on_click = on_click_callable
