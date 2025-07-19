from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick


class MovingForceComponent(BaseComponent):
    def __init__(self, moving_force: float):
        super().__init__()
        self._moving_force = moving_force

        self._transform_component: TransformComponent = None

    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    def on_tick(self, event_tick: EventTick) -> None:
        self._transform_component.transform.position += Position(self._moving_force, 0)