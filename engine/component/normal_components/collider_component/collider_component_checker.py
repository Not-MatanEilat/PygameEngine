from collections.abc import Callable
from typing import List, cast

from engine.collision.collision_checker import CollisionChecker
from engine.component.normal_components.collider_component.collider.base_collider import BaseCollider
from engine.component.normal_components.collider_component.collider.box_collider import BoxCollider
from engine.component.normal_components.collider_component.collider.collider_type import ColliderType
from engine.component.normal_components.transform_component.position import Position
from engine.game_object.game_object import GameObject

ColliderCheckerCallable = Callable[[BaseCollider, Position, BaseCollider, Position, GameObject], bool]

class ColliderChecker:
    @staticmethod
    def is_colliding(collider_type1: ColliderType, collider_type2: ColliderType) -> bool:
        collision_check_functions: List[List[ColliderCheckerCallable]] = \
 \
            [[ColliderChecker.check_collision_box_vs_box]]

    @staticmethod
    def check_collision_box_vs_box(collider1: BaseCollider, collider1_position: Position,
                                   collider2: BaseCollider, collider2_position: Position) -> bool:
        box_collider1: BoxCollider = cast(BoxCollider, collider1)
        box_collider2: BoxCollider = cast(BoxCollider, collider2)



        return(
            collider1_position.x > collider2_position.x + box_collider2.get_width()


        )
