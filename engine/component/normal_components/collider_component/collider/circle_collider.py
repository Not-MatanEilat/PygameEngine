from overrides import override
from shapely.geometry.base import BaseGeometry
from shapely.geometry.point import Point

from engine.component.normal_components.collider_component.collider.base_collider import BaseCollider
from engine.component.normal_components.collider_component.collider.collider_type import ColliderType
from engine.component.normal_components.transform_component.position import Position


class CircleCollider(BaseCollider):
    def __init__(self, radius: float):
        self._radius = radius

    @override
    def get_base_geometry(self, position: Position) -> BaseGeometry:
        return Point((position.x, position.y)).buffer(self._radius, resolution=1)