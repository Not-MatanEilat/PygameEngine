from abc import ABC, abstractmethod

from engine.component.normal_components.collider_component.collider.collider_type import ColliderType


class BaseCollider(ABC):
    @abstractmethod
    def get_collider_type(self) -> ColliderType:
        ...