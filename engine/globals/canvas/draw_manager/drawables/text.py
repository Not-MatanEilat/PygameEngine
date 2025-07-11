import pygame
from pygame import Surface

from engine.colors import Color
from engine.component.ui_components.text_component.dynamic_font import DynamicFont


class Text:
    def __init__(self, string: str, font: DynamicFont, color: Color, anti_alias: bool, text_surface: Surface):
        self._string = string
        self._font = font
        self._color = color
        self._anti_alias = anti_alias
        self._text_surface = text_surface

    def set_string(self, string: str) -> None:
        self._string = string
        self.re_render_font(pygame_font=self._font.get_font(),
                            string=string,
                            anti_alias=self._anti_alias,
                            color=self._color)

    def get_string(self) -> str:
        return self._string
    
    def set_font(self, pygame_font: pygame.Font, size: int) -> None:
        self._font.set_font(pygame_font, size)
        self.re_render_font(pygame_font=pygame_font,
                            string=self._string,
                            anti_alias=self._anti_alias,
                            color=self._color)

    def set_font_by_name(self, font_name: str) -> None:
        self._font.set_font_by_name(font_name)
        self.re_render_font(pygame_font=self._font.get_font(),
                            string=self._string,
                            anti_alias=self._anti_alias,
                            color=self._color)

    def set_size(self, size: int) -> None:
        self._font.set_size(size)
        self.re_render_font(pygame_font=self._font.get_font(),
                            string=self._string,
                            anti_alias=self._anti_alias,
                            color=self._color)

    def set_color(self, color: Color) -> None:
        self._color = color
        self.re_render_font(pygame_font=self._font.get_font(),
                            string=self._string,
                            anti_alias=self._anti_alias,
                            color=color)
        
    
    def re_render_font(self, pygame_font: pygame.Font, string: str, anti_alias: bool, color: Color) -> None:
        self._text_surface = pygame_font.render(text=string,
                                                antialias=anti_alias,
                                                color=color)

    def get_text_surface(self) -> Surface:
        return self._text_surface

    def get_size(self) -> int:
        return self._font.get_size()

    def get_color(self) -> Color:
        return self._color

    def get_font_name(self) -> str:
        return self._font.get_font_name()

    def get_font(self) -> DynamicFont:
        return self._font
