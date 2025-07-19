from abc import ABC, abstractmethod

from shapely.geometry.base import BaseGeometry

from engine.component.normal_components.collider_component.collider.collider_type import ColliderType
from engine.component.normal_components.transform_component.position import Position


class BaseCollider(ABC):
    @abstractmethod
    def get_base_geometry(self, position: Position) -> BaseGeometry:
        ...