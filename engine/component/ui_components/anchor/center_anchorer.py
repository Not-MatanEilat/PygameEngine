from overrides import override

from engine.component.transform_component.position import Position
from engine.component.transform_component.rotation import Rotation
from engine.component.transform_component.scale import Scale
from engine.component.transform_component.transform import Transform
from engine.component.ui_components.anchor.base_anchorer import BaseAnchorer


class CenterAnchorer(BaseAnchorer):
    @override
    def anchor_transform(self, old_transform_scale: Scale, relative_transform: Transform) -> Transform:
        position_x = relative_transform.position.x + relative_transform.scale.x / 2 - old_transform_scale.x / 2
        position_y = relative_transform.position.y + relative_transform.scale.y / 2 - old_transform_scale.y / 2
        return Transform(position=Position(position_x, position_y),
                         scale=Scale(old_transform_scale.x, old_transform_scale.y),
                         rotation=Rotation(0))