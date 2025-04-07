from abc import ABC, abstractmethod
from typing import List

import pygame.event
from pygame import Surface

from engine.sprite.position import Position


class Sprite(ABC):

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        raise NotImplementedError()

    @abstractmethod
    def on_tick(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_position(self) -> Position:
        raise NotImplementedError()
