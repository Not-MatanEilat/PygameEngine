from imaplib import Debug
from typing import Callable

from overrides import override
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import Point as ShapelyPoint
from shapely.geometry.base import BaseGeometry

from engine.component.base_component import BaseComponent
from engine.component.normal_components.collider_component.collider.base_collider import BaseCollider
from engine.component.normal_components.transform_component.transform_component import TransformComponent
from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject
from engine.globals.global_manager import GlobalManager
from engine.logger.logger import EngineLogger

OnCollisionCallable = Callable[[GameObject], None]

class ColliderComponent(BaseComponent):
    def __init__(self, collider: BaseCollider):
        super().__init__()

        self._transform_component: TransformComponent = None
        self._collider = collider

    @override
    def start(self) -> None:
        self._transform_component = self.get_component(TransformComponent)

    @override
    def on_tick(self, event_tick: EventTick) -> None:
        all_game_objects = GlobalManager.get_instance().get_current_screen().get_game_objects()
        game_objects_with_colliders = [game_object for game_object in all_game_objects if game_object.has_component(ColliderComponent)]

        for other_game_object in game_objects_with_colliders:

            other_collider_component: ColliderComponent = other_game_object.get_component(ColliderComponent)
            # skip if same game_object
            if self is other_collider_component:
                continue

            if intersects(self.get_geometry_from_collider(), other_collider_component.get_geometry_from_collider()):
                self.__run_on_collision(other_game_object)

    def get_geometry_from_collider(self) -> BaseGeometry:
        return self._collider.get_base_geometry(self._transform_component.transform.position)

    def __run_on_collision(self, collided_game_object: GameObject) -> None:
        self.get_game_object().on_collision(collided_game_object)

def intersects(first_collider: BaseGeometry, second_collider: BaseGeometry) -> bool:
    return not first_collider.intersection(second_collider).is_empty