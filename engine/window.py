from typing import Tuple

import pygame

from engine.colors import Color
from engine.logger.logger import EngineLogger
from engine.screen.base_screen import BaseScreen


class Window:
    def __init__(self, start_screen: BaseScreen, display: pygame.Surface, caption: str):
        self.starting_screen = start_screen
        self.display_screen = display
        self.caption = caption

    def init(self) -> None:
        pygame.display.set_caption(self.caption)

    def run(self) -> None:
        self.starting_screen.run()
        EngineLogger.info("Quitting window...")