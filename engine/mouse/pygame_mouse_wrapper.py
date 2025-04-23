import pygame.mouse

from engine.component.transform_component.position import Position
from engine.mouse.mouse_wrapper import BaseMouseWrapper


class PygameMouseWrapper(BaseMouseWrapper):
    def get_mouse_position(self) -> Position:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return Position(mouse_x, mouse_y)