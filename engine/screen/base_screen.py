from abc import ABC, abstractmethod
from math import trunc
from typing import List

import pygame.event


class BaseScreen(ABC):

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
