import pygame.font


class DynamicFont:
    def __init__(self, font_name: str, size: int):
        self._font_name = font_name
        self._size = size

        self._font = pygame.font.SysFont(self._font_name, self._size)

    def get_font_name(self) -> str:
        return self._font_name

    def get_size(self) -> int:
        return self._size

    def get_font(self) -> pygame.Font:
        return self._font

    def set_font_name(self, font_name: str) -> None:
        self._font = pygame.font.SysFont(font_name, self._size)

    def set_size(self, size: int) -> None:
        self._font = pygame.font.SysFont(self._font_name, size)

