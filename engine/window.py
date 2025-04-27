from typing import Tuple

import pygame

from engine.colors import Color
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger
from engine.screen.screen import Screen


class Window:
    def __init__(self, caption: str, global_manager: GlobalManager):
        self.caption = caption
        self.global_manager = global_manager

    def init(self) -> None:
        pygame.display.set_caption(self.caption)

    def run(self) -> None:
        self.global_manager.get_instance().get_current_screen().run()
        EngineLogger.info("Quitting window...")