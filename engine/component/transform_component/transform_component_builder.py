from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale
from engine.component.transform_component.transform_component import TransformComponent


class TransformComponentBuilder:
    def __init__(self):
        self._position = Position()
        self._rotation = Rotation()
        self._scale = Scale()

    def set_position(self, x: float, y: float) -> 'TransformComponentBuilder':
        self._position = Position(x, y)
        return self

    def set_rotation(self, degrees: float) -> 'TransformComponentBuilder':
        self._rotation = Rotation(degrees)
        return self

    def set_scale(self, x: float, y: float) -> 'TransformComponentBuilder':
        self._scale = Scale(x, y)
        return self

    def create_component(self) -> TransformComponent:
        return TransformComponent(
            position=self._position,
            rotation=self._rotation,
            scale=self._scale
        )