from typing import List

import pygame

from engine.collision_checker import CollisionChecker
from engine.colors import RED
from engine.component.base_component import BaseComponent
from engine.component.transform_component.position import Position
from engine.component.transform_component.transform import Transform
from engine.events.event_tick import EventTick
from engine.globals.global_manager import GlobalManager


class TransformComponent(BaseComponent):
    def __init__(self, transform: Transform):
        super().__init__()

        self.transform = transform

    def start(self) -> None:
        pass

    def on_tick(self, event_tick: EventTick) -> None:
        if GlobalManager.get_instance().debug_mode:
            GlobalManager.get_instance().get_canvas_manager().draw_rectangle_border(self.transform, RED, 3)

    def on_event_tick(self, events: List[pygame.event.Event]) -> None:
        pass

    def collide_point(self, point: Position) -> bool:
        # there is no reason to check collision as a rotated rectangle if the angle is normalized
        # calculating the collision as a rotated rectangle requires trigonometry which are considered
        # very heavy calculating functions
        if is_normalized_angle(self.transform.rotation.degrees):
            return CollisionChecker.rect_collides_point(transform=self.transform,
                                                        point=point)
        else:
            return CollisionChecker.rotated_rect_collides_point(
                transform=self.transform,
                point=point
            )


def is_normalized_angle(angle: float) -> bool:
    return angle % 360 == 0