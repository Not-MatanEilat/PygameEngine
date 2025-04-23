import math

from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale


class CollisionChecker:
    @staticmethod
    def rect_collides_point(position: Position, scale: Scale, point: Position) -> bool:
        half_width = scale.x / 2
        half_height = scale.y / 2

        return (
                position.x - half_width <= point.x <= position.x + half_width and
                position.y - half_height <= point.y <= position.y + half_height
        )

    @staticmethod
    def rotated_rect_collides_point(position: Position, rotation: Rotation, scale: Scale, point: Position) -> bool:
        dx = point.x - position.x
        dy = point.y - position.y

        angle_rad = -math.radians(rotation.degrees)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        local_x = dx * cos_theta - dy * sin_theta
        local_y = dx * sin_theta + dy * cos_theta

        half_width = scale.x / 2
        half_height = scale.y / 2

        return -half_width <= local_x <= half_width and -half_height <= local_y <= half_height