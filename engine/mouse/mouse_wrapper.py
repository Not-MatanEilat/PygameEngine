from engine.component.transform_component.position import Position
from abc import ABC, abstractmethod

class BaseMouseWrapper(ABC):

    @abstractmethod
    def get_mouse_position(self) -> Position:
        ...