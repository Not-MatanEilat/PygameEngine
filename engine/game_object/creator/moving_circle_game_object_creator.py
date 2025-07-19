from engine.colors import RED, Color
from engine.component.normal_components.circle_renderer_component.circle_renderer_component import \
    CircleRendererComponent
from engine.component.normal_components.collider_component.collider.box_collider import BoxCollider
from engine.component.normal_components.collider_component.collider.circle_collider import CircleCollider
from engine.component.normal_components.collider_component.collider_component import ColliderComponent
from engine.component.normal_components.moving_force_component.moving_force_component import MovingForceComponent
from engine.component.normal_components.rectangle_renderer_component.rectangle_renderer_component import \
    RectangleRendererComponent
from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.transform_builder import TransformBuilder
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.game_object.game_object import GameObject
from engine.logger.logger import EngineLogger


class MovingCircleGameObjectCreator:
    @staticmethod
    def create(start_position: Position, moving_force: float, color: Color) -> GameObject:
        game_object = GameObject()
        game_object.add_component(TransformComponent(TransformBuilder().set_scale(250, 50).set_position(start_position.x, start_position.y).create_component()))
        game_object.add_component(ColliderComponent(CircleCollider(125)))
        game_object.get_component(ColliderComponent).add_on_collision_callable(lambda other: EngineLogger.debug("check"))
        game_object.add_component(MovingForceComponent(moving_force))
        game_object.add_component(CircleRendererComponent(125, color))

        return game_object