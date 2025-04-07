from typing import List, Optional

import pygame.event
from pygame import Surface

from engine.sprite.position import Position, to_position
from engine.sprite.sprite import Sprite
from engine.ui.on_click_listener import OnClickListener, OnClickCallable, observe
from engine.ui.view import View


class Image(View, Sprite, OnClickListener):
    def __init__(self, rect: pygame.Rect, image: pygame.Surface):
        self._rect = rect
        self._image = image

        self._on_click: Optional[OnClickCallable] = None

    def draw(self, screen: Surface) -> None:
        screen.blit(self._image, self._rect)

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        if self._on_click:
            observe(self._on_click, self._rect, events)

    def get_position(self) -> Position:
        return to_position(self._rect)

    def set_on_click_listener(self, on_click_callable: OnClickCallable) -> None:
        self._on_click = on_click_callable
