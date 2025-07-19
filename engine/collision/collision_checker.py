import math

from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.transform import Transform


class CollisionChecker:
    @staticmethod
    def rect_collides_point(transform: Transform, point: Position) -> bool:
        return (
                transform.position.x - transform.scale.x <= point.x <= transform.position.x + transform.scale.x and
                transform.position.y - transform.scale.y <= point.y <= transform.position.y + transform.scale.y
        )

    @staticmethod
    def rotated_rect_collides_point(transform: Transform, point: Position) -> bool:
        dx = point.x - transform.position.x
        dy = point.y - transform.position.y

        angle_rad = -math.radians(transform.rotation.degrees)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        local_x = dx * cos_theta - dy * sin_theta
        local_y = dx * sin_theta + dy * cos_theta

        half_width = transform.scale.x / 2
        half_height = transform.scale.y / 2

        return -half_width <= local_x <= half_width and -half_height <= local_y <= half_height
