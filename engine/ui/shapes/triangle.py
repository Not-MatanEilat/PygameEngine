from dataclasses import dataclass
from typing import Tuple

from engine.sprite.position import Position


@dataclass
class Triangle:
    x1: float
    y1: float
    x2: float
    y2: float
    x3: float
    y3: float


TrianglePoints = Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]]


def to_triangle_points(triangle: Triangle) -> TrianglePoints:
    return ((triangle.x1, triangle.y1),
            (triangle.x2, triangle.y2),
            (triangle.x3, triangle.y3))


def get_middle(triangle: Triangle) -> Position:
    return Position(
        (triangle.x1 + triangle.x2 + triangle.x3) / 3,
        (triangle.y1 + triangle.y2 + triangle.y3) / 3,
    )
