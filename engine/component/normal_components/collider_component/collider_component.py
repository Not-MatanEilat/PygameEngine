from typing import Callable

from overrides import override

from engine.component.base_component import BaseComponent
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject
from engine.globals.global_manager import GlobalManager


OnCollisionCallable = Callable[[GameObject], None]

class ColliderComponent(BaseComponent):
    def __init__(self, collider: BaseCollider):
        super().__init__()

        self._transform_component: TransformComponent = None
        self._collider = collider
        self._on_collision_callables: list[OnCollisionCallable] = []

    @override
    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    @override
    def on_tick(self, event_tick: EventTick) -> None:
        all_game_objects = GlobalManager.get_instance().get_current_screen().get_game_objects()
        game_objects_with_colliders = [game_object for game_object in all_game_objects if game_object.has_component(ColliderComponent)]
        if 1 == 1:
            self.__run_on_collision_callables()

    def __run_on_collision_callables(self, collided_game_object: GameObject,) -> None:
        for on_collision_callable in self._on_collision_callables:
            on_collision_callable(collided_game_object)

    def add_on_collision_callable(self, on_collision: OnCollisionCallable) -> None:
        self._on_collision_callables.append(on_collision)