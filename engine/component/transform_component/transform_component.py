from typing import List

import pygame

from engine.collision_checker import CollisionChecker
from engine.component.base_component import BaseComponent
from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale


class TransformComponent(BaseComponent):
    def __init__(self, position: Position, rotation: Rotation, scale: Scale):
        super().__init__()

        self._position = position
        self._rotation = rotation
        self._scale = scale

    def start(self) -> None:
        pass

    def on_tick(self) -> None:
        pass

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        pass

    def collide_point(self, point: Position) -> bool:
        # there is no reason to check collision as a rotated rectangle if the angle is normalized
        # calculating the collision as a rotated rectangle requires trigonometry which are considered
        # very heavy calculating functions
        if is_normalized_angle(self._rotation.degrees):
            return CollisionChecker.rect_collides_point(position=self._position,
                                                        scale=self._scale,
                                                        point=point)
        else:
            return CollisionChecker.rotated_rect_collides_point(
                position=self._position,
                rotation=self._rotation,
                scale=self._scale,
                point=point
            )


def is_normalized_angle(angle: float) -> bool:
    return angle % 360 == 0