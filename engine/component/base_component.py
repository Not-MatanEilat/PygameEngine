from __future__ import annotations

from abc import ABC, abstractmethod

from typing import Type

from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject


class BaseComponent(ABC):
    def __init__(self):
        self._game_object: GameObject = None

    def get_component(self, component_type: Type[BaseComponent]) -> BaseComponent:
        return self._game_object.get_component(component_type)

    def set_game_object(self, entity: GameObject) -> None:
        self._game_object = entity

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def on_tick(self, event_tick: EventTick) -> None:
        ...
