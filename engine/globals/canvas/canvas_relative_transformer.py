from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.scale import Scale
from engine.component.normal_components.transform_component.transform import Transform
from engine.logger.logger import EngineLogger


class CanvasRelativeTransformer:
    RELATIVE_HORIZONTAL_SCALE_SIZE = 1200
    RELATIVE_VERTICAL_SCALE_SIZE = 800

    def __init__(self, canvas_scale: Scale):
        self.canvas_scale = canvas_scale

    def create_transform_relative_to_canvas(self, old_transform: Transform) -> Transform:
        # EngineLogger.debug(f"transform {scale.x}, {scale.y}")
        x_position = old_transform.position.x * self.canvas_scale.x / self.RELATIVE_HORIZONTAL_SCALE_SIZE
        y_position = old_transform.position.y * self.canvas_scale.y / self.RELATIVE_VERTICAL_SCALE_SIZE
        x_scale = old_transform.scale.x * self.canvas_scale.x / self.RELATIVE_HORIZONTAL_SCALE_SIZE
        y_scale = old_transform.scale.y * self.canvas_scale.y / self.RELATIVE_VERTICAL_SCALE_SIZE
        return Transform(position=Position(x_position, y_position),
                         rotation=old_transform.rotation,
                         scale=Scale(x_scale, y_scale))

    def create_point_relative_to_canvas(self, old_point: Position) -> Position:
        # EngineLogger.debug(f"point {old_point.x}, {old_point.y}")
        x_position = old_point.x / self.canvas_scale.x * self.RELATIVE_HORIZONTAL_SCALE_SIZE
        y_position = old_point.y / self.canvas_scale.y * self.RELATIVE_VERTICAL_SCALE_SIZE
        return Position(x_position, y_position)