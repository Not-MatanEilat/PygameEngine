from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.rotation import Rotation
from engine.component.normal_components.transform_component.scale import Scale
from engine.component.normal_components.transform_component.transform import Transform
from engine.component.normal_components.transform_component.transform_component import TransformComponent


class TransformBuilder:
    def __init__(self):
        self._position = Position()
        self._rotation = Rotation()
        self._scale = Scale()

    def set_position(self, x: float, y: float) -> 'TransformBuilder':
        self._position = Position(x, y)
        return self

    def set_rotation(self, degrees: float) -> 'TransformBuilder':
        self._rotation = Rotation(degrees)
        return self

    def set_scale(self, x: float, y: float) -> 'TransformBuilder':
        self._scale = Scale(x, y)
        return self

    def create_component(self) -> Transform:
        return Transform(
            position=self._position,
            rotation=self._rotation,
            scale=self._scale)
