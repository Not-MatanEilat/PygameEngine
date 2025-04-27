from dataclasses import dataclass

from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale


@dataclass
class Transform:
    position: Position
    rotation: Rotation
    scale: Scale