from typing import Tuple

import pygame


class Window:
    def __init__(self, screen: pygame.Surface, caption: str, background_color: Tuple):
        self.screen = screen
        self.caption = caption
        self.background_color = background_color

    def init(self) -> None:
        self.screen.fill(self.background_color)

        pygame.display.set_caption(self.caption)
