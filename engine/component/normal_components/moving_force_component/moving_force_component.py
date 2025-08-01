from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject
from engine.logger.logger import EngineLogger


class MovingForceComponent(BaseComponent):
    def __init__(self, moving_force: float):
        super().__init__()
        self._moving_force = moving_force

        self._transform_component: TransformComponent = None

    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self, event_tick: EventTick) -> None:
        self._transform_component.transform.position += Position(self._moving_force, 0)

    def on_collision(self, collided_game_object: GameObject) -> None:
        ...
        # if collided_game_object.get_tag() == "circle":
        #     EngineLogger.debug(f"Collided with circle and {collided_game_object.get_instance_id()}")
        # if collided_game_object.get_tag() == "rect":
        #     EngineLogger.debug(f"Collided with rect and {collided_game_object.get_instance_id()}")