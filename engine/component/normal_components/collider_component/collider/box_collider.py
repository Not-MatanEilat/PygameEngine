from overrides import override

from engine.component.normal_components.collider_component.collider.base_collider import BaseCollider
from engine.component.normal_components.collider_component.collider.collider_type import ColliderType


class BoxCollider(BaseCollider):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @override
    def get_collider_type(self) -> ColliderType:
        return ColliderType.BOX

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height