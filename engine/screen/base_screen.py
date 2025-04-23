from abc import ABC, abstractmethod
from math import trunc
from typing import List

import pygame.event

from engine.game_object.game_object import GameObject
from engine.logger.logger import EngineLogger


class BaseScreen(ABC):
    def __init__(self):
        self._game_objects: List[GameObject] = []

    def add_game_object(self, game_object: GameObject) -> None:
        self._game_objects.append(game_object)

    def get_game_objects(self) -> List[GameObject]:
        return self._game_objects

    def tick_game_objects(self) -> None:
        for game_object in self._game_objects:
            game_object.tick_components()

    def event_tick_game_objects(self, events: List[pygame.event.Event]) -> None:
        for game_object in self._game_objects:
            game_object.event_tick_components(events)


    @abstractmethod
    def run(self) -> None:
        ...

    @abstractmethod
    def finish(self) -> None:
        ...

def check_quit(events: List[pygame.event.Event]) -> bool:
    return any(event.type == pygame.QUIT for event in events)

def start_screen(current_screen: BaseScreen, screen_to_start: BaseScreen, finish_current=False):
    if finish_current:
        current_screen.finish()

    screen_to_start.run()

def init_screen(screen: BaseScreen) -> None:
    EngineLogger.info("Initiating current screen")
    for game_object in screen.get_game_objects():
        game_object.init()
