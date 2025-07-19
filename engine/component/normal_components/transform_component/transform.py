from dataclasses import dataclass

from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.rotation import Rotation
from engine.component.normal_components.transform_component.scale import Scale


@dataclass
class Transform:
    position: Position
    rotation: Rotation
    scale: Scale

    def clone(self) -> 'Transform':
        return Transform(position=Position(self.position.x, self.position.y),
                         rotation=Rotation(self.rotation.degrees),
                         scale=Scale(self.scale.x, self.scale.y))