from engine.component.normal_components.transform_component.position import Position
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject


class Camera:
    def __init__(self, camera_game_object: GameObject):
        self._camera_game_object = camera_game_object

    def init(self) -> None:
        self._camera_game_object.init()

    def on_tick(self, event_tick: EventTick) -> None:
        self._camera_game_object.tick_components(event_tick)

    @property
    def position(self) -> Position:
        return self._camera_game_object.get_component(TransformComponent).transform.position

    def add_to_position(self, position: Position) -> None:
        self._camera_game_object.get_component(TransformComponent).transform.position += position