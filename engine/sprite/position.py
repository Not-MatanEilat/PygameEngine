from dataclasses import dataclass

import pygame


@dataclass
class Position:
    x: float
    y: float


def to_position(rect: pygame.Rect):
    return Position(rect.x, rect.y)
